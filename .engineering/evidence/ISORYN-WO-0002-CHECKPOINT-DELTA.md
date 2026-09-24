# ISORYN WO-0002 Proposed Checkpoint Delta

Status: PROPOSED_ONLY_CORRECTION_REQUIRED. Independent review corrected two factual summaries before promotion: the Godot support interpretation now uses the official release policy, and the GPU-control summary no longer claims that upstream reproduced this build's early Vulkan segfault. Because canonical sources changed, the previous HIVE/MCP proof is stale until the corrected head is re-indexed and re-proved. This file changes nothing by itself. The checkpoint is promoted only by the independent
architecture/toolchain audit of ISORYN-WO-0002, through the governed flow, against the exact head recorded in
`.engineering/evidence/ISORYN-WO-0002-EVIDENCE.md`. The executor does not promote, and does not merge PR #5.

## FROM

`docs/project-brain/13-CHECKPOINT.md` at admission head `2d567f97d5e3affa32bf190b8393a3e6d20d6327`:

- STATUS: ARCHITECTURE DISCOVERY ACTIVE
- VERSION: ISORYN 0.0 - Clean Foundation
- PHASE: 1 - Architecture / Godot Baseline / Toolchain Discovery
- IN PROGRESS: ISORYN-WO-0002-ARCHITECTURE-TOOLCHAIN-DISCOVERY

## TO

- STATUS: READY_FOR_ARCHITECTURE_TOOLCHAIN_AUDIT
- VERSION: ISORYN 0.0 - Clean Foundation (unchanged - no production engine code exists yet and none was written)
- PHASE: 1 - Architecture / Godot Baseline / Toolchain Discovery (unchanged; discovery work is complete, the
  phase closes only at audit)
- IN PROGRESS: NONE - WO-0002 stops at the audit gate. The next admitted Work Order is chosen by the reviewer
  after the audit; `docs/project-brain/14-BACKLOG.md` rows 9 and 10 are the two items this increment leaves
  half-executed and they are ordered by that fact, not by convenience.

## WHAT THIS INCREMENT ESTABLISHED

1. **The Godot baseline is a pinned external source, proven by execution.** `4.7.2-stable` @
   `ed1daf0bf001b61586d9930840f2f1394092c079` is the measured line; `4.6.3-stable` @
   `35e80b3a8822a9df9be390814b62f44c0a9c69e8` is the compatibility reference; the 4.8 development line is
   observation-only. ADR-0001 freezes the baseline and the unmodified-upstream/topology rule as PROPOSED.
2. **The toolchain produced a linked, runnable engine binary** from that source: 6,777 s, exit 0, 2,420 compile
   steps, 68,254,208-byte binary with SHA-256 recorded, version string `4.7.2.stable.custom_build.ed1daf0bf`
   (`docs/project-brain/09-TOOLCHAIN-AND-BENCHMARK-BASELINE.md` §5). ADR-0002 freezes the command line, the
   isolation rules, the receipt discipline and the upstream-sync procedure as PROPOSED.
3. **The editor target is not buildable on this host class, and that is a measured host prerequisite** rather
   than a preference: MSVC fails upstream's ~102 MB generated translation unit at `-j8`, `-j4` and `-j1`
   (ISORYN-D-015). Toolchain proof therefore comes from a `template_release` build, and the two editor-side
   smoke cases are recorded `NOT_AVAILABLE` with their cause instead of being omitted.
4. **A measurement contract exists and was executed against.** Metric vocabulary, one committed workload
   (`.engineering/evidence/wo-0002/bench/`) and eight measurement rules (§3, §4), with the first measured series
   in §6: headless p50 6.898 ms, p95 15.175 ms, p99 15.590 ms over three repeats, and the corresponding
   single-host tolerance (p50 0.06 %, p95 1.3 %, p99 3.4 % spread).
5. **A GPU frame-time baseline does not exist and the reason is now executed, not assumed.** The only windowed
   path that completes the harness on this host is `d3d12`, and its own readback contradicts its numbers: under
   `--write-movie --fixed-fps` it returns frames that are black at every one of 921,600 pixels and byte-identical
   across runs, then dies at `0x887a0005` (`DXGI_ERROR_DEVICE_REMOVED`) while requesting the picture back. The
   control separates the failures instead of reproducing them all: upstream's published binary reproduces the
   host-side shader/device refusal and the OpenGL crash, but it **does not** reproduce this build's early Vulkan
   segfault; upstream remains alive until the timeout where the local build exits after about 3 seconds (§7).
   ISORYN-D-016 records the rule that came out of it: a device is admitted by a readback gate whose
   pixels show the scene, not by an exit code and not by a frame file existing.
6. **The extension seams are real mechanisms with citations, and seam 3 is half-proven.** `custom_modules`
   imports an out-of-tree module into upstream's build with exit 0 and still configures with the module flag off
   (`custom-modules-feasibility.txt`, ADR-0003); compiling such a module both ways is the remaining half
   (backlog row 9).
7. **Coverage is enumerated rather than assumed**: `06-MASTER-MODULE-INDEX.md` (30 module rows across every scope
   family, with dependencies, seam and proof needs) and `07-PROPRIETARY-TECHNOLOGY-REGISTRY.md` (12 entries, each
   with a fallback and no unmeasured superiority claim), including eight confirmed upstream absences.

## WHAT REMAINS OPEN FOR THE AUDIT TO DECIDE

- **The host device blocker (backlog row 10)** is the binding constraint of the next measurement increment:
  choose a host whose display driver works, or accept a headless-only series for the time being. Installing the
  D3D12 SDK is no longer on the list as a fix on its own, because that path was measured and does not draw here.
- **Seam-3 compile proof** (backlog row 9) and the module-disabled negative check at compile level.
- **Whether the `accesskit` / `d3d12` / `angle` configuration exclusions are acceptable** for the scope families
  that depend on them, and therefore whether ISORYN-D-011's isolation rule keeps its current form.
- **Cross-host determinism**: one host is not a hardware class, so the §6 tolerance is explicitly single-host and
  every claim drawn from it must say so.
- Promotion of ADR-0001/0002/0003 from PROPOSED, which is the reviewer's authority and nobody else's.

## EVIDENCE POINTER

`.engineering/evidence/ISORYN-WO-0002-EVIDENCE.md` (exact base/head SHAs, tests, CI state, HIVE/MCP proof,
receipt inventory, errors corrected, residual risks, rollback). Raw discovery workspace
`D:\GodotDiscovery\ISORYN-WO-0002\` is operator-local and disposable by design; every claim in the canonical
sources above points at a committed receipt rather than at that directory.


## INDEPENDENT REVIEW CORRECTION GATE

Before this delta can be promoted, the executor must re-run only the invalidated exact-head surfaces on the
reviewer-corrected branch head: HIVE v1.0.0 inspect/index/corpus/retrieval, the real MCP session, deterministic
governance/tests/secret-scan as applicable, and exact-head Governance CI. The expensive Godot source build,
headless benchmark series and GPU control experiments remain valid for the identities they measured and must not
be repeated unless the official stable tag changed or a correction changes their inputs.
