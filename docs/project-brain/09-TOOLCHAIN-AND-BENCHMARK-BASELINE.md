# ISORYN Toolchain and Benchmark Baseline

Status: DISCOVERY_BASELINE (delivered by ISORYN-WO-0002)

This document freezes three things at once: the build chain that makes an engine claim reproducible
(ADR-0002), the metric vocabulary and workload contract that make a performance claim meaningful
(`docs/project-brain/11-TEST-PLAN.md`), and the first measured numbers on the pinned baseline. Machine-readable
receipts live in `.engineering/evidence/wo-0002/`. Nothing here is a comparison against upstream quality; no
admitted workload has been measured against a competing implementation, and none is claimed.

## 1. Toolchain baseline (observed, not assumed)

| Item | Value on the discovery host |
| --- | --- |
| OS | Windows 11 Home Single Language 10.0.26200, x64, 22.9 GB visible RAM |
| CPU | AMD Ryzen 5 2500U with Radeon Vega Mobile Gfx, 4 cores / 8 threads, 2000 MHz base |
| GPU (active display) | AMD Radeon (TM) Vega 8 Graphics, driver 31.0.21925.1001 (2026-05-19), desktop 2560x1440@60 |
| Compiler | Visual Studio Build Tools 2022 (17.14.37628.2), toolset family 14.3 (v143), installed compiler 14.44.35207 |
| Windows SDK | 10.0.26100.0 |
| Python / SCons | 3.12.10 / 4.11.1 (venv-local; there is no global `scons` on this host) |
| Git | 2.55.0.windows.3 |
| Disk on the build volume | 213.8 GB free |

Upstream enforces `SCons >= 4.8.0` for the v143 family and `>= 4.10.1` for the newer family
(`platform/windows/detect.py:187-192`), so the SCons version is part of the toolchain contract rather than an
environment detail. Full probe list and raw values: `.engineering/evidence/wo-0002/toolchain-inventory.json`.

These are **host facts**, deliberately kept out of portable configuration: `scripts/validate_governance.py`
rejects drive-letter paths in scripts, environment template and context locks, so a future executor cannot
inherit this machine as if it were the specification.

## 2. Reproducible build

Source state: `4.7.2-stable` @ `ed1daf0bf001b61586d9930840f2f1394092c079`, shallow clone outside the repository.

```
git clone --depth 1 --branch 4.7.2-stable https://github.com/godotengine/godot.git godot-4.7.2
python -m venv venv-scons && venv-scons/Scripts/python.exe -m pip install scons
venv-scons/Scripts/scons.exe platform=windows target=template_release arch=x86_64 accesskit=no d3d12=no angle=no disable_path_overrides=no -j8
```

`disable_path_overrides=no` belongs to the measured command because a template binary otherwise refuses an
unpacked project, which is the whole point of the harness below. The editor target takes the same command with
`target=editor` and does not need the option: `OVERRIDE_PATH_ENABLED` is implied by an editor build
(`SConstruct:1101-1102`).

Six executions were needed. Each is preserved as a receipt pair: the log the toolchain wrote, plus a .meta
companion carrying command, start/stop UTC, exit code and elapsed seconds. Nothing was overwritten, including the
failures. MSVC writes part of its output in the host's locale (CP-1252 with CRLF endings) and the repository
carries LF-only text, so a committed receipt is the UTF-8 normalization of the raw log and
`.engineering/evidence/wo-0002/build-receipts-index.txt` records each raw file's byte size and SHA-256 next to the
committed copy's; the raw bytes stay in the disposable discovery workspace. A reviewer who has that workspace can
re-hash them, and one who does not can still read the same content.

