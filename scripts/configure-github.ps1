param([string]$Repo = "KayzenRoot/isoryn-engine")

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

if (-not (Get-Command gh -ErrorAction SilentlyContinue)) { throw "GitHub CLI (gh) is required." }
gh auth status | Out-Host

gh api --method PATCH "repos/$Repo" -f allow_squash_merge=true -f allow_merge_commit=false -f allow_rebase_merge=false -f allow_auto_merge=true -f delete_branch_on_merge=true -f allow_update_branch=true -f use_squash_pr_title_as_default=true -f has_wiki=false | Out-Null

$rulesetName = "main-professional-protection"
$existing = gh api "repos/$Repo/rulesets" | ConvertFrom-Json
$current = @($existing) | Where-Object { $_.name -eq $rulesetName } | Select-Object -First 1

$payload = @{
  name = $rulesetName
  target = "branch"
  enforcement = "active"
  bypass_actors = @()
  conditions = @{ ref_name = @{ include = @("~DEFAULT_BRANCH"); exclude = @() } }
  rules = @(
    @{ type = "deletion" },
    @{ type = "non_fast_forward" },
    @{ type = "required_linear_history" },
    @{ type = "pull_request"; parameters = @{ dismiss_stale_reviews_on_push = $true; require_code_owner_review = $false; require_last_push_approval = $false; required_approving_review_count = 0; required_review_thread_resolution = $true } },
    @{ type = "required_status_checks"; parameters = @{ strict_required_status_checks_policy = $true; do_not_enforce_on_create = $false; required_status_checks = @(@{ context = "Governance" }) } }
  )
} | ConvertTo-Json -Depth 12

$temp = New-TemporaryFile
try {
  Set-Content -Path $temp -Value $payload -Encoding utf8
  if ($current) { gh api --method PUT "repos/$Repo/rulesets/$($current.id)" --input $temp | Out-Null }
  else { gh api --method POST "repos/$Repo/rulesets" --input $temp | Out-Null }
} finally { Remove-Item $temp -Force -ErrorAction SilentlyContinue }

Write-Host "GitHub professional configuration applied to $Repo." -ForegroundColor Green
gh api "repos/$Repo/rulesets"
