# ISORYN Bootstrap Runbook

Canonical workspace: D:\Hive\Projects\isoryn-engine

## Local synchronization and HIVE
After cloning, or through Codex/Coder, run (the workspace path is operator input on purpose; the script has no
built-in machine default):

powershell -ExecutionPolicy Bypass -File scripts/bootstrap-local.ps1 -Workspace "<canonical-workspace>" `
  -HiveRepoPath "<path-to-HIVE>" -StartHive

The script fails closed on a non-empty non-Git directory, unexpected origin, dirty tree, missing HIVE checkout or
failed governance/HIVE preparation. HIVE inspect/index/corpus runs inside a container and is slow, so the bootstrap
uses a long per-request timeout (`--timeout`, default 180s, 600s recommended on first index).

## GitHub professional settings
With authenticated gh:

powershell -ExecutionPolicy Bypass -File scripts/configure-github.ps1 -WithoutStatusChecks

This configures squash-only PR merges, auto-merge capability, branch cleanup/update, disables wiki drift, and upserts
one `main-governance` ruleset requiring PR flow, linear history, resolved review threads, no branch deletion and no
force updates. `-WithoutStatusChecks` withholds the `Governance` status-check rule until that exact context has been
observed on a real check run; requiring a context that never reports would make main unmergeable. Once it is observed,
re-run without the switch to apply the complete manifest:

powershell -ExecutionPolicy Bypass -File scripts/configure-github.ps1

The repository state is declared in `.engineering/github/repository-settings.json` and
`.engineering/github/ruleset-main-governance.json`; the script reads both and writes BEFORE/AFTER receipts under
`.engineering/evidence/github/`.

## Validation
python scripts/validate_governance.py
python -m unittest discover -s tests -p "test_*.py" -v
python scripts/hive_bootstrap.py --relative-path isoryn-engine --timeout 600

Open Codex/Coder from the canonical workspace. Repository `.codex/config.toml` requires HIVE MCP for normal Codex
work, and `.mcp.json` carries the equivalent project-scoped configuration for other MCP-capable CLIs.

STOP: do not start engine implementation until ISORYN-WO-0001 is audited and the checkpoint is promoted.