| # | Command (after the common flags) | Result | Receipt |
| --- | --- | --- | --- |
| 1 | `target=editor -j8` (no driver overrides) | exit 255 after 14 s - **configuration refused** | `build-4.7.2-editor.attempt1-configure-failure.log` |
| 2 | `target=editor accesskit=no d3d12=no -j8` | exit 2 after 4689 s (01:17:24) - 1830 objects compiled, then six `C1060` deaths, no link | `build-4.7.2-editor-attempt2.log` |
| 3 | identical to 2 with `-j4` | exit 2 after 277 s - the five collateral units compiled; `doc_translations.gen.cpp` still died | `build-4.7.2-editor-attempt3.log` |
| 4 | `-j1`, single target `bin/obj/editor/translations/doc_translations.gen.windows.editor.x86_64.obj`, nothing else running | exit 2 after 73 s - same `C1060` at line 503845 | `build-4.7.2-editor-attempt4.log` |
| 5 | `target=template_release accesskit=no d3d12=no angle=no -j8` | **terminated by decision** after 1388 s and 657 target outputs (620 `.obj` + 37 `.lib`) - a completed build of this command could never have run the benchmark harness (see below) | `build-4.7.2-template-release-terminated.log` |
| 6 | attempt 5 plus `disable_path_overrides=no` | §5 records this run's wall time, exit code, binary identity and smoke set | `build-4.7.2-template-release-measurable.log` |

**What attempt 1 proved.** Three optional rendering/accessibility drivers need host state that a clean
toolchain does not have: `accesskit` (`misc\scripts\install_accesskit.py`), `d3d12`
(`misc\scripts\install_d3d12_sdk_windows.py`) and `angle` (`misc\scripts\install_angle.py` - upstream warns and
tells the operator to pass `angle=no` explicitly). The same log carries the detection line
`Using Visual Studio 14.3 with Windows SDK 10.0.26100.0.`, which is the compiler identity every later receipt
depends on.

**What attempts 2-4 proved.** The editor target is not buildable on this host, and parallelism is not the
cause. SCons generated `editor/translations/doc_translations.gen.cpp` as a single 102,310,230-byte / 858,554-line
translation unit from `doc/translations/*` (`editor/SCsub:59-71` has no switch to shrink it), and MSVC's compiler
heap cannot hold it even when it is the only process running with 8.6 GB of the 22.9 GB visible RAM free and a
12 GB pagefile. Attempts 2 and 3 differ only in `-j`, and attempt 4 removes contention entirely; all three fail
at the same line. `editor/docks/*` and `editor/doc/editor_help.cpp` were collateral damage of the same memory
pressure, not independent defects - they compiled at `-j4`.

**Decision that follows from it.** Toolchain proof therefore comes from a `template_release` build: it exercises
the same configure, compile and **link** path and produces a runnable engine binary, while the editor-only
generated translations are simply not part of that target. The editor boot smoke test is recorded
as `NOT_AVAILABLE` on this host with the exact failing command above, not as a pass and not as a silent omission.

