# ISORYN Godot Baseline and Repository Topology

Status: DISCOVERY_BASELINE (ISORYN-WO-0002)

This document records what was verified from official sources on 2026-09-23, the options that were
compared, and what ADR-0001 proposes to freeze. Machine-readable receipts live in
`.engineering/evidence/wo-0002/`. Build and toolchain results live in
`docs/project-brain/09-TOOLCHAIN-AND-BENCHMARK-BASELINE.md`.

## 1. Verified official state

| Role | Official tag | Commit SHA | Published | How verified |
| --- | --- | --- | --- | --- |
| Current stable (mandatory discovery target) | `4.7.2-stable` | `ed1daf0bf001b61586d9930840f2f1394092c079` | 2026-08-18T16:12:28Z | `git ls-remote` of the upstream repository, then `git clone --depth 1 --branch 4.7.2-stable` and `git describe --tags` inside the clone; `version.py` reads 4.7 / stable |
| Immediately previous supported line (compatibility reference) | `4.6.3-stable` | `35e80b3a8822a9df9be390814b62f44c0a9c69e8` | 2026-05-20T20:49:16Z | `git ls-remote` tag resolution; branch `4.6` head `a80a06c3e819d5b77a1737441aec9ccf1d93eda7` carries `version.py` 4.6.4-rc |
| Development line (observation only) | none - `master` branch | `4e244f2112c687885767fa3c24ce9233a24a1659` | 2026-09-23 | `git ls-remote` branch head; `version.py` reads 4.8.0-dev |
| Maintenance heads at execution time | `4.7` / `4.6` branches | `83dec14d549108e1f314f57c1ce7e932c65370dd` / `a80a06c3e819d5b77a1737441aec9ccf1d93eda7` | 2026-09-20 / 2026-08-14 | branch heads carry 4.7.3-rc and 4.6.4-rc in `version.py` |

Re-verification of the admission claims: the Work Order was admitted on the statement that `4.7.2-stable`
is the current stable release and that a `4.8-dev6` pre-release exists. Both statements were confirmed,
with one correction that matters for citation hygiene: **`4.8-dev6` is a distributed build label, not a git
tag**. Any claim about the development line must therefore bind to a commit, not to a dev label.

Independent review added the official release-policy source that the executor's receipt omitted:
`https://docs.godotengine.org/en/latest/about/release_policy.html`. At review time it explicitly lists
Godot 4.7 and 4.6 as receiving bug/security/platform-support fixes, Godot 4.5 as receiving security and
platform-support fixes only, and Godot 4.4 and older 4.x lines as no longer supported. Therefore 4.6 remains
the immediately previous **fully supported** minor line for the compatibility reference, but that conclusion
comes from upstream's support timeline, not from inferring maintenance solely from branch version bumps.
The raw executor receipt is intentionally not rewritten; this paragraph is the reviewer correction that
supersedes its support-policy interpretation.

## 2. Options compared

| Criterion | A: track `master` | B: pin current stable, upgrade by ADR | C: permanent fork repository | D: vendor engine source into ISORYN |
| --- | --- | --- | --- | --- |
| Upstream security/bug fixes | immediate, unstable | one ADR step behind, deliberate | manual, decays | manual, decays |
| Sync cost | highest (moving API, dev churn) | bounded and schedulable | grows with every local edit | grows with every local edit |
| Reproducible build | no (branch head changes daily) | yes (tag + commit + `version.py`) | only with pinned mirror | only with pinned mirror |
| Public API stability for tooling | no | yes within a minor line | depends on local churn | depends on local churn |
| Fits `ISORYN-D-005` and the decision ladder | no | yes | only when seam 4 is proven | forbidden by AGENTS.md without an ADR; no benefit over B |
| Repository hygiene | clone outside repo | clone outside repo | extra canonical state | engine tree inside repo, violates WO-0002 out-of-scope |
| Risk accepted | churn risk | upgrade lag | maintenance liability | license/attribution and diff-noise liability |

