# ISORYN Integration Contracts

Status: DISCOVERY_BASELINE (refined by ISORYN-WO-0002)

Each contract states: role, transport and surface, canonical authority, versioning rule, failure behavior,
security boundary and explicit non-goals. "Not frozen" is a state, not a placeholder: a partner cannot be
depended on beyond what is written here.

Global rules for every partner: **no shared-database coupling** and no write authority over ISORYN canonical
state; integrations are versioned contracts, fingerprints/events or explicit tool/API boundaries; a partner's
derived view never supersedes Git; and a degraded partner degrades the *capability*, reported as such, rather
than silently substituting a guess.

## HIVE - derived project intelligence (live contract)

| Field | Contract |
| --- | --- |
| Role | Derived context, structural index, retrieval, memory and checkpoint assistance for the ISORYN repository |
| Transport / surface | Read-only MCP over the pinned v1.0.0 core surface: `project.list`, `project.status`, `context.build`, `context.search`, `memory.search`, `memory.get`, `checkpoint.read`, launched through `scripts/hive_mcp.py` |
| Pin | HIVE v1.0.0 @ `a53b5b9fcf55c32a5696180fb1b1ef80ccd1edcf`; changing the pin is an ADR-level action, not a runtime accident |
| Canonical authority | None. Git and Project Brain outrank every HIVE answer; HIVE reads the canonical workspace, it does not own it |
| Workspace binding | The canonical workspace path is declared in `docs/project-brain/12-LOCAL-DEPLOYMENT.md`; HIVE registration resolves the project by its `relative_path` inside that root, so a proof executed against a different path proves nothing |
| Versioning | The Work Order Context Lock records the pins; a pin change or a canonical-source change invalidates derived context |
| Failure behavior | Staleness is surfaced (`source_not_current`) rather than hidden; the executor records `STALE_CONTEXT` and re-indexes before leaning on retrieved content. Semantic-embedding absence degrades to lexical retrieval with the fallback declared, not silently. If the runtime is unreachable, HIVE-first preflight fails and the Work Order stops or declares degraded-safe execution only where its text allows |
| Security boundary | Read-only. No canonical write, no credential storage, no shared database; the container sees the workspace through a read-only mount |
| Non-goals | HIVE is not a build system, not a benchmark host and not an arbiter of architecture decisions |
| Evidence | ISORYN-WO-0001 proved registration, inspection, index, corpus currency, canonical retrieval and a real MCP session at exact heads; ISORYN-WO-0002 re-proves them on its own head |

## Godot - engine foundation (now a concrete contract)

| Field | Contract |
| --- | --- |
| Role | Engine baseline that ISORYN builds on, extends and re-pins deliberately |
| Surface ISORYN may depend on | `doc/classes/` (810 class documents at the pinned tag), the dumped extension API (`core/extension/extension_api_dump.cpp`, `gdextension_interface.*`), `*Server` singleton interfaces, `custom_modules` build detection, editor plugin/importer extension points |
| Not a contract | Internal C++ headers reached through a seam-3 module. They are private and re-verified at every rebase; ADR-0003 requires the dependency list in evidence |
| Pin | Tag + 40-character commit + `version.py` fields (ADR-0001); a branch name is never a pin |
| Failure behavior | An unmet upstream build prerequisite aborts configuration with an exit code and a preserved log (WO-0002 recorded exactly that for the `accesskit`/`d3d12` optional drivers) rather than being worked around silently |
| Security boundary | Fetched read-only from official sources; no mirror, no patch, no vendored copy in this repository |
| Non-goals | Godot does not own ISORYN decisions, and an upstream release does not move the baseline without a Work Order |

## CORE - governed execution reference (not frozen)

- **Role today**: architectural reference for governed execution, agents, capabilities and verification. No runtime coupling exists or is authorized.
- **Future contract shape**: request/response plus eventing over a versioned interface with declared idempotency, timeouts and audit records. A Core-driven action against the ISORYN repository must pass through the same Work Order gate a human does - it cannot admit its own scope.
- **Failure behavior (required before adoption)**: an unavailable or mismatched CORE version must be a hard stop for the affected capability, never a silent fallback to local inference.
- **Non-goals**: CORE does not own ISORYN canonical state; it does not get a privileged write path.

## IRIS - media, asset and quality reference (not frozen)

- **Role today**: reference for media/asset/quality/production systems. No runtime coupling exists or is authorized.
- **Future contract shape**: asset fingerprints and quality-report handshakes across an explicit boundary (import/export manifests, golden-reference hashes), so that an ISORYN asset pipeline can be verified without sharing a database with IRIS.
- **Failure behavior (required before adoption)**: a missing or stale quality report blocks the promotion that depends on it, mirroring the governance-validator pattern already in this repository.
- **Non-goals**: IRIS is not an engine subsystem and ISORYN does not become an IRIS consumer by default.

## Addendum from discovery

The WO-0002 seam analysis (ADR-0003) shows that the practical external surface for AI-native editor automation
is upstream's own automation vocabulary - GDScript LSP (`modules/gdscript/language_server/`), debug adapter
(`editor/debugger/debug_adapter/`), the machine-readable class dump and command-line project operations such as
`--import`, `--headless`, `--quit-after`, `--fixed-fps` and `--write-movie`. Read-only observation of a project is
therefore already available through public interfaces; anything that mutates project state needs its own contract,
with idempotency and an audit record, before it can be admitted (PT-09 in the technology registry).

One execution limit found in WO-0002 belongs to this contract, not to the toolchain appendix: the mutating half
of that vocabulary is editor-only. `--import` is labelled `CLI_OPTION_AVAILABILITY_EDITOR`
(`main/main.cpp:700`) and both it and `--export-*` are parsed only under `TOOLS_ENABLED`
(`main/main.cpp:1597-1766`), so an automation contract that promises import or export needs a host that can build
the editor target, while a contract limited to observation, replay and capture runs on the template binary this
increment measured.
