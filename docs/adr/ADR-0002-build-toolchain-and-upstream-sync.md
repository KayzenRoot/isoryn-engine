# ADR-0002: Build toolchain baseline and upstream synchronization procedure

Status: PROPOSED - freezes on independent audit of ISORYN-WO-0002; not self-promoted.

Date: 2026-09-23
Deciders: ISORYN executor (proposal), independent reviewer (authority)
Related: `docs/project-brain/09-TOOLCHAIN-AND-BENCHMARK-BASELINE.md`, ADR-0001, ADR-0003, `.engineering/evidence/wo-0002/`

## Context

`ISORYN-D-006` requires measurable proof before any performance or quality claim, and ADR-0001 pins the
engine baseline to an external, unmodified upstream clone. That makes the compiler chain part of the
canonical architecture: if the build is not reproducible, no benchmark, smoke result or seam-3 module
claim can be reproduced either.

WO-0002 therefore executed the toolchain rather than describing it. Everything below was observed on the
current host at execution time (machine-readable copy:
`.engineering/evidence/wo-0002/toolchain-inventory.json`), not recalled from notes.

### Observed host and toolchain

| Item | Value |
| --- | --- |
| OS | Windows 11 Home Single Language, 10.0.26200, x64, 22.9 GB visible RAM |
| CPU | AMD Ryzen 5 2500U with Radeon Vega Mobile Gfx, 4 cores / 8 logical, 2000 MHz base |
| GPU (active display) | AMD Radeon (TM) Vega 8 Graphics, driver 31.0.21925.1001 (2026-05-19), desktop 2560x1440@60 |
| Other display adapters reported | Parsec Virtual Display Adapter 0.45.0.0; "Radeon 535 Series" 26.20.12036.1 - both non-primary, but they make GPU enumeration ambiguous on this host |
| Compiler | Visual Studio Build Tools 2022 (17.14.37628.2), MSVC toolset family 14.3 (v143), installed compiler 14.44.35207 |
| Windows SDK | 10.0.26100.0 (single installed version) |
| Python | 3.12.10 (system), plus an isolated virtual environment for the build |
| SCons | 4.11.1 inside the isolated environment; **no** global `scons` on this host |
| Git | 2.55.0.windows.3 |
| Other | CMake 4.4.3 present but unused by Godot; Ninja absent; disk free on the build volume 213.8 GB |

### Why each of those numbers is load-bearing

- Upstream requires **SCons >= 4.8.0 for the VS2022 toolset family** and >= 4.10.1 for the newer family
  (`platform/windows/detect.py:187-192`), so an ambient older SCons is a hard failure, not a warning.
- The three optional drivers that need extra local installation state - `accesskit`, `d3d12` and `angle` -
  behave differently and all three were observed. `accesskit` and `d3d12` abort **configuration**; `angle` emits a
  warning that instructs the operator to pass `angle=no` explicitly, so the frozen command states all three
  instead of relying on ambient defaults. The first attempt recorded the abort (exit 255 after 14 seconds, log
  `.engineering/evidence/wo-0002/build-4.7.2-editor.attempt1-configure-failure.log`). The resolution uses
  upstream's documented overrides rather than installing third-party SDK state on the host, so the toolchain
  claim stays reviewable. The completed binary states the consequence of that choice itself when asked for the
  driver it was compiled without: `Unknown rendering driver 'd3d12', aborting. Valid options are 'vulkan',
  'opengl3' and 'dummy'.` (`godot-4.7.2-smoke.txt`), which is why the smoke set records that case as
  `NOT_AVAILABLE` on this build rather than omitting it.