## 3. Proposed baseline (ADR-0001)

1. **Foundation baseline**: Godot `4.7.2-stable` @ `ed1daf0bf001b61586d9930840f2f1394092c079`, unmodified upstream, cloned and built **outside** the ISORYN repository.
2. **Compatibility reference**: Godot `4.6.3-stable` @ `35e80b3a8822a9df9be390814b62f44c0a9c69e8` - used to test whether ISORYN-facing extensions keep working across a minor line, not as a second shipping target.
3. **Observation only**: `master` @ `4e244f2112c687885767fa3c24ce9233a24a1659` (4.8.0-dev). Not adoptable in this increment; pre-release status plus no adopted need.
4. **Upgrade trigger**: a new stable patch (`4.7.3-stable` or later) or minor (`4.8-stable`) release does **not** move the baseline automatically. It requires a Work Order that re-runs the toolchain receipt, the smoke set and the deterministic baseline on the new tag, then a decision entry.
5. **Stale condition**: this baseline claim goes stale if a stable tag newer than `4.7.2-stable` is published before the audit, or if the official archive stops listing `4.7.2-stable` as current stable. Receipts must then be re-captured rather than inherited.

## 4. Repository and topology decision

**Single canonical repository** (`KayzenRoot/isoryn-engine`) holding ISORYN-owned governance, modules,
addons, tooling, tests and evidence. Godot stays external and unmodified.

| Element | Where it lives | Why |
| --- | --- | --- |
| Governance, Project Brain, evidence, ADRs | ISORYN repository | canonical state is Git-owned |
| ISORYN native modules (seam 3) | ISORYN repository, built into the engine through upstream's `custom_modules` option (`SConstruct:280`, `SConstruct:446-464`) | no fork needed to add a module |
| ISORYN addons / editor tooling / GDExtension clients (seam 2) | ISORYN repository | plain project content and DSO sources, upstream remains untouched |
| Upstream Godot tree | external, operator-local pinned clone; never committed | WO-0002 out-of-scope forbids vendoring; keeps diff noise and attribution risk at zero |
| Build outputs (objects, binaries) | external scratch directory | generated artifacts are operator state, not repository state |
| A future fork, if ever proven necessary | separate repository, separate ADR | explicitly not admitted here |

The `custom_modules` finding is what makes this topology cheap enough to prefer over a fork: the engine
compiles ISORYN modules from a path outside its own tree, so an upstream rebase does not merge-conflict
with engine code - ISORYN code never edits engine code.

## 5. Upstream synchronization policy

1. **Baseline identity** is recorded as tag + 40-character commit + `version.py` fields, in the official-state receipt, in every Work Order Context Lock that touches the engine, and in build evidence.
2. **Rebase cadence**: evaluate at every stable patch release, and mandatorily before admitting any Work Order that changes a seam-3 module.
3. **Rebase procedure** (documented as a runbook, executed in an external clone): fetch the new tag read-only; build with the frozen toolchain; run the smoke set; run the deterministic baseline; compare metric series; only then move the pin.
4. **Module compatibility check**: seam-3 modules must compile with their enable flag both on and off, and must not require edits to upstream files. A module that needs an upstream edit is evidence that it is a seam-4 candidate, which needs its own ADR.
5. **API stability surface**: prefer `doc/classes/` (810 XML class documents at the pinned tag) and the dumped extension API (`core/extension/extension_api_dump.cpp`) as the contract; treat internal C++ headers as private and re-check them at every rebase.
6. **No silent divergence**: any ISORYN-side patch to upstream code, however small, must appear in the evidence bundle as a named diff with a reason, or it is a defect.

## 6. What is frozen, what is still open

