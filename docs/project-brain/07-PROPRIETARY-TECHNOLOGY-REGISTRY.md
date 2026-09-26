# ISORYN Proprietary Technology Registry

Status: DISCOVERY_BASELINE (ISORYN-WO-0002)

Every entry below is `PROPOSED / NOT ADMITTED`. This registry records **obligations**, not results: no
entry claims that ISORYN's version of a capability is faster, better-looking or cheaper than upstream
Godot, because no admitted workload has been measured against an admitted baseline yet
(`docs/project-brain/11-TEST-PLAN.md`, `ISORYN-D-006`). An entry becomes an implementation only through
an admitted Work Order that carries the proof obligations written here.

Required fields per entry: purpose, hypothesis, dependencies, seam, maturity, proof obligations,
fallback, compatibility impact, risk. A proposal missing any field cannot be admitted.

## Index

| ID | Technology | Family (index) | Seam | Maturity |
| --- | --- | --- | --- | --- |
| PT-01 | Camera-aware relevance scheduler | M-20, M-07 | 2 -> 3 | PROPOSED |
| PT-02 | Budget-driven world streaming manager | M-08 | 3 | PROPOSED |
| PT-03 | LOD/HLOD chain generator | M-06 | 2 -> 3 | PROPOSED |
| PT-04 | GPU-driven instance culling pipeline | M-05, M-17 | 3 | PROPOSED |
| PT-05 | Isometric terrain system | M-09 | 3 | PROPOSED |
| PT-06 | VRAM budget and texture residency policy | M-04 | 2 -> 3 | PROPOSED |
| PT-07 | Mass heterogeneous agent layer | M-17 | 3 | PROPOSED |
| PT-08 | Deterministic capture and replay harness | M-31, M-28 | 2 | PROPOSED |
| PT-09 | Governed editor-automation contract | M-32 | 2 | PROPOSED |
| PT-10 | Third-party native extension trust boundary | M-25 | 2 | DEFERRED |

## PT-01 Camera-aware relevance scheduler

- **Purpose**: decide, before culling and batching, what an isometric/2.5D camera can actually influence, so downstream cost is paid only for relevant content. Follows the frozen optimization ordering in `docs/project-brain/04-ARCHITECTURE.md`.
- **Hypothesis (measurable)**: on a fixed isometric scene and a scripted camera path, a relevance pre-pass reduces the number of primitives and draw calls submitted per frame, relative to upstream visibility ranges plus occlusion culling.
- **Dependencies**: M-07 occlusion (`scene/3d/occluder_instance_3d.cpp`, `servers/rendering/renderer_scene_occlusion_cull.cpp`), M-20 camera nodes, M-28 `Performance` monitors for the measurement itself.
- **Seam**: start at 2 (addon/GDScript node + editor tool driving existing culling); escalate to 3 only if the pre-pass must run inside the cull loop.
- **Maturity**: PROPOSED / NOT ADMITTED.
- **Proof obligations**: run the PT-08 deterministic workload at identical quality settings; report `RENDER_TOTAL_PRIMITIVES_IN_FRAME`, `RENDER_TOTAL_DRAW_CALLS_IN_FRAME`, `TIME_PROCESS` percentiles and visual-preservation checks (no lost object that should have been visible). Average FPS alone is insufficient.
- **Fallback**: keep upstream visibility ranges and occlusion only (seam 1); the scheduler stays an authoring-time analysis tool.
- **Compatibility impact**: low at seam 2. At seam 3 it touches upstream culling order, so it must be additive (a module that registers, not a rewrite) to survive upstream rebases.
- **Risk**: correctness regressions are visually subtle (popping, missing shadows); mitigation is the golden-frame comparison of PT-08.

## PT-02 Budget-driven world streaming manager

