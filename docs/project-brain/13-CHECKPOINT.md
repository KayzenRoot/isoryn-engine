# ISORYN Checkpoint

## STATUS
BOOTSTRAP CORRECTION REQUIRED

## VERSION
ISORYN 0.0 - Clean Foundation

## PHASE
0 - GEF/HIVE Repository Foundation

## OBJECTIVE
Establish the professional Source Pack, GEF v1.0.0 governance, HIVE v1.0.0 integration, Codex MCP bridge and exact-head governance CI before engine implementation begins.

## IN PROGRESS
ISORYN-WO-0001-C03-MAIN-RULESET-UNLOCK.

## BLOCKERS
MAIN_RULESET_SELF_LOCK: the live `main-governance` ruleset contains GitHub's restrict-updates rule while `bypass_actors` is empty. The attempted squash merge of approved PR #2 was rejected by GitHub with HTTP 405, "Repository rule violations found / Cannot update this protected ref." The repository desired state now removes that rule and adds regression guards, but the live administrative ruleset still requires executor-side `gh` application and fresh evidence.

## NEXT STEP
Execute `ISORYN-WO-0001-C03-MAIN-RULESET-UNLOCK`: apply the corrected live `main-governance` ruleset without the restrict-updates rule, capture BEFORE/AFTER receipts, verify pull-request merging is permitted, re-run exact-head Governance and return for independent re-review. Do not merge or begin engine implementation while this correction is open.
