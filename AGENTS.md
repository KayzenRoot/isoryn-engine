# ISORYN Executor Contract

ISORYN is governed by GEF and is HIVE-first.

## Authority
1. Resolve authority through .engineering/SOURCE-HIERARCHY.md.
2. Read docs/project-brain/13-CHECKPOINT.md first.
3. Then read Decisions, Scope, Definition of Done, Architecture and Requirements as required by the active Work Order.
4. Git and exact executable evidence outrank derived summaries and chat memory.
5. Product implementation requires an admitted Work Order.

## HIVE-first preflight
Before product edits resolve repository root, branch, HEAD and cleanliness; verify the HIVE v1.0.3 context/MCP baseline; resolve ISORYN through HIVE's read-only MCP; retrieve only minimum sufficient context; prefer deterministic Git/static/test proof over LLM inference; record Git/HIVE basis in evidence.

HIVE v1.0.3 reference read-only MCP tools (confirm actual exposure): project.list, project.status, context.build, context.search, memory.search, memory.get, checkpoint.read.

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

## HIVE v1.0.3 context-first work and prompt contract

The current HIVE executor-context baseline is the published **v1.0.3** read-only MCP surface. This is a context and prompt-preparation baseline; it does **not** change this repository's product dependency, runtime, compatibility pin, or HIVE V1/V2 integration contract. Keep those project-specific pins unchanged unless their own authorized Work Order validates and admits an upgrade. This repository's Git state, approved checkpoint, source hierarchy, decisions, scope, and active Work Order remain authoritative over HIVE-derived memory/context.

### Preflight

1. Confirm the exact repository, branch, HEAD/base SHA, and active Work Order or issue before building context. Read this repository's checkpoint/source hierarchy and the Work Order's scope, allowed files, acceptance criteria, and stop condition.
2. When HIVE MCP is available in this execution surface, verify the handshake and the reported v1.0.3 context baseline. Resolve this repository by its actual registered identity; use only an existing, canonical task ID. Never guess a project or task ID.
3. Use only read-only tools actually exposed by the handshake. The v1.0.3 reference surface includes `project.list`, `project.status`, `context.build`, `context.search`, `memory.search`, `memory.get`, and `checkpoint.read`. Build task context only for a valid task ID. Retrieve the minimum context needed for this Work Order; do not load unrelated history or the whole corpus.
4. Record the exact Git basis and only HIVE version, project/task identity, source references, or context fingerprint actually returned. A HIVE summary is derived context, not canonical approval or evidence that an unobserved check passed.
5. If HIVE is absent, stale, mismatched, or not exposed here, label it accurately and continue from canonical repository sources whenever the Work Order permits. Finish independent authorized work and do not stop for routine confirmation. Mark BLOCKED only when an explicit gate requires unavailable HIVE evidence. Never claim local HIVE access from a hosted execution surface, or vice versa.
6. Do not synchronize/reindex a corpus, create tasks, write a database, call a provider, or mutate remote/runtime state unless the active Work Order explicitly authorizes that operation.

### Compact HIVE-grounded executor prompt

When preparing a Codex/Cursor or other executor prompt, include only the task-relevant context and these fields:

- **Identity:** repository/path, Work Order/issue, branch, exact base and current HEAD.
- **Authority:** canonical checkpoint and source paths; the active Work Order and Context Lock, if present.
- **HIVE context:** v1.0.3 handshake status, verified project/task IDs, and returned source references/fingerprint — or the truthful status `UNAVAILABLE`, `STALE`, or `NOT_REQUIRED`.
- **Work:** objective, exact allowed change surface, acceptance criteria, required focused checks, evidence to return, exclusions, and stop condition.
- **Execution direction:** complete every authorized step, fix review findings within scope, perform the required review, and report which checks actually ran. Do not ask for routine confirmation; do not widen scope or claim unperformed work.

Prefer canonical file paths and short HIVE context references over copying full documents or chat history. Keep stable policy, Work Order-specific requirements, and volatile runtime evidence in separate, compact sections.
