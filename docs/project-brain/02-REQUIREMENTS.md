# ISORYN Requirements

Status: DISCOVERY_BASELINE (extended by ISORYN-WO-0002)

PR-001: use GEF governance and exact-head evidence.
PR-002: use HIVE as preferred derived context/retrieval/checkpoint layer while Git remains canonical.
PR-003: maintain explicit contracts with HIVE, CORE and IRIS.
PR-004: Godot 4.x is the foundation direction; exact upstream/fork/version strategy must be frozen before engine implementation.
PR-005: performance work defines measurable CPU/GPU/RAM/VRAM/frame-time/loading targets before claiming improvement.
PR-006: graphics/lighting work defines objective quality/performance comparisons against an admitted baseline.
PR-007: support progressive hardware adaptation.
PR-008: camera-aware/isometric relevance scheduling should be exploited where measurable.
PR-009: proprietary technologies include purpose, assumptions, proof obligations, fallback and compatibility impact.
PR-010: preserve upstream synchronization where practical.
PR-011: native code/plugins/scripting/import pipelines/external tools are threat-modeled and tested.
PR-012: a release is complete only when functional, tested, documented, deployable and objectively validated.

Requirements added by discovery, because the Work Order proved they were missing rather than assumed:

PR-013: any engine build claim requires a reproducible command receipt - command line, toolchain versions, exit code, timestamps and produced-binary identity - recorded at an exact head.
PR-014: any capability claim about upstream must cite the pinned tag, the commit and the path or symbol; a claim about a gap must distinguish a searched absence from an untested assumption.

## Discovery-time satisfaction state

| Requirement | State after ISORYN-WO-0002 | Where it is carried |
| --- | --- | --- |
| PR-001 | Satisfied and exercised | GEF namespaces, Evidence Bundle, Governance CI |
| PR-002 | Satisfied; HIVE re-proved per head | `docs/project-brain/05-INTEGRATION-CONTRACTS.md`, WO-0002 evidence `hivePreflight` / `mcpProof` |
| PR-003 | HIVE and Godot contracts concrete; CORE and IRIS explicitly unfrozen | `05-INTEGRATION-CONTRACTS.md` |
| PR-004 | Baseline and topology proposed for freeze, pending audit | ADR-0001, `08-GODOT-BASELINE-AND-TOPOLOGY.md` |
| PR-005 | Metric vocabulary and workload contract defined; first baseline measured | `09-TOOLCHAIN-AND-BENCHMARK-BASELINE.md` |
| PR-006 | Gate defined per family; no comparison claimed without an admitted workload | `06-MASTER-MODULE-INDEX.md` proof-gate column |
| PR-007 | Host inventory captured; hardware-class matrix still open (one class measured) | `06-MASTER-MODULE-INDEX.md` M-29, toolchain receipt |
| PR-008 | Relevance-first ordering kept; PT-01 carries the proof obligation | `07-PROPRIETARY-TECHNOLOGY-REGISTRY.md` PT-01 |
| PR-009 | Registry populated with proposal-level entries | `07-PROPRIETARY-TECHNOLOGY-REGISTRY.md` |
| PR-010 | `custom_modules` overlay topology preserves upstream unmodified | ADR-0001, ADR-0003 seam 3 |
| PR-011 | Import/plugin/native surfaces mapped; threat model for third-party native code deferred (PT-10) | `06-MASTER-MODULE-INDEX.md` M-25/M-27, `10-SECURITY-GOVERNANCE.md` |
| PR-012 | Unchanged; product increments still need full evidence | `15-DEFINITION-OF-DONE.md` |
| PR-013 | First receipts produced with this Work Order | `.engineering/evidence/wo-0002/` |
| PR-014 | Applied throughout the discovery documents | `06`, `08`, ADR-0001 |
