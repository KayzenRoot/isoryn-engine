# ISORYN-WO-0001 Checkpoint Correction Record

Status: PROPOSED_ONLY_AWAITING_INDEPENDENT_REVIEW

This file is the executor's proposal. It does not promote anything: `docs/project-brain/13-CHECKPOINT.md` is the
canonical checkpoint, the derived bridge views move only with it, and promotion belongs to an independent audit of
the delivered head.

## Why the C02 promotion was revoked

The C02 independent review at `74f443f3d83c8bb1642314ab28632342fcf0b50f` correctly closed
`CANONICAL_WORKSPACE_MISMATCH`. The reviewer then promoted the checkpoint and obtained a green Governance run on
`a4c1aa6ee241d9d021483a79a2c8ed57b7d9bbf4`.

A real squash-merge attempt immediately exposed a separate governance defect that the static desired-state checks had
encoded instead of detecting:

- GitHub response: HTTP 405, `Repository rule violations found / Cannot update this protected ref.`
- live rule: branch ruleset `main-governance` (id 23776080) included `update`
- bypass state: `bypass_actors: []`, `current_user_can_bypass: never`
- effect: GitHub's restrict-updates rule allows only bypass actors to move the matching ref, so the protected `main`
  branch was not mergeable even through an otherwise valid pull request

## What correction C03 delivered

- The corrected desired state was applied to live ruleset 23776080 through the authorized local `gh` session. The
  ruleset now carries exactly `deletion`, `non_fast_forward`, `required_linear_history`, `pull_request`
  (squash-only, no approval gate this repository cannot satisfy) and `required_status_checks`
  (strict, context `Governance`). No `update` rule, no bypass actor added, no protection weakened.
- BEFORE/AFTER receipts, `gh ruleset check main` (five rules), `gh ruleset view`, the ruleset list and a second,
  idempotent application are under `.engineering/evidence/github`.
- `scripts/configure-github.ps1` now captures the per-ruleset read before upserting, because the ruleset list
  endpoint omits `rules`; two tests pin that capture and the fail-closed guard against a self-locking manifest.
- PR #2 is `OPEN`, `MERGEABLE`, `mergeStateStatus CLEAN`, and was not merged.
- HIVE v1.0.0 was re-proved for the C03 lineage against the reused isolated pinned stack at
  `70996f5322990010a171c46b9e4f0288f3e585d0`, including the real MCP session.
- `Governance` passed on every C03 head: run 35885436589 on `e0e0bd5056e68ce2b57ef68ade4fb46b50598cb8`, run
  35887146651 on `70996f5322990010a171c46b9e4f0288f3e585d0`, and run 35887776564 on the delivered head
  `12e2148e5353e6424639d1afdf26954e0abc6531`, each read from GitHub for the exact commit named. The live ruleset was
  re-read alongside the last one and still applies five rules with no bypass actor.

## Proposed checkpoint field values

For the reviewer to apply, in `docs/project-brain/13-CHECKPOINT.md`, only if C03 is approved at the delivered head:

- `## STATUS` - `BOOTSTRAP APPROVED`
- `## VERSION` - unchanged: `ISORYN 0.0 - Clean Foundation`
- `## PHASE` - unchanged: `0 - GEF/HIVE Repository Foundation`
- `## IN PROGRESS` - `NONE. ISORYN-WO-0001 was independently reviewed and APPROVED at head <reviewer fills the
  exact audited head>; this checkpoint records the reviewer-authorized promotion of the C01, C02 and C03
  correction chain.`
- `## BLOCKERS` - `NONE. Correction C03 removed the self-locking restrict-updates rule from the live
  main-governance ruleset and read the applied state back through gh, retaining deletion, non-fast-forward, linear
  history, pull-request and required Governance protections with no bypass actor added. Product/engine
  implementation remains unauthorized until the next governed discovery Work Order admits it.`
- `## NEXT STEP` - `Merge approved PR #2 by squash into main, confirm the resulting main head, then admit
  ISORYN-WO-0002-ARCHITECTURE-TOOLCHAIN-DISCOVERY from that exact base. Freeze architecture and toolchain decisions
  only from measured evidence before engine implementation begins.`

Then regenerate `.engineering/CHECKPOINT.md` and `.engineering/CHECKPOINT.json` from those values, since the
validator fails on any drift between the canonical checkpoint and its derived views.

## What this correction explicitly does not authorize

No merge, no checkpoint promotion, no engine or toolchain work, no pin change, no bypass actor, no weakening of any
rule. The C01 and C02 records above and in the Evidence Bundle stay as written for the heads they describe.
