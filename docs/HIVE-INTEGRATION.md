# HIVE v1.0.0 Integration

ISORYN is prepared for stable HIVE v1.0.0 at commit a53b5b9fcf55c32a5696180fb1b1ef80ccd1edcf.

## Architecture
HIVE remains a separate local-first runtime. ISORYN is mounted/read by HIVE beneath HIVE_PROJECTS_ROOT. Do not copy the HIVE backend, database or Docker stack into this repository.

HIVE v1.0.0 expects these tracked governance paths:
- docs/project-brain/13-CHECKPOINT.md
- docs/project-brain/03-SCOPE.md
- docs/project-brain/15-DEFINITION-OF-DONE.md
- docs/project-brain/04-ARCHITECTURE.md
- docs/project-brain/16-DECISIONS-LEDGER.md

ISORYN materializes all five.

## Local workspace
Canonical user workspace: D:\Hive\Projects\isoryn-engine

Recommended HIVE projects root for that layout: D:\Hive\Projects

Recommended separate HIVE checkout: D:\Hive\hive or configure HIVE_REPO_PATH to the actual stable HIVE checkout.

After HIVE is running:
python scripts/hive_bootstrap.py --relative-path isoryn-engine

The bootstrap verifies HIVE health, resolves/registers ISORYN, reinspects Git state, indexes the repository and synchronizes the retrieval corpus.

## Codex MCP
.codex/config.toml requires a project-scoped STDIO server named hive using scripts/hive_mcp.py. The launcher resolves HIVE from HIVE_REPO_PATH first and then common nearby layouts, and starts the MCP server through HIVE's running Docker Compose API service.

HIVE memory and retrieval are derived context. Tracked canonical Git files remain authoritative.
