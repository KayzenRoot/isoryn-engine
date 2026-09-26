# ISORYN Scope

Status: DISCOVERY_BASELINE (extended by ISORYN-WO-0002)

## NECESSARY now
Repository/governance bootstrap; GEF v1.0.0 target-project contract; HIVE v1.0.0 structural/MCP integration; professional GitHub baseline; architecture discovery/module map; benchmark strategy; explicit HIVE/CORE/IRIS/Godot boundaries.

Completed and carried forward: bootstrap (ISORYN-WO-0001, merged to `main`) and architecture/toolchain discovery
(ISORYN-WO-0002, awaiting independent audit). The discovery output is the baseline set: `06-MASTER-MODULE-INDEX.md`,
`07-PROPRIETARY-TECHNOLOGY-REGISTRY.md`, `08-GODOT-BASELINE-AND-TOPOLOGY.md`,
`09-TOOLCHAIN-AND-BENCHMARK-BASELINE.md` and ADR-0001/0002/0003.

## Product scope to plan
Rendering; lighting/GI/shadows; materials/shaders; textures/VRAM; geometry/GPU-driven rendering; LOD/HLOD; visibility/occlusion; world/asset streaming; terrain; vegetation; water/weather; VFX; animation; characters; physics; navigation; mass entities; gameplay/runtime support; procedural systems; isometric camera systems; networking; audio; UI/editor tooling; persistence; modding/UGC; localization; security; profiling/performance; hardware adaptation; build/release; simulation/testing; AI-native editor/automation.

Each family above has exactly one row in `docs/project-brain/06-MASTER-MODULE-INDEX.md` with a class
(NECESSARY / IMPORTANT / FUTURE / OUT OF SCOPE), a seam, and the proof gate that must run before it can move.
Scope defines the families; the index defines their current standing. Adding a family means editing this file
first, never the index alone.

`navigation` was added here during ISORYN-WO-0002 rather than only in the index: upstream ships a first-party
navigation server and navmesh generator (`servers/navigation_3d/`, `modules/navigation_3d/`), and the isometric
product intent cannot plan agent movement without pathfinding. Listing it is a planning-scope decision, not a
capability claim - M-16 stays class IMPORTANT behind its own proof gate.

## OUT OF SCOPE for bootstrap
Production engine code; permanent Godot fork decision without evidence; copying HIVE/CORE/IRIS internals; unmeasured performance/quality claims; uncontrolled scope expansion.

## OUT OF SCOPE for the discovery increment (recorded so the next Work Order chooses deliberately)
- Any production renderer, runtime, editor or gameplay implementation, and any implementation of a registry entry.
- Vendoring an engine tree or engine build outputs into this repository (ADR-0001).
- Creating or using a fork repository (seam 4 needs its own ADR plus explicit authorization).
- Adopting a Godot pre-release because it is newer.
- Building the engine in CI on every push: the toolchain is frozen, but the cost (external pinned clone, a compiler chain, a full-template build measured in `docs/project-brain/09-TOOLCHAIN-AND-BENCHMARK-BASELINE.md`, and an editor target that the discovery host cannot build at all) makes it a separate admission.
- The `accesskit` and `d3d12` engine driver paths, which were disabled for this build because their prerequisites are extra host installation state.
- A second hardware class or a second operating system: every WO-0002 measurement is one mobile-APU Windows host, and it is labelled that way.
- Shipping/support promises for the 4.6 compatibility reference line.
