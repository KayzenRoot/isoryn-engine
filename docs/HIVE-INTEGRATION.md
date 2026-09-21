# HIVE v1.0.0 Integration

ISORYN targets stable HIVE v1.0.0 at commit `a53b5b9fcf55c32a5696180fb1b1ef80ccd1edcf`. HIVE stays a
separate local-first runtime: never copy its backend, database or Docker stack into ISORYN, and never
let product correctness depend on HIVE being reachable. Git and `docs/project-brain/` remain canonical;
HIVE holds derived index state only.

## Operator configuration (not repository constants)

| Variable | Meaning |
| --- | --- |
| `HIVE_API_URL` | Local API base. Use `http://127.0.0.1:8000`, not `localhost`: HIVE binds IPv4 only, and `localhost` can resolve to `::1`. |
| `HIVE_REPO_PATH` | HIVE checkout providing `docker-compose.yml` and `backend/`. Set only when auto-discovery fails. |
| `HIVE_HOME` | Exported by a standard local HIVE install (`<install>\app`). `scripts/hive_mcp.py` honours it, so the MCP launcher works with no per-machine setting. |
| `HIVE_ISORYN_RELATIVE_PATH` | This repository's path relative to HIVE's `HIVE_PROJECTS_ROOT` (`isoryn-engine`). |
| `HIVE_REQUEST_TIMEOUT` | Per-request seconds. Registration, indexing and corpus sync exceed the 15s default on a cold corpus; the runbook uses 600. |

Start HIVE with its own supported procedure (`hive-up`, or `docker compose up -d` in the HIVE
checkout) and confirm `GET /api/v1/health` before bootstrapping.

## Bootstrap and proof

```
python scripts/hive_bootstrap.py --relative-path isoryn-engine --timeout 600
```

Health → resolve/register → inspect → index → retrieval corpus sync. Registration is resolved by exact
relative path, and an ambiguous project identity fails closed instead of silently re-pointing at
another project. Re-run after every head change so HIVE's inspection head matches the reviewed head.

## Working-tree line endings are load-bearing

HIVE inspects and indexes the repository from inside a Linux container that applies no line-ending
conversion. With a CRLF working tree (what `core.autocrlf=true` produces on Windows) every tracked file
reads as modified, HIVE reports the source as not current, and retrieval answers `results: []` instead
of the canonical text. `.gitattributes` pins text to LF and `scripts/validate_governance.py` fails if a
text file in the working tree carries CRLF, so this cannot regress silently.

## Staleness guard

A stale inspection head makes HIVE answer `source_not_current` with an empty result set rather than
serving old content. Treat an empty retrieval as the enforced signal it is: re-inspect, re-index and
re-sync, then re-prove. Never cache around it or describe a stale read as a live one.

The guard tests modified tracked paths (`git status --porcelain=v1 --untracked-files=no`), so an
untracked scratch file does not fail HIVE's reads while any dirty tracked file does. Because a corpus
left CURRENT by an earlier sync still answers retrieval for a head that was never indexed, a retrieval
proof is only meaningful together with the inspect/index/sync result for that same head.

Windows git rewrites `.git/index` at the same time the container reads it through the mount, so a
single status read can fail with `git_status_unavailable` at a genuinely clean head and the next call
then reports `source_not_current`. Re-run the pipeline before believing it: the runbook retries with a
recorded attempt count so a transient race is never published as a result.

## MCP surface

`.codex/config.toml` (project-scoped) and `.mcp.json` require the launcher `scripts/hive_mcp.py`, which
starts `python -m app.mcp_server` through `docker compose exec -T api` in the HIVE checkout. The pinned
v1.0.0 surface is exactly seven read-only tools: `project.list`, `project.status`, `context.build`,
`context.search`, `memory.search`, `memory.get`, `checkpoint.read`. `code.*`, `run.*`, `decision.*`,
`validation.*`, `telemetry.*` and `project.open` appear in the design documents but v1.0.0 does not
expose them; do not claim or implement against them.

The MCP cold start goes through Docker, so a client with a ~5s startup timeout reports a spurious
failure; `.codex/config.toml` raises `startup_timeout_sec` to 120. Configuring a launcher is not proof:
reload the CLI session and show an executed `tools/list` plus one read-only call, as
`.engineering/evidence/<WO-ID>-EVIDENCE.md` does.
