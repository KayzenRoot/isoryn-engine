# ISORYN Architecture

Status: DISCOVERY_BASELINE (extended by ISORYN-WO-0002)

Git + Project Brain are authoritative. GEF governs lifecycle/evidence. HIVE supplies derived context/retrieval/memory/read-only MCP. CORE is a reference/future partner for execution/orchestration contracts. IRIS is a reference/future partner for media/assets/quality/production systems.

## Foundation baseline

Godot 4.x is the foundation direction. As of ISORYN-WO-0002 the concrete baseline is proposed for freezing by
ADR-0001: upstream `4.7.2-stable` at commit `ed1daf0bf001b61586d9930840f2f1394092c079`, unmodified, cloned and
built **outside** this repository, with `4.6.3-stable` (`35e80b3a8822a9df9be390814b62f44c0a9c69e8`) kept as the
compatibility reference line and the 4.8 development line as observation only. Until the audit promotes that ADR,
this is the working baseline the Work Order itself was executed against.

ISORYN is one canonical repository. It holds governance, ISORYN-owned modules, addons, tooling, tests and
evidence; it never holds a copy of the engine tree or of engine build outputs. Bounded native modules are
compiled from outside the engine through upstream's own `custom_modules` build option (`SConstruct:280`,
`SConstruct:446-464` at the pinned tag), so adding engine-side capability does not require editing or forking
upstream code.

Two host facts discovered while proving that topology bound what this machine can evidence, and both are carried
by ADR-0002: the `editor` target requires a compiler able to hold upstream's ~102 MB generated documentation
translation unit (this host's MSVC cannot, at any `-j`), and a non-editor binary accepts `--path` only when built
with `disable_path_overrides=no`, which is why the frozen command line states that option. Neither fact changes
the topology; each decides which receipts a given host is allowed to claim.

## Decision ladder (seams)

1. use upstream capability when sufficient (seam 1);
2. extend via addon/GDExtension/editor tooling when sufficient (seam 2);
3. add bounded engine modules when evidence requires (seam 3, via `custom_modules`);
4. fork/replace subsystems only when measured value exceeds maintenance cost (seam 4, needs an ADR naming the subsystem, the sync owner and the rebase cost).

ADR-0003 makes each rung testable: what it may touch, what evidence admits it, and how it fails. A change that
requires editing an upstream file is a seam-4 request even when it looks like a one-line module detail.

## Layered view

The pinned baseline's layers, the cited paths inside them, and the family-by-family capability map live in
`docs/project-brain/06-MASTER-MODULE-INDEX.md`. Summary: `core/` (objects, Variant, IO, GDExtension host),
`main/` (frame loop, CLI, `Performance` monitors), `servers/` (thread-isolated subsystems behind `*Server`
singletons, including `renderer_rd` over `drivers/` backends), `scene/` (nodes and resources), `editor/`
(importers, debugger, plugins, export), `modules/` (57 optional feature units at the pinned tag), `drivers/`
(rendering/audio/image/OS backends), `platform/` (per-OS display servers and toolchain detection), and
`doc/classes/` (810 machine-readable class documents: the public API surface).

Optimization principle:
camera/visibility/relevance -> budgets -> geometry/textures/lighting/shadows/animation/VFX/streaming.

Ownership boundaries:
- **upstream-owned**: the Godot tree, cited by tag + commit, never vendored;
- **ISORYN-owned**: governance, modules, addons, tooling, tests, evidence, canonical docs;
- **external-partner-owned**: HIVE, CORE and IRIS state, reached only through versioned contracts.

No shared-database coupling with HIVE/CORE/IRIS. Integrations use versioned contracts, fingerprints/events or explicit tool/API boundaries.

## Measurement dependency

No architecture claim outranks an executed, exact-head receipt. The metric vocabulary, the deterministic
workload and the regression rules are defined in `docs/project-brain/09-TOOLCHAIN-AND-BENCHMARK-BASELINE.md`;
the proprietary-technology proposals in `docs/project-brain/07-PROPRIETARY-TECHNOLOGY-REGISTRY.md` each gate on
that contract, and the measurement harness itself is PT-08.
