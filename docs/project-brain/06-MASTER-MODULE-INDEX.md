# ISORYN Master Module Index

Status: DISCOVERY_BASELINE (ISORYN-WO-0002)

Upstream facts in this file were read from a pinned, unmodified upstream clone at
`Godot 4.7.2-stable / ed1daf0bf001b61586d9930840f2f1394092c079`, held **outside** this repository
(`.engineering/evidence/wo-0002/godot-official-state.json` binds the tag to the commit). Every path below
is a citation into that tree. No upstream file, header, shader or binary is vendored into ISORYN.

## How to read this index

- **Family** - one product-scope line from `docs/project-brain/03-SCOPE.md`. Every family listed there appears exactly once here.
- **Upstream capability** - what the pinned baseline already provides, with the cited path or symbol.
- **Gap** - what is missing or insufficient for ISORYN's intent. A gap is an observation, never a performance claim.
- **Class** - `NECESSARY` (planned in the next governed increments), `IMPORTANT` (needed before content scale), `FUTURE` (deferred until an earlier dependency is measured), `OUT OF SCOPE` (explicitly excluded).
- **Seam** - position on the ladder frozen by ADR-0003: `1` use upstream as-is, `2` addon / GDExtension / editor tooling, `3` bounded module compiled through `custom_modules`, `4` fork or subsystem replacement (requires an ADR per subsystem).
- **Proof gate** - the measurement that must exist in an admitted Work Order before the row may move to a lower seam or a higher class. Gates use the metric vocabulary in `docs/project-brain/09-TOOLCHAIN-AND-BENCHMARK-BASELINE.md`.

## A. Architecture surface map of the pinned baseline

| Layer | Path | Role | Why ISORYN cares |
| --- | --- | --- | --- |
| Core | `core/` (`io/`, `object/`, `variant/`, `os/`, `input/`, `config/`, `crypto/`, `extension/`, `debugger/`, `profiling/`, `math/`, `string/`, `templates/`, `error/`) | Containers, RefCounted/Object model, Variant, resource loading/saving, OS abstraction, GDExtension host | Resource lifecycle and `core/io/resource_loader.cpp` are where streaming and load-time budgets live |
| Entry / frame loop | `main/main.cpp`, `main/performance.h` | CLI surface (`--path`, `--headless`, `--quit-after`, `--fixed-fps`, `--write-movie`, `--disable-vsync`, `--gpu-index`), boot order, and the `Performance` monitor enum | The flags make a deterministic, scriptable measurement harness possible without engine code - with one build-time condition: `--path` is compiled out of a stock non-editor binary (`SConstruct:1101-1102`, `main/main.cpp:1818-1822`), so a measurement binary needs `disable_path_overrides=no` |
| Servers | `servers/rendering/`, `servers/physics_2d/`, `servers/physics_3d/`, `servers/navigation_2d/`, `servers/navigation_3d/`, `servers/audio/`, `servers/text/`, `servers/display/`, `servers/debugger/`, `servers/movie_writer/`, `servers/camera/`, `servers/xr/` | Thread-isolated subsystems behind `*Server` singletons | Server interfaces are the stable seams: replacing a server implementation is a bounded act, not a fork |
| Rendering (RD) | `servers/rendering/renderer_rd/` with `forward_clustered/`, `forward_mobile/`, `storage_rd/`, `environment/`, `effects/`, `shaders/`, plus `cluster_builder_rd.h`, `framebuffer_cache_rd.h`, `pipeline_cache_rd.h`, `rendering_device.cpp`, `rendering_device_driver.cpp` | Rendering Device abstraction (Vulkan/D3D12/Metal/GLES3 backends in `drivers/`), scene/renderer split, storage per resource type | GPU-driven work attaches to `rendering_device_*` and the storage classes, not to a private copy of the renderer |
| Scene | `scene/2d/`, `scene/3d/` (incl. `scene/3d/physics/`), `scene/resources/` (incl. `scene/resources/2d/`, `scene/resources/3d/`), `scene/animation/`, `scene/gui/`, `scene/main/`, `scene/theme/`, `scene/audio/` | Node and Resource types, gameplay-facing API, 2D/3D culling entry points | Most ISORYN value can be expressed as nodes/resources, which keeps it at seam 1-2 |
| Editor | `editor/` (`import/`, `debugger/`, `plugins/`, `docks/`, `scene/`, `inspector/`, `export/`, `file_system/`, `run/`, `settings/`, `shader/`, `translations/`) | Tooling, importers, export platforms, debugger UI, editor plugins | Editor plugins and `editor/import/editor_import_plugin.h` are the automation surface an AI-native pipeline needs |
| Modules | `modules/` - 57 module directories; the discovery build's generated `modules/modules_enabled.gen.h` enables 55 for the Windows editor target (`mono` and `text_server_fb` excluded) | Optional, self-contained feature units selected by `module_<name>_enabled` (`methods.py`) | Custom modules are the sanctioned way to add native capability: see seam 3 below |
| Drivers | `drivers/` (`vulkan/`, `d3d12/`, `metal/`, `gles3/`, `png/`, `wasapi/`, `xaudio2/`, `winmidi/`, `alsa/`, `coreaudio/`, `sdl/`, `backtrace/`, ...) | Rendering/audio/image/OS backends behind the server interfaces | Backend selection and fallback behavior are the hardware-adaptation lever |
| Platform | `platform/windows/`, `linuxbsd/`, `macos/`, `android/`, `ios/`, `visionos/`, `web/` | Per-OS `DisplayServer`, build entry, `detect.py` toolchain probing | `platform/windows/detect.py` is where the compiler/SDK requirements in the toolchain ADR come from |
| Public API data | `doc/classes/` - 810 XML files; `core/extension/extension_api_dump.cpp` | Machine-readable class/property/signal surface | The dumped API is what a GDExtension or codegen tool can rely on across versions |
| Tests | `tests/` (`test_macros.h`, per-area suites) | Upstream C++ unit-test harness | Any seam-3 module inherits an existing test home instead of inventing one |

