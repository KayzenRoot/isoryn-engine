# ISORYN-WO-0001 - GEF/HIVE Bootstrap

OBJECTIVE: establish the clean professional ISORYN repository foundation with GEF v1.0.0 and HIVE v1.0.0 integration.

CONTEXT: new repository; canonical local workspace D:\Hive\Projects\isoryn-engine; HIVE/CORE/IRIS are reference bases; Godot 4.x is engine foundation direction.

SCOPE: Source Pack; GEF target-project artifacts; HIVE MCP/bootstrap tooling; deterministic governance validator/tests; governance CI; PR template; repository-setting handoff.

OUT OF SCOPE: production engine implementation; Godot fork/toolchain freeze; product module implementation.

FILES/SOURCES TO READ: AGENTS.md; .engineering/SOURCE-HIERARCHY.md; canonical checkpoint/decisions/scope/DoD/architecture/requirements; docs/GEF-BOOTSTRAP.md; docs/HIVE-INTEGRATION.md.

REQUIREMENTS: exact-head evidence; HIVE-first preflight; Git canonical; no silent degraded HIVE; no vendoring HIVE/CORE/IRIS/GEF.

ARCHITECTURE RULES: integrations remain external/versioned; machine paths stay configuration/documentation, not portable runtime constants.

CONSTRAINTS: no force-push/history rewrite; no secret material; no product code.

ACCEPTANCE CRITERIA:
1. required governance files exist and validator passes;
2. HIVE MCP launcher and registration/index/corpus bootstrap exist and unit tests pass;
3. GitHub Governance workflow passes at exact head;
4. local HIVE registration/index/corpus status is evidenced from Windows workspace;
5. professional main ruleset is evidenced or an exact capability gap is recorded;
6. audit returns APPROVED before checkpoint promotion.

TESTS: python scripts/validate_governance.py; python -m py_compile scripts/validate_governance.py scripts/hive_bootstrap.py scripts/hive_mcp.py; python -m unittest discover -s tests -p "test_*.py" -v; GitHub Governance workflow.

DELIVERABLES: repository foundation, evidence bundle, PR/settings receipt if applicable, proposed Checkpoint Delta.

REVIEW FORMAT: Portuguese (Brazil), findings first, exact-head verdict.

STOP CONDITION: stop at READY_FOR_BOOTSTRAP_AUDIT or BLOCKED. Do not begin engine module implementation.
