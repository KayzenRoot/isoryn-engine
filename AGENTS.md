# ISORYN Executor Contract

ISORYN is governed by GEF and is HIVE-first.

## Authority
1. Resolve authority through .engineering/SOURCE-HIERARCHY.md.
2. Read docs/project-brain/13-CHECKPOINT.md first.
3. Then read Decisions, Scope, Definition of Done, Architecture and Requirements as required by the active Work Order.
4. Git and exact executable evidence outrank derived summaries and chat memory.
5. Product implementation requires an admitted Work Order.

## HIVE-first preflight
Before product edits resolve repository root, branch, HEAD and cleanliness; verify HIVE v1.0.0; resolve ISORYN through HIVE's read-only MCP; retrieve only minimum sufficient context; prefer deterministic Git/static/test proof over LLM inference; record Git/HIVE basis in evidence.

Stable HIVE v1.0.0 MCP tools: project.list, project.status, context.build, context.search, memory.search, memory.get, checkpoint.read.

Never fabricate HIVE evidence. Degraded-safe execution is allowed only when the active Work Order says so.

## Boundaries
HIVE owns derived project intelligence/retrieval/memory. CORE is a reference for governed execution/orchestration. IRIS is a reference for media/assets/quality systems. ISORYN owns engine/runtime/editor/rendering responsibilities admitted by its canonical sources. Godot 4.x is the accepted foundation direction; exact version/fork/replacement boundaries require evidence before implementation.

Do not vendor HIVE, CORE, IRIS or GEF workspaces into ISORYN without an explicit ADR.

## Autonomous Work Order execution
An attached or admitted Work Order is the complete scope authorization for every chat working on
`KayzenRoot/isoryn-engine`. Execute that scope end to end without pausing to ask the user for
permission on individual steps, and never hand an in-scope item back as a pending question or leave
it partially done.

This standing authorization covers, inside the admitted Work Order scope: reading and editing
repository files, running local validators/tests/builds, calling HIVE through its read-only MCP
surface, Git operations on the Work Order branch, pushing that branch, and creating or updating the
single pull request the Work Order designates.

This authorization never overrides a hard stop, and a stop is reported, not asked about: merging a
pull request, force-push or history rewrite, deleting or overwriting uncommitted user work,
adopting/amending/reversing an approved decision, promoting a checkpoint, paid or third-party
actions, and shared or production infrastructure changes. Product/engine implementation still
requires an admitted Work Order (Authority item 5).

## Review
Verdicts: APPROVED, CORRECTION REQUIRED, BLOCKED. No known HIGH/CRITICAL defect may be promoted. Reviewers directly fix small, causal, in-scope defects when current tools can implement and validate them safely; delegate only residual work requiring broader execution, local state, dependency/architecture/scope/security admission, or unavailable assurance. Any direct fix creates a new exact head.

Reviews are in Brazilian Portuguese unless a Work Order explicitly requires another language.


## Prompt artifact policy
All executor prompts for ISORYN must be delivered to the user as downloadable PDF artifacts, not as copyable prompt boxes. Repository Work Orders remain Markdown as canonical version-controlled sources; when a Work Order is handed to Codex, Coder, Qoder or another CLI executor, the user-facing handoff artifact must also be rendered as PDF. Reviews remain in Brazilian Portuguese. This policy applies across all chats working on KayzenRoot/isoryn-engine.


## Review-first direct correction policy
This policy is mandatory for every review cycle in every chat working on `KayzenRoot/isoryn-engine`.

1. After any Codex/Coder/Qoder executor delivery, the reviewer MUST independently audit the resulting Git/PR/evidence state before admitting continuation.
2. If defects are found, the FIRST correction path is always direct reviewer/chat correction using the connected GitHub capabilities whenever the defect can be safely, causally and completely fixed and objectively validated from the current environment.
3. The reviewer SHOULD fix all CHAT_FIXABLE findings in the same review cycle, including repository files, governance/documentation drift, bounded configuration defects, tests/evidence defects that can be repaired here, and other safe in-scope corrections.
4. Codex/Coder/Qoder MUST NOT be used merely because a defect exists. Delegate a correction only when it is genuinely EXECUTOR_REQUIRED, such as local-machine/runtime state, unavailable administrative capability, broad implementation requiring the executor environment, dependency/toolchain execution unavailable to the reviewer, or a correction that cannot be safely validated here.
5. When residual EXECUTOR_REQUIRED findings remain, produce one bounded correction Work Order covering only those residual findings. The user-facing executor prompt MUST follow the PDF artifact policy. Preserve the same Work Order/PR when safe; do not create unnecessary parallel correction work.
6. After executor correction, perform a new independent review. Repeat direct correction first for any newly found CHAT_FIXABLE defects.
7. If the audit finds no blocking defect and all applicable acceptance/DoD gates are satisfied, do not create a correction prompt. Record APPROVED, promote the audited checkpoint delta through the governed flow, then compile the next necessary increment.
8. Never advance to the next increment while the current one is CORRECTION REQUIRED or BLOCKED. Never promote with a known HIGH/CRITICAL defect.
9. Every direct correction creates a new exact head and invalidates stale exact-head evidence; rerun the applicable validation/CI and bind the review to the corrected SHA.
10. Do not hide, downgrade or bypass failures to avoid executor usage. Direct correction is preferred only when it remains safe, scoped and objectively verifiable.