## B. Extension surfaces available at the pinned baseline

| Seam | Mechanism | Cited evidence | Constraint |
| --- | --- | --- | --- |
| 2a | Addon / editor plugin / GDScript and C# tooling | `editor/plugins/`, `editor/import/editor_import_plugin.h`, `modules/gdscript/`, `modules/mono/` | Runs on unmodified engine binaries; ships per project |
| 2b | GDExtension (native DSO, no recompile of the engine) | `core/extension/gdextension.cpp`, `gdextension_interface.gen.h`, `gdextension_manager.cpp`, `gdextension_library_loader.cpp`, `extension_api_dump.cpp` | ABI bound to the dumped interface; a class-name collision with an upstream ClassDB type is a load failure, not a warning |
| 3 | Bounded engine module compiled from **outside** the upstream tree | `SConstruct:280` `opts.Add("custom_modules", "A list of comma-separated directory paths containing custom modules to build.", "")`, `SConstruct:281` `custom_modules_recursive`, `SConstruct:446-464`, `SConstruct:470-492` (module options loop), `methods.detect_modules()` | Needs the build toolchain frozen by ADR-0002; a module is detected only if its directory holds `register_types.h`, `SCsub` and `config.py` (`methods.py:239-244`), and it gets a `module_<name>_enabled` switch (`SConstruct:485`, honored at `SConstruct:1113`) |
| 4 | Fork / subsystem replacement | Only route left when the capability must change upstream-owned code paths (for example a new primary render pipeline inside `renderer_rd`) | Requires an ADR naming the subsystem, the sync cost and the rebase policy. Not admitted by this document |

The `custom_modules` finding is the load-bearing one: a bounded native module no longer requires a
Godot fork repository. ISORYN can keep upstream unmodified, keep its own modules in the ISORYN
repository, and have SCons compile both together.

## C. Master Module Index