- **Purpose**: upstream provides threaded resource loading primitives (`core/io/resource_loader.cpp`: `load_threaded_request`, `load_threaded_get_status`, `load_threaded_get`) but no spatial streaming manager (confirmed absence, index section D). ISORYN needs content to arrive against a frame-time budget instead of blocking.
- **Hypothesis**: a budget + priority loader reduces p95 frame-time spikes during a scripted traversal, at equal or lower memory, versus synchronous or unthrottled threaded loading.
- **Dependencies**: M-04 texture residency, M-06 LOD chains (a cell may load low LOD first), PT-01 relevance, PCK packaging.
- **Seam**: 3 (needs engine-visible scheduling hooks and its own module switch), with a seam-2 prototype over GDScript first.
- **Maturity**: PROPOSED / NOT ADMITTED.
- **Proof obligations**: hitch histogram (p50/p95/p99/max frame time), load-completion time per cell, peak `MEMORY_STATIC` and `RENDER_VIDEO_MEM_USED`, and a determinism check that the same traversal produces the same request order.
- **Fallback**: manual cell loading driven by scene author + `ResourceLoader` threaded API.
- **Compatibility impact**: moderate. It must not change upstream resource semantics; failure behavior is "load never completes" unless a timeout is explicit, so the contract must define cancellation and error propagation.
- **Risk**: highest scope risk in the registry; it is the subsystem most likely to be requested as a fork (seam 4) before evidence justifies it. Blocking seam 4 requires measurement first.

## PT-03 LOD/HLOD chain generator

- **Purpose**: upstream consumes LOD chains (`scene/resources/mesh.h` surface LOD dictionaries; `doc/classes/GeometryInstance3D.xml` `visibility_range_*`, `lod_bias`) but does not generate them or build hierarchical clusters.
- **Hypothesis**: an import-time generator plus cluster builder raises effective instance counts at equal frame time; the claim is about *content throughput*, not about beating upstream rendering.
- **Dependencies**: M-04 codecs, `modules/meshoptimizer` (already upstream, seam 1 for simplification), M-05 instancing, editor import pipeline (`editor/import/`).
- **Seam**: 2 (editor import plugin producing standard `.mesh` + LOD metadata) then 3 for runtime cluster building.
- **Maturity**: PROPOSED / NOT ADMITTED.
- **Proof obligations**: report simplification error against a reference image, generator wall time per asset, and the runtime frame-time/primitive-count curve with chains enabled versus ranges-only.
- **Fallback**: hand-authored LODs through the editor (upstream-only path).
- **Compatibility impact**: low - it emits upstream-valid resources, so projects remain openable by an unmodified engine.
- **Risk**: silently accepting poor LODs; requires a visual-diff gate, not a numeric-only gate.

## PT-04 GPU-driven instance culling pipeline

- **Purpose**: move culling/LOD selection for high instance counts onto the GPU using the Rendering Device (`servers/rendering/rendering_device.cpp`, `rendering_device_driver.cpp`, `renderer_rd/cluster_builder_rd.h`, `multi_uma_buffer.h`).
- **Hypothesis**: for instance counts above a threshold measured on the admitted hardware classes, GPU-side selection costs less CPU frame time than node-per-instance scene culling.
- **Dependencies**: PT-01 (must agree with the CPU-side relevance decision), PT-03, M-15 physics representation of instanced bodies, `modules/meshoptimizer`.
- **Seam**: 3. Not a seam-4 candidate unless a Rendering Device extension point proves insufficient.
- **Maturity**: PROPOSED / NOT ADMITTED.
- **Proof obligations**: threshold curve (instances vs CPU and GPU frame time) per hardware class, correctness parity against the CPU path on the same scene, and a fallback path when a required Vulkan/D3D12 feature is missing.
- **Fallback**: MultiMesh (`scene/resources/multimesh.cpp`) with CPU-side selection - already upstream, seam 1.
- **Compatibility impact**: hardware-dependent by construction; the capability matrix of M-29 becomes a hard prerequisite, and the driver/backend matrix (Vulkan and D3D12) must both be tested or explicitly excluded.
- **Risk**: highest technical risk in the registry; a wrong assumption here is expensive to undo, so the threshold must be published before adoption.

## PT-05 Isometric terrain system

