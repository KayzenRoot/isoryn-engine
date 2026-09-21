param(
  [string]$Workspace = "D:\Hive\Projects\isoryn-engine",
  [string]$Repository = "https://github.com/KayzenRoot/isoryn-engine.git",
  [string]$HiveRepoPath = $env:HIVE_REPO_PATH,
  [switch]$StartHive
)

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

function Assert-Command([string]$Name) {
  if (-not (Get-Command $Name -ErrorAction SilentlyContinue)) {
    throw "Required command not found on PATH: $Name"
  }
}

Assert-Command git
Assert-Command python

$parent = Split-Path -Parent $Workspace
New-Item -ItemType Directory -Force -Path $parent | Out-Null

if (-not (Test-Path $Workspace)) {
  git clone $Repository $Workspace
} elseif (-not (Test-Path (Join-Path $Workspace ".git"))) {
  $items = @(Get-ChildItem -Force $Workspace)
  if ($items.Count -ne 0) { throw "Workspace exists and is not an empty Git repository: $Workspace" }
  git clone $Repository $Workspace
} else {
  Push-Location $Workspace
  try {
    $origin = (git remote get-url origin).Trim()
    if ($origin -notmatch "KayzenRoot/isoryn-engine(\.git)?$") { throw "Unexpected origin: $origin" }
    if ((git status --porcelain).Length -ne 0) { throw "Workspace has local changes. Refusing automatic synchronization." }
    git fetch origin --prune
    git checkout main
    git pull --ff-only origin main
  } finally { Pop-Location }
}

if (-not $HiveRepoPath) {
  $candidates = @("D:\Hive\hive", "D:\Hive\Projects\hive", (Join-Path $parent "hive"))
  foreach ($candidate in $candidates) {
    if ((Test-Path (Join-Path $candidate "docker-compose.yml")) -and (Test-Path (Join-Path $candidate "backend"))) {
      $HiveRepoPath = $candidate
      break
    }
  }
}
if (-not $HiveRepoPath) { throw "HIVE checkout not found. Pass -HiveRepoPath or set HIVE_REPO_PATH." }

$env:HIVE_REPO_PATH = (Resolve-Path $HiveRepoPath).Path
$env:HIVE_API_URL = "http://localhost:8000"
$env:HIVE_ISORYN_RELATIVE_PATH = "isoryn-engine"

if ($StartHive) {
  Assert-Command docker
  Push-Location $env:HIVE_REPO_PATH
  try { docker compose up -d }
  finally { Pop-Location }
}

Push-Location $Workspace
try {
  python scripts/validate_governance.py
  python -m unittest discover -s tests -p "test_*.py" -v
  python scripts/hive_bootstrap.py --relative-path isoryn-engine
  Write-Host ""
  Write-Host "ISORYN local bootstrap: READY" -ForegroundColor Green
  Write-Host "Workspace: $Workspace"
  Write-Host "HIVE:      $env:HIVE_REPO_PATH"
  Write-Host "Open Codex/Coder from this workspace so .codex/config.toml can start HIVE MCP."
} finally { Pop-Location }