| ID | Family | Upstream capability (cited) | Gap for ISORYN intent | Class | Seam | Proof gate |
| --- | --- | --- | --- | --- | --- | --- |
| M-01 | Rendering core | `servers/rendering/rendering_server.cpp`, `servers/rendering/renderer_rd/forward_clustered/`, `servers/rendering/renderer_rd/forward_mobile/`, `servers/rendering/rendering_device.cpp` | No ISORYN-owned pipeline exists; needs a measurable reason to add one | NECESSARY (use) | 1 | Baseline frame-time of a fixed scene before any pipeline claim |
| M-02 | Lighting / GI / shadows | `servers/rendering/renderer_rd/environment/gi.cpp`, `servers/rendering/renderer_rd/environment/sky.cpp`, `servers/rendering/renderer_rd/environment/fog.cpp`, shadow atlases in `servers/rendering/renderer_rd/storage_rd/light_storage.cpp`, `doc/classes/WorldEnvironment.xml`, `doc/classes/Environment.xml` (`gi_mode`, `sdfgi_*`), `doc/classes/VoxelGI.xml`, `doc/classes/LightmapGI.xml` | Quality/perf envelope unmeasured on ISORYN workloads; no unified relevance-aware lighting budget | NECESSARY (use first) | 1 -> 2 | Lighting benchmark contract rows (draw calls, GPU time, VRAM) on the pinned baseline |
| M-03 | Materials / shaders | `scene/resources/material.cpp` family, `servers/rendering/shader_*.h`, `servers/rendering/shader_*.cpp`, `servers/rendering/renderer_rd/shaders/` | Nothing missing; the gap is governance of shader variants and compile cost | NECESSARY (use) | 1 | `PIPELINE_COMPILATIONS_*` monitor trend on a fixed scene |
| M-04 | Textures / VRAM | `scene/resources/texture.h` (Texture2D family), `servers/rendering/renderer_rd/storage_rd/texture_storage.cpp`, compressed codecs `modules/{betsy,etcpak,astcenc,basis_universal,ktx,dds,webp,tinyexr,bcdec,cvtt}` | No VRAM budget enforcement or streaming priority above the engine's own heuristics | IMPORTANT | 2 -> 3 | `RENDER_TEXTURE_MEM_USED`/`RENDER_VIDEO_MEM_USED` budget test per content profile |
| M-05 | Geometry / GPU-driven rendering | `servers/rendering/renderer_rd/cluster_builder_rd.h`, `servers/rendering/renderer_rd/storage_rd/mesh_storage.cpp`, `servers/rendering/multi_uma_buffer.h`, `modules/meshoptimizer` | No indirect-draw GPU culling pipeline; instance upload path is engine-owned | IMPORTANT | 3 | Instance-count scaling curve measured at fixed quality settings |
| M-06 | LOD / HLOD | Surface LOD dictionaries `scene/resources/mesh.h` (`_surface_get_lods`, `lods`) and per-node ranges `doc/classes/GeometryInstance3D.xml` (`visibility_range_*`, `lod_bias`) | Authoring/import pipeline does not generate LOD chains automatically; no hierarchical LOD (HLOD) cluster builder at engine level | NECESSARY | 2 -> 3 | LOD chain hit-rate and frame-time delta versus seam 1 ranges |
| M-07 | Visibility / occlusion | `scene/3d/occluder_instance_3d.cpp`, `servers/rendering/renderer_scene_occlusion_cull.cpp`, `renderer_scene_cull.cpp` | Occlusion data is manual; no camera-relevance scheduler driving it for isometric framing | NECESSARY | 2 -> 3 | `RENDER_TOTAL_PRIMITIVES_IN_FRAME` and `RENDER_TOTAL_DRAW_CALLS_IN_FRAME` with/without the scheduler |
| M-08 | World / asset streaming | `core/io/resource_loader.cpp` (`load_threaded_request`, `load_threaded_get_status`, `load_threaded_get`), `core/io/resource_importer.cpp`, `editor/import/resource_importer_*`, PCK via `core/io/pck_packer.cpp` | Threaded loading exists; there is **no** engine-level spatial/visibility streaming manager - no `stream*` subsystem exists beyond byte I/O peers | NECESSARY | 3 | Load-time and hitch metrics (p95 frame-time during a scripted world traversal) |
| M-09 | Terrain | 2D terrain masking exists in the tile set (`scene/resources/2d/tile_set.h`, terrain-set API); 3D only offers `scene/resources/3d/height_map_shape_3d.cpp` (a physics shape) and `GridMap` (`modules/gridmap`) | No 3D terrain material/LOD/collision subsystem - searched absence confirmed by the matching `*terrain*` file set, which is only 2D tileset editor icons | IMPORTANT | 3 | Isometric-scene build cost plus memory per terrain resolution step |
| M-10 | Vegetation | No upstream surface found: `find scene servers modules editor -iname "*vegetation*"` returns nothing at the pinned tag | Whole capability is ISORYN-side | FUTURE | 3 | Density/framing study first; benchmark only after M-05/M-06 |
| M-11 | Water / weather | No water implementation anywhere in `scene/`, `servers/`, `modules/` or `editor/` (searched absence); `servers/rendering/renderer_rd/environment/fog.cpp` provides volumetric fog | No water surface/caustics system; weather is a content concern built on fog/rain particles | FUTURE | 2 | Visual-quality reference set before any performance work |
| M-12 | VFX | `scene/3d/gpu_particles_3d.cpp`, `scene/2d/cpu_particles_2d.cpp`, `scene/resources/particle_process_material.cpp`, `modules/visual_shader` | No cross-system budget or LOD policy for particles | IMPORTANT | 2 | Particle cost share of `TIME_PROCESS` at a fixed emitter script |
| M-13 | Animation | `scene/animation/animation_tree.cpp`, `scene/animation/animation_player.cpp`, `scene/animation/animation_mixer.cpp` (root-motion accumulation), `scene/3d/skeleton_3d.cpp` | No measured cost model per skin count/blend weight | NECESSARY (use) | 1 -> 2 | Animation budget test on a fixed character roster |
| M-14 | Characters | `scene/3d/physics/character_body_3d.cpp`, `scene/2d/physics/character_body_2d.cpp`, `scene/2d/parallax_2d.cpp` | Nothing structural; movement quality is content + M-15 | NECESSARY (use) | 1 | Included in the gameplay-scene deterministic workload |
| M-15 | Physics | `servers/physics_3d/physics_server_3d.cpp` interface, `modules/godot_physics_3d/`, `modules/jolt_physics/` | Server interface makes the backend replaceable; budget per body count is undefined | NECESSARY (use) | 1 -> 3 | `PHYSICS_3D_ACTIVE_OBJECTS`/`COLLISION_PAIRS` and `TIME_PHYSICS_PROCESS` on the fixed workload |
| M-16 | Navigation | `servers/navigation_3d/navigation_server_3d.cpp`, `servers/navigation_3d/navigation_path_query_parameters_3d.cpp`, `modules/navigation_3d/3d/nav_mesh_generator_3d.cpp`, `modules/navigation_3d/3d/nav_mesh_queries_3d.cpp` | No large-world agent budget; navmesh generation is offline/editorial | IMPORTANT | 2 -> 3 | `NAVIGATION_3D_*` monitors plus query latency under a scripted agent load |
| M-17 | Mass entities | `scene/resources/multimesh.cpp`, `scene/3d/multimesh_instance_3d.cpp` (GPU-instanced static draws) | No heterogeneous agent simulation layer above MultiMesh | IMPORTANT | 3 | Simulation cost per 1k agents at fixed view relevance rules |
| M-18 | Gameplay / runtime support | `scene/main/` (`node.cpp`, `scene_tree.cpp`), `modules/gdscript/`, signals/groups | No ISORYN-side constraint; ordering policy is the deliverable here | NECESSARY (use) | 1 | Frame-slice budget: `TIME_PROCESS` split by system, from `Performance` |
| M-19 | Procedural systems | `modules/noise/` (FastNoiseLite), `modules/csg/`, `modules/xatlas_unwrap`, `modules/vhacd` | No deterministic seeded generation contract | IMPORTANT | 2 | Reproducibility test: identical seed -> identical asset hash |
| M-20 | Isometric camera systems | `scene/3d/camera_3d.cpp`, `scene/2d/camera_2d.cpp`, `servers/rendering/renderer_compositor.cpp` | The optimization principle starts here: relevance must be camera-aware before M-05/M-07/M-17 pay off | NECESSARY | 2 | Relevance-culling yield measured on a fixed isometric rig |
| M-21 | Networking | `scene/main/multiplayer_api.cpp`, `modules/multiplayer/` (spawner/synchronizer), `modules/{enet,webrtc,websocket,mbedtls,upnp}` | No ISORYN-side requirement yet beyond contract and bandwidth budget | FUTURE | 2 | Deterministic replay harness before any netcode claim |
| M-22 | Audio | `servers/audio/audio_server.cpp`, `servers/audio/effects/`, `modules/{vorbis,ogg,mp3,theora,interactive_music}`, `drivers/{wasapi,xaudio2,coreaudio,alsa,pulseaudio,sdl}` | Mixed-bus budget and DSP cost envelope undefined | IMPORTANT | 1 -> 2 | Audio thread share of `TIME_PROCESS` and `AUDIO_OUTPUT_LATENCY` |
| M-23 | UI / editor tooling | `scene/gui/control.cpp` and siblings, `editor/` (see layer map) | ISORYN needs project-specific authoring tools; no gap in the widget layer itself | NECESSARY | 2 | Editor start/import wall-time on the reference project |
| M-24 | Persistence | `core/io/resource_saver.cpp`, `core/io/dir_access.cpp`, `core/os/os.cpp` user dirs, `modules/zip` | No save-schema versioning/migration contract | IMPORTANT | 2 | Save/load round-trip test with schema migration fixture |
| M-25 | Modding / UGC | `core/extension/` (GDExtension), PCK mounting, `modules/zip` | No sandbox or trust policy for third-party native code | FUTURE | 2 | Threat model in `docs/project-brain/10-SECURITY-GOVERNANCE.md` must pass first |
| M-26 | Localization | `core/string/translation.cpp`, `core/string/translation_domain.cpp`, `core/io/translation_loader_po.cpp`, `modules/text_server_adv` (shaping/fallback) | Pipeline exists; glossary/domain governance is ISORYN-side | IMPORTANT | 1 -> 2 | Coverage + shaping fallback test per target script |
| M-27 | Security | `core/crypto/{crypto,hashing_context}.cpp`, `thirdparty/mbedtls`, `modules/mbedtls`, `editor/export/codesign.cpp` | No ISORYN-side supply-chain gate for native extensions yet | NECESSARY | 2 | Secret scan + pinned-dependency audit in CI (already partially in place) |
| M-28 | Profiling / performance | `main/performance.h` monitors, `core/debugger/{engine_profiler,remote_debugger}.cpp`, `editor/debugger/editor_debugger_node.cpp`, `modules/objectdb_profiler` | Needs ISORYN-side capture of monitor series into the evidence format used by this repository | NECESSARY | 2 | The benchmark contract in `09-TOOLCHAIN-AND-BENCHMARK-BASELINE.md` |
| M-29 | Hardware adaptation | `drivers/vulkan/rendering_context_driver_vulkan.cpp` and `rendering_device_driver_vulkan.cpp` (device features/extensions), `rendering_device_driver.cpp`, `platform/*/detect.py`, `doc/classes/RenderingDevice.xml` | No published ISORYN hardware-class matrix or graceful-degradation table, and the baseline has no fail-fast path when an accepted device refuses every shader (absence D.8) | IMPORTANT | 2 | One measured run per admitted hardware class before a class claim |
| M-30 | Build / release | `SConstruct` + `methods.py`, `platform/`, `editor/export/`, `misc/dist/` | Reproducible CI builds of the engine are not set up yet | NECESSARY | 1 | Toolchain receipt produced twice with identical version/flag output |
| M-31 | Simulation / testing | `tests/` upstream harness, `--write-movie` + `--fixed-fps` deterministic capture (`main/main.cpp`) | No golden-reference pipeline for visual regression | IMPORTANT | 2 | Frame-hash reproducibility across two runs on the same host |
| M-32 | AI-native editor / automation | `editor/debugger/debug_adapter/` (DAP), `modules/gdscript/language_server/` (LSP), `doc/classes/` machine-readable API, `core/extension/extension_api_dump.cpp` | No contract yet for HIVE/CORE/IRIS-driven editor automation | IMPORTANT | 2 | Read-only MCP session already proven; write-side needs its own ADR |

