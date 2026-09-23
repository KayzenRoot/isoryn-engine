# ADR-0001: Godot baseline and repository topology

Status: PROPOSED - freezes on independent audit of ISORYN-WO-0002; not self-promoted.

Date: 2026-09-23
Deciders: ISORYN executor (proposal), independent reviewer (authority)
Related: `docs/project-brain/08-GODOT-BASELINE-AND-TOPOLOGY.md`, `docs/project-brain/04-ARCHITECTURE.md`, `ISORYN-D-005`, ADR-0002, ADR-0003

## Context

`ISORYN-D-005` accepted Godot 4.x as the foundation direction while explicitly deferring the exact
version, fork and upstream-sync boundaries to evidence-backed discovery. WO-0002 must therefore freeze a
baseline that later Work Orders can build against, without pre-committing to a maintenance liability.

Facts established at execution time (all from official sources; receipts in
`.engineering/evidence/wo-0002/godot-official-state.json`):

- `4.7.2-stable` is the current stable release, published 2026-08-18, resolving to commit `ed1daf0bf001b61586d9930840f2f1394092c079`; the pinned clone's `version.py` reports 4.7 / stable and `git describe --tags` reports `4.7.2-stable`.
- The immediately previous supported line is 4.6 (`4.6.3-stable` @ `35e80b3a8822a9df9be390814b62f44c0a9c69e8`, branch `4.6` head carries 4.6.4-rc); 4.5 stopped receiving bumps on 2026-03-19.
- Upstream publishes no LTS or numbered support-lifetime policy, so "supported" is an inference from active maintenance branches.
- `4.8-dev6` is a build label, not a tag; the development line is only citable as `master` @ `4e244f2112c687885767fa3c24ce9233a24a1659` (4.8.0-dev).
- Upstream `SConstruct` exposes `custom_modules` (line 280) and consumes it at lines 446-464, which allows a native module that lives outside the engine tree to be compiled into the engine without editing upstream code.

## Decision

1. Adopt **Godot `4.7.2-stable` @ `ed1daf0bf001b61586d9930840f2f1394092c079`** as the ISORYN foundation baseline. The baseline is expressed as tag **and** 40-character commit plus `version.py` fields, never as a branch name.
2. Keep **`4.6.3-stable` @ `35e80b3a8822a9df9be390814b62f44c0a9c69e8`** as the compatibility reference line for testing whether ISORYN-side extensions survive a minor-line transition. It is not a shipping target.
3. Treat the 4.8 development line as **observation only**. A pre-release is not adoptable because it is newer.
4. Use a **single canonical repository** (`KayzenRoot/isoryn-engine`) for governance, ISORYN modules, addons, tooling, tests and evidence. **Do not create a permanent Godot fork repository** in this increment.
5. **Never vendor the engine tree or engine build outputs into ISORYN.** Upstream lives in an operator-local pinned clone outside the repository, fetched read-only over official HTTPS sources, and is identified by tag/commit in evidence.
6. Add native capability through upstream's `custom_modules` mechanism (seam 3 in ADR-0003), keeping ISORYN module sources inside the ISORYN repository. A seam-3 module must compile with its own enable flag on and off, and must not require edits to upstream files.
7. Baseline changes require a Work Order that re-executes the toolchain receipt, the smoke set and the deterministic benchmark on the candidate tag, followed by a decision entry. A published upstream release never moves the pin by itself.

## Consequences

**Positive**
- Upstream security and bug fixes remain one deliberate step away instead of a permanent merge burden.
- Builds are reproducible: tag + commit + `version.py` + frozen toolchain identify exactly one source state.
- Engine-side risk is bounded: no ISORYN commit ever touches upstream code, so a rebase is a rebuild, not a merge-conflict session.
- A future fork, if ever justified, stays a separate admitted action rather than an accidental drift.

**Negative / accepted costs**
- ISORYN cannot use upstream APIs that exist only on `master`; capability gaps must be solved at seam 2/3 or deferred.
- Upgrade work is batched and therefore occasionally larger than a continuous-tracking approach.
- `custom_modules` compiles against upstream internals, so a seam-3 module inherits recompile risk at every minor line; the compatibility reference line exists specifically to surface that risk before adoption.
- Vendoring remains forbidden, so an engine tree never travels with the repository; a clean build always needs the external pinned clone as an input.

## Evidence

- `.engineering/evidence/wo-0002/godot-official-state.json` (official tag/commit verification and the commands used).
- `docs/project-brain/09-TOOLCHAIN-AND-BENCHMARK-BASELINE.md` and `.engineering/evidence/wo-0002/` build/smoke receipts, which show the adopted baseline actually configures, compiles and runs on the frozen toolchain.
- WO-0002 Evidence Bundle entries `godot_official_source_verification` and `godot_current_stable_build`.

## Reconsider when

- A stable release newer than `4.7.2-stable` is published and a Work Order has re-run the receipts on it.
- A proven capability gap requires editing upstream code (seam 4): then this ADR is superseded per subsystem by a new ADR naming the fork, its sync owner and its rebase cadence.
- Upstream publishes an official support-lifetime policy that invalidates the "supported line" inference.
- A second platform or hardware class enters scope and the single-repository overlay stops compiling for it.
