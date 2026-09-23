# GEF Bootstrap in ISORYN

ISORYN targets GEF Bootstrap v1.0.0 at upstream commit 866fe3af8cccc65c929aaf6a47a924401fa448b3. GEF v1.0.0 is a source workspace, not a published global npm CLI, so ISORYN materializes the target-project governance contract instead of vendoring the whole repository.

Installed surfaces: canonical Source Pack, source hierarchy/checkpoint bridges, GEF adoption/profile/source bridge/
policy/protocol records, deterministic governance validation, GitHub CI/review scaffolding and HIVE-first executor
integration. The Work Order and Context Lock namespaces were materialized by ISORYN-WO-0001 under
`.engineering/work-orders/`, `.engineering/context-locks/` and `.engineering/evidence/`, matching the file naming that
GEF v1.0.0 uses for its own governance records.

## Contract audit (ISORYN-WO-0001)
Disputed artifact names were classified against the pinned release rather than against filenames remembered from
chat. Method: `git clone --filter=blob:none --no-checkout --branch v1.0.0` of the GEF source, then
`git ls-tree -r --name-only HEAD` (976 tracked files) and `git grep` over that tree. The tag `v1.0.0` peels to
`866fe3af8cccc65c929aaf6a47a924401fa448b3`.

| Artifact name | Classification | Evidence |
| --- | --- | --- |
| `.engineering/context-locks/<WO-ID>.json` | REQUIRED (pattern) | GEF keeps six of them, e.g. `.engineering/context-locks/GBS-WO-M13-001.json` |
| `.engineering/evidence/<WO-ID>-EVIDENCE.md` | REQUIRED (pattern) | GEF keeps 31, e.g. `.engineering/evidence/GBS-WO-M13-001-EVIDENCE.md` |
| `.engineering/REVIEW-AUTOFIX-POLICY.md` | REQUIRED (Work Order instruction only) | absent from the GEF tree; ISORYN-WO-0001 names the file and its core rule |
| `docs/GEF-INTEGRATION.md` | NOT REQUIRED | absent from the GEF tree; `docs/GEF-BOOTSTRAP.md` already carries adoption, pins and validation, and `.engineering/SOURCE-HIERARCHY.md` has no authority slot for a second GEF document |
| `scripts/gef_preflight.py` | NOT REQUIRED | absent from the GEF tree; GEF's kernel check is a library (`packages/adoption-engine/src/policy.ts:106` `MGK_REQUIRED`), and ISORYN's equivalent deterministic preflight is `scripts/validate_governance.py` |
| `harness/tests/test_gef_core_conformance.py` | NOT REQUIRED | absent from the GEF tree, which tests its own packages under `tests/`; ISORYN asserts kernel conformance through the validator and `tests/test_governance.py` |
| `.gef/project.json`, `GEF-BASELINE.json`, `GEF-CURRENT.json`, `adopted-version.json` | NOT REQUIRED | no `.gef/` directory and no such filename exists anywhere in the pinned release tree; ISORYN records adoption in `.engineering/gef/` |

Identifier precision: the Work Order cites `GEF-WAVE-00-CANONICAL-REQUIREMENT-MATRIX`,
`GEF-IMPLEMENTED-MINIMAL-GOVERNANCE-KERNEL` and `PROJECT-STATE-CHECKPOINT-BRIDGE` as literal identifiers. None appears
in the pinned tree; the same mechanisms appear as the Canonical Requirement Matrix (module M09) and the Minimal
Governance Kernel (module M13), and the checkpoint bridge appears as GEF's own
`.engineering/CHECKPOINT.md`/`CHECKPOINT.json` pair. ISORYN therefore implements the semantic classes and does not
create files to match unreleased identifier spellings. `PC-08` (no secrets or machine-local values in portable config,
`planning/modules/area-a-foundation-and-governance/m02-configuration-and-schema/S02-project-configuration.md:95`),
`SC-04` (closed core, `.../S03-schemas.md:60`) and `SC-06` (explicit validation phases, `.../S03-schemas.md:78`) are
enforced by `scripts/validate_governance.py`.

Independent approval: GEF's own reviewer agent instructs the reviewer not to invent an independent approval identity
(`.github/agents/gef-reviewer.agent.md`). ISORYN has one owner who is also the pull request author, so
`require_code_owner_review` and required approvals stay off and `.github/CODEOWNERS` is routing metadata only.


Upstream validation:
git clone https://github.com/KayzenRoot/gef-bootstrap.git
cd gef-bootstrap
git checkout v1.0.0
npm ci
npm run validate