- **A build option is not a rendering device, and only the second one is measurable.** Excluding `d3d12` raised
  the question of whether the frozen command can produce a GPU baseline at all, so WO-0002 executed the driver
  through upstream's own published binary for the same tag instead of arguing about it. That run completes the
  harness and prints a full metric series - and the frames it gives back when asked are empty: each
  `--write-movie` execution that returned anything at all returned one frame of the 700 requested, every such frame
  is byte-identical, 1280x720 and black at all 921,600 pixels, and the run then dies at
  `Can't create buffer of size: 3686400, error 0x887a0005` (one 1,280x720 RGBA frame) and segfaults, while the plain
  windowed run of the same workload finishes with zero logged errors (`gpu-windowed-device-control.txt`,
  `gpu-readback-golden-frame.txt`). The host can present, and what it hands back when asked for the picture contains
  none of it; a measurement needs the second one. A series that cannot be checked against a drawn output is not a
  baseline, so ISORYN-D-016 admits a windowed device only through a readback gate, and installing the SDK is now
  known not to be a sufficient fix on this host. Receipt discipline follows: a smoke case is reported with the
  artifact that proves it drew, not with its exit code.
- **A missing output line needs a second sink before it can be read as a fact - and that control separated a host
  fault from a build fault.** The windowed cases first carried no harness line, which was then explained away as
  buffered stdout lost to the segfault. Neither statement had been executed. `windowed-output-sink-control.txt`
  runs each windowed path writing to the redirected console and to the engine's own `--log-file` writer at once:
  the line reaches both sinks on the headless paths and reaches both on upstream's binary running the same windowed
  Vulkan path with the same flags, and reaches neither on this build, which dies before the workload is
  instantiated. So the device refusal both artifacts report belongs to the host, while this build's segfault about
  3 s in - where upstream's binary is still rendering 300 s later - does not, and WO-0002 does not explain it. Until
  that difference is attributed, the Decision item 2 command line is a measurement build and not a CI reference
  build, which is the condition Decision item 6 already keeps out of the repository workflow.
- **Compiler memory, not compiler parallelism, is the editor target's constraint on this class of host.**
  SCons generates `editor/translations/doc_translations.gen.cpp` as one ~102 MB / 858k-line translation unit from
  `doc/translations/*` with no switch to shrink it (`editor/SCsub:59-71`). MSVC fails it with `fatal error C1060`
  at `-j8`, at `-j4`, and at `-j1` with nothing else running (attempts 2, 3 and 4 in
  `docs/project-brain/09-TOOLCHAIN-AND-BENCHMARK-BASELINE.md`). A build host therefore needs a compiler that can
  hold that unit before it can build the editor at all; a host that cannot must build a template target and say
  so rather than describe an editor build it never produced.
- **A template binary cannot load an unpacked project until it is asked to.** `disable_path_overrides` defaults
  to `True` and `OVERRIDE_PATH_ENABLED` is defined only for editor builds or when that option is cleared
  (`SConstruct:272-278`, `SConstruct:1101-1102`), so a stock `template_release` refuses both an explicit project
  path (`main/main.cpp:1818-1822`) and a project found in the working directory (`main/main.cpp:2115-2123`) and
  expects an exported `.pck`. Exporting a pack is an editor operation, so on a host that cannot build the editor
  the only way to run a committed harness against a release-optimised engine is the option upstream names in
  that error text: `disable_path_overrides=no`. The build is marked "template unsafe" for exactly that reason
  (`--path` carries `CLI_OPTION_AVAILABILITY_TEMPLATE_UNSAFE`, `main/main.cpp:576`) - acceptable for a local
  measurement binary, not for a shipped one.

## Decision

1. **Toolchain baseline (minimum, not preference)**: Windows 11 x64; Visual Studio Build Tools 2022 with
   the v143 (14.3) toolset family and MSVC 14.44.35207 or newer inside that family; Windows SDK
   10.0.26100.0; Python 3.12.10; SCons 4.11.1 installed **only** in a per-discovery virtual environment;
   Git 2.55+. On top of that, a host that intends to build the **editor** target must be able to compile a
   ~100 MB generated translation unit in one compiler process - this discovery host (22.9 GB visible RAM,
   12 GB pagefile) cannot, and that is a measured fact rather than a guess. A build host that differs must
   re-run the receipts before its numbers are comparable.