## D. Confirmed upstream absences at the pinned baseline

These are negative findings from targeted searches over the pinned clone, plus one behavior established by
execution on this host. They justify seam 2-3 rows above and are the only "gap" claims this index is allowed
to make without a measurement.

1. No virtual texturing / sparse-texture subsystem (no matching symbols in `servers/rendering/`).
2. No 3D terrain subsystem and no vegetation subsystem at all; the only `terrain` surfaces are 2D tile-set terrain
   masking (`scene/resources/2d/tile_set.h`) and its editor icons, and `HeightMapShape3D` is a physics shape.
3. No engine-level world/asset streaming manager; `stream*` files are `core/io/stream_peer*` byte I/O.
4. No hierarchical LOD (HLOD) cluster builder; per-node visibility ranges exist but are authored, not generated.
5. No `servers/rendering/driver/` directory - rendering backends live in `drivers/`.
6. No `modules/gdextension/` - GDExtension is core infrastructure in `core/extension/`.
7. No numbered LTS/support-lifetime policy published upstream (see `noOfficialLtsStatement` in the official-state receipt); the supported set is inferred from branches still carrying a version bump.
8. No graceful unsupported-rendering-device path. `drivers/vulkan/rendering_context_driver_vulkan.cpp` accepts a
   device from its own capability check and only later discovers that the driver refuses every shader module; the
   null `RID`s returned by `servers/rendering/rendering_device.cpp` then travel on into the draw path instead of
   stopping the run with a stated reason. A second failure mode was measured here and is harder to catch: a path
   can complete the frame loop, print full percentile and submission counters and exit 0 while the picture it
   returns on request contains nothing - on this host the `d3d12` driver fails the frame-sized buffer a readback
   needs with `0x887a0005`, and the frames it did hand back are 1280x720 and black at all 921,600 pixels, although
   the workload has a current `Camera3D` and a non-black default clear color (receipts
   `.engineering/evidence/wo-0002/gpu-windowed-device-control.txt`, `gpu-windowed-device-blocker.txt` and
   `gpu-readback-golden-frame.txt`, with the frame files under `frames/`). The same absence appears one level up in
   the readback itself: `servers/movie_writer/movie_writer.cpp:202` calls `texture_2d_get`, which returns an empty
   `Ref<Image>` on a failed readback (`servers/rendering/renderer_rd/storage_rd/texture_storage.cpp:1891-1892`),
   and `movie_writer.cpp:204` dereferences it without a check - so an unusable device ends the run in a segfault
   instead of a stated reason. Both behaviors appear on upstream's published `4.7.2-stable` binary on the same
   machine, so they are a property of the pinned baseline rather than of this build; what is *not* shared is this
   build's early Vulkan segfault, recorded in `.engineering/evidence/wo-0002/windowed-output-sink-control.txt`.
   What ISORYN needs is a probe
   that fails fast with a stated reason before a workload or CI run depends on the device - and, for measurement, a
   device accepted only after the frame it returns shows the scene, not merely after a file appears
   (`ISORYN-D-016`).