- **Purpose**: upstream has no 3D terrain subsystem - only 2D tile-set terrain masking and a `HeightMapShape3D` physics shape (index section D). ISORYN's target production style needs real terrain.
- **Hypothesis**: a terrain representation tuned for fixed-angle isometric framing reduces memory and draw cost per unit of authored area versus a generic mesh.
- **Dependencies**: M-04, M-06, M-08, physics heightmap (`scene/resources/3d/height_map_shape_3d.cpp`), navigation mesh generation.
- **Seam**: 3 (new module, own enable flag), authored through a seam-2 editor plugin.
- **Maturity**: PROPOSED / NOT ADMITTED.
- **Proof obligations**: memory per area step, triangulation/frame cost at fixed camera distance, collision and navigation consistency, plus an art-side usability check.
- **Fallback**: hand-authored meshes or `GridMap` (`modules/gridmap`), seam 1.
- **Compatibility impact**: low as an additive module; high if it tries to replace mesh rendering internals.
- **Risk**: competes with an eventual upstream capability; keep it module-bounded so it can be dropped without touching core.

## PT-06 VRAM budget and texture residency policy

- **Purpose**: many codecs exist upstream (`modules/betsy`, `basis_universal`, `astcenc`, `etcpak`, `ktx`, `dds`, `webp`, `tinyexr`), but a project-level VRAM budget with priority-based residency does not exist as a policy object.
- **Hypothesis**: an explicit budget per content profile keeps `RENDER_VIDEO_MEM_USED` under a hardware-class ceiling without exceeding a frame-time regression threshold.
- **Dependencies**: M-04, PT-02, M-29 hardware classes.
- **Seam**: 2 first (transcode/import policy + editor audit), 3 only if residency decisions must move inside `texture_storage.cpp`.
- **Maturity**: PROPOSED / NOT ADMITTED.
- **Proof obligations**: budget-conformance test per profile, transcode quality reference set, and a stall/hitch measurement when the budget is over-subscribed.
- **Fallback**: engine default import settings and manual artist discipline.
- **Compatibility impact**: low; output stays upstream-valid `.tres`/`.res` assets.
- **Risk**: quality regressions from aggressive transcoding; needs golden-image references, not a file-size metric.

## PT-07 Mass heterogeneous agent layer

- **Purpose**: MultiMesh covers homogeneous GPU-instanced draws; a large population with individual decisions and movement needs a simulation layer that renders through it.
- **Hypothesis**: separating agent simulation (fixed-timestep, LOD-of-simulation by relevance) from representation (MultiMesh/GPU instancing) raises sustainable agent counts at equal frame time.
- **Dependencies**: PT-01, PT-04, M-15 physics (agents must not all be physics bodies), M-16 navigation, M-13 animation.
- **Seam**: 3.
- **Maturity**: PROPOSED / NOT ADMITTED.
- **Proof obligations**: agents/second cost curve, `TIME_PROCESS` and `TIME_PHYSICS_PROCESS` split, determinism of a scripted population run, and visual parity spot checks at population LOD steps.
- **Fallback**: ordinary `CharacterBody3D` + navigation agents (seam 1), which caps population rather than engine design.
- **Compatibility impact**: contained if it exposes standard nodes; leaks if gameplay code depends on its internal representation.
- **Risk**: heavy dependence on PT-01/PT-04; admitting it before those is a scheduling error, which is why it sits behind them.

## PT-08 Deterministic capture and replay harness

