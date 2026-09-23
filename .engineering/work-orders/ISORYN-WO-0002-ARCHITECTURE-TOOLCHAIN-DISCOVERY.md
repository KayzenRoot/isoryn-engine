# ISORYN-WO-0002 - Architecture, Godot Baseline & Toolchain Discovery

OBJECTIVE: establish the evidence-backed architecture baseline required before any production engine implementation.
Discover and verify the current official Godot 4.x baseline, prove local source-build/toolchain viability, decide the
repository/fork/upstream-sync topology and extension seams, define objective benchmark contracts, build the ISORYN
Master Module Index and initial proprietary-technology registry, refine HIVE/CORE/IRIS boundaries, update canonical
architecture/requirements/test/backlog/decision sources, create exact-head evidence, and stop for independent review.

HIVE PREFLIGHT: resolve the canonical workspace, branch, exact HEAD and cleanliness first; refresh the ISORYN HIVE
v1.0.0 inspection/index/corpus on the active WO-0002 head before treating retrieved context as current; execute a real
read-only MCP session through scripts/hive_mcp.py; use HIVE progressively and minimally; Git/static/build/benchmark
evidence outranks retrieval. A stale or degraded HIVE result is recorded and repaired before architectural claims
depend on it.

CANONICAL BASIS: docs/project-brain/13-CHECKPOINT.md; docs/project-brain/16-DECISIONS-LEDGER.md;
docs/project-brain/03-SCOPE.md; docs/project-brain/15-DEFINITION-OF-DONE.md; docs/project-brain/04-ARCHITECTURE.md;
docs/project-brain/02-REQUIREMENTS.md; docs/project-brain/11-TEST-PLAN.md; docs/project-brain/05-INTEGRATION-CONTRACTS.md;
docs/project-brain/14-BACKLOG.md; AGENTS.md; .engineering/SOURCE-HIERARCHY.md. Admission base is exact main SHA
74c47fa204a5da79c1418fb9bcc2557603422f88. GEF remains pinned to v1.0.0 @ 866fe3af8cccc65c929aaf6a47a924401fa448b3 and HIVE to v1.0.0 @
a53b5b9fcf55c32a5696180fb1b1ef80ccd1edcf. Godot is not frozen at admission: the executor must verify official
release/tag/commit truth before proposing an ADR.

CONTEXT BUDGET: checkpoint first, then only the canonical sources needed by the current discovery question. Use HIVE
for cross-source retrieval. Inspect external Godot source by Git/AST/static tools rather than loading whole trees into
LLM context. Summarize subsystem ownership and extension seams from deterministic paths/symbols. Do not copy HIVE,
CORE or IRIS source into ISORYN.

RISK/ASSURANCE: ELEVATED. This Work Order executes third-party engine builds and makes architecture/toolchain decisions
that constrain later implementation. Use official Godot sources only, exact tags/commits, isolated external scratch
workspaces, reproducible command receipts, build/hash/version evidence, no secrets, no paid services, no modification
of concurrent HIVE/CORE/IRIS runtimes, and rollback-friendly decisions. No benchmark claim may rely on average FPS
alone.

CONTEXT: WO-0001 is merged and bootstrap is approved. ISORYN is a clean engine program using Godot 4.x as foundation
direction, with HIVE/CORE/IRIS as external reference/partner systems. On 2026-09-23 the official Godot archive lists
4.7.2-stable as the current stable maintenance release and 4.8-dev6 as pre-release development. Re-verify those facts
from official sources at execution time; do not treat admission-time release data as a frozen decision.

SCOPE:
- refresh HIVE/MCP exact-head context for WO-0002;
- inventory the actual local Windows compiler/build/runtime/hardware environment used for evidence;
- verify official Godot release policy, tags and source commit SHAs;
- mandatory build/smoke baseline for the current supported stable Godot candidate;
- compatibility-reference build or static/build feasibility check for the immediately previous supported stable line;
- forward-looking delta analysis of the current Godot 4.x development line without adopting a pre-release by default;
- architecture surface map of core, scene, servers, rendering, editor, modules, GDExtension, import/resource and platform seams;
- decision matrix and ADR(s) for exact baseline version, repository/fork topology, extension-vs-module-vs-fork policy and upstream synchronization;
- toolchain baseline and reproducible build commands;
- benchmark contract and initial measured baseline sufficient to gate later performance/graphics claims;
- Master Module Index covering every product-scope family in docs/project-brain/03-SCOPE.md, classified NECESSARY / IMPORTANT / FUTURE / OUT OF SCOPE;
- initial proprietary-technology registry with purpose, dependency, assumptions, proof obligations, fallback and compatibility impact;
- explicit HIVE/CORE/IRIS integration/ownership boundary refinement;
- canonical documentation/checkpoint/evidence updates and one governed PR.

