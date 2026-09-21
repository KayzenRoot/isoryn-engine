# ISORYN Bootstrap Runbook

Canonical workspace: D:\Hive\Projects\isoryn-engine

## Local synchronization and HIVE
After cloning, or through Codex/Coder, run:

powershell -ExecutionPolicy Bypass -File scripts/bootstrap-local.ps1 -HiveRepoPath "<path-to-HIVE>" -StartHive

The script fails closed on a non-empty non-Git directory, unexpected origin, dirty tree, missing HIVE checkout or failed governance/HIVE preparation.

## GitHub professional settings
With authenticated gh:

powershell -ExecutionPolicy Bypass -File scripts/configure-github.ps1

This configures squash-only PR merges, auto-merge capability, branch cleanup/update, disables wiki drift, and creates a main ruleset requiring PR flow, linear history, resolved review threads, no branch deletion/force-push and the Governance status check.

## Validation
python scripts/validate_governance.py
python -m unittest discover -s tests -p "test_*.py" -v
python scripts/hive_bootstrap.py --relative-path isoryn-engine

Open Codex/Coder from D:\Hive\Projects\isoryn-engine. Repository .codex/config.toml requires HIVE MCP for normal Codex work.

STOP: do not start engine implementation until ISORYN-WO-0001 is audited and the checkpoint is promoted.
