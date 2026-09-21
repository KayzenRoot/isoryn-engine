<#
.SYNOPSIS
    Applies the ISORYN GitHub governance target state from the checked-in desired-state manifests.
.DESCRIPTION
    Idempotent: repository settings are PATCHed from the manifest, and exactly one branch ruleset named
    main-governance is upserted by name (never duplicated). Captures BEFORE/AFTER receipts under
    .engineering/evidence/github so the Evidence Bundle can cite executed state instead of intent.
.PARAMETER WithoutStatusChecks
    Applies every rule except required_status_checks. Use only while the exact Governance check context has
    not yet been observed on a real check run, because requiring a context that never reports makes a
    protected branch permanently unmergeable.
#>
param(
  [string]$Repo = "KayzenRoot/isoryn-engine",
  [string]$Root = (Split-Path -Parent $PSScriptRoot),
  [switch]$WithoutStatusChecks
)

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$Utf8NoBom = New-Object System.Text.UTF8Encoding($false)

function Write-TextFile {
  param([string]$Path, [string]$Content)
  $dir = Split-Path -Parent $Path
  if (-not (Test-Path $dir)) { New-Item -ItemType Directory -Path $dir -Force | Out-Null }
  [System.IO.File]::WriteAllText($Path, $Content, $Utf8NoBom)
}

function Save-Receipt {
  param([string]$Name, [string[]]$Lines)
  $path = Join-Path $EvidenceDir $Name
  Write-TextFile -Path $path -Content (($Lines | Out-String).TrimEnd() + "`n")
  Write-Host "  receipt: $path"
}

function Invoke-Gh {
  param([string[]]$CliArgs)
  & gh @CliArgs
  if ($LASTEXITCODE -ne 0) { throw "gh $($CliArgs -join ' ') failed with exit $LASTEXITCODE" }
}

$ManifestDir = Join-Path $Root ".engineering\github"
$EvidenceDir = Join-Path $Root ".engineering\evidence\github"
$RepoManifest = Join-Path $ManifestDir "repository-settings.json"
$RulesetManifest = Join-Path $ManifestDir "ruleset-main-governance.json"
$RulesetName = "main-governance"

foreach ($f in @($RepoManifest, $RulesetManifest)) {
  if (-not (Test-Path $f)) { throw "Missing desired-state manifest: $f" }
}

if (-not (Get-Command gh -ErrorAction SilentlyContinue)) { throw "GitHub CLI (gh) is required." }
Invoke-Gh @("auth", "status")

New-Item -ItemType Directory -Path $EvidenceDir -Force | Out-Null

Write-Host "Capturing BEFORE state for $Repo" -ForegroundColor Cyan
Save-Receipt -Name "before-repository.json" -Lines (Invoke-Gh @("api", "repos/$Repo"))
Save-Receipt -Name "before-rulesets.json" -Lines (Invoke-Gh @("api", "repos/$Repo/rulesets"))

Write-Host "Applying repository settings from $(Split-Path -Leaf $RepoManifest)" -ForegroundColor Cyan
Invoke-Gh @("api", "--method", "PATCH", "repos/$Repo", "--input", $RepoManifest) | Out-Null

Write-Host "Probing optional security endpoints (recorded, not assumed)" -ForegroundColor Cyan
$probeLines = @()
foreach ($ep in @("vulnerability_alerts", "automated_security_fixes")) {
  $raw = ""
  try { $raw = (& gh api --method PUT "repos/$Repo/$ep" 2>&1 | Out-String).Trim() } catch { $raw = ($_ | Out-String).Trim() }
  $exit = $LASTEXITCODE
  $first = (($raw -split "`n") | Where-Object { $_.Trim() } | Select-Object -First 1)
  if ($exit -eq 0 -and [string]::IsNullOrWhiteSpace($first)) { $first = "enabled" }
  $state = "APPLIED"
  if ($exit -ne 0) {
    if ($first -match "404|403|Not Found|Forbidden") { $state = "NOT_AVAILABLE" } else { $state = "FAILED" }
  }
  $probeLines += "$ep => $state (exit=$exit) $first"
}
$probePath = Join-Path ([System.IO.Path]::GetTempPath()) "isoryn-security-probe.txt"
Write-TextFile -Path $probePath -Content (($probeLines -join "`n") + "`n")
Copy-Item $probePath (Join-Path $EvidenceDir "security-endpoints.txt") -Force
Remove-Item $probePath -Force -ErrorAction SilentlyContinue
Write-Host ($probeLines -join "`n")

Write-Host "Upserting ruleset '$RulesetName'" -ForegroundColor Cyan
$existing = (Invoke-Gh @("api", "repos/$Repo/rulesets")) | ConvertFrom-Json
$current = @(@($existing) | Where-Object { $_.name -eq $RulesetName })
if ($current.Count -gt 1) { throw "Duplicate rulesets named ${RulesetName}: $($current.id -join ',')" }

$payloadPath = Join-Path ([System.IO.Path]::GetTempPath()) ("isoryn-ruleset-" + [guid]::NewGuid().ToString("N") + ".json")
try {
  if ($WithoutStatusChecks) {
    $payload = Get-Content $RulesetManifest -Raw | ConvertFrom-Json
    $payload.rules = @($payload.rules | Where-Object { $_.type -ne "required_status_checks" })
    $filtered = $payload | ConvertTo-Json -Depth 20
    if ($filtered -notmatch "main-governance" -or $filtered -match "required_status_checks") {
      throw "Filtered ruleset payload lost target state; refusing to apply."
    }
    Write-TextFile -Path $payloadPath -Content $filtered
  } else {
    Copy-Item $RulesetManifest $payloadPath -Force
  }
  if ($current.Count -eq 1) {
    $applied = Invoke-Gh @("api", "--method", "PUT", "repos/$Repo/rulesets/$($current[0].id)", "--input", $payloadPath)
  } else {
    $applied = Invoke-Gh @("api", "--method", "POST", "repos/$Repo/rulesets", "--input", $payloadPath)
  }
} finally {
  Remove-Item $payloadPath -Force -ErrorAction SilentlyContinue
}

$appliedId = ($applied | ConvertFrom-Json).id

Write-Host "Capturing AFTER state and verification" -ForegroundColor Cyan
Save-Receipt -Name "after-repository.json" -Lines (Invoke-Gh @("api", "repos/$Repo"))
Save-Receipt -Name "after-ruleset.json" -Lines (Invoke-Gh @("api", "repos/$Repo/rulesets/$appliedId"))
Save-Receipt -Name "ruleset-check-main.txt" -Lines (Invoke-Gh @("ruleset", "check", "main", "--repo", $Repo))
Save-Receipt -Name "ruleset-list.json" -Lines (Invoke-Gh @("ruleset", "list", "--repo", $Repo))
Save-Receipt -Name "ruleset-view.txt" -Lines (Invoke-Gh @("ruleset", "view", "$appliedId", "--repo", $Repo))

Write-Host "GitHub governance state applied to $Repo (ruleset id $appliedId)." -ForegroundColor Green