OUT OF SCOPE:
- production renderer/runtime/editor/gameplay implementation;
- implementing proprietary technologies;
- importing or vendoring a Godot source tree into this repository;
- creating a permanent Godot fork repository unless the evidence-backed topology ADR explicitly requires it and the reviewer later authorizes that separate action;
- adopting a Godot pre-release merely because it is newer;
- performance superiority claims against Godot without admitted workloads and executed measurements;
- changing GEF/HIVE pins;
- changing or copying HIVE/CORE/IRIS ownership/canonical state;
- merge, checkpoint self-promotion, release publication, paid services or destructive local cleanup.

FILES/SOURCES TO READ: AGENTS.md; .engineering/SOURCE-HIERARCHY.md; this Work Order; its Context Lock; canonical
checkpoint, Decisions, Scope, DoD, Architecture, Requirements, Test Plan, Integration Contracts and Backlog;
docs/HIVE-INTEGRATION.md; .engineering/gef/GEF-EXECUTION-PROTOCOL.md; .engineering/gef/GEF-EVIDENCE-SPEC.md;
scripts/validate_governance.py; official Godot repository/release archive/release-policy/build documentation;
HIVE-derived reference context for CORE and IRIS only where relevant to ownership/integration patterns.

REQUIREMENTS:
1. Re-verify current official Godot stable/support state. At admission, 4.7.2-stable is the mandatory current-stable
   candidate, 4.6.3-stable is a previous-supported compatibility reference, and 4.8-dev6 is observation-only. If the
   official stable channel changes before execution, update the matrix and evidence rather than silently using stale data.
2. Every Godot candidate used in evidence is identified by official tag and exact commit SHA.
3. External Godot clones/build trees live outside this repository and are never committed as vendored source.
4. Record actual CPU/GPU/RAM/OS/compiler/Python/SCons and relevant SDK/tool versions from the execution machine.
5. Prove at least the current-stable candidate can be configured/built enough to validate the chosen toolchain, or
   return BLOCKED_TOOLCHAIN with exact failing command/log. Do not replace build proof with prose.
6. Baseline metrics include build wall time, produced binary identity/size, editor/headless smoke result, startup/load
   timing where reproducibly measurable, memory observations where available, and frame-time/CPU/GPU metrics only on
   an admitted deterministic scene/workload. Average FPS alone is forbidden.
7. Freeze exact Godot baseline/fork/topology/upstream-sync policy only if the evidence satisfies the decision criteria.
   Otherwise propose the narrow unresolved experiment and stop BLOCKED_DECISION instead of guessing.
8. Define a seam policy: upstream first; addon/GDExtension/tooling second; bounded engine module third; fork/subsystem
   replacement only when proof obligations justify maintenance cost.
9. Master Module Index must cover all product-scope families and state dependencies, owner/seam, benchmark needs,
   risk and scope class. It is a planning index, not permission to implement every module.
10. Proprietary technology entries make no superiority claim. Each entry has purpose, dependencies, assumptions,
    measurable proof obligations, fallback, compatibility/upstream impact and scope class.
11. HIVE/CORE/IRIS contracts remain external/versioned and no shared database coupling is introduced.
12. Update canonical docs and Decisions Ledger/ADRs only with claims supported by executed evidence.
13. Preserve professional GitHub governance and all WO-0001 regression guards.

ARCHITECTURE RULES:
- Git + Project Brain remain authoritative; HIVE remains derived read-only context.
- Godot 4.x remains the accepted foundation direction unless a future separately admitted decision supersedes it.
- Favor upstream compatibility and reversible seams.
- Separate ISORYN-owned modules from upstream-owned code and external partner systems.
- No shared-database coupling with HIVE/CORE/IRIS.
- External source/build caches are operator state, not repository state.
- Stable ABI/API and failure behavior must be documented for every proposed integration seam.
- Camera/visibility/relevance -> budgets -> geometry/textures/lighting/shadows/animation/VFX/streaming remains the
  optimization ordering unless measurements justify a change.

CONSTRAINTS:
- base branch main; working branch isoryn-wo-0002-architecture-toolchain-discovery; existing PR #5;
- no force-push, history rewrite or destructive cleanup;
- no merge and no self-approval;
- no secrets or credentials in evidence;
- do not stop/reconfigure unrelated Docker/HIVE stacks;
- do not commit generated Godot binaries or third-party source unless a later explicit artifact policy admits them;
- official upstream sources must be fetched read-only/pinned and checksummed/identified;
- use current machine facts, not chat memory, for hardware/toolchain evidence.

