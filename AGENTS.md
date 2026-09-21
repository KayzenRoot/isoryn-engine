# ISORYN Executor Contract

ISORYN is governed by GEF and is HIVE-first.

## Authority
1. Resolve authority through .engineering/SOURCE-HIERARCHY.md.
2. Read docs/project-brain/13-CHECKPOINT.md first.
3. Then read Decisions, Scope, Definition of Done, Architecture and Requirements as required by the active Work Order.
4. Git and exact executable evidence outrank derived summaries and chat memory.
5. Product implementation requires an admitted Work Order.

## HIVE-first preflight
Before governed product edits:
- resolve repository root, branch, HEAD and cleanliness;
- verify HIVE v1.0.0 availability;
- resolve ISORYN through the read-only HIVE MCP surface;
- read checkpoint/project status through HIVE when available;
- retrieve the minimum sufficient context;
- prefer Git/static/AST/test evidence over LLM inference when deterministic proof exists;
- record Git and HIVE basis in execution evidence.

Stable HIVE v1.0.0 MCP tools:
project.list, project.status, context.build, context.search, memory.search, memory.get, checkpoint.read.

Never fabricate HIVE evidence. If HIVE is unavailable, proceed only when the Work Order explicitly permits degraded-safe execution.

## GEF lifecycle
ANALYZE -> SOURCE CHECK -> NEXT NECESSARY INCREMENT -> WORK ORDER -> CONTEXT LOCK -> PREFLIGHT -> EXECUTOR -> TESTS/EVIDENCE -> PR -> AUDIT -> VERDICT -> CHECKPOINT DELTA -> MERGE -> NEXT

Verdicts: APPROVED, CORRECTION REQUIRED, BLOCKED.
No known HIGH or CRITICAL defect may be promoted.

## ISORYN boundaries
- HIVE owns durable project intelligence, retrieval and derived memory.
- CORE is a reference for governed execution/orchestration contracts.
- IRIS is a reference for media/asset/quality systems and future integration.
- ISORYN owns game-engine/runtime/editor/rendering responsibilities admitted by its canonical sources.
- Godot 4.x is the accepted foundation direction; exact upstream/fork/version and replacement boundaries must be frozen by evidence before implementation.
- Do not vendor HIVE, CORE, IRIS or GEF source workspaces into ISORYN unless a later explicit ADR authorizes it.

## Reviewer-first correction
During review, fix small, causal, in-scope defects directly when current repository/GitHub tools can implement and validate them safely. Delegate to Codex/another executor only when correction requires substantial implementation, unavailable local state, dependency/architecture/scope/security admission, or assurance unavailable to the reviewer.

Every direct fix creates a new exact head and invalidates stale head-bound evidence.

## Completion
Green tests and merges are evidence, not completion. Canonical checkpoint promotion follows objective audit and the Definition of Done. Reviews are in Brazilian Portuguese unless a Work Order explicitly says otherwise.
