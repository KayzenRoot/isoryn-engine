# ISORYN-WO-0001 Proposed Checkpoint Delta

Status: PROPOSED_ONLY
Rule: an executor may propose promotion but must not self-approve or promote it (AGENTS.md Review,
`.engineering/gef/GEF-POLICY.md` item 8, Work Order stop condition). Apply only after an independent audit returns
APPROVED at the exact candidate head.
Revision: this is the delta proposed for correction C02. The C01 delta proposed the same field values and carried
`CANONICAL_WORKSPACE_MISMATCH`; C02 closes that blocker with a re-executed proof at the canonical workspace instead
of relaxing the criterion, and only an independent re-audit at the C02 head can promote it.

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
| BLOCKERS | `CANONICAL_WORKSPACE_MISMATCH: ...` | `NONE. C02 materialized the canonical workspace as a real directory at D:\\Hive\\Projects\\isoryn-engine and re-proved the isolated pinned HIVE v1.0.0 runtime against that exact path at 8eba7b4ef6258d708fdf24554822310531f151f3, so the mismatch C01 left open is closed by current proof rather than by editing the words out. Product/engine implementation remains unauthorized.` | Evidence Bundle `c02Recovery`, `.engineering/evidence/hive-preflight.json` |

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
| Local HIVE registration/index/corpus sync evidenced | PASS at the canonical workspace | C02 re-ran the whole pipeline against `D:\\Hive\\Projects\\isoryn-engine`: `hive-preflight.json` (READY, index and corpus COMPLETED, `working_tree_clean` observed), `hive-retrieval-proof.json` (three canonical targets with measured ranks), `mcp-proof.json` (real session through `scripts/hive_mcp.py` on the isolated pinned project) |
| Main protection/ruleset evidenced or gap recorded | PASS with recorded gaps | `.engineering/evidence/github/`, `unsupportedPlatformFeatures` |
| Audit returns APPROVED | AWAITING INDEPENDENT RE-REVIEW | the reviewer who issued C02 must re-audit at the corrected head; C02 only supplies the proof that closes the criterion that reviewer blocked on |
| Checkpoint promoted after audit | NOT DONE (correct) | this file is a proposal only |