- **Purpose**: make every other claim measurable. Uses upstream mechanisms only: `--path`, `--headless`, `--quit-after`, `--fixed-fps`, `--write-movie`, `--disable-vsync` (`main/main.cpp`), `Performance` monitors (`main/performance.h`), and the remote debugger channels (`core/debugger/`).
- **Hypothesis**: not a performance hypothesis - a measurement precondition: the same input script must produce repeatable metric series and comparable frame hashes on a fixed host.
- **Dependencies**: none beyond the pinned baseline; consumed by every other entry and by `09-TOOLCHAIN-AND-BENCHMARK-BASELINE.md`. One build-level precondition discovered in WO-0002: `--path` is compiled out of a stock non-editor binary, so the harness runs against a `disable_path_overrides=no` build (ADR-0002) and a number from any other variant is not comparable.
- **Seam**: 2 (a Godot project plus scripts kept as evidence tooling, no engine change).
- **Maturity**: PROPOSED, and the first candidate for admission because everything else gates on it. WO-0002 executed its first half: three repeats of the reference workload on the pinned build gave p50 6.897-6.901 ms (0.06 % spread), p95 15.091-15.286 ms (1.3 %) and p99 15.555-16.091 ms (3.4 %), with byte-identical structural monitors in all three runs - so repeat-median reporting and a stated single-host tolerance are proven, on a headless series only.
- **Proof obligations**: run the same capture twice on the same host and show metric variance within a stated tolerance (done, headless, `bench-repeats-headless.txt` and §6 of `09-TOOLCHAIN-AND-BENCHMARK-BASELINE.md`); document the host-controlling steps (power state, background load) that make the number reproducible (done - host load is captured with the series); state the cross-host variance honestly rather than hiding it (open, one host class); **and the frame-hash half is not executable here**: the `--write-movie` + `--fixed-fps` reproducibility pair needs a device that draws, and on this host every windowed path fails that readback gate, including the one that prints a full series (`gpu-windowed-device-control.txt`, `ISORYN-D-016`). Comparable frame hashes therefore remain an obligation for a second host, not a claim.
- **Fallback**: manual timed runs recorded into the evidence bundle - which is what WO-0002 used for its unavailable cases, with the failing command preserved.
- **Compatibility impact**: none on the engine; the workload definition must not assume private machine state.
- **Risk**: a low-power single test host produces numbers that do not generalize - hence one baseline per admitted hardware class instead of one global baseline. WO-0002 sharpens the risk: a host can also be *unable* to measure the thing the harness is for, and report a plausible series while doing so, which is why the gate is a written frame rather than an exit code.

## PT-09 Governed editor-automation contract

- **Purpose**: expose editor and project operations to HIVE/CORE/IRIS through versioned, read-only-first contracts over upstream automation surfaces: DAP (`editor/debugger/debug_adapter/`), GDScript LSP (`modules/gdscript/language_server/`), the machine-readable class dump (`doc/classes/`, `core/extension/extension_api_dump.cpp`) and command-line project operations.
- **Hypothesis**: production tasks (import, audit, profiling capture) can be driven through existing public automation interfaces, so no engine fork is needed for AI-native tooling.
- **Dependencies**: ADR-0003 seam policy; HIVE v1.0.0 read-only MCP surface already proven in WO-0001. Host constraint found in WO-0002: the command-line project operations this entry wants (`--import`, export) are editor-only, so on a host that cannot build the editor target its proof obligations cannot be executed there - the read-only class-dump part can.
- **Seam**: 2.
- **Maturity**: PROPOSED / NOT ADMITTED (read-only path is already evidenced; write path is not).
- **Proof obligations**: enumerate which operations are read-only versus mutating; each mutating operation needs its own contract with failure behavior, idempotency and an audit record. No shared-database coupling with HIVE/CORE/IRIS.
- **Fallback**: human-driven editor with derived context only (today's state).
- **Compatibility impact**: none while limited to public interfaces; a private-protocol dependency would be a maintenance liability and is not proposed.
- **Risk**: automation that mutates project state can create unreviewed changes; requires the same Work Order discipline as code.

## PT-10 Third-party native extension trust boundary

- **Purpose**: modding/UGC requires a policy for loading untrusted native code (GDExtension DSOs in `core/extension/`).
- **Hypothesis**: none claimed; this is a security obligation, not a performance proposal.
- **Dependencies**: `docs/project-brain/10-SECURITY-GOVERNANCE.md`, `core/crypto/`, packaging (`core/io/pck_packer.cpp`, `modules/zip`).
- **Seam**: 2 (policy + tooling).
- **Maturity**: DEFERRED - out of scope until an admitted Work Order opens modding.
- **Proof obligations**: threat model first; signature/version pinning; sandbox or explicit trust prompt; abuse tests.
- **Fallback**: no third-party native code (current stance).
- **Compatibility impact**: could restrict legitimate upstream behavior if enforced engine-wide, which is why it stays policy-side.
- **Risk**: HIGH if opened without the threat model; the deferral is the mitigation.

## Admission rules

1. No entry may be implemented before a Work Order names its ID, its proof gate and its fallback.
2. A proof gate that cannot be executed with PT-08 must first extend PT-08, not invent a one-off measurement.
3. Failing a proof gate keeps the entry at PROPOSED and drops it back to its fallback; it does not license a seam-4 fork.
4. Any result that would reverse a promoted decision (for example adopting a fork) goes to review as a proposal, never as a silent change.
