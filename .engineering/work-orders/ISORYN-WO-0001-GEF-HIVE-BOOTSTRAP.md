# ISORYN-WO-0001 - Synchronization, GEF/HIVE Bootstrap & GitHub Foundation

OBJECTIVE: synchronize the clean ISORYN repository into the canonical local workspace, complete and validate the
GEF/GEFI + HIVE bootstrap, configure project-scoped Codex/CLI HIVE MCP integration, harden the GitHub repository
professionally through authenticated gh, create objective evidence, push a governed branch, open one PR, wait for
required CI, and stop for independent review. No engine or product feature is implemented by this Work Order.

HIVE PREFLIGHT: repository root, branch, HEAD and cleanliness must be known before any product edit; ISORYN must
resolve to a registered HIVE project through the read-only MCP surface; retrieval may only supply minimum sufficient
context; Git/static/test evidence outranks retrieved context. A HIVE failure is reported as degraded-safe with the
exact failing step, never as success.

CANONICAL BASIS: AGENTS.md, .engineering/SOURCE-HIERARCHY.md, docs/project-brain/13-CHECKPOINT.md, then Decisions,
Scope, Definition of Done, Architecture and Requirements. Upstream pins are GEF Bootstrap v1.0.0 at
866fe3af8cccc65c929aaf6a47a924401fa448b3 and HIVE v1.0.0 at a53b5b9fcf55c32a5696180fb1b1ef80ccd1edcf, validated
read-only and never vendored. Executor handoff artifact: ISORYN-WO-0001-SYNC-GEF-HIVE-GITHUB-FOUNDATION.pdf.

CONTEXT BUDGET: read the checkpoint first, then only the canonical files the failing or unproven criterion needs.
Retrieve through HIVE rather than re-reading whole directories; cap per-step evidence to the artifact that proves the
criterion. Do not load GEF/HIVE/CORE/IRIS source trees into this workspace to save a lookup.

RISK/ASSURANCE: highest risks are destructive local synchronization and unproven platform claims. Mitigation: inspect
before moving, verify byte equality and Git integrity before removing anything, refuse to discard uncommitted user
work, and require executed command output for every HIVE, MCP, CI and GitHub statement. Toolchain and build assurance
is explicitly deferred (see OUT OF SCOPE).

CONTEXT: new repository; canonical local workspace D:\Hive\Projects\isoryn-engine; HIVE/CORE/IRIS are reference bases;
Godot 4.x is engine foundation direction.

SCOPE: local synchronization; Source Pack audit; GEF target-project artifacts; HIVE MCP/launcher/registration and
project-scoped CLI MCP configuration; deterministic governance validator/tests; governance CI; PR template and
repository governance files; professional GitHub settings and main-governance ruleset; Evidence Bundle; one PR.

OUT OF SCOPE: production engine implementation; Godot fork/toolchain freeze; product module implementation; renderer,
runtime, editor, packaging, simulation or benchmark code; any change to an approved decision; merging.

FILES/SOURCES TO READ: AGENTS.md; .engineering/SOURCE-HIERARCHY.md; canonical checkpoint/decisions/scope/DoD/
architecture/requirements; docs/GEF-BOOTSTRAP.md; docs/HIVE-INTEGRATION.md; scripts/validate_governance.py;
scripts/hive_bootstrap.py; scripts/hive_mcp.py; .codex/config.toml; .github/workflows/governance.yml.

REQUIREMENTS: exact-head evidence; HIVE-first preflight; Git canonical; no silent degraded HIVE; no vendoring
HIVE/CORE/IRIS/GEF; validator must cover every artifact that is actually mandatory without being weakened; ruleset
application must be idempotent and read back.

ARCHITECTURE RULES: integrations remain external/versioned; machine paths stay configuration/documentation, not
portable runtime constants; no shared-database coupling with HIVE, CORE or IRIS.

CONSTRAINTS: no force-push/history rewrite; no secret material; no product code; commit only Work Order scope; base
branch main; working branch isoryn-wo-0001-foundation; do not merge; do not self-approve a checkpoint promotion.

ACCEPTANCE CRITERIA:
1. canonical local workspace exists with the correct origin and no unexpected conflict or loss;
2. repository audit records present/missing/forbidden files with cited paths, plus no stale canonical statements;
3. GEF target-project contract is validated against GEF v1.0.0 without inventing unsupported modules or CLI claims;
4. HIVE MCP client configuration is project-scoped and uses only documented read tools;
5. ISORYN HIVE registration/index/sync status is proven or the exact capability blocker is recorded;
6. GitHub professional settings and one active main-governance ruleset are applied through authenticated gh and read
   back; unsupported platform capabilities are recorded as NOT_AVAILABLE rather than simulated;
7. governance validator/tests/CI pass at the exact candidate head;
8. every mandatory governance artifact is present and consistent; no ornamental files are added;
9. PDF prompt policy and review-autofix policy are preserved;
10. no product/engine code is introduced;
11. Evidence Bundle is complete and exact-SHA-bound;
12. PR is open, green and unmerged for independent review;
13. no known HIGH/CRITICAL defect remains.

TESTS: python scripts/validate_governance.py; python -m py_compile scripts/validate_governance.py
scripts/hive_bootstrap.py scripts/hive_mcp.py; python -m unittest discover -s tests -p "test_*.py" -v; git diff --check;
repository secret scan; HIVE health/inspect/index/corpus readback; MCP tools/list and tools/call handshake; GitHub
Actions exact-head Governance check; gh pr checks --watch and --required; gh ruleset list/view/check; REST readback of
repository settings and available security settings.

EVIDENCE: .engineering/evidence/ISORYN-WO-0001-EVIDENCE.md, bound to the exact base and head SHAs, containing files
changed, validator/compiler/test results, HIVE preflight truth and failure classification, MCP handshake, GitHub
BEFORE/AFTER administrative state, ruleset id and effective normalized rules, unsupported platform features, errors
found and corrected, risks and rollback posture, PR/CI state, proposed checkpoint delta and the stop-condition result.
Raw command receipts live under .engineering/evidence/github/.

DELIVERABLES: repository foundation, evidence bundle, PR/settings receipt, proposed Checkpoint Delta.

REVIEW FORMAT: Portuguese (Brazil), findings first, exact-head verdict.

STOP CONDITION: stop when the local repository is synchronized, bootstrap is complete, GEF/HIVE integration is
objectively validated, HIVE registration/indexing is proven, GitHub hardening is applied and read back, the PR exact
head is green and evidence is complete - or at BLOCKED_ADMIN_PERMISSION / STALE_CONTEXT / BLOCKED_USER_WORK. Do not
begin engine module implementation.
