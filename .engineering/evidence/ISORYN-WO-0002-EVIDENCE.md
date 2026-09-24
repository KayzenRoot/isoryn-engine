# ISORYN-WO-0002 - Evidence Bundle

Status: DELIVERED_FOR_AUDIT (supersedes the ADMISSION_BASELINE record in place)

Everything below was executed against `D:\Hive\Projects\isoryn-engine`, the canonical workspace, on branch
`isoryn-wo-0002-architecture-toolchain-discovery` against base main `74c47fa`. The Godot baseline is
`4.7.2-stable` at `ed1daf0bf001b61586d9930840f2f1394092c079`, verified against the official tag and a local
clone; the engine tree stays outside the repository and nothing of it is vendored.

Three claims in this increment were written and then measured wrong, and each was corrected by executing a control
rather than by rephrasing: a windowed run truncated below the harness report point was first read as a clean render;
the readback gate counted frames in the wrong directory and so reported none when four existed; and a missing output
line was attributed to buffered stdout without testing it. The third correction is the one that changed a
conclusion - the two-sink control shows this build segfaulting on the Vulkan path where upstream's published binary
keeps rendering, so the device refusal is host state while the early crash is a property of this build that WO-0002
does not explain and that gates CI adoption.

The GPU frame-time baseline is recorded `NOT_AVAILABLE` with its executed controls, including four committed frames
that are black at all 921,600 pixels.

`governance_ci` is `UNKNOWN` in this block because the run for the delivered head does not exist yet at write
time and a commit cannot carry its own check-run; the exact-head result is captured in
`.engineering/evidence/wo-0002/ci.json` by the push this delivery produces and is stated in the delivery
record on the pull request.

