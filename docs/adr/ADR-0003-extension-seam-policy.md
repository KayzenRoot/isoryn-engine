# ADR-0003: Extension seam policy

Status: PROPOSED - freezes on independent audit of ISORYN-WO-0002; not self-promoted.

Date: 2026-09-23
Deciders: ISORYN executor (proposal), independent reviewer (authority)
Related: `docs/project-brain/04-ARCHITECTURE.md` (decision ladder), `docs/project-brain/06-MASTER-MODULE-INDEX.md`, `docs/project-brain/07-PROPRIETARY-TECHNOLOGY-REGISTRY.md`, ADR-0001, ADR-0002

## Context

`docs/project-brain/04-ARCHITECTURE.md` already states the ladder in principle: upstream first, then
addon/GDExtension/tooling, then bounded modules, then fork or replacement. A principle is not testable.
WO-0002 discovered the concrete mechanisms available at the pinned baseline, so this ADR turns the ladder
into rules a review can check: which seams exist, what each one may touch, what evidence admits a move,
and what "failing" looks like at each level.

Two discoveries drive the shape of the policy:

- `core/extension/` (GDExtension host: `gdextension.cpp`, `gdextension_manager.cpp`, `gdextension_interface.gen.h`, `extension_api_dump.cpp`) plus `doc/classes/` (810 class documents at the pinned tag) form a public, machine-checkable surface that needs no engine recompile.
- `SConstruct:280` / `SConstruct:446-464` accept `custom_modules` paths, so a native engine module can be compiled from outside the engine tree. Before this discovery, "add a module" implicitly meant "fork the engine"; it no longer does. WO-0002 executed the mechanism rather than reading it: a probe module living entirely outside the clone (`custom_modules=<discovery>/custom_modules_probe/isoryn_probe`) was imported by upstream's own build system, printed its `config.py` marker and reached `scons: done building targets` with exit 0, and the same command with `module_isoryn_probe_enabled=no` still configured cleanly (exit 0). No upstream file was touched. Receipt: `.engineering/evidence/wo-0002/custom-modules-feasibility.txt`. What that dry run does **not** prove is compile and link of a module's C++ objects, which needs hours of build time and remains an admission gate rather than an assumption.

## Decision

### Seam 1 - use upstream as-is

- **May touch**: project content, scenes, resources, `.godot` settings. Nothing in native code.
- **Admission evidence**: none beyond the pinned baseline itself.
- **Failure mode**: a capability is assumed to exist that the pinned tag does not provide. Guarded by citing tag + commit + path/symbol in any capability claim.

### Seam 2 - addon, editor plugin, GDExtension client, or tooling

- **May touch**: GDScript/C# addons, `editor/plugins/` and `editor/import/editor_import_plugin.h` extension points, native DSOs loaded through `core/extension/`, command-line and CI tooling, and public automation surfaces (DAP in `editor/debugger/debug_adapter/`, GDScript LSP in `modules/gdscript/language_server/`).
- **Must not touch**: upstream source files, engine internals behind private headers, or another project's globals.
- **Admission evidence**: runs against an **unmodified official engine binary** built at the pinned tag; declares its compatibility range as tag bounds; documents what happens when the extension is absent (degrade, not crash).
- **Failure mode**: version drift against the dumped API. A class-name collision with an upstream ClassDB type is a load failure; the contract must state that outcome rather than discover it in the field.

### Seam 3 - bounded engine module built through `custom_modules`

- **May touch**: its own directory tree outside the engine source, registered through upstream's module detection; may use engine headers that are not part of the dumped public API.
- **Must not touch**: any upstream file. A change that requires editing upstream code is a seam-4 request, not a seam-3 detail.
- **Admission evidence**: (a) compiles with the module flag on **and** off; (b) ships a `config.py` default that is conservative; (c) names the upstream headers it depends on, since those are private and re-checked at every rebase; (d) runs the smoke set on a build with the module enabled; (e) proves it on the compatibility reference line before a minor-line transition is claimed.
- **Failure mode**: silent coupling to internals, which surfaces as a broken build after a rebase. The header list is the mitigation and belongs in evidence.

### Seam 4 - fork or subsystem replacement

- **Requires**: an ADR naming the specific subsystem, the measured evidence that seams 1-3 cannot deliver, the rebase cost model, the sync owner, and an explicit user authorization to create or use a fork repository. ADR-0001 does **not** pre-authorize this.
- **Admission evidence**: benchmark deltas on an admitted deterministic workload plus a maintenance-cost statement, not a capability argument.
- **Failure mode**: the classic drift trap - a fork becomes the baseline and upstream fixes stop arriving. Any seam-4 ADR must state how upstream commits continue to flow in.

### Cross-seam rules

1. **Downward is cheap, upward is expensive**: a proposal may move from a higher seam to a lower one with review; moving up requires the proof gate named in the Master Module Index row.
2. **No silent divergence**: any patch to upstream code, however small, must appear in the evidence bundle as a named diff with a reason, or it is a defect.
3. **One owner per boundary**: ISORYN-owned, upstream-owned and external-partner (HIVE/CORE/IRIS) code stay in separate namespaces; integrations use versioned contracts, fingerprints/events or explicit tool/API boundaries, and never a shared database.
4. **Documented failure behavior**: every seam declares timeout, retry and degradation semantics; "unknown state" is not an acceptable outcome for an editor or CI automation path.
5. **Stable ABI/API assumption is not assumed**: only the dumped interface (`gdextension_interface.*`, `doc/classes/`) is treated as stable within its declared range. Everything else is re-verified per tag.

## Consequences

- Most near-term ISORYN value (PT-01, PT-03, PT-06, PT-08, PT-09) can be attempted at seam 2, which means it can ship against official engine builds and be dropped without residue.
- Seam 3 is now a real option rather than a euphemism for a fork, so ISORYN can grow native capability while ADR-0001 keeps upstream unmodified.
- Reviews gain a concrete question: *which seam does this change actually occupy, and does its evidence match?* A pull request that edits an upstream file while claiming seam 3 is a finding, not a nuance.
- The cost is documentation: a header dependency list, a compatibility range and a degrade path per extension.

## Reconsider when

- Upstream changes the module or GDExtension mechanism (for example a different build option or a stabilized module ABI), or
- a seam-3 module repeatedly breaks on rebase for reasons the header list did not predict, or
- a measured result shows a seam-2 implementation cannot reach the budget that its proof gate defines.
