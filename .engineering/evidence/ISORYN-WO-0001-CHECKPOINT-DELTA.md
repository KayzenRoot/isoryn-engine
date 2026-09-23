# ISORYN-WO-0001 Checkpoint Correction Record

Status: PROMOTION_REVOKED_CORRECTION_REQUIRED

The C02 independent review at `74f443f3d83c8bb1642314ab28632342fcf0b50f` correctly closed
`CANONICAL_WORKSPACE_MISMATCH`. The reviewer then promoted the checkpoint and obtained a green Governance run on
`a4c1aa6ee241d9d021483a79a2c8ed57b7d9bbf4`.

A real squash-merge attempt immediately exposed a separate governance defect that the static desired-state checks
had encoded instead of detecting:

- GitHub response: HTTP 405, `Repository rule violations found / Cannot update this protected ref.`
- live rule: branch ruleset `main-governance` includes `update`
- bypass state: `bypass_actors: []`
- effect: GitHub's restrict-updates rule allows only bypass actors to update the matching ref, so the protected
  `main` branch is not mergeable even through an otherwise valid pull request

## Reviewer direct correction

The repository desired state removes the `update` rule. The governance validator and unit tests now reject any
future desired state that combines restrict-updates with no approved bypass actor. `scripts/configure-github.ps1`
also fails closed before applying such a manifest.

## Residual EXECUTOR_REQUIRED work

The available chat GitHub connection does not expose repository-ruleset administration writes. An executor with the
already-authorized local `gh` session must therefore:

1. synchronize the current PR branch;
2. apply `scripts/configure-github.ps1` so live ruleset id 23776080 matches the corrected manifest;
3. capture BEFORE/AFTER ruleset receipts and `gh ruleset check main`;
4. prove the live ruleset no longer contains `update` while retaining deletion, non-fast-forward, linear history,
   pull-request and required `Governance` protections;
5. refresh the WO-0001 Evidence Bundle and exact-head CI evidence;
6. stop for independent review without merging.

The prior promotion is revoked until C03 is independently approved. Product/engine implementation remains blocked.
