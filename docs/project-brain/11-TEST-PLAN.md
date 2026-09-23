# ISORYN Test and Benchmark Plan

Status: DISCOVERY_BASELINE (extended by ISORYN-WO-0002)

## Repository gates (deterministic, always run)

Governance validator (`python scripts/validate_governance.py`), Python compilation of every script,
HIVE bridge and governance unit tests (`python -m unittest discover -s tests -p "test_*.py" -v`),
`git diff --check` on a clean tracked tree, repository secret scan, and exact-head GitHub Actions
(`Governance` context required by the `main-governance` ruleset). These are admission gates, not
advisories: an exact head that fails one of them cannot be promoted.

## Engine measurement gates (added by discovery)

Before any performance/graphics module: freeze baseline workload/scenes; target hardware classes; CPU/GPU/RAM/VRAM metrics; frame-time percentiles/stutter limits; loading/streaming metrics; objective visual-quality checks/golden references where applicable; determinism/replay needs; regression thresholds; rollback criteria.

The concrete vocabulary, workload, environment controls and first measured numbers are in
`docs/project-brain/09-TOOLCHAIN-AND-BENCHMARK-BASELINE.md`. Summary of what a measurement must state to count:

1. **Identity**: engine tag + commit + `version.py`, toolchain versions, build command line and the binary's version string, size and SHA-256.
2. **Workload**: a fixed, seeded scene and camera path (the WO-0002 harness is `.engineering/evidence/wo-0002/bench/`), with frame counts and warm-up declared.
3. **Engine flags**: `--headless`, `--disable-vsync`, `--fixed-fps`, `--quit-after`, `--write-movie`, `--resolution`, `--rendering-method`, `--rendering-driver`, `--gpu-index` and `--audio-driver` are the controls; a run must name the ones it used.
4. **Metrics**: frame-time percentiles (p50/p95/p99/max), `TIME_PROCESS` and `TIME_PHYSICS_PROCESS`, `RENDER_TOTAL_OBJECTS_IN_FRAME`, `RENDER_TOTAL_PRIMITIVES_IN_FRAME`, `RENDER_TOTAL_DRAW_CALLS_IN_FRAME`, `RENDER_VIDEO_MEM_USED` / `RENDER_TEXTURE_MEM_USED` / `RENDER_BUFFER_MEM_USED`, `MEMORY_STATIC`, `OBJECT_*` counts, `PIPELINE_COMPILATIONS_*` for shader-stutter work, and load/import wall time.
5. **Environment control**: power state, background load, adapter selection on multi-adapter hosts, and repeat count; median across repeats, not a single run.
6. **Regression rule**: a claim of improvement needs the same workload, the same host class, the same flags and a stated tolerance; a claim of parity needs the same. Otherwise it is an observation.

Average FPS alone is never sufficient evidence.

## Smoke set required for any engine build receipt

