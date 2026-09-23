# ISORYN GEF Evidence Specification

Every Evidence Bundle must identify Work Order, base SHA, head SHA, branch/PR when applicable, changed files, canonical inputs, tests/checks, security/performance/benchmark evidence when required, failures corrected, residual risks, HIVE preflight truth, and proposed Checkpoint Delta.

Evidence bound to an older head is stale for changed inputs. UNKNOWN is never converted into PASS.

## ISORYN namespaces
Namespaces follow the materialized GEF v1.0.0 convention observed in the pinned release
(`.engineering/evidence/<ID>-EVIDENCE.md`, `.engineering/context-locks/<ID>.json`):
- Evidence Bundle: `.engineering/evidence/<WO-ID>-EVIDENCE.md`, one per Work Order, updated in place. Its machine
  payload lives in a single fenced `json` block so the deterministic validator can read it and a reviewer can read the
  prose around it.
- Raw command receipts: `.engineering/evidence/github/` and sibling per-WO directories.
- Context Lock: `.engineering/context-locks/<WO-ID>.json`.
- Proposed checkpoint delta: `.engineering/evidence/<WO-ID>-CHECKPOINT-DELTA.md`.
- Evidence-only commits added after the bundle change no validated input. Each one is appended to `followUpHeads`
  with its own observed result, so no claim is carried over to a head it was not executed on.

## Required bundle fields
`schemaVersion`, `workOrder`, `role`, `baseSha`, `headSha`, `candidateHeadSha`, `branch`, `pr`, `upstreamPins`,
`canonicalInputs`, `filesChanged`, `checks`, `hivePreflight`, `mcpProof`, `github`, `unsupportedPlatformFeatures`,
`errorsFoundAndCorrected`, `residualRisks`, `rollback`, `proposedCheckpointDelta`, `stopCondition`, `verdict`.

## Result vocabulary
Every executed assertion carries `PASS`, `FAIL`, `NOT_AVAILABLE`, `DEFERRED_BY_WO` or `UNKNOWN`. `DEFERRED_BY_WO`
requires a quote of the clause that defers it. `UNKNOWN` may never be reported as `PASS`, and a toolchain, benchmark,
security or performance gate is never claimed as satisfied without an executed artifact.

