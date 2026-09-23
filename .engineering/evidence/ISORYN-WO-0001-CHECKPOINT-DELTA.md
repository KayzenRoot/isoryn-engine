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
| BLOCKERS | as recorded | `CANONICAL_WORKSPACE_MISMATCH: C01 successfully closed HIVE_RUNTIME_DRIFT by isolating and re-proving HIVE v1.0.0, but the proof was executed against D:\\Projects\\isoryn-engine while README.md, docs/project-brain/12-LOCAL-DEPLOYMENT.md and docs/project-brain/13-CHECKPOINT.md still define D:\\Hive\\Projects\\isoryn-engine as the canonical workspace. No ADR supersedes that authority. Bootstrap promotion remains blocked until the repository is safely synchronized at the canonical workspace and HIVE registration/index/corpus/MCP is re-proved against that path without disrupting concurrent HIVE runtimes. Product/engine implementation remains unauthorized.` | Evidence Bundle `c01Recovery` and `environmentDrift.closedBy` |

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
| Local HIVE registration/index/corpus sync evidenced | CORRECTION REQUIRED | C01 proves the isolated pinned runtime itself, but `hive-preflight.json` explicitly states the proof workspace was `D:\\Projects\\isoryn-engine`, not the canonical `D:\\Hive\\Projects\\isoryn-engine`; synchronize and re-prove against the canonical workspace before promotion |
| Main protection/ruleset evidenced or gap recorded | PASS with recorded gaps | `.engineering/evidence/github/`, `unsupportedPlatformFeatures` |
| Audit returns APPROVED | CORRECTION REQUIRED | independent re-review confirms C01 closed runtime isolation, but found an unsatisfied canonical-workspace acceptance criterion; promotion remains blocked until that local-path mismatch is corrected and re-proved |
| Checkpoint promoted after audit | NOT DONE (correct) | this file is a proposal only |