```json
{
  "schemaVersion": "isoryn-gef-evidence-v1",
  "workOrder": "ISORYN-WO-0002",
  "role": "DELIVERY",
  "supersedes": "ADMISSION_BASELINE (headSha ec1f419e... recorded at admission, no executed claim)",
  "capturedAt": "2026-09-24T00:15:28Z",
  "commandsExecutedAtHead": "958d5ed0bfb74be40eec5f7b3ef0f57fee76b9f4",
  "commandsExecutedAtNote": "governance_validator, unittest_suite, py_compile, git_diff_check, secret_scan and no_vendored_engine_source were produced by running those commands against this working tree while this record was being written; the other rows bind to proofHeadSha and carry their receipts.",
  "baseSha": "74c47fa204a5da79c1418fb9bcc2557603422f88",
  "admissionHeadSha": "2d567f97d5e3affa32bf190b8393a3e6d20d6327",
  "proofHeadSha": "958d5ed0bfb74be40eec5f7b3ef0f57fee76b9f4",
  "headSha": "958d5ed0bfb74be40eec5f7b3ef0f57fee76b9f4",
  "candidateHeadSha": "958d5ed0bfb74be40eec5f7b3ef0f57fee76b9f4",
  "headBindingNote": "Nothing in this record claims a proof ran at a head it did not run at. The executed discovery receipts were captured between 2026-09-23T17:50:00Z and 2026-09-23T23:16:16Z, while the branch head was the admission head and this Work Order's artifacts were still uncommitted in the working tree; the security-analysis receipt was captured at the pre-delivery head; the HIVE/MCP receipt was captured at the proof head and is corroborated by the container's own `git rev-parse HEAD`. The engine build is bound to upstream by the version compiled into the binary, not by a repository head at all.",
  "receiptHeadBinding": {
    "discoveryReceipts": {
      "windowUtc": [
        "2026-09-23T17:50:00Z",
        "2026-09-23T23:16:16Z"
      ],
      "branchHeadAtWindowStart": "2d567f97d5e3affa32bf190b8393a3e6d20d6327",
      "branchHeadAtWindowEnd": "2d567f97d5e3affa32bf190b8393a3e6d20d6327",
      "workingTreeAtCapture": "WO-0002 deliverables present but uncommitted"
    },
    "securityAnalysisReceipt": {
      "capturedAt": "2026-09-23T23:58:49Z",
      "branchHeadAtCapture": "4fb5cc26357e56cd821f591cc016bd95e3cab0fe"
    },
    "hiveMcpProofReceipt": {
      "capturedAt": "2026-09-24T00:10:58Z",
      "branchHeadAtCapture": "958d5ed0bfb74be40eec5f7b3ef0f57fee76b9f4",
      "corroboratedBy": "in-container git rev-parse HEAD"
    },
    "engineBuild": {
      "embeddedVersion": "4.7.2.stable.custom_build.ed1daf0bf",
      "upstreamCommit": "ed1daf0bf001b61586d9930840f2f1394092c079",
      "artifactSha256": "7052a3f08be1872418cae83c08c15c5ff46e52950b2fb8d43b19b24587914a18",
      "note": "A binary is identified by what went into it and by its own hash; the repository head at build time identifies the documents, not the engine."
    },
    "gap": "Receipts quote their capture instant and the identity of what they measured, but not `git rev-parse HEAD` at that instant, so the head binding above is reconstructed from the receipts' own timestamps against this branch's commit order. Recording the head inside each receipt is a one-line change to the capture scripts and belongs to the next increment."
  },
  "branch": "isoryn-wo-0002-architecture-toolchain-discovery",
  "canonicalWorkspace": "D:\\Hive\\Projects\\isoryn-engine",
  "pr": {
    "number": 5,
    "url": "https://github.com/KayzenRoot/isoryn-engine/pull/5",
    "state": "OPEN",
    "merged": false
  },
  "hivePreflight": {
    "target": {
      "launcher": "python scripts/hive_mcp.py",
      "composeProjectSelectedByLauncher": "isoryn-c02-v100",
      "ambientComposeProjectNameDuringProof": "hive-v102",
      "argv": [
        "docker",
        "compose",
        "-p",
        "isoryn-c02-v100",
        "exec",
        "-T",
        "api",
        "python",
        "-m",
        "app.mcp_server"
      ],
      "apiBaseUrl": "http://127.0.0.1:18199",
      "projectId": "cf0e7dee-bfa4-4f54-b8fa-8391afefbcfd",
      "relativePath": "isoryn-engine",
      "isolationNote": "The machine still exports COMPOSE_PROJECT_NAME for the drifted v1.0.2 stack; only HIVE_COMPOSE_PROJECT makes the launcher pass -p, and the container that answered is the pinned v1.0.0 one whose HEAD matches the proof head below."
    },
    "result": "PASS",
    "health": {
      "status": "ok",
      "version": "1.0.0"
    },
    "bootstrap": {
      "command": "python scripts/hive_bootstrap.py --base-url http://127.0.0.1:18199 --relative-path isoryn-engine",
      "exitCode": 0,
      "stderr": null
    },
    "pipeline": {
      "project_id": "cf0e7dee-bfa4-4f54-b8fa-8391afefbcfd",
      "relative_path": "isoryn-engine",
      "git_branch": "isoryn-wo-0002-architecture-toolchain-discovery",
      "git_head_sha": "958d5ed0bfb74be40eec5f7b3ef0f57fee76b9f4",
      "state": "READY",
      "working_tree_clean": true,
      "index_status": "COMPLETED",
      "corpus_status": "COMPLETED"
    },
    "workingTreeCleanAtProof": true,
    "inContainerHeadProbe": "958d5ed0bfb74be40eec5f7b3ef0f57fee76b9f4",
    "note": "Executed at the proof head on the isolated compose project named in the receipt. Derived state only: Git and the canonical checkpoint outrank HIVE, and the container's own `git rev-parse HEAD` is what confirms the index is looking at the head the proofs claim.",
    "receipt": ".engineering/evidence/wo-0002/hive-mcp-proof.json"
  },
  "upstreamPins": {
    "godot": {
      "currentStable": {
        "tag": "4.7.2-stable",
        "commit": "ed1daf0bf001b61586d9930840f2f1394092c079",
        "publishedAt": "2026-08-18T16:12:28Z",
        "tagKind": "lightweight (refs/tags/4.7.2-stable resolves directly to the commit)"
      },
      "compatibilityReference": {
        "tag": "4.6.3-stable",
        "commit": "35e80b3a8822a9df9be390814b62f44c0a9c69e8",
        "why": "Two maintenance branches are still version-bumped at execution time: 4.7 is at 4.7.3-rc and 4.6 is at 4.6.4-rc, while 4.5 stopped at 4.5.2 (2026-03-19). 4.6 is therefore the immediately previous supported stable line; 4.5 and older are not maintained."
      },
      "observationOnly": {
        "branch": "master",
        "headSha": "4e244f2112c687885767fa3c24ce9233a24a1659",
        "versionPy": "4.8.0-dev",
        "adoptable": false,
        "note": "Observation only. '4.8-dev6' is a distributed pre-release build label; no 4.8-dev git tag exists in the official tag list, so any statement about the development line is bound to the master commit above rather than to a tag."
      },
      "vendored": false
    },
    "gef": {
      "version": "1.0.0",
      "releaseCommit": "866fe3af8cccc65c929aaf6a47a924401fa448b3",
      "vendored": false
    },
    "hive": {
      "version": "1.0.0",
      "releaseCommit": "a53b5b9fcf55c32a5696180fb1b1ef80ccd1edcf",
      "vendored": false
    }
  },
  "officialSourceVerification": {
    "sources": {
      "repository": "https://github.com/godotengine/godot (upstream, unmodified)",
      "website": "https://godotengine.org/download/archive/",
      "windowsBuildDocs": "https://docs.godotengine.org/en/latest/engine_details/development/compiling/compiling_for_windows.html"
    },
    "admissionClaimsReverified": "CONFIRMED",
    "noOfficialLtsStatement": "Neither the release archive nor the release list publishes a numbered support-lifetime or LTS policy. The supported set is therefore inferred from the branches that still carry a version bump at execution time, and that inference is stated as an inference.",
    "staleWhenReverified": "If a 4.7.3-stable or newer stable tag is published before the audit, the candidate matrix must be re-verified rather than inherited from this receipt.",
    "receipt": ".engineering/evidence/wo-0002/godot-official-state.json"
  },
  "toolchainInventory": {
    "host": "Microsoft Windows 11 Home Single Language 10.0.26200 x64, 22.9 GB visible",
    "cpu": "AMD Ryzen 5 2500U with Radeon Vega Mobile Gfx",
    "gpu": "AMD Radeon(TM) Vega 8 Graphics driver 31.0.21925.1001 (2026-05-19), 2 adapters reported",
    "compiler": "Visual Studio Build Tools 2022 17.14.37628.2, MSVC 14.44.35207 (14.3 (v143)), Windows SDK 10.0.26100.0",
    "buildTooling": "Python 3.12.10, SCons 4.11.1.b97f32b9adab83a96af767ec1d7dc8d7a41c7c74 (venv only), Git 2.55.0.windows.3",
    "hardwareClass": "Low-power mobile APU with integrated graphics. Treated as one hardware class, not as a representative ISORYN target.",
    "receipt": ".engineering/evidence/wo-0002/toolchain-inventory.json"
  },
  "builds": {
    "frozenCommand": "venv-scons/Scripts/scons.exe platform=windows target=template_release arch=x86_64 accesskit=no d3d12=no angle=no disable_path_overrides=no -j8",
    "templateRelease": {
      "exit": 0,
      "elapsedSeconds": 6777,
      "objectsCompiled": 2422,
      "artifact": "godot.windows.template_release.x86_64.exe",
      "artifactBytes": 68254208,
      "artifactSha256": "7052a3f08be1872418cae83c08c15c5ff46e52950b2fb8d43b19b24587914a18",
      "versionString": "4.7.2.stable.custom_build.ed1daf0bf",
      "receipts": [
        "build-4.7.2-template-release-measurable.log",
        "build-4.7.2-template-release-measurable.meta",
        "godot-4.7.2-binary-identity.txt"
      ]
    },
    "firstAttemptAborted": {
      "exit": 127,
      "elapsedSeconds": 1388,
      "reason": "killed after the operator session ended; kept to show the command line without disable_path_overrides=no cannot run a project",
      "receipts": [
        "build-4.7.2-template-release-terminated.log",
        "build-4.7.2-template-release-terminated.meta",
        "build-4.7.2-template-release-terminated.note.txt"
      ]
    },
    "editorTarget": {
      "result": "NOT_AVAILABLE",
      "exit": 2,
      "reason": "MSVC C1060 on editor/translations/doc_translations.gen.cpp (102,310,230 B) at -j8, -j4 and -j1 on a 22.9 GB host (ISORYN-D-015)",
      "attempts": [
        "build-4.7.2-editor.attempt1-configure-failure.log",
        "build-4.7.2-editor-attempt2.log",
        "build-4.7.2-editor-attempt3.log",
        "build-4.7.2-editor-attempt4.log"
      ],
      "compatibilityDryRun": "build-4.6.3-editor-configure-dryrun.log (exit 0, -n only)"
    }
  },
  "benchmark": {
    "contract": "docs/project-brain/09-TOOLCHAIN-AND-BENCHMARK-BASELINE.md sections 3-4 (metric vocabulary, eight measurement rules, frozen workload identity)",
    "workload": ".engineering/evidence/wo-0002/bench/ (bench.gd, bench.tscn, project.godot; seed 20260923, 1,200 instances, 90 warm-up + 600 measured frames)",
    "headlessSeries": {
      "p50Ms": 6.898,
      "p95Ms": 15.175,
      "p99Ms": 15.59,
      "repeats": 3,
      "spreadPct": {
        "p50": 0.06,
        "p95": 1.3,
        "p99": 3.4
      },
      "label": "CPU/logic cost on one host, never a frame-time baseline (rule 7)",
      "receipts": [
        "bench-repeats-headless.txt",
        "bench-determinism.txt"
      ]
    },
    "gpuFrameTimeBaseline": "NOT_AVAILABLE - see gpuDeviceState"
  },
  "gpuDeviceState": {
    "verdict": "NOT_AVAILABLE on this host, executed rather than assumed",
    "windowedPaths": {
      "builtVulkan": "exit 139, 607 ERROR lines, device refuses every shader module; no harness line in either output sink, so the workload was never instantiated",
      "builtGl": "exit 139 with no harness line in either sink",
      "officialVulkan": "exit 124 - same refusal, still rendering when the 300 s cap killed it",
      "officialGl": "exit 139, one line deeper than this build",
      "officialD3d12": "exit 0 with a complete series, but its own readback returns four byte-identical 1280x720 frames that are black at all 921,600 pixels, then fails at Can't create buffer of size: 3686400, error 0x887a0005 (DXGI_ERROR_DEVICE_REMOVED)"
    },
    "policy": "ISORYN-D-016 admits a device only through a readback gate whose decoded pixels show the scene",
    "receipts": [
      "gpu-device-enumeration.txt",
      "gpu-windowed-device-blocker.txt",
      "gpu-windowed-device-control.txt",
      "gpu-readback-golden-frame.txt",
      "windowed-output-sink-control.txt",
      "frames/ (four PNGs, 2,772 B each)"
    ]
  },
  "mcpProof": {
    "runtime": "HIVE v1.0.0 at http://127.0.0.1:18199, isolated compose project isoryn-c02-v100",
    "health": "ok",
    "bootstrap": {
      "project_id": "cf0e7dee-bfa4-4f54-b8fa-8391afefbcfd",
      "relative_path": "isoryn-engine",
      "git_branch": "isoryn-wo-0002-architecture-toolchain-discovery",
      "git_head_sha": "958d5ed0bfb74be40eec5f7b3ef0f57fee76b9f4",
      "state": "READY",
      "working_tree_clean": true,
      "index_status": "COMPLETED",
      "corpus_status": "COMPLETED"
    },
    "inContainerHeadMatchesProofHead": true,
    "serverInfo": {
      "name": "hive-mcp",
      "version": "mcp-core-surface-v1"
    },
    "protocolVersion": "2025-06-18",
    "toolsAreExactlyTheGovernedSeven": true,
    "allReadOnly": true,
    "executedCalls": {
      "project.list": {
        "isError": false
      },
      "project.status": {
        "isError": false
      },
      "checkpoint.read": {
        "isError": false
      },
      "context.search": {
        "isError": false
      },
      "memory.search": {
        "isError": false
      },
      "context.build": {
        "isError": true
      }
    },
    "contextSearchTopPaths": [
      ".engineering/evidence/wo-0002/hive-mcp-proof.json",
      "docs/project-brain/16-DECISIONS-LEDGER.md",
      "docs/project-brain/08-GODOT-BASELINE-AND-TOPOLOGY.md",
      "docs/project-brain/08-GODOT-BASELINE-AND-TOPOLOGY.md",
      "docs/adr/ADR-0002-build-toolchain-and-upstream-sync.md"
    ],
    "memorySearchReturned": 0,
    "retrievalState": "LEXICAL_FALLBACK_SEMANTIC_UNAVAILABLE",
    "launcherExit": 0,
    "launcherStderr": [],
    "receipt": ".engineering/evidence/wo-0002/hive-mcp-proof.json",
    "proofHead": "958d5ed0bfb74be40eec5f7b3ef0f57fee76b9f4"
  },
  "architectureDeliverables": {
    "adrs": [
      "docs/adr/ADR-0001-godot-baseline-and-repository-topology.md",
      "docs/adr/ADR-0002-build-toolchain-and-upstream-sync.md",
      "docs/adr/ADR-0003-extension-seam-policy.md"
    ],
    "masterModuleIndex": "docs/project-brain/06-MASTER-MODULE-INDEX.md (30 module rows, every scope family, with the absent-mechanism list A-D)",
    "registry": "docs/project-brain/07-PROPRIETARY-TECHNOLOGY-REGISTRY.md (12 entries, each a proof obligation with a documented fallback)",
    "baselineTopology": "docs/project-brain/08-GODOT-BASELINE-AND-TOPOLOGY.md",
    "toolchainBenchmark": "docs/project-brain/09-TOOLCHAIN-AND-BENCHMARK-BASELINE.md",
    "seamProbe": "custom_modules out-of-tree import reaches configure with the marker ISORYN_PROBE_MODULE_CONFIGURED and still configures with the flag off (custom-modules-feasibility.txt); compiling and linking it both ways is open backlog row 9",
    "newGovernanceIds": [
      "ISORYN-D-011..ISORYN-D-016 (PROPOSED, this Work Order)"
    ]
  },
  "canonicalInputs": [
    "AGENTS.md",
    ".engineering/SOURCE-HIERARCHY.md",
    ".engineering/work-orders/ISORYN-WO-0002-ARCHITECTURE-TOOLCHAIN-DISCOVERY.md",
    "docs/project-brain/13-CHECKPOINT.md",
    "docs/project-brain/16-DECISIONS-LEDGER.md",
    "docs/project-brain/03-SCOPE.md",
    "docs/project-brain/15-DEFINITION-OF-DONE.md",
    "docs/project-brain/04-ARCHITECTURE.md",
    "docs/project-brain/02-REQUIREMENTS.md",
    "docs/project-brain/11-TEST-PLAN.md",
    "docs/project-brain/05-INTEGRATION-CONTRACTS.md",
    "docs/project-brain/14-BACKLOG.md"
  ],
  "filesChanged": [
    {
      "path": ".engineering/CHECKPOINT.json",
      "change": "modified"
    },
    {
      "path": ".engineering/CHECKPOINT.md",
      "change": "modified"
    },
    {
      "path": ".engineering/SOURCE-HIERARCHY.md",
      "change": "modified"
    },
    {
      "path": ".engineering/context-locks/ISORYN-WO-0002.json",
      "change": "added"
    },
    {
      "path": ".engineering/evidence/ISORYN-WO-0002-ADMISSION.md",
      "change": "added"
    },
    {
      "path": ".engineering/evidence/ISORYN-WO-0002-CHECKPOINT-DELTA.md",
      "change": "added"
    },
    {
      "path": ".engineering/evidence/ISORYN-WO-0002-EVIDENCE.md",
      "change": "added"
    },
    {
      "path": ".engineering/evidence/wo-0002/bench-determinism.txt",
      "change": "added"
    },
    {
      "path": ".engineering/evidence/wo-0002/bench-repeats-headless.txt",
      "change": "added"
    },
    {
      "path": ".engineering/evidence/wo-0002/bench/bench.gd",
      "change": "added"
    },
    {
      "path": ".engineering/evidence/wo-0002/bench/bench.tscn",
      "change": "added"
    },
    {
      "path": ".engineering/evidence/wo-0002/bench/project.godot",
      "change": "added"
    },
    {
      "path": ".engineering/evidence/wo-0002/build-4.6.3-editor-configure-dryrun.log",
      "change": "added"
    },
    {
      "path": ".engineering/evidence/wo-0002/build-4.6.3-editor-configure-dryrun.meta",
      "change": "added"
    },
    {
      "path": ".engineering/evidence/wo-0002/build-4.7.2-editor-attempt2.log",
      "change": "added"
    },
    {
      "path": ".engineering/evidence/wo-0002/build-4.7.2-editor-attempt2.meta",
      "change": "added"
    },
    {
      "path": ".engineering/evidence/wo-0002/build-4.7.2-editor-attempt3.log",
      "change": "added"
    },
    {
      "path": ".engineering/evidence/wo-0002/build-4.7.2-editor-attempt3.meta",
      "change": "added"
    },
    {
      "path": ".engineering/evidence/wo-0002/build-4.7.2-editor-attempt4.log",
      "change": "added"
    },
    {
      "path": ".engineering/evidence/wo-0002/build-4.7.2-editor-attempt4.meta",
      "change": "added"
    },
    {
      "path": ".engineering/evidence/wo-0002/build-4.7.2-editor.attempt1-configure-failure.log",
      "change": "added"
    },
    {
      "path": ".engineering/evidence/wo-0002/build-4.7.2-editor.attempt1.meta",
      "change": "added"
    },
    {
      "path": ".engineering/evidence/wo-0002/build-4.7.2-template-release-measurable.log",
      "change": "added"
    },
    {
      "path": ".engineering/evidence/wo-0002/build-4.7.2-template-release-measurable.meta",
      "change": "added"
    },
    {
      "path": ".engineering/evidence/wo-0002/build-4.7.2-template-release-terminated.log",
      "change": "added"
    },
    {
      "path": ".engineering/evidence/wo-0002/build-4.7.2-template-release-terminated.meta",
      "change": "added"
    },
    {
      "path": ".engineering/evidence/wo-0002/build-4.7.2-template-release-terminated.note.txt",
      "change": "added"
    },
    {
      "path": ".engineering/evidence/wo-0002/build-receipts-index.txt",
      "change": "added"
    },
    {
      "path": ".engineering/evidence/wo-0002/custom-modules-feasibility.txt",
      "change": "added"
    },
    {
      "path": ".engineering/evidence/wo-0002/frames/gf100000000.png",
      "change": "added"
    },
    {
      "path": ".engineering/evidence/wo-0002/frames/gf200000000.png",
      "change": "added"
    },
    {
      "path": ".engineering/evidence/wo-0002/frames/movie.100000000.png",
      "change": "added"
    },
    {
      "path": ".engineering/evidence/wo-0002/frames/movie.200000000.png",
      "change": "added"
    },
    {
      "path": ".engineering/evidence/wo-0002/github-security-analysis.json",
      "change": "added"
    },
    {
      "path": ".engineering/evidence/wo-0002/godot-4.7.2-binary-identity.txt",
      "change": "added"
    },
    {
      "path": ".engineering/evidence/wo-0002/godot-4.7.2-smoke.txt",
      "change": "added"
    },
    {
      "path": ".engineering/evidence/wo-0002/godot-official-state.json",
      "change": "added"
    },
    {
      "path": ".engineering/evidence/wo-0002/gpu-device-enumeration.txt",
      "change": "added"
    },
    {
      "path": ".engineering/evidence/wo-0002/gpu-readback-golden-frame.txt",
      "change": "added"
    },
    {
      "path": ".engineering/evidence/wo-0002/gpu-windowed-device-blocker.txt",
      "change": "added"
    },
    {
      "path": ".engineering/evidence/wo-0002/gpu-windowed-device-control.txt",
      "change": "added"
    },
    {
      "path": ".engineering/evidence/wo-0002/hive-mcp-proof.json",
      "change": "added"
    },
    {
      "path": ".engineering/evidence/wo-0002/toolchain-inventory.json",
      "change": "added"
    },
    {
      "path": ".engineering/evidence/wo-0002/windowed-output-sink-control.txt",
      "change": "added"
    },
    {
      "path": ".engineering/work-orders/ISORYN-WO-0002-ARCHITECTURE-TOOLCHAIN-DISCOVERY.md",
      "change": "added"
    },
    {
      "path": "README.md",
      "change": "modified"
    },
    {
      "path": "docs/adr/ADR-0001-godot-baseline-and-repository-topology.md",
      "change": "added"
    },
    {
      "path": "docs/adr/ADR-0002-build-toolchain-and-upstream-sync.md",
      "change": "added"
    },
    {
      "path": "docs/adr/ADR-0003-extension-seam-policy.md",
      "change": "added"
    },
    {
      "path": "docs/project-brain/00-README-UPLOAD-ORDER.md",
      "change": "modified"
    },
    {
      "path": "docs/project-brain/01-PROJECT-OVERVIEW.md",
      "change": "modified"
    },
    {
      "path": "docs/project-brain/02-REQUIREMENTS.md",
      "change": "modified"
    },
    {
      "path": "docs/project-brain/03-SCOPE.md",
      "change": "modified"
    },
    {
      "path": "docs/project-brain/04-ARCHITECTURE.md",
      "change": "modified"
    },
    {
      "path": "docs/project-brain/05-INTEGRATION-CONTRACTS.md",
      "change": "modified"
    },
    {
      "path": "docs/project-brain/06-MASTER-MODULE-INDEX.md",
      "change": "added"
    },
    {
      "path": "docs/project-brain/07-PROPRIETARY-TECHNOLOGY-REGISTRY.md",
      "change": "added"
    },
    {
      "path": "docs/project-brain/08-GODOT-BASELINE-AND-TOPOLOGY.md",
      "change": "added"
    },
    {
      "path": "docs/project-brain/09-TOOLCHAIN-AND-BENCHMARK-BASELINE.md",
      "change": "added"
    },
    {
      "path": "docs/project-brain/11-TEST-PLAN.md",
      "change": "modified"
    },
    {
      "path": "docs/project-brain/12-LOCAL-DEPLOYMENT.md",
      "change": "modified"
    },
    {
      "path": "docs/project-brain/13-CHECKPOINT.md",
      "change": "modified"
    },
    {
      "path": "docs/project-brain/14-BACKLOG.md",
      "change": "modified"
    },
    {
      "path": "docs/project-brain/16-DECISIONS-LEDGER.md",
      "change": "modified"
    },
    {
      "path": "scripts/validate_governance.py",
      "change": "modified"
    },
    {
      "path": "tests/test_governance.py",
      "change": "modified"
    }
  ],
  "receiptInventory": [
    {
      "path": ".engineering/evidence/wo-0002/bench/bench.gd",
      "bytes": 4951,
      "sha256": "61e8a472f12e2d2df00c8e6df74eaf3518bffcd099a603b5864455ea4e0595b7"
    },
    {
      "path": ".engineering/evidence/wo-0002/bench/bench.tscn",
      "bytes": 165,
      "sha256": "8324176e2e7caea6e747899fed9692f90d309f8da0fcee238b141a1cd3bd8c4d"
    },
    {
      "path": ".engineering/evidence/wo-0002/bench/project.godot",
      "bytes": 1062,
      "sha256": "5ad6e2f6e0e66cfa6d15ef43f83f6c828128cb09b322aad875e3545d28c917da"
    },
    {
      "path": ".engineering/evidence/wo-0002/bench-determinism.txt",
      "bytes": 1074,
      "sha256": "e9061286549554aaed896124f8107cbc2ea0b6f39ad75fc5e1358a3e44b9d5d0"
    },
    {
      "path": ".engineering/evidence/wo-0002/bench-repeats-headless.txt",
      "bytes": 2981,
      "sha256": "5e80c0bcc2a51120c3f87e91574bc838d72eb55d15fed2f4db9b0df2bbfa9044"
    },
    {
      "path": ".engineering/evidence/wo-0002/build-4.6.3-editor-configure-dryrun.log",
      "bytes": 174799,
      "sha256": "e155dbe25bc0f04f408b572202e092fae54d38467ffc8611ddd0d5481122434f"
    },
    {
      "path": ".engineering/evidence/wo-0002/build-4.6.3-editor-configure-dryrun.meta",
      "bytes": 155,
      "sha256": "05e08381696578c72df4490458f642a7ed4eef39338feaf3096d78d2d70a92c3"
    },
    {
      "path": ".engineering/evidence/wo-0002/build-4.7.2-editor-attempt2.log",
      "bytes": 119958,
      "sha256": "9ee496e38eba171d935fd0ae5cc042455df4a04a4d2878510ad8322040229daf"
    },
    {
      "path": ".engineering/evidence/wo-0002/build-4.7.2-editor-attempt2.meta",
      "bytes": 172,
      "sha256": "909ba21de2c162909cae03381e175298b97f2f32c28c2eeb12e3108d0f78340a"
    },
    {
      "path": ".engineering/evidence/wo-0002/build-4.7.2-editor-attempt3.log",
      "bytes": 1741,
      "sha256": "272fbe5b50949318e75d8daf007462498e2e245407a2119d6fc1030930c4b603"
    },
    {
      "path": ".engineering/evidence/wo-0002/build-4.7.2-editor-attempt3.meta",
      "bytes": 168,
      "sha256": "e7e2974df942881e7f0fbc23a7cd5c7edc42a6e8d9e2e998d965a70e27ac51c4"
    },
    {
      "path": ".engineering/evidence/wo-0002/build-4.7.2-editor-attempt4.log",
      "bytes": 952,
      "sha256": "0266e9e3d8496e9213812ace8d17eefd64150e89e938e92b14b509a917287d55"
    },
    {
      "path": ".engineering/evidence/wo-0002/build-4.7.2-editor-attempt4.meta",
      "bytes": 242,
      "sha256": "798a7dfe4481decb2bc1aa8ea0a6d8c1f5edddec61998c32d9d54675e844c0b8"
    },
    {
      "path": ".engineering/evidence/wo-0002/build-4.7.2-editor.attempt1-configure-failure.log",
      "bytes": 862,
      "sha256": "589378e7faca197b83a3eac8b402b368ec145ae210c0411320cbb3b2c3dfbc01"
    },
    {
      "path": ".engineering/evidence/wo-0002/build-4.7.2-editor.attempt1.meta",
      "bytes": 89,
      "sha256": "dc2e826f15ee4d2c0cdf9f45cbd518df7cdf0e6bb1523ea9f6bde73dbbf18aea"
    },
    {
      "path": ".engineering/evidence/wo-0002/build-4.7.2-template-release-measurable.log",
      "bytes": 143929,
      "sha256": "3fa9e57894ec72009ce5f23fe2641587bbc28ec7ad92ce497fae6081a6a48dc8"
    },
    {
      "path": ".engineering/evidence/wo-0002/build-4.7.2-template-release-measurable.meta",
      "bytes": 214,
      "sha256": "68ca2d15390a94b6caffa8f74dbd7fd0b6c6b0b38472ff0ce8670c3cea6323d2"
    },
    {
      "path": ".engineering/evidence/wo-0002/build-4.7.2-template-release-terminated.log",
      "bytes": 37820,
      "sha256": "c803e28facee9bf15dad0263c94c27f50020a13de9c8db07b0b7f976920ee82c"
    },
    {
      "path": ".engineering/evidence/wo-0002/build-4.7.2-template-release-terminated.meta",
      "bytes": 190,
      "sha256": "90f0330e832617f1b6d4317a42bb656a54f2a3b268c8801e9203313eb5f4d4f6"
    },
    {
      "path": ".engineering/evidence/wo-0002/build-4.7.2-template-release-terminated.note.txt",
      "bytes": 1257,
      "sha256": "7668e1f5795531753a973cfc7673c7a7af81a6450e760e18f9b4d10068a6b0bf"
    },
    {
      "path": ".engineering/evidence/wo-0002/build-receipts-index.txt",
      "bytes": 3809,
      "sha256": "fe9c9033f2f13ad18e060a4064b9642449aa25061dd0390630d18247f8dfb0af"
    },
    {
      "path": ".engineering/evidence/wo-0002/custom-modules-feasibility.txt",
      "bytes": 896,
      "sha256": "58bb814d8d86293a3e494382a18c0dba37ab0c39f3e4aa7971f65c50a57e33bb"
    },
    {
      "path": ".engineering/evidence/wo-0002/frames/gf100000000.png",
      "bytes": 2772,
      "sha256": "0b37fe2b760522c6101c70c0322547ae6c9dcca72424fd596870988e00b13196"
    },
    {
      "path": ".engineering/evidence/wo-0002/frames/gf200000000.png",
      "bytes": 2772,
      "sha256": "0b37fe2b760522c6101c70c0322547ae6c9dcca72424fd596870988e00b13196"
    },
    {
      "path": ".engineering/evidence/wo-0002/frames/movie.100000000.png",
      "bytes": 2772,
      "sha256": "0b37fe2b760522c6101c70c0322547ae6c9dcca72424fd596870988e00b13196"
    },
    {
      "path": ".engineering/evidence/wo-0002/frames/movie.200000000.png",
      "bytes": 2772,
      "sha256": "0b37fe2b760522c6101c70c0322547ae6c9dcca72424fd596870988e00b13196"
    },
    {
      "path": ".engineering/evidence/wo-0002/github-security-analysis.json",
      "bytes": 1025,
      "sha256": "4fd378772199b6b60df4ac64a294894221e08f559836279e5734b59d830dcd08"
    },
    {
      "path": ".engineering/evidence/wo-0002/godot-4.7.2-binary-identity.txt",
      "bytes": 607,
      "sha256": "ea5990287408af973d592c36c33e1dc8fed6fcb51ef399cd7e7d7ec7d37bf9f1"
    },
    {
      "path": ".engineering/evidence/wo-0002/godot-4.7.2-smoke.txt",
      "bytes": 2313,
      "sha256": "a3e73e93c3894d779cd2778042f390ae5ddf3675efe2046b92b514709b757227"
    },
    {
      "path": ".engineering/evidence/wo-0002/godot-official-state.json",
      "bytes": 4326,
      "sha256": "5c158175a6a53e0d088c7f6ae96cd3eb6573738984386fbe1be95adb71aca3d3"
    },
    {
      "path": ".engineering/evidence/wo-0002/gpu-device-enumeration.txt",
      "bytes": 1571,
      "sha256": "eaa5200d89149447c19dc1be711b62990bc848e971f983c4d16dcd3a08e0ef5e"
    },
    {
      "path": ".engineering/evidence/wo-0002/gpu-readback-golden-frame.txt",
      "bytes": 4430,
      "sha256": "383c39f11199da299a9aea2c537e9ccc79010bde023b67e7daca5ae2ddd716ff"
    },
    {
      "path": ".engineering/evidence/wo-0002/gpu-windowed-device-blocker.txt",
      "bytes": 5023,
      "sha256": "6e7c28cd0debfc5b62c885f5ee709339ae79659c8b2eb2e99f2f0d80de441e3a"
    },
    {
      "path": ".engineering/evidence/wo-0002/gpu-windowed-device-control.txt",
      "bytes": 5867,
      "sha256": "594db255bdf68f89bf66455b799e927c5ab6f9638bd826aa2f403d161d7f88ba"
    },
    {
      "path": ".engineering/evidence/wo-0002/hive-mcp-proof.json",
      "bytes": 7554,
      "sha256": "4932eda0ab40940dcbb2f58a99d73e61d619542453aedaa6752d1a1fbfa5eb71"
    },
    {
      "path": ".engineering/evidence/wo-0002/toolchain-inventory.json",
      "bytes": 5187,
      "sha256": "4ce2ce0ace5d915d133ee82db43125aeaa47fd5647fd1c759d5d470d5f3a8613"
    },
    {
      "path": ".engineering/evidence/wo-0002/windowed-output-sink-control.txt",
      "bytes": 6296,
      "sha256": "818a8046f9e1e773329e65e2fc97ddc9a757b0fbcfd27f4bede812c40e46d452"
    }
  ],
  "checks": {
    "hive_preflight": "PASS",
    "mcp_proof": "PASS",
    "godot_official_source_verification": "PASS",
    "toolchain_inventory": "PASS",
    "godot_current_stable_build": "PASS",
    "benchmark_baseline": "PASS",
    "governance_validator": "PASS",
    "unittest_suite": "PASS",
    "governance_ci": "UNKNOWN",
    "secret_scan": "PASS",
    "py_compile": "PASS",
    "git_diff_check": "PASS",
    "clean_worktree_for_hive": "PASS",
    "no_vendored_engine_source": "PASS",
    "line_endings": "PASS",
    "gpu_frame_time_baseline": "NOT_AVAILABLE",
    "editor_target_build": "NOT_AVAILABLE",
    "editor_smoke_cases": "NOT_AVAILABLE",
    "custom_module_compile_link": "NOT_AVAILABLE",
    "mcp_memory_get": "NOT_AVAILABLE",
    "mcp_context_build_happy_path": "NOT_AVAILABLE"
  },
  "governanceRun": {
    "status": "PENDING_AT_WRITE",
    "note": "A commit cannot observe its own check-run. The capture at .engineering/evidence/wo-0002/ci.json names the exact commit GitHub evaluated, and gh pr checks 5 --required is the authority for the head that carries this record."
  },
  "tests": [
    {
      "command": "python -m py_compile scripts/validate_governance.py scripts/hive_bootstrap.py scripts/hive_mcp.py",
      "result": "PASS - exit 0"
    },
    {
      "command": "python scripts/validate_governance.py",
      "result": "PASS - ISORYN governance validation: PASS; Required artifacts: 61; Governed MCP tools: 7"
    },
    {
      "command": "python -m unittest discover -s tests -p \"test_*.py\"",
      "result": "PASS - Ran 34 tests in 0.428s, OK"
    },
    {
      "command": "git diff --check (unstaged and staged) + git status --porcelain=v1 empty",
      "result": "PASS - no whitespace errors in either index"
    },
    {
      "command": "repository secret scan (pattern sweep over every tracked and untracked file, plus credential-scanning state read from the GitHub API)",
      "result": "PASS - 125 text files and 4 binary files reported by name out of 129 listed, 0 pattern matches; platform side, 0 secret scanning alerts with push protection enabled"
    },
    {
      "command": "HIVE health/inspect/index/corpus/retrieval + MCP initialize/tools/list/project.status/checkpoint.read/context.search through scripts/hive_mcp.py",
      "result": "PASS at proofHead 958d5ed0bfb74be40eec5f7b3ef0f57fee76b9f4; the container's own git rev-parse HEAD returned 958d5ed0bfb74be40eec5f7b3ef0f57fee76b9f4 and the bootstrap that refreshed the index exited 0 with state READY"
    },
    {
      "command": "official Godot tag/commit verification against refs/tags and a local clone",
      "result": "PASS - 4.7.2-stable resolves to ed1daf0bf001b61586d9930840f2f1394092c079"
    },
    {
      "command": "pinned source build + smoke set (six cases)",
      "result": "PASS with two executed failures and three stated unavailable cases"
    },
    {
      "command": "deterministic baseline metrics (three repeats plus a fixed-fps reproducibility pair)",
      "result": "PASS for the headless series; the movie pair is NOT_AVAILABLE on this host and recorded with its failure signature"
    },
    {
      "command": "check that no Godot/HIVE/CORE/IRIS vendored source or generated binary entered the tree",
      "result": "PASS - 0 engine markers or binaries and 0 tracked files over 1 MB; the only committed media are the four evidentiary PNG frames",
      "engineMarkersAndBinaries": [],
      "trackedFilesOverOneMB": []
    },
    {
      "command": "byte scan for CR over every tracked and untracked file (the .gitattributes eol=lf contract)",
      "result": "PASS - 0 text files containing a CR byte, with 4 binary files named and excluded because PNG data legitimately contains CR"
    },
    {
      "command": "gh pr checks 5 --required",
      "result": "run after the push this delivery produces; see checks.governance_ci"
    }
  ],
  "securityChecks": {
    "credentialPatternSweep": {
      "filesListed": 129,
      "textFilesScanned": 125,
      "binaryFilesReportedByName": [
        ".engineering/evidence/wo-0002/frames/gf100000000.png",
        ".engineering/evidence/wo-0002/frames/gf200000000.png",
        ".engineering/evidence/wo-0002/frames/movie.100000000.png",
        ".engineering/evidence/wo-0002/frames/movie.200000000.png"
      ],
      "patterns": [
        "aws-access-key",
        "credential-assignment",
        "github-token",
        "jwt",
        "openai-key",
        "private-key-block",
        "slack-token",
        "url-userinfo"
      ],
      "matches": [],
      "verdict": "PASS"
    },
    "platformSecretScanning": {
      "receipt": ".engineering/evidence/wo-0002/github-security-analysis.json",
      "securityAndAnalysis": {
        "secret_scanning": {
          "status": "enabled"
        },
        "secret_scanning_push_protection": {
          "status": "enabled"
        },
        "dependabot_security_updates": {
          "status": "enabled"
        },
        "secret_scanning_non_provider_patterns": {
          "status": "disabled"
        },
        "secret_scanning_validity_checks": {
          "status": "disabled"
        }
      },
      "secretScanningAlert": {
        "response": [],
        "count": 0,
        "open": []
      }
    },
    "machinePathsInPortableConfig": "PASS - the validator's MACHINE_PATH gate covers scripts and config globs; receipts that name an operator path are evidence, not portable configuration",
    "lineEndings": {
      "byteScanOfTree": {
        "filesWithCR": [],
        "binaryFilesExcludedBySniffing": [
          ".engineering/evidence/wo-0002/frames/gf100000000.png",
          ".engineering/evidence/wo-0002/frames/gf200000000.png",
          ".engineering/evidence/wo-0002/frames/movie.100000000.png",
          ".engineering/evidence/wo-0002/frames/movie.200000000.png"
        ],
        "result": "PASS"
      },
      "validatorGate": "check_line_endings in scripts/validate_governance.py, run by the generator and by the Governance CI job",
      "history": "the one CRLF this cycle introduced (gpu-readback-golden-frame.txt, 12 lines carried in from engine log bytes) was caught by the gate and normalized rather than exempted"
    }
  },
  "errorsFoundAndCorrected": [
    "`--quiet` suppresses print(), so the first headless harness receipt recorded a passing exit code with no measurement. Fixed by never combining --quiet with a harness run and re-executing the case.",
    "A windowed case capped at --quit-after 60 was first read as 'the d3d12 path renders cleanly'. It never reached the harness report point (90 warm-up + 600 measured frames), so nothing had been measured. Every windowed receipt now runs the full workload with the cap only as a backstop.",
    "The readback gate first counted frame files in the directory it launched from and reported none, which produced the committed claim that this host had never returned a frame. A relative --write-movie path resolves against res://, and two runs sharing one base name delete each other's output, so four frames had in fact been returned. Corrected by re-running each case with its own base name and counting frames in the project directory, which produced gpu-readback-golden-frame.txt and the four frames committed under frames/. The phase scripts that ran those cases are operator-local and deliberately not committed, so the receipts and the committed frames are the reproducible part.",
    "An absent harness line was explained as buffered stdout dying with the process - an idea that had never been executed. windowed-output-sink-control.txt tests two sinks at once and shows the line arriving in both wherever a run reaches _ready(), including upstream's binary on the same windowed Vulkan path. The absence is therefore about the run, and reading it that way exposed a second fact: this build segfaults on the Vulkan path where upstream's binary keeps rendering, so the earlier 'the control reproduces both crash paths' sentence was wrong and has been replaced everywhere it appeared.",
    "The governance validator caught 12 CRLF lines introduced by the new readback receipt (engine log bytes carried CR); normalized to LF rather than exempted.",
    "The first version of this bundle failed two gates of the repository's own schema and was rewritten rather than the schema relaxed: it dropped the required hivePreflight field, and it recorded governance_ci as 'PENDING_AT_WRITE', a value outside the documented result vocabulary. The vocabulary has no word for 'not run yet', so the row now reads UNKNOWN until GitHub reports the run for the pushed head, and the binding to that head lives in governanceRun instead of inside a status token.",
    "The independent CR scan first reported four offending files, all of them committed PNG frames: binary data contains CR bytes legitimately. Text is now decided by the same NUL sniff the credential sweep uses and the excluded binaries are named in the record instead of the scan quietly narrowing itself.",
    "The HIVE/MCP receipt described above was assembled with a hand-written bootstrap summary: the block stated state READY, working_tree_clean true and index/corpus COMPLETED as typed literals next to a real session capture. That is fabricated evidence even when it happens to match what ran, so the assembler now executes `scripts/hive_bootstrap.py` itself, parses the summary out of its stdout, records its exit code, and only then runs the MCP sessions - which is also what re-indexed the tree at the proof head and made the current receipts retrievable through context.search.",
    "Two citation defects: movie_writer.cpp:201 should be :202 for the texture_2d_get call, and a receipt reference needed its full .meta file name to resolve.",
    "context.build was first called with a query argument that the governed schema rejects (additionalProperties false); re-called with schema-valid arguments, which returned resource_not_found because no task is registered for this project on the pinned stack."
  ],
  "unsupportedPlatformFeatures": [
    {
      "capability": "editor target build on this host class",
      "result": "NOT_AVAILABLE",
      "detail": "MSVC fatal error C1060 on editor/translations/doc_translations.gen.cpp (102,310,230 B) at -j8, -j4 and -j1 with nothing else running, on a host with 22.9 GB visible RAM and a 12 GB pagefile. Recorded as ISORYN-D-015: a build host must hold that unit in one compiler process or say that it built a template target."
    },
    {
      "capability": "d3d12 rendering driver in this build",
      "result": "NOT_AVAILABLE",
      "detail": "Configured out with d3d12=no because the Windows SDK component was absent at build time; installing the SDK is a reviewer decision and is not by itself a fix, since the path was measured through the official binary and does not draw on this host."
    },
    {
      "capability": "windowed GPU frame-time baseline on this host",
      "result": "NOT_AVAILABLE",
      "detail": "Every windowed path fails the ISORYN-D-016 readback gate: Vulkan and OpenGL crash or refuse, and the d3d12 path returns four byte-identical 1280x720 frames that are black at all 921,600 pixels before failing the frame-sized buffer with 0x887a0005 (DXGI_ERROR_DEVICE_REMOVED)."
    },
    {
      "capability": "HIVE memory.get and the context.build happy path on the pinned stack",
      "result": "NOT_AVAILABLE",
      "detail": "memory.search returned zero entries and no task is registered for this project, so context.build answers resource_not_found. Both were called with schema-valid arguments; neither is recorded as a pass."
    }
  ],
  "residualRisks": [
    "The built binary's early Vulkan segfault is not reproduced by upstream's published binary and is not attributed. Until it is explained the frozen command line is a measurement build, not a CI reference build (backlog row 10, ADR-0002).",
    "One mobile-APU Windows host is not a hardware class; every number here is single-host and labelled.",
    "Retrieval on the pinned HIVE stack is lexical (hybrid_state LEXICAL_FALLBACK_SEMANTIC_UNAVAILABLE), so HIVE results are keyword recall, not semantic evidence.",
    "The machine still runs a drifted HIVE v1.0.2 on port 8000; only HIVE_COMPOSE_PROJECT plus the -p flag keeps proofs pointed at the pinned v1.0.0 stack.",
    "Seam 3 is proven at configure level only; the compile-and-link proof is open backlog row 9.",
    "Godot 4.8 is pre-release and observation-only; the candidate matrix must be re-verified if a newer stable tag is published before the audit.",
    "Executed receipts do not record `git rev-parse HEAD` at their own capture instant, so their binding to a repository head is reconstructed from timestamps against the commit order (see receiptHeadBinding.gap). A capture that outlives a commit, or a rebased branch, breaks that reconstruction silently; the fix is one line in the capture scripts and is not applied to receipts that are already closed.",
    "Registry entries (07) are proof obligations, not adopted technology; none may be cited as superiority over upstream."
  ],
  "rollback": "Close PR #5 and delete only the WO-0002 branch artifacts if discovery is abandoned. The engine clone, virtual environment and every build output are operator-local and disposable (ISORYN-D-011); no vendored source, binary or generated media beyond the four evidentiary frames entered the repository, so rollback touches no external state.",
  "github": {
    "baseMainSha": "74c47fa204a5da79c1418fb9bcc2557603422f88",
    "pr": "https://github.com/KayzenRoot/isoryn-engine/pull/5",
    "branch": "isoryn-wo-0002-architecture-toolchain-discovery",
    "proofHeadSha": "958d5ed0bfb74be40eec5f7b3ef0f57fee76b9f4",
    "deliveredHeadSha": "set by the push this record produces",
    "mergeAttempted": false,
    "note": "Merging is a hard stop for this Work Order; the PR is delivered open, and the exact-head Governance result is in governanceRun."
  },
  "proposedCheckpointDelta": {
    "status": "PROPOSED_ONLY",
    "path": ".engineering/evidence/ISORYN-WO-0002-CHECKPOINT-DELTA.md",
    "note": "Executor proposes; only the reviewer promotes through the governed flow."
  },
  "productionCodeConfirmation": "No engine, runtime, editor or module implementation was written in this Work Order. The only executable content is the committed measurement fixture (.engineering/evidence/wo-0002/bench/, a GDScript harness inside the evidence namespace), the governance validator's two new repository-shape gates, and their tests.",
  "stopCondition": "READY_FOR_ARCHITECTURE_TOOLCHAIN_AUDIT",
  "verdict": "DELIVERED_FOR_AUDIT"
}
```
