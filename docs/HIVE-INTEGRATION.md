# HIVE v1.0.0 Integration

ISORYN targets stable HIVE v1.0.0 at commit a53b5b9fcf55c32a5696180fb1b1ef80ccd1edcf.

HIVE remains a separate local-first runtime. Do not copy HIVE backend/database/Docker stack into ISORYN.

Canonical workspace: D:\Hive\Projects\isoryn-engine
Recommended HIVE_PROJECTS_ROOT for that layout: D:\Hive\Projects
Set HIVE_REPO_PATH to the actual stable HIVE checkout when it is not discoverable automatically.

HIVE v1.0.0 reads these canonical paths: docs/project-brain/13-CHECKPOINT.md, 03-SCOPE.md, 15-DEFINITION-OF-DONE.md, 04-ARCHITECTURE.md and 16-DECISIONS-LEDGER.md.

After HIVE is running:
python scripts/hive_bootstrap.py --relative-path isoryn-engine

The script verifies health, resolves/registers ISORYN, inspects Git state, indexes the repository and synchronizes the retrieval corpus.

.codex/config.toml requires the project-scoped HIVE MCP launcher scripts/hive_mcp.py. HIVE retrieval/memory is derived context; tracked Git remains canonical.