Version string; headless resource import; headless scene run to clean exit; windowed run that initializes the
real rendering device on the GPU and exits cleanly; editor boot when the build host can produce an editor
binary; and the negative check that a build with an ISORYN module disabled still configures. A smoke failure is
preserved as its own receipt (WO-0002 did this for the `accesskit`/`d3d12` configuration abort and for the
editor target's `C1060` compiler-heap failure). Where a case cannot run because the host could not produce that
binary, the receipt says `NOT_AVAILABLE` plus the exact failing command - an omitted case and an unavailable case
are different claims, and only the second one is honest about a limit that a reviewer can re-test.

Two of those cases are editor-only in the engine itself: `--import` is labelled
`CLI_OPTION_AVAILABILITY_EDITOR` (`main/main.cpp:700`) and both it and `--editor` are parsed only under
`TOOLS_ENABLED` (`main/main.cpp:1597-1766`). On a host that cannot produce an editor binary, headless resource
import and editor boot therefore share one cause. What WO-0002 could execute from its own template binary is the
version string (pass), the headless scene run (pass), the windowed device run (executed and failed on this host's
driver state, with the OpenGL path failing the same way) and the `d3d12` attempt (refused by configuration) - two
passes, two executed failures and three stated unavailable cases, not five silent passes.

A third through sixth mechanics trap came from the windowed cases, and each would have produced a false pass:

- **A run truncated by `--quit-after` never reaches the harness report point.** The harness prints its series
  after 90 warm-up + 600 measured frames; a case capped at 60 frames exits 0 having printed only its config line,
  which reads like "no error, no result" and proves nothing about the device. Every windowed receipt now runs the
  full workload, with the frame cap only as a backstop above the harness's own quit point.
- **An exit code and a printed series are not evidence that anything was drawn.** `d3d12` on upstream's own binary
  completed the full harness and printed percentile and submission counters, exiting 0 with no error line at all -
  while the same path, asked for the picture back, returned frames that are black at all 921,600 pixels and then
  died at `Can't create buffer of size: 3686400, error 0x887a0005`, a buffer exactly one 1,280x720 RGBA frame, and
  segfaulted. The host can present and cannot give a picture of the scene back. The gate is therefore readback: a
  windowed series is admitted only from a path that can write golden frames for the same workload and whose frames
  are demonstrably not empty (`ISORYN-D-016`), checked by pixel hash rather than by the presence of a file.
- **A frame count is only as good as the directory it looks in.** `--write-movie` with a relative path resolves
  against `res://`, not the working directory the engine was launched from
  (`servers/movie_writer/movie_writer_pngwav.cpp:66-70`), so counting where the process was started reports zero
  frames for a run that wrote one - which is exactly how one receipt in this increment came to claim that nothing
  had ever been read back. And `write_begin` deletes `<base>00000000.png` onward before recording
  (`servers/movie_writer/movie_writer_pngwav.cpp:75-83`), so two runs sharing one base name erase each other's
  output, and a zero from the earlier of the two is unreadable. Every movie case now carries its own base name and
  is counted in the project directory.
- **A missing output line is only a statement about the run once a second sink agrees with it.** A windowed case
  that logs no harness line can mean "never reached `_ready()`" or "the capture lost it", and those readings support
  opposite conclusions. The receipts that carried the empty field explained it as buffered stdout dying with the
  process, an idea that had never been executed; `windowed-output-sink-control.txt` now runs each windowed path
  against the redirected console and the engine's own `--log-file` writer at once, and the line arrives in both
  sinks on the headless paths and in both on upstream's binary running the same windowed Vulkan path. Where two
  sinks agree on an absence, the run is what stopped short - and reading it that way is also what exposed that this
  build's early Vulkan exit is not a behavior the control binary shares.

Two mechanics traps were found while producing those receipts and are now part of the plan. `--quiet` suppresses
`print()` output, so it must never be combined with a harness run whose result is a printed line - the first
headless receipt recorded a passing exit code with no measurement because of exactly that. And running an
unpacked project on a template binary always logs `Could not load global script cache.` from
`ProjectSettings::get_global_class_list` (`core/config/project_settings.cpp:1458`, path built at `:1470`), because
the cache file is editor-generated project data; a receipt that shows that one line and nothing else is a clean
run, not a failed one.

Headless and windowed results are never pooled: `--headless` uses the dummy display server, so it measures
script and culling cost, not GPU submission.

## Visual-quality and determinism gates

Frame-capture comparison uses upstream's deterministic movie writing (`--write-movie` with `--fixed-fps`) so a
visual change produces comparable frames rather than screenshots taken at arbitrary moments. Cross-host
reproducibility is an open item: one host is one hardware class, and PT-08 must state its variance honestly
before a number is generalized.

## Promotion rule

No known HIGH/CRITICAL defect may be promoted, and a fix that changes the head invalidates the exact-head
evidence bound to the previous one - re-run and re-bind rather than editing the old receipt.
