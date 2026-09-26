# ISORYN Local Deployment

Status: DISCOVERY_BASELINE (extended by ISORYN-WO-0002)

Current phase deploys governance/integration scaffolding plus a reproducible engine discovery toolchain. No
product runtime is deployed by this phase.

## Canonical workspace

Canonical workspace: D:\Hive\Projects\isoryn-engine

Every proof that claims to describe this repository - HIVE registration/index/corpus/MCP, governance
validation, tests, evidence capture - must run against this path. A proof executed in a different clone of the
same repository proves that clone, not the canonical state (the blocker ISORYN-WO-0001 closed for exactly this
reason).

## Prerequisites

- Git 2.55+, Python 3.12+, Docker Desktop/Compose for HIVE, a local HIVE v1.0.0 checkout/runtime, optional local GEF v1.0.0 source checkout, and a Codex/other MCP-capable CLI when used.
- Engine discovery (from ADR-0002): Visual Studio Build Tools 2022 with the v143 (14.3) toolset family (MSVC 14.44.35207 observed), Windows SDK 10.0.26100.0, and SCons 4.11.1 installed **in an isolated virtual environment** - there is no global `scons` on this host and none is required.
- Upstream requires SCons >= 4.8.0 for the v143 family; that constraint is enforced by the engine's own Windows detection, so an ambient older SCons fails configuration with a message rather than producing a wrong build.

## Layout convention

| State | Where | Owner |
| --- | --- | --- |
| Canonical repository and governance sources | the canonical workspace above | Git |
| HIVE runtime | pinned Docker Compose project, read-only mount of the projects root, explicit port so a concurrent default stack is never disturbed | operator |
| External engine clone + build outputs + scratch | operator-local discovery root, one subdirectory per Work Order (`D:\GodotDiscovery\ISORYN-WO-0002` for this one) | operator, disposable |
| Command/build/smoke/benchmark receipts | `.engineering/evidence/wo-<n>/` inside the repository | Git |

Engine clones and build outputs are never committed: they are disposable operator state. The repository keeps
the receipts, the exact commands, the binary identity (version string, size, SHA-256) and the failure logs.

## Reproduce the discovery build

1. `git clone --depth 1 --branch <pinned tag> https://github.com/godotengine/godot.git` into the Work Order's discovery directory; record the resolved commit.
2. Create a virtual environment there and install SCons into it (do not install SCons globally).
3. Run the command line frozen in ADR-0002:
   `scons platform=windows target=template_release arch=x86_64 accesskit=no d3d12=no angle=no disable_path_overrides=no -j8`.
   `disable_path_overrides=no` is what lets that binary load an unpacked project and therefore run the benchmark
   harness; the shipping-template form of the same command drops the option and cannot (ADR-0002 finding).
   Substitute `target=editor` only on a host that can compile upstream's ~102 MB generated
   documentation-translation unit; this Work Order's host cannot, and the failure ladder is in
   `docs/project-brain/09-TOOLCHAIN-AND-BENCHMARK-BASELINE.md` section 2.
4. Capture start/end timestamps, exit code, the detected compiler/SDK log line, then run the smoke set in `docs/project-brain/11-TEST-PLAN.md`.

`accesskit`, `d3d12` and `angle` stay disabled on purpose: enabling them requires upstream installer scripts that
add third-party SDK state to the host, which this Work Order deliberately avoided. Revisit only with an admitted
need, and re-issue the receipts when you do.

## Deferred

Building the engine in CI remains deferred until a separate Work Order admits it (external pinned clone,
compiler chain, a measured full-template build cost on this host class recorded in
`docs/project-brain/09-TOOLCHAIN-AND-BENCHMARK-BASELINE.md`, and an editor target that this particular host cannot
even build). Export templates, code-signing and release publication are likewise deferred; deployment of any
ISORYN runtime is out of scope until a product Work Order is admitted.
