# ISORYN-WO-0001 Proposed Checkpoint Delta

Status: PROPOSED_ONLY
Rule: an executor may propose promotion but must not self-approve or promote it (AGENTS.md Review,
`.engineering/gef/GEF-POLICY.md` item 8, Work Order stop condition). Apply only after an independent audit returns
APPROVED at the exact candidate head.

## Canonical checkpoint
`docs/project-brain/13-CHECKPOINT.md` is the only canonical state source. `.engineering/CHECKPOINT.md` and
`.engineering/CHECKPOINT.json` are derived views and must be regenerated from it, never edited independently.

## Field deltas

| Field | Current | Proposed | Authority |
| --- | --- | --- | --- |
| STATUS | `BOOTSTRAP ACTIVE` | `BOOTSTRAP AUDIT PENDING` | Work Order stop condition: execution finished, independent review outstanding |
| PHASE | `0 - GEF/HIVE Repository Foundation` | unchanged | phase 0 is still the active phase until the audit promotes it |
| IN PROGRESS | `ISORYN-WO-0001-GEF-HIVE-BOOTSTRAP.` | `NONE. ISORYN-WO-0001 delivered and awaiting independent audit.` | Work Order: stop for independent review, do not advance to the next increment |
| NEXT STEP | validate local HIVE registration, configure professional main ruleset, collect exact-head CI/evidence, audit, promote | `Audit ISORYN-WO-0001 at the exact PR head; on APPROVED, promote this delta and open the architecture/toolchain discovery Work Order` | Definition of Done and the review-first policy |
| BLOCKERS | as recorded | `NONE. HIVE_RUNTIME_DRIFT was closed by correction C01: the pinned HIVE v1.0.0 baseline runs isolated and re-proves health, unique registration, READY inspection, index, CURRENT corpus, canonical retrieval and a real MCP session at f293fabfd4cde0a202d917b75eee590567b2027e. The machine default on 127.0.0.1:8000 is HIVE 1.0.2 with no ISORYN registration, so ISORYN calls must name the pinned stack explicitly. Product/engine implementation remains unauthorized.` | Evidence Bundle `c01Recovery` and `environmentDrift.closedBy` |

## Explicitly not changed
- No adopted decision is amended, superseded or reversed; `docs/project-brain/16-DECISIONS-LEDGER.md` is untouched.
- No engine, Godot version, fork topology, toolchain or build-pipeline claim is added, because no executed benchmark
  supports one (`docs/project-brain/03-SCOPE.md` forbids unmeasured performance/quality claims).
- `docs/project-brain/15-DEFINITION-OF-DONE.md` gates stay intact; this delta reports against them instead of relaxing
  them.
- HIVE remains derived context only; nothing in this delta lets HIVE write canonical state.

## DoD reconciliation for the bootstrap gate
| Definition of Done element | Result | Where |
| --- | --- | --- |
| Source Pack passes deterministic validation | PASS | `scripts/validate_governance.py`, `.engineering/evidence/checks.json` |
| GEF target-project artifacts exist | PASS | `.engineering/gef/`, Work Order, Context Lock, Evidence Bundle |
| HIVE MCP/registration tooling exists and is unit-tested | PASS | `scripts/hive_mcp.py`, `scripts/hive_bootstrap.py`, `tests/` |
| Exact-head governance CI passes | recorded per head | `.engineering/evidence/ISORYN-WO-0001-EVIDENCE.md` `checks` and `followUpHeads` |
| Local HIVE registration/index/corpus sync evidenced | PASS at `f293fabfd4cd` | Historical PASS remains for `d5de04c5ac157236de55875bb530f81d3d02ce86`; correction C01 re-proved it against the pinned v1.0.0 baseline on its own Compose project - see Evidence Bundle `c01Recovery.results` and `hive-preflight.json` |
| Main protection/ruleset evidenced or gap recorded | PASS with recorded gaps | `.engineering/evidence/github/`, `unsupportedPlatformFeatures` |
| Audit returns APPROVED | AWAITING INDEPENDENT RE-REVIEW | the CORRECTION REQUIRED verdict named one residual item - re-prove current local HIVE without disrupting concurrent work - and C01 delivered it; promotion still belongs to a fresh independent audit at the exact PR head |
| Checkpoint promoted after audit | NOT DONE (correct) | this file is a proposal only |
