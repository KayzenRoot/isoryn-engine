# ISORYN Source Pack Read Order

Status: DISCOVERY_BASELINE (extended by ISORYN-WO-0002)

1. 13-CHECKPOINT.md
2. 16-DECISIONS-LEDGER.md
3. 03-SCOPE.md
4. 15-DEFINITION-OF-DONE.md
5. 04-ARCHITECTURE.md
6. 02-REQUIREMENTS.md
7. 08-GODOT-BASELINE-AND-TOPOLOGY.md
8. 06-MASTER-MODULE-INDEX.md
9. 07-PROPRIETARY-TECHNOLOGY-REGISTRY.md
10. 09-TOOLCHAIN-AND-BENCHMARK-BASELINE.md
11. docs/adr/ADR-0001-godot-baseline-and-repository-topology.md
12. docs/adr/ADR-0002-build-toolchain-and-upstream-sync.md
13. docs/adr/ADR-0003-extension-seam-policy.md
14. 10-SECURITY-GOVERNANCE.md
15. 11-TEST-PLAN.md
16. 12-LOCAL-DEPLOYMENT.md
17. 05-INTEGRATION-CONTRACTS.md
18. 14-BACKLOG.md

Items 7-13 are the architecture baseline produced by ISORYN-WO-0002. They are read after the governance
core because they depend on Scope, Definition of Done and the accepted decisions, and they are read before
the test, deployment and integration docs because those now reference the frozen seams and metric vocabulary.

Git is canonical. HIVE and GEF derived views never silently supersede these sources. Upstream Godot is
external reference material: it is cited by tag and commit, and it is never vendored into this repository.