ACCEPTANCE CRITERIA:
1. HIVE v1.0.0 inspection/index/corpus and real MCP calls are current for an exact WO-0002 head.
2. Official Godot release/support/tag evidence is captured with exact source commit SHAs.
3. Current-stable Godot source-build/toolchain viability is executed and evidenced, or an exact reproducible blocker is recorded.
4. Compatibility and development-line candidates are compared only for the questions they can legitimately answer.
5. Actual local hardware/toolchain inventory is captured without hardcoding private machine state into portable config.
6. A reproducible benchmark contract exists and at least one initial deterministic baseline workload/smoke measurement is captured where available.
7. Architecture surface map identifies upstream ownership and ISORYN extension/module/fork seams with cited paths/symbols.
8. An evidence-backed ADR freezes, or explicitly blocks, exact Godot baseline version and repository/fork topology.
9. An evidence-backed ADR freezes, or explicitly blocks, build toolchain and upstream-sync policy.
10. Extension-vs-module-vs-fork decision rules are canonical and testable.
11. Master Module Index covers every scope family with dependencies, scope classification, owner/seam, proof needs and risk.
12. Proprietary Technology Registry exists with proof obligations/fallbacks and no unmeasured superiority claim.
13. HIVE/CORE/IRIS integration contracts are refined without ownership leakage or shared-db coupling.
14. Architecture, Requirements, Test Plan, Integration Contracts, Backlog and Decisions/ADRs are mutually consistent.
15. No production engine code or Godot source tree is committed.
16. Governance validator, compile checks, unit tests, git diff check, secret scan and exact-head Governance CI pass.
17. Evidence Bundle is complete, exact-SHA-bound and records failures/residual risks honestly.
18. PR #5 is open, green and unmerged for independent review.
19. No known HIGH/CRITICAL defect remains.

TESTS:
- python -m py_compile scripts/validate_governance.py scripts/hive_bootstrap.py scripts/hive_mcp.py;
- python scripts/validate_governance.py;
- python -m unittest discover -s tests -p "test_*.py" -v;
- git diff --check and clean tracked-tree verification;
- repository secret scan using the established method;
- HIVE health/inspect/index/corpus/retrieval + MCP initialize/tools/list/project.status/checkpoint.read/context.search;
- official Godot Git tag/commit verification;
- reproducible source-build/smoke commands for admitted candidates;
- deterministic baseline metrics specified by the benchmark contract;
- checks that no Godot/HIVE/CORE/IRIS vendored source or generated binary entered the repository;
- gh pr checks 5 --required and exact-head GitHub Actions readback.

EVIDENCE: update .engineering/evidence/ISORYN-WO-0002-EVIDENCE.md in place. Include exact base/head SHAs,
canonical inputs, official Godot URLs/tags/commit SHAs, hardware/toolchain inventory, source-build commands/logs,
benchmark workload definitions and raw results, architecture surface-map references, decision matrix/ADRs,
Master Module Index and technology-registry summaries, HIVE/MCP proof, changed files, tests, security checks,
errors corrected, unsupported capabilities, residual risks, rollback, PR/CI state and proposed checkpoint delta.
Raw build/benchmark receipts may live under .engineering/evidence/wo-0002/; do not commit huge generated binaries.

DELIVERABLES:
- completed WO-0002 Evidence Bundle and proposed Checkpoint Delta;
- docs/project-brain/06-MASTER-MODULE-INDEX.md;
- docs/project-brain/07-PROPRIETARY-TECHNOLOGY-REGISTRY.md;
- docs/project-brain/08-GODOT-BASELINE-AND-TOPOLOGY.md;
- docs/project-brain/09-TOOLCHAIN-AND-BENCHMARK-BASELINE.md;
- ADR(s) under docs/adr/ for Godot baseline/topology, toolchain/upstream sync and extension seam policy as needed;
- updated Architecture, Requirements, Test Plan, Integration Contracts, Backlog, Decisions Ledger and upload/source map where affected;
- reproducible discovery/build/benchmark helper scripts only if necessary; no production engine implementation;
- updated PR #5 with exact-head evidence and PT-BR executor report.

REVIEW FORMAT: Portuguese (Brazil). Findings first. Report exact base/head SHA, branch/PR, official Godot candidates and
commit SHAs, build/toolchain results, benchmark evidence, architecture/fork decisions, canonical docs changed, HIVE/MCP
state, tests/CI, errors corrected, residual risks, proposed checkpoint delta and explicit no-production-code confirmation.

STOP CONDITION: READY_FOR_ARCHITECTURE_TOOLCHAIN_AUDIT when all acceptance criteria are evidenced and PR #5 is
green/open/unmerged. Stop BLOCKED_TOOLCHAIN, BLOCKED_DECISION, STALE_CONTEXT or BLOCKED_USER_WORK when the named
condition prevents objective completion. Never begin production engine/module implementation inside WO-0002.