## E. Change rules

- A row changes class or seam only through an admitted Work Order plus a decision entry, and any move to seam 4 needs an ADR naming the subsystem and its rebase cost.
- A "gap" may not be rewritten into a performance or quality claim until the row's proof gate has executed evidence at an exact head.
- Adding a family requires updating `docs/project-brain/03-SCOPE.md` first; this index mirrors scope, it does not define it.
- Upstream citations are pinned to a tag plus commit. Re-verifying them is part of any Work Order that edits this file after an upstream release.

## F. Scope coverage checklist

Every product-scope family in `docs/project-brain/03-SCOPE.md` maps to exactly one row above. The labels are
repeated verbatim because `scripts/validate_governance.py` checks this coverage deterministically: adding a
family to scope without adding it here fails the Governance gate, which is the point.

| Scope family (verbatim from 03-SCOPE.md) | Row |
| --- | --- |
| `Rendering` | M-01 |
| `lighting/GI/shadows` | M-02 |
| `materials/shaders` | M-03 |
| `textures/VRAM` | M-04 |
| `geometry/GPU-driven rendering` | M-05 |
| `LOD/HLOD` | M-06 |
| `visibility/occlusion` | M-07 |
| `world/asset streaming` | M-08 |
| `terrain` | M-09 |
| `vegetation` | M-10 |
| `water/weather` | M-11 |
| `VFX` | M-12 |
| `animation` | M-13 |
| `characters` | M-14 |
| `physics` | M-15 |
| `navigation` | M-16 |
| `mass entities` | M-17 |
| `gameplay/runtime support` | M-18 |
| `procedural systems` | M-19 |
| `isometric camera systems` | M-20 |
| `networking` | M-21 |
| `audio` | M-22 |
| `UI/editor tooling` | M-23 |
| `persistence` | M-24 |
| `modding/UGC` | M-25 |
| `localization` | M-26 |
| `security` | M-27 |
| `profiling/performance` | M-28 |
| `hardware adaptation` | M-29 |
| `build/release` | M-30 |
| `simulation/testing` | M-31 |
| `AI-native editor/automation` | M-32 |