2. **Reproducible discovery build command**, executed inside the isolated environment against the pinned
   external clone (full receipts, including wall time and exit code, in
   `docs/project-brain/09-TOOLCHAIN-AND-BENCHMARK-BASELINE.md`):

   ```
   scons platform=windows target=template_release arch=x86_64 accesskit=no d3d12=no angle=no disable_path_overrides=no -j8
   ```

   `disable_path_overrides=no` is part of the frozen command, not an optional extra: without it the binary this
   command produces cannot load the committed benchmark harness (see the finding above). A shipping export
   template is built from the same line **with that option dropped**, and that variant is never the one a
   measurement is taken from. The editor target uses the same flags with `target=editor`, and on this host it
   stops at the generated documentation-translation unit described above; the two commands are therefore
   recorded as separate receipts with separate outcomes, not averaged into one "build works" claim.
3. **Isolation rules**: the engine clone and every build output live outside the ISORYN repository; the
   virtual environment is not committed; environment variables inherited from other projects (for example
   an ambient Compose project name) must not affect the build, so discovery commands run with an explicit,
   recorded working directory rather than relying on shell state.
4. **Receipt discipline**: a toolchain claim needs the command line, the start/end UTC timestamps, the exit
   code, the detected compiler/SDK line from the build log, the produced binary's version string, size and
   SHA-256, and the failing log when something failed. Failures are preserved as separate receipts, never
   overwritten.
5. **Upstream synchronization procedure** (the operative half of ADR-0001 item 7):
   1. fetch the candidate tag read-only into the external clone and record tag + commit + `version.py`;
   2. build with this command line and record the receipt;
   3. run the smoke set (version string, import, headless run, windowed run on the GPU, and editor boot where
      the host can build the editor at all - an unavailable editor binary is recorded as `NOT_AVAILABLE` with the
      failing command, never skipped in silence). The windowed case counts as passed only if the run reaches the
      harness's own report point *and* the same path can read frames back under `--write-movie`: an exit code of 0
      with a printed series is not sufficient, because ISORYN-WO-0002 measured a path that did exactly that while
      its device was already removed (`ISORYN-D-016`);
   4. run the deterministic benchmark workload and compare metric series to the current baseline;
   5. only then move the pin in a Work Order that carries all four artifacts.
6. **CI boundary**: the repository's Governance workflow stays deterministic and engine-free. Building the
   engine in CI is a separate decision requiring its own Work Order, because it needs the external pinned
   clone, a compiler chain, and a build whose cost on this class of host is the measured number in
   `docs/project-brain/09-TOOLCHAIN-AND-BENCHMARK-BASELINE.md` §5 rather than an estimate written here.

## Consequences

- Engine claims become re-executable by anyone with the same toolchain family, and a reviewer can check a
  receipt against a command line rather than against prose.
- The optional-driver overrides mean the discovery build does **not** include `accesskit` or `d3d12`. That is
  an explicit, recorded gap rather than a silent one: accessibility and the Direct3D 12 driver path are
  outside every WO-0002 conclusion, and any later claim about them needs their prerequisites installed and a
  new receipt. The `d3d12` half of that gap was probed anyway, through upstream's own published binary, and the
  result is in the context section above: enabling the driver is not by itself what would buy this project a GPU
  baseline on this host.
- Because the toolchain is pinned to a *family*, a compiler point upgrade inside the family is allowed and
  must still be recorded; a family change (for example 14.3 to 14.5) is an ADR-level event.
- Build cost is a measured planning input, not an estimate: `docs/project-brain/09-TOOLCHAIN-AND-BENCHMARK-BASELINE.md`
  §2 carries the wall time, exit code and object count of each attempt on this 4-core mobile host. The
  `editor` target was never completed on this host (the compiler-heap failure in ISORYN-D-015), so no editor wall
  time is claimed; the completed-build number is the `template_release` receipt, and it is large enough that
  incremental builds and module-flag discipline matter for iteration.
- Two engine binaries now have distinct roles that must not be confused in a receipt: the
  `disable_path_overrides=no` build is the development/measurement binary, and a shipping template is a different
  command line whose binary cannot open an unpacked project. Every benchmark claim names which one produced it.

## Reconsider when

- a second hardware class or operating system enters scope (then the receipts are per-class, not one global baseline);
- the `accesskit` or `d3d12` gap blocks an admitted requirement;
- upstream raises its SCons/compiler/SDK minimum beyond this baseline;
- CI is admitted for engine builds, which needs its own caching and disk-space plan.