**What attempt 5 proved, and why it was terminated.** Attempt 5 was 620 objects into a clean run when it was
stopped deliberately, because finishing it would have produced a binary that cannot run the benchmark harness.
`disable_path_overrides` defaults to `True` (`SConstruct:272-278`), and `OVERRIDE_PATH_ENABLED` is defined only
`if env.editor_build or not env["disable_path_overrides"]` (`SConstruct:1101-1102`). Without that define a
non-editor binary refuses an explicit project path (`main/main.cpp:1818-1822`: "this Godot binary was compiled
without support for path overrides. Aborting.") and refuses a project found in the working directory
(`main/main.cpp:2115-2123`), whose own error text tells the operator to rebuild with `disable_path_overrides=no`.
That option is what upstream marks `--path` as requiring (the `CLI_OPTION_AVAILABILITY_TEMPLATE_UNSAFE` tag at
`main/main.cpp:576`), because it also re-enables `--scene` and script running - correct for a development and
measurement binary, wrong for a shipping export template. Attempt 6 therefore adds `disable_path_overrides=no`
and is the single build that serves as both the toolchain proof and the measurement host. The partial objects
from attempt 5 were deleted rather than reused, so no killed-process artifact can enter the receipt; the
terminated log, its .meta companion and a note file (`build-4.7.2-template-release-terminated.note.txt`)
stay in the evidence set as the record of this finding.

**Optional-driver gap, stated.** Because the build passes `accesskit=no d3d12=no angle=no` rather than running
upstream's installer scripts, this baseline has no screen-reader driver, no Direct3D 12 driver and no ANGLE
driver. Installing third-party SDK state on the host to make a build easier is a side effect the Work Order did
not authorize, and it would make the receipt unreproducible on another machine. No WO-0002 conclusion covers any
of the three paths.

**Host capacity contract.** A build receipt is only comparable if its `-j`, its target and its host memory are
stated. The measured fact on this host is that the editor target requires a compiler that can hold a ~100 MB
generated translation unit; any ISORYN host that intends to build the editor must clear that bar and re-run
these receipts before its wall times are compared with these.

### 2.1 The previous supported stable line (4.6.3)

The Work Order asks for a compatibility reference on the immediately previous supported stable line, not a
second shipping target. Executed as a configure-only feasibility check so it costs no compile hours and does not
perturb the timed build above:

```
git clone --depth 1 --branch 4.6.3-stable https://github.com/godotengine/godot.git godot-4.6.3
cd godot-4.6.3 && <venv>/Scripts/scons.exe -n platform=windows target=editor arch=x86_64 accesskit=no d3d12=no angle=no -j8
```

`4.6.3-stable` resolved to commit `35e80b3a8822a9df9be390814b62f44c0a9c69e8`, which equals the tag object recorded
in `.engineering/evidence/wo-0002/godot-official-state.json` - the clone is the tagged source, not a branch tip.
The dry run **completed with exit 0 in 87 s** (`build-4.6.3-editor-configure-dryrun.log` and its .meta companion), reaching
`scons: done building targets` after generating the renderer shader headers. So the frozen toolchain configures
the previous stable line unchanged on this host, including the same three optional-driver overrides. What is *not*
proven is a 4.6 link or a 4.6 runtime: that needs compile hours, is deliberately out of scope here, and belongs
to a Work Order that has a reason to ship on 4.6.

## 3. Metric vocabulary (frozen)

The measurable surface is the engine's own monitor set (`main/performance.h`) plus wall-clock facts. Baselines
report these, not a bare FPS number:

| Group | Metric | Source |
| --- | --- | --- |
| Frame cost | `frame_ms_p50/p95/p99/max`, mean frame ms | per-frame `Time.get_ticks_usec()` deltas in the harness |
| CPU loop | `TIME_PROCESS`, `TIME_PHYSICS_PROCESS`, `TIME_NAVIGATION_PROCESS` | `Performance` |
| Submission | `RENDER_TOTAL_OBJECTS_IN_FRAME`, `RENDER_TOTAL_PRIMITIVES_IN_FRAME`, `RENDER_TOTAL_DRAW_CALLS_IN_FRAME` | `Performance` |
| Memory | `MEMORY_STATIC`, `RENDER_VIDEO_MEM_USED`, `RENDER_TEXTURE_MEM_USED`, `RENDER_BUFFER_MEM_USED` | `Performance` |
| Objects | `OBJECT_COUNT`, `OBJECT_RESOURCE_COUNT`, `OBJECT_NODE_COUNT`, `OBJECT_ORPHAN_NODE_COUNT` | `Performance` |
| Shader stutter | `PIPELINE_COMPILATIONS_{CANVAS,MESH,SURFACE,DRAW,SPECIALIZATION}` | `Performance` |
| Physics | `PHYSICS_3D_ACTIVE_OBJECTS`, `PHYSICS_3D_COLLISION_PAIRS`, `PHYSICS_3D_ISLAND_COUNT` (+2D) | `Performance` |
| Navigation | `NAVIGATION_3D_{ACTIVE_MAPS,REGION_COUNT,AGENT_COUNT, polygon/edge counters}` | `Performance` |
| Load | import wall time, startup wall time, scene-ready time | external timer + `ISORYN_BENCH_CONFIG` |
| Build | configure/build wall time, exit code, binary size, binary SHA-256, version string | SCons + shell |
| Audio | `AUDIO_OUTPUT_LATENCY` | `Performance` |

## 4. Workload contract

The reference workload is the committed harness `.engineering/evidence/wo-0002/bench/` - a Godot *project*, not
engine code: `project.godot`, `bench.tscn` and `bench.gd`. It builds 1200 boxes from a constant seed
(`RNG_SEED = 20260923`) in a 40-column grid with a shadow-casting directional light and a fixed camera, warms
up for 90 frames, then measures 600 frames while applying a constant yaw step, prints one
`ISORYN_BENCH <json>` line and quits. No input, no audio, no network, no clock-derived randomness.

Controls an engine-flag run must declare (all exist in `main/main.cpp` at the pinned tag):
`--path`, `--headless`, `--quit-after`, `--fixed-fps`, `--disable-vsync`, `--max-fps`, `--resolution`,
`--rendering-method`, `--rendering-driver`, `--gpu-index`, `--audio-driver`, `--render-thread`,
`--write-movie`, `--print-fps`, `--import`, `--quiet`, `--no-header`, `--log-file`.

Not every flag is available to every binary, and a run says which binary variant it used: `--path` is compiled
out of a stock non-editor build (`disable_path_overrides` default, `SConstruct:1101-1102`) and `--import` is
editor-only (`main/main.cpp:700`). So the harness runs against the frozen `disable_path_overrides=no` template
build, import-driven measurements would need an editor build, and a number from any other variant is a different
configuration rather than the same one.

Measurement rules:

1. **Repeat and median.** Each configuration runs at least 3 times; the reported number is the median, with min/max shown. A single run is never a baseline.
2. **Fixed host state.** Plugged in, balanced power plan, no other CPU-heavy work, and the same adapter selection for every GPU comparison - this host enumerates three display adapters, so `--gpu-index` must be pinned before GPU numbers are trusted across runs.
3. **Declared configuration.** Renderer, driver, resolution, frame counts and seed are part of the receipt; a change to any of them is a different workload, not a regression.
4. **Percentiles, not averages.** Frame-time p95/p99 and the max spike are the primary results; `TIME_FPS` is recorded only as context.
5. **Regression rule.** A claim of improvement or parity needs identical workload, identical host class, identical flags, and a stated tolerance; the current single-host tolerance is recorded with the numbers below.
6. **Rollback criterion.** A change that increases p95 frame time, draw calls, primitives submitted, or VRAM use beyond the stated tolerance on the same workload is reverted, not tuned around.
7. **Declared execution mode.** Windowed and headless runs are different workloads and are never pooled.
   `--headless` selects the dummy display server, so its frame times measure GDScript and culling but not GPU
   submission; they are a logic smoke test and a CPU-cost signal, not a frame-time baseline. Every GPU number in
   a baseline comes from a windowed run with `--disable-vsync`, and the reproducibility gate uses
   `--write-movie` plus `--fixed-fps`, which removes wall-clock timing from the comparison entirely.
8. **Forbidden.** Average FPS alone, a number from a different host class presented as comparable, and any "faster than Godot" phrasing without an admitted workload plus executed measurement on both sides.

## 5. Build and binary evidence

**Attempt 6 completed**, so the toolchain claim is a linked, runnable binary rather than a configure dry run:

| Fact | Value |
| --- | --- |
| Command | `scons platform=windows target=template_release arch=x86_64 accesskit=no d3d12=no angle=no disable_path_overrides=no -j8` |
| Start / stop (UTC) | 2026-09-23T19:39:56Z / 2026-09-23T21:32:54Z |
| Elapsed / exit code | 6,777 s (1 h 52 min 57 s) / **0** |
| Compiler identity, from log line 2 | `Using Visual Studio 14.3 with Windows SDK 10.0.26100.0.` |
| Compile and link | 2,420 `Compiling` steps, 2,422 `*template_release*` objects under `bin/obj`, then `Linking Program bin\godot.windows.template_release.x86_64.exe ...` and `scons: done building targets.` |
| Binary | `godot.windows.template_release.x86_64.exe`, 68,254,208 bytes, SHA-256 `7052a3f08be1872418cae83c08c15c5ff46e52950b2fb8d43b19b24587914a18` |
| Console wrapper | `godot.windows.template_release.x86_64.console.exe`, 292,864 bytes, SHA-256 `272c53715fd949b61354088717482e974aa47c04ece70acb2ec67fcf87c843b8` |
| Version string | `4.7.2.stable.custom_build.ed1daf0bf` |
| Receipts | `build-4.7.2-template-release-measurable.log` with `build-4.7.2-template-release-measurable.meta` (both hashed in `build-receipts-index.txt`), artifact identities in `godot-4.7.2-binary-identity.txt` |

The version string is the build's own proof of source identity. Upstream's published binary for the same tag
reports `4.7.2.stable.official.ed1daf0bf`; the two agree on the commit and differ only in the `custom_build` /
`official` label that `version.py` derives from official build configuration. A reviewer can therefore check this
binary against a downloaded official artifact instead of taking this table on trust, and §7 does exactly that.

**Smoke set.** `godot-4.7.2-smoke.txt` carries every case with exit code, wall time, error-line count and the
harness's own configuration line:

| Case | Outcome |
| --- | --- |
| version string | exit 0 in 178 ms - `4.7.2.stable.custom_build.ed1daf0bf` |
| headless scene run | exit 0 in 1,416 ms, harness printed `ISORYN_BENCH_CONFIG`; its single `ERROR:` is the expected `Could not load global script cache.` for an unpacked project on a template binary |
| windowed Vulkan | **exit 139** after 3,043 ms, 607 `ERROR:` lines - §7 records the executed cause, and the harness configuration line is missing from both sinks that `windowed-output-sink-control.txt` reads |
| windowed GL compatibility | **exit 139** after 1,254 ms, with nothing in either sink; upstream's binary dies at the same place one line later (receipt just cited) |
| `--rendering-driver d3d12` | `NOT_AVAILABLE` on this binary - the driver was configured out; upstream's own refusal (`Unknown rendering driver 'd3d12'`) is inside the receipt |
| headless resource import | `NOT_AVAILABLE` - `--import` is editor-only (`main/main.cpp:700`) and this host cannot compile the editor (§2) |
| editor boot | `NOT_AVAILABLE` - same cause |

Two passes, two executed failures, three stated unavailable cases - no silent omission, and the failures are not
counted as passes.

An empty configuration field is a claim about the run, so it was tested rather than read: `windowed-output-sink-control.txt`
re-runs each windowed path writing to two sinks at once, the redirected console and the engine's own `--log-file`
writer (`main/main.cpp:1517`). The harness line reaches both on the headless paths and reaches both on upstream's
binary running the same windowed Vulkan path with the same flags, and it is absent from both for this build. Two
sinks that agree on an absence make it a fact about how far the process got, not an artifact of how it was captured.

## 6. Initial measured series (headless)

Three repeats of the frozen workload against the §5 binary (`--headless --quit-after 999`), from
`bench-repeats-headless.txt`, which also keeps each run's complete JSON series line:

| Metric (ms) | run 1 | run 2 | run 3 | median | min-max |
| --- | --- | --- | --- | --- | --- |
| `frame_ms_p50` | 6.901 | 6.898 | 6.897 | **6.898** | 6.897-6.901 |
| `frame_ms_p95` | 15.175 | 15.091 | 15.286 | **15.175** | 15.091-15.286 |
| `frame_ms_p99` | 15.590 | 15.555 | 16.091 | **15.590** | 15.555-16.091 |
| `frame_ms_max` | 15.711 | 25.513 | 34.791 | 25.513 | 15.711-34.791 |
| `mean_frame_ms` | 7.376 | 7.401 | 7.417 | 7.401 | 7.376-7.417 |
| run wall time | 5,814 | 5,700 | 5,640 | 5,700 | 5,640-5,814 |

**Stated single-host tolerance (rule 5).** Across three repeats p50 spread is 0.06 %, p95 1.3 % and p99 3.4 %.
A later claim on this host and this configuration may use those spreads; `frame_ms_max` is reported but is never
a gate, because it varied 2.2x and is dominated by scheduler noise rather than by the workload. Scene-ready cost
(`ready_us` in `ISORYN_BENCH_CONFIG`) was 22.6-27.3 ms across the runs.

**What this series does and does not measure.** The structural monitors were bit-identical in all three repeats
(`object_count` 2585, `object_node_count` 1204, `object_resource_count` 1, orphan nodes 0), which is the harness's
own evidence that each run built the same scene from the same seed. Every `render_*` monitor is `0.0` and
`frames_drawn` is `0`, because `--headless` selects the dummy display server. Under rule 7 this is therefore a
CPU/logic and culling baseline and **not** a frame-time baseline; no GPU number is claimed from it. The host was
6 % busy at the end of the series (`host_percent_processor_time`), so the runs were not competing with a build.

## 7. Windowed device state on this host

No windowed GPU baseline is admitted from this host, and the reason was established by execution rather than
assumed. `gpu-windowed-device-control.txt` runs the full harness (each case allowed to reach its own report point,
so a printed series can only mean 690 frames elapsed) on the §5 binary and on upstream's own published
`4.7.2-stable` binary, whose identity is recorded next to it (`4.7.2.stable.official.ed1daf0bf`, same commit), and
`gpu-readback-golden-frame.txt` runs the readback gate on the same two binaries:

| Case | Result | What it rules in or out |
| --- | --- | --- |
| built binary, Vulkan | exit 139 after 2,963 ms, 607 `ERROR:` lines, no series, and no `_ready()` line in either sink | the accepted device refuses shader-module creation: 109x `Error (-3) creating module for shader stage Compute.`, 94x the Vertex equivalent, then null `RID`s and a segfault before the workload is instantiated |
| built binary, GL compatibility | exit 139 after 816 ms; `windowed-output-sink-control.txt` records 207 B on the console, 0 B in the engine log, and the `_ready()` line in neither | the fallback driver dies during context creation |
| official binary, Vulkan | exit 124 - still unfinished after 300 s, 3,759 `ERROR:` lines, no series, `_ready()` line present | the same refusal on an artifact upstream built, so the refusal is this host's; the *early crash* is not reproduced, which is the divergence below |
| official binary, GL | exit 139; the same control records its engine log holding 7 lines where this build's holds none, and the `_ready()` line in neither | same failure as the built binary's GL case, one line deeper |
| official binary, `d3d12` | **exit 0 in 4,159 ms with a complete series**: p50 3.227, p95 4.189, p99 4.670, max 5.171 ms, `frames_drawn` 689, 1,953 objects and 23,436 primitives in frame, 78,630,912 B video memory, zero `ERROR:` lines | the only path on this machine that reaches the report point at all |
| official binary, `d3d12` + `--write-movie --fixed-fps 60` | **exit 139**; of the 700 frames asked for, the run wrote **one** and died on the next. Across every such execution on this host the frame files are byte-identical to each other: 2,772 B, 1280x720, **all 921,600 pixels (0,0,0)** | the readback path returns a buffer, and what is in it is not the scene - see reason 1 below |
| built binary, Vulkan + `--write-movie` | exit 139, and no `movie00000000.png` survived it (`gpu-windowed-device-control.txt` §D) | the same gate fails earlier on the default path: this binary's device never reaches a frame it can write |

**The control reproduces the refusal, not this build's crash.** That distinction matters, because the sentence this
section carried before the control ran was "upstream's binary reproduces both crash paths, so the cause is host
state and not the build", and only half of it survives measurement. On the OpenGL path both artifacts exit 139
without instantiating the workload, which is a reproduced failure. On the Vulkan path both report the same
shader-module refusal, but this build segfaults about 3 s in while upstream's binary keeps rendering until the
timeout kills it - at 120 s in the control receipt and still alive at 301 s in the full-length run. The accepted
device and its refusal belong to the host; the early exit belongs to this build, and nothing in WO-0002 explains
it. It is recorded as a residual risk and it is a gate on adopting the §5 command line as CI's reference build,
because a build that dies where upstream's survives has either a configuration difference or a defect, and the two
are told apart by a symbolised crash - which needs `debug_symbols=yes`, and that is a build of hours on a host this
Work Order already measured as marginal for the editor target.

The four frames the `d3d12` gate did return are committed under `.engineering/evidence/wo-0002/frames/`, and
`gpu-readback-golden-frame.txt` records each execution's exit code, the file list, the counted error signatures
and the decoded pixel hash, so the identity of the four files is checkable without rerunning anything.

How those four files were found is itself a finding. The first attempt at the gate counted frame files in the
directory it launched the engine from and reported none, which the earlier `gpu-windowed-device-control.txt` §C and
§D lines repeat; a relative `--write-movie` path is not resolved against the working directory but prefixed with
`res://` (`servers/movie_writer/movie_writer_pngwav.cpp:66-70`, and the same rule in `MovieWriter::begin` at
`servers/movie_writer/movie_writer.cpp:110-113`), so frames land in the project directory. The counting fix is in
the readback receipt, which also gives every execution its own base name for a second reason: `write_begin`
deletes `<base>00000000.png` onward before recording (`servers/movie_writer/movie_writer_pngwav.cpp:75-83`), so two
runs sharing a base erase each other's output. §C and §D of the device-control receipt do share one base, and §D ran
last, so §D's zero is readable (no `movie00000000.png` exists) while §C's is not - it cannot be told apart from a
run whose frame §D deleted. The readback receipt therefore gives each of its three cases its own base, and under
that discipline the built binary's Vulkan path returned no frame file at all.

**Why the `d3d12` series is not promoted to a baseline.** Three reasons, each sufficient on its own, and they are
recorded separately rather than blended into one claim:

1. **Its own readback contradicts it.** `0x887a0005` is `DXGI_ERROR_DEVICE_REMOVED`, and this host's `d3d12` path
   presents 690 frames without logging an error and then fails the first request for the picture back:
   `Can't create buffer of size: 3686400, error 0x887a0005` (a buffer exactly one 1,280x720 RGBA frame) and
   `Create(Graphics)PipelineState failed with error 0x887a0005`, after which the process segfaults. On the runs that
   did answer once before dying, the frame they returned is black at every pixel - and this scene cannot present
   black everywhere: it has a current `Camera3D`
   (`.engineering/evidence/wo-0002/bench/bench.gd:27-31`), the project sets no clear-color
   override, so the viewport clears to `rendering/environment/defaults/default_clear_color` = `Color(0.3, 0.3, 0.3)`
   (`main/main.cpp:3640`, applied at `main/main.cpp:3999-4000`). Whether the buffer came back unwritten or written
   with nothing in it, no pixel has ever come back from this device showing the 1,953 objects the series reports,
   and the crash itself is the null `Ref<Image>` that `texture_2d_get` returns on readback failure
   (`servers/rendering/renderer_rd/storage_rd/texture_storage.cpp:1892`) being dereferenced by the writer
   (`servers/movie_writer/movie_writer.cpp:204`). A device whose only readable frame is empty cannot anchor a
   measurement, which is why ISORYN-D-016 admits one through a readback gate rather than through an exit code.
2. **It is not this build.** The frozen toolchain command excludes `d3d12` (§2, attempt 1), so the only binary
   that can produce that series is upstream's. Under ADR-0002's receipt discipline a measurement and a build
   identity travel together; a number from a different artifact is a different configuration.
3. **It is one host.** §1 and §6 are explicit that a single machine is not a hardware class, so even a verified
   series here would be one class of one.

**What would change this.** Either a host whose driver passes the readback gate - which means returning a frame
that is not uniformly black, checked by pixel hash rather than by the existence of a file - or a build with
`d3d12=yes`, which needs upstream's `misc\scripts\install_d3d12_sdk_windows.py` to run on the host: a third-party
SDK installation that ISORYN-D-011's isolation rule currently keeps out, and which is now known not to be
sufficient by itself, since the driver it would enable has already failed readback here. Both are reviewer
decisions, and `docs/project-brain/14-BACKLOG.md` row 10 carries them with this evidence attached.

**What is claimed instead.** §6's headless series, labelled as CPU/logic cost under rule 7; the executed failures
above; and the absence of a fail-fast unsupported-device path in upstream, which is a real finding for ISORYN's
hardware-adaptation seam (M-29, absence D.8 in `docs/project-brain/06-MASTER-MODULE-INDEX.md`) rather than an
inconvenience of this machine.