| Item | State |
| --- | --- |
| Godot baseline (tag + commit) | proposed for freeze by ADR-0001 |
| Topology (upstream + overlay, no fork repository) | proposed for freeze by ADR-0001 |
| Build toolchain and command line | proposed for freeze by ADR-0002, gated on the build receipt |
| Extension seam ladder | proposed for freeze by ADR-0003 |
| Benchmark contract | defined in `09-TOOLCHAIN-AND-BENCHMARK-BASELINE.md`; the contract is frozen, the first executed series is headless-only because no windowed rendering device works on this host (see the row below) |
| Windowed rendering device on this host | OPEN, and it is the binding constraint of this increment - no device path on this machine produces a verifiable frame. The Vulkan loader skips the current AMD ICD and the one device it keeps refuses every shader module, so both windowed paths this binary can select end in a crash while the headless path runs clean; the OpenGL path dies during context creation; and the third path, `d3d12`, completes the harness on the official binary yet returns nothing when asked for the picture back - the `--write-movie` executions this increment can speak for produced four frames in total, each 1280x720 and black at all 921,600 pixels although the scene has a current `Camera3D` and the viewport clears to a non-black default, and each run then dies at `Can't create buffer of size: 3686400, error 0x887a0005` - so its series cannot be checked against any drawn output (ISORYN-D-016 admits a device only through a readback gate that returns pixels of the scene). Upstream's own `4.7.2-stable` binary reproduces the device refusal and the OpenGL crash on the same host (and is the only binary that can attempt the third path, since this build excludes that driver), but it does not reproduce this build's early Vulkan exit: on the same flags it is still rendering when the 300 s cap kills it, so the refusal is host state while the segfault about 3 s in is a property of this build that WO-0002 leaves unexplained (`windowed-output-sink-control.txt`). Executed controls: `.engineering/evidence/wo-0002/gpu-windowed-device-blocker.txt` (crash cause, configured-driver refusal), `gpu-windowed-device-control.txt` (full-harness runs plus the readback gate), `windowed-output-sink-control.txt` (two sinks at once, which is what turns a missing output line into a statement about the run) and `gpu-readback-golden-frame.txt` with the frame files under `frames/` (the gate's output, decoded to a pixel hash); headless numbers are never substituted for a GPU baseline |
| Cross-host determinism tolerance | OPEN - one host is not a hardware class matrix; requires the PT-08 harness plus at least one second class |
| Optional driver support on this host | OPEN, and now measured rather than assumed - all three drivers that need extra host state (`accesskit`, `d3d12`, `angle`) are disabled in the frozen command line; `accesskit`/`d3d12` abort configuration unless upstream's installer scripts run first (`misc/scripts/install_d3d12_sdk_windows.py`), and `angle` warns until it is passed explicitly. `d3d12` looked like the way out and is not: upstream's own binary completes the harness through it, and the same path hands back an empty picture when its output is read - the frames its `--write-movie` runs produced are all 1280x720 and black at every pixel, and the runs end at `Can't create buffer of size: 3686400, error 0x887a0005` - so its numbers cannot be checked against any drawn output (ISORYN-D-016). Admitting the SDK install would therefore buy a build option, not a GPU baseline; the binding constraint is this host's display driver stack, and that is a reviewer decision rather than an executor convenience |
| Editor target on this hardware class | OPEN - the `editor` target cannot be compiled here (MSVC `C1060` on upstream's ~102 MB generated translation unit, at `-j8`, at `-j4`, and at `-j1` with nothing else running); the toolchain proof and every measurement come from a `template_release` binary, and ISORYN-D-015 states what a host must clear to build the editor |
| Import-time asset pipeline and export templates | OPEN - resource import (`--import`) and `.pck`/`.export` generation are editor-only (`main/main.cpp:700`, `main/main.cpp:1597-1766`), so on a host that cannot build the editor the importer path, the export path and the shipping-template form of the binary are all unverified. The WO-0002 harness is procedural geometry and does not touch them |
| Shipping template variant | OPEN by design - the measurement binary carries `disable_path_overrides=no`; the shipping form drops it and cannot load an unpacked project (ADR-0002). Neither variant has been built as an export template here, because exporting needs the editor |
| Second stable-line shipping target | OUT OF SCOPE - 4.6 is a compatibility reference, not a support promise |
