# ISORYN-WO-0002 - Evidence Bundle

Status: DELIVERED_FOR_INDEPENDENT_REREVIEW (WO-0002 delivery, re-proved for HIVE and re-verified for upstream by
ISORYN-WO-0002-C01-SUPPORT-POLICY-HIVE-REBIND, with the context.build interpretation corrected by
ISORYN-WO-0002-C01-CD01 and the HEAD/CI binding reconciled by ISORYN-WO-0002-C01-CD02; supersedes the
ADMISSION_BASELINE record in place)

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

Independent review then corrected two things in this record - the support-policy citation and the GPU summary - and
`ISORYN-WO-0002-C01-SUPPORT-POLICY-HIVE-REBIND` exists only because those canonical edits invalidated the exact-head
HIVE/MCP proof. C01 re-verified the official Godot state from official sources and confirmed `4.7.2-stable` at
`ed1daf0bf…` is still current stable, so no build, benchmark or GPU receipt was repeated: the expensive evidence below
is the same evidence with the same identities. It also re-proved HIVE v1.0.0 and the seven read-only MCP tools at the
reviewer-corrected head, and that second proof is where the honest difficulty sits. The pinned stack needed a root
cause rather than a retry: HIVE gives every git call five seconds and this workspace reaches the container read-only
over 9p, so a cold `git status` inside it blew the budget and the indexer died with git_status_unavailable. Repacking
the host repository's loose objects and warming the container's cache fixed it, with both the cold timings and the
failed attempts recorded. Retrieval also had to be measured properly rather than asserted - the first C01 run reported
no correction markers while returning chunks that contained them, because it matched whole responses instead of each
result snippet. Four of six searches in one session came back `database_unavailable` against healthy postgres and
redis containers, which is reproduced but not attributed, and the receipt now distinguishes that from an empty result
set instead of quietly recording recall.

The support-policy claim is now sourced from Godot's release-policy page, fetched with its byte count and SHA-256
recorded, rather than inferred from which branches still carry a version bump. The raw executor receipt keeps its
original text and is marked historical and superseded, so the correction can be checked against what it replaced.

`ISORYN-WO-0002-C01-CD01` corrected one of those replacements. The C01 receipt's explanation for `context.build` said
the call was refused because the probe task was not registered on the pinned stack; the bytes the same receipt
captured say `stale` / `source_not_current` / `project source is not current`, which is a source-currency refusal and
says nothing about the task. That sentence had been inherited from the WO-0002 receipt, which had genuinely captured a
different answer (`not_found` / `resource_not_found`) - so the defect was an explanation that outlived the response it
described, and the same class of drift is why the `memory.search` detail was tightened to what an unfiltered search of
limit 5 actually shows. No raw capture was edited: the verdict, error object, argument set and response hash are
compared field-by-field against the committed receipt, and the superseded sentence is kept verbatim under
`detailCorrection.supersededDetail`. `context.build` stays `NOT_AVAILABLE`, because a corrected reason for a refusal
still is not a happy path. CD01 did not stop at re-wording: it re-indexed the source the canonical way at a clean
committed head, confirmed `COMPLETED`/`CURRENT` against that head, and issued exactly one governed read. That answer
moved to `not_found` / `resource_not_found`, which locates the C01 refusal in the currency guard rather than in the
task, and still leaves the happy path unproduced - so the inventory row did not move and the task_id's status is
recorded as unknown, not as absent.

`ISORYN-WO-0002-C01-CD02` reconciled which head this record says it delivered. The CI-binding commits left
`headSha`, `candidateHeadSha`, `commandsExecutedAtHead` and `github.deliveredHeadSha` naming the head the CD01
correction was pushed at, and `ci.json` had no check-run for the head that was current, so the versioned record
described a candidate older than the one under review. The fix is a binding, not a re-run: the current head's
check-run was read from the GitHub API and appended to `ci.json` with the earlier observations untouched, the delivery
fields now name exactly the head that observation certifies, and `headRoleTable`, `historicalHeadsDeclared` and
`checkExecutionHeads` give every other SHA one declared role - base, admission, proof head, or the head a given command
ran at. Proof heads, receipt `capturedAt` values and raw captures were not modified, no governed HIVE call was issued
for CD02, and the gate `head_rebinding_fields_match_governance_observation` fails a future regeneration whose delivery
fields drift from an observed run or which drops an observation while appending one.

`governance_ci` reads `PASS` for the delivery head `bd5aba188` - the check-run for that exact commit is quoted
in the `governanceRun` block below and captured per-commit in `.engineering/evidence/wo-0002/ci.json`, and it
is the only head this record calls delivered. Heads that were the branch tip earlier, including the one the
CD01 correction was pushed at, are listed under `historicalHeadsDeclared` and keep their own bindings. The
commit that carries this sentence is a descendant of that head and cannot observe its own run, so `gh pr
checks 5 --required` on the pull request is the authority for it.

```json
{
  "schemaVersion": "isoryn-gef-evidence-v1",
  "workOrder": "ISORYN-WO-0002",
  "role": "DELIVERY",
  "supersedes": "ADMISSION_BASELINE (headSha ec1f419e... recorded at admission, no executed claim)",
  "capturedAt": "2026-09-24T18:51:31Z",
  "commandsExecutedAtHead": "bd5aba1883daee0a9e1825c2f2f385b7ab401cf4",
  "commandsExecutedAtNote": "governance_validator, unittest_suite, py_compile, git_diff_check, secret_scan and no_vendored_engine_source were produced by running those commands against this working tree while this record was being written; the other rows bind to proofHeadSha and carry their receipts.",
  "baseSha": "74c47fa204a5da79c1418fb9bcc2557603422f88",
  "admissionHeadSha": "2d567f97d5e3affa32bf190b8393a3e6d20d6327",
  "proofHeadSha": "958d5ed0bfb74be40eec5f7b3ef0f57fee76b9f4",
  "reviewerCorrectionHeadSha": "e481b3376c13cdbdfae243d945d10789d39a23fc",
  "c01ProofHeadSha": "ad4fdf81c0f8cde59671bbe2252eb48f86784eff",
  "headSha": "bd5aba1883daee0a9e1825c2f2f385b7ab401cf4",
  "candidateHeadSha": "bd5aba1883daee0a9e1825c2f2f385b7ab401cf4",
  "deliveryHeadSemantics": "The delivery/candidate head is the highest branch head for which .engineering/evidence/wo-0002/ci.json carries a completed Governance check-run read from GitHub. headSha, candidateHeadSha, commandsExecutedAtHead and github.deliveredHeadSha all name that one head, and no proof ran at it beyond the deterministic checks listed in `tests`, which ran against this working tree.",
  "headRolesNote": "Every SHA in this record holds exactly one of four roles. (1) Delivery/candidate head: bd5aba188, the head the fields above name and whose Governance run is bound in ci.json. (2) Historical proof heads: the WO-0002 discovery proof head 958d5ed0b, the reviewer correction head e481b3376, the C01 HIVE proof head ad4fdf81c (the head HIVE inspected and indexed) and the CD01 re-read head 24485b1c3. (3) The head each command ran at, stated per row in `tests` and `checkExecutionHeads`. (4) Carrier commits: this file lives in a descendant of the head it describes, and a commit cannot observe its own check-run, so the carrier's own status is read with `gh pr checks 5 --required` and never asserted here. No proof is attributed to a head it did not run at. CD02 moved no execution and altered no receipt: it changed only which of these fields names which head.",
  "headBindingNote": "Nothing in this record claims a proof ran at a head it did not run at. The executed discovery receipts were captured between 2026-09-23T17:50:00Z and 2026-09-23T23:16:16Z, while the branch head was the admission head and this Work Order's artifacts were still uncommitted in the working tree; the security-analysis receipt was captured at the pre-delivery head; the HIVE/MCP receipt was captured at the proof head and is corroborated by the container's own `git rev-parse HEAD`. The engine build is bound to upstream by the version compiled into the binary, not by a repository head at all.",
  "headRoleTable": {
    "74c47fa204a5da79c1418fb9bcc2557603422f88": "BASE_MAIN_UNCHANGED - origin/main at capture; no commit was made on main",
    "2d567f97d5e3affa32bf190b8393a3e6d20d6327": "ADMISSION_HEAD_HISTORICAL - the head this Work Order was admitted at",
    "958d5ed0bfb74be40eec5f7b3ef0f57fee76b9f4": "PROOF_HEAD_HISTORICAL - the WO-0002 discovery HIVE/MCP receipt, superseded by the C01 row",
    "e481b3376c13cdbdfae243d945d10789d39a23fc": "REVIEWER_CORRECTION_HEAD_HISTORICAL - hand-applied review correction, still asserted by gate",
    "ad4fdf81c0f8cde59671bbe2252eb48f86784eff": "PROOF_HEAD_HISTORICAL - the head the C01 HIVE v1.0.0 read-only MCP proof indexed and inspected",
    "24485b1c3e579a7c1f7be699087c5be069a03a0c": "PROOF_HEAD_HISTORICAL - the head the CD01 bounded context.build re-read ran at",
    "bd5aba1883daee0a9e1825c2f2f385b7ab401cf4": "DELIVERY_HEAD_CURRENT - the head the delivery fields name and whose Governance run ci.json binds"
  },
  "historicalHeadsDeclared": {
    "previouslyDeliveredOrProvedHeads": [
      {
        "head": "7a12df9243b54fd9ac5e5dd7dfcf7f2bbb47e1e0",
        "result": "PASS",
        "governanceRun": "https://github.com/KayzenRoot/isoryn-engine/actions/runs/35937813544/job/107438732251"
      },
      {
        "head": "2d567f97d5e3affa32bf190b8393a3e6d20d6327",
        "result": "PASS",
        "governanceRun": "https://github.com/KayzenRoot/isoryn-engine/actions/runs/35894586565/job/107295219344"
      },
      {
        "head": "ec1f419ec04be2bc1759a010b86306c63d496500",
        "result": "PASS",
        "governanceRun": "https://github.com/KayzenRoot/isoryn-engine/actions/runs/35894231988/job/107294031650"
      },
      {
        "head": "3d442fb8f17b0de2079073ea01883c4d3d69dfdf",
        "result": "PASS",
        "governanceRun": "https://github.com/KayzenRoot/isoryn-engine/actions/runs/36017729211/job/107694443843"
      },
      {
        "head": "db613904a2ed9c4f7db36022ca07726a3898aa83",
        "result": "PASS",
        "governanceRun": "https://github.com/KayzenRoot/isoryn-engine/actions/runs/36019148911/job/107699282758"
      },
      {
        "head": "81f605c2b7074a8ac403bd000c5aa1010eb89d96",
        "result": "PASS",
        "governanceRun": "https://github.com/KayzenRoot/isoryn-engine/actions/runs/36032079943/job/107743044652"
      }
    ],
    "note": "Each entry was a branch head that passed Governance when it was captured. None of them is the delivery head of this record, and CD02 re-attributed no proof from one to another: the receipts listed in `receiptHeadBinding` keep their own capture heads."
  },
  "checkExecutionHeads": {
    "deterministicCommands": {
      "head": "bd5aba1883daee0a9e1825c2f2f385b7ab401cf4",
      "commands": [
        "python scripts/validate_governance.py",
        "python -m unittest discover -s tests -v",
        "python -m py_compile <governance and evidence scripts>",
        "git diff --check",
        "git diff --cached --check",
        "credential pattern sweep over the tree"
      ],
      "howKnown": "executed by the generator against this working tree at the head named here"
    },
    "governanceCheckRuns": {
      "head": "bd5aba1883daee0a9e1825c2f2f385b7ab401cf4",
      "howKnown": "check-run read from the GitHub API per commit and stored in ci.json"
    },
    "hiveMcpReadOnlyProof": {
      "head": "ad4fdf81c0f8cde59671bbe2252eb48f86784eff",
      "howKnown": "receipt plus in-container git rev-parse HEAD"
    },
    "contextBuildReread": {
      "head": "24485b1c3e579a7c1f7be699087c5be069a03a0c",
      "howKnown": "receipt plus index/corpus state at that head"
    },
    "upstreamReverification": {
      "head": "e481b3376c13cdbdfae243d945d10789d39a23fc",
      "howKnown": "the branch head at the instant the receipt quotes, resolved through git"
    }
  },
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
      "corroboratedBy": "in-container git rev-parse HEAD",
      "status": "HISTORICAL_SUPERSEDED_BY_C01"
    },
    "c01HiveMcpProofReceipt": {
      "capturedAt": "2026-09-24T14:55:39Z",
      "branchHeadAtCapture": "ad4fdf81c0f8cde59671bbe2252eb48f86784eff",
      "corroboratedBy": [
        [
          "docker",
          "exec",
          "isoryn-c02-v100-api-1",
          "git",
          "-c",
          "safe.directory=*",
          "-C",
          "/workspace/projects/isoryn-engine",
          "rev-parse",
          "HEAD"
        ],
        "/api/v1/projects/cf0e7dee-bfa4-4f54-b8fa-8391afefbcfd/index/status"
      ],
      "headRecordedInsideReceipt": true
    },
    "c01UpstreamReverificationReceipt": {
      "capturedAt": "2026-09-24T13:31:18Z",
      "branchHeadAtCapture": "e481b3376c13cdbdfae243d945d10789d39a23fc",
      "headRecordedInsideReceipt": false,
      "note": "This receipt quotes its capture instant and the official sources it read, but not `git rev-parse HEAD` at that instant, so its head binding is the reconstructed one the gap row already describes. It was committed at ad4fdf81c, the head the C01 proof then used, so the corpus HIVE answered from contains it."
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
      "isolationNote": "Only HIVE_COMPOSE_PROJECT makes the launcher pass -p; the container that answered is the pinned v1.0.0 proof stack, whose own git rev-parse HEAD is recorded below. The machine's drifted v1.0.2 stack on port 8000 was not addressed by any command here."
    },
    "result": "PASS",
    "health": {
      "status": "ok",
      "version": "1.0.0"
    },
    "bootstrap": {
      "command": "python scripts/hive_bootstrap.py --base-url http://127.0.0.1:18199 --relative-path isoryn-engine",
      "exitCode": 0,
      "stderr": null,
      "attemptsNeeded": 1
    },
    "pipeline": {
      "project_id": "cf0e7dee-bfa4-4f54-b8fa-8391afefbcfd",
      "relative_path": "isoryn-engine",
      "git_branch": "isoryn-wo-0002-architecture-toolchain-discovery",
      "git_head_sha": "ad4fdf81c0f8cde59671bbe2252eb48f86784eff",
      "state": "READY",
      "working_tree_clean": true,
      "index_status": "COMPLETED",
      "corpus_status": "COMPLETED"
    },
    "workingTreeCleanAtProof": true,
    "inContainerHeadProbe": "ad4fdf81c0f8cde59671bbe2252eb48f86784eff",
    "indexStatus": "COMPLETED",
    "corpusStatus": "CURRENT",
    "note": "Executed at the C01 proof head on the isolated compose project named in the receipt, after the reviewer's canonical corrections. Derived state only: Git and the canonical checkpoint outrank HIVE, and the container's own `git rev-parse HEAD` is what confirms the index is looking at the head the proof claims.",
    "receipt": ".engineering/evidence/wo-0002/hive-mcp-proof-c01.json",
    "priorReceiptPreserved": ".engineering/evidence/wo-0002/hive-mcp-proof.json"
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
        "why": "Independent review superseded the branch-activity inference with Godot's official release policy: 4.7 and 4.6 receive bug/security/platform fixes, 4.5 receives security/platform fixes only, and 4.4 and older 4.x lines are unsupported. 4.6 remains the immediately previous fully supported minor line and therefore the compatibility reference.",
        "historicalExecutorWording": "Two maintenance branches are still version-bumped at execution time: 4.7 is at 4.7.3-rc and 4.6 is at 4.6.4-rc, while 4.5 stopped at 4.5.2 (2026-03-19). 4.6 is therefore the immediately previous supported stable line; 4.5 and older are not maintained.",
        "historicalWordingStatus": "SUPERSEDED_BY_INDEPENDENT_REVIEW - kept so the reviewer correction can be seen against what it replaced"
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
      "windowsBuildDocs": "https://docs.godotengine.org/en/latest/engine_details/development/compiling/compiling_for_windows.html",
      "releasePolicy": "https://docs.godotengine.org/en/latest/about/release_policy.html"
    },
    "admissionClaimsReverified": "CONFIRMED",
    "supportPolicyReviewerCorrection": "The executor receipt omitted the official Godot release-policy page. Independent review re-verified that page on 2026-09-24: 4.7 and 4.6 receive bug/security/platform-support fixes; 4.5 receives security/platform-support fixes only; 4.4 and older 4.x lines are unsupported. This supersedes the branch-only support inference without changing the 4.7.2 baseline or 4.6 compatibility-reference choice.",
    "historicalExecutorStatement": {
      "text": "Neither the release archive nor the release list publishes a numbered support-lifetime or LTS policy. The supported set is therefore inferred from the branches that still carry a version bump at execution time, and that inference is stated as an inference.",
      "status": "HISTORICAL_SUPERSEDED_BY_INDEPENDENT_REVIEW",
      "why": "The WO-0002 receipt inferred the supported set from branches that still carry a version bump. That inference is kept so the correction can be checked against what it replaced; the official release policy, not branch activity, is the cited source from here on."
    },
    "c01Reverification": {
      "capturedAt": "2026-09-24T13:31:18Z",
      "newestFourXStableTag": "4.7.2-stable",
      "noNewerStableTagExists": true,
      "currentStableStillAdmitted": true,
      "compatibilityReferenceStillAdmitted": true,
      "officialPageReproducesReviewerCorrection": "CONFIRMED",
      "releasePolicyBytes": 1385229,
      "releasePolicySha256": "7675fe5fea665594305528307f0eb5b0becd0028621fbd35a357d05ef5c3a69e",
      "expensiveReceiptsRepeated": false,
      "decision": {
        "baselineStillCurrent": "CONFIRMED",
        "expensiveReceiptsRepeated": false,
        "stopConditionTriggered": ""
      },
      "receipt": ".engineering/evidence/wo-0002/godot-c01-upstream-reverification.json"
    },
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
    "proofHead": "958d5ed0bfb74be40eec5f7b3ef0f57fee76b9f4",
    "historicalRole": "Superseded as the current exact-head proof by the C01 rebind below. Kept byte-for-byte because it is the record of what was proved at its own head; the reviewer edited canonical sources afterwards, so this receipt now describes text that no longer matches the canonical workspace."
  },
  "independentReviewCorrection": {
    "reviewerHead": "e481b3376c13cdbdfae243d945d10789d39a23fc",
    "reviewerCommit": "docs(review): correct WO-0002 support policy and GPU summary",
    "whatItCorrected": [
      "the compatibility-reference justification, which now cites Godot's official release policy instead of inferring support from branch version bumps",
      "the GPU summary, which now states that upstream's published binary reproduces the host-side shader/device refusal and the OpenGL crash but does NOT reproduce this build's early Vulkan segfault - so the device refusal is host state and the early crash is an unexplained property of the build created here",
      "the canonical checkpoint, which now reads ARCHITECTURE DISCOVERY CORRECTION REQUIRED and names ISORYN-WO-0002-C01-SUPPORT-POLICY-HIVE-REBIND as the active Work Order"
    ],
    "measuredEffectOnEvidence": "Editing ADR-0001, docs/project-brain/08, the checkpoint and this bundle invalidated the exact-head HIVE/MCP proof by the repository's own rule, which is the only thing C01 was for.",
    "receiptsAddedByC01": [
      ".engineering/evidence/wo-0002/godot-c01-upstream-reverification.json",
      ".engineering/evidence/wo-0002/hive-mcp-proof-c01.json"
    ],
    "correctionSentencesCheckedAtHead": {
      "adr0001-support-policy": "docs/adr/ADR-0001-godot-baseline-and-repository-topology.md",
      "brain08-support-policy": "docs/project-brain/08-GODOT-BASELINE-AND-TOPOLOGY.md",
      "checkpoint-correction-status": "docs/project-brain/13-CHECKPOINT.md",
      "gpu-segfault-distinction": ".engineering/evidence/ISORYN-WO-0002-CHECKPOINT-DELTA.md"
    },
    "correctionSentencesMissing": []
  },
  "c01HiveRebind": {
    "workOrder": "ISORYN-WO-0002-C01-SUPPORT-POLICY-HIVE-REBIND",
    "reviewerCorrectionHead": "e481b3376c13cdbdfae243d945d10789d39a23fc",
    "proofHead": "ad4fdf81c0f8cde59671bbe2252eb48f86784eff",
    "proofHeadIsDescendantOfReviewerCorrection": true,
    "canonicalWorkspace": "D:\\Hive\\Projects\\isoryn-engine",
    "branch": "isoryn-wo-0002-architecture-toolchain-discovery",
    "workingTreeCleanAtProof": true,
    "runtime": {
      "health": {
        "status": "ok",
        "version": "1.0.0",
        "environment": "development",
        "timestamp": "2026-09-24T14:52:49.947908Z",
        "data_root": "/var/lib/hive",
        "checks": {
          "postgres": {
            "status": "ok",
            "details": {
              "pgvector": true
            }
          },
          "redis": {
            "status": "ok",
            "details": {
              "canonical": false
            }
          },
          "storage": {
            "status": "ok",
            "details": {
              "configured": true,
              "writable": true,
              "canonical_data_root": "/var/lib/hive"
            }
          }
        }
      },
      "composeProject": "isoryn-c02-v100",
      "containerHeadMatchesProofHead": true,
      "apiContainerStartedAt": "2026-09-24T14:17:21.241636651Z",
      "isolation": "Only HIVE_COMPOSE_PROJECT makes the launcher pass -p; the container that answered is the pinned v1.0.0 proof stack, whose own git rev-parse HEAD is recorded below. The machine's drifted v1.0.2 stack on port 8000 was not addressed by any command here."
    },
    "bootstrap": {
      "exitCode": 0,
      "attemptsNeeded": 1,
      "state": "READY",
      "gitHeadShaReported": "ad4fdf81c0f8cde59671bbe2252eb48f86784eff",
      "containerGitSeconds": [
        {
          "seconds": 3.3,
          "returncode": 0,
          "bytes": 0
        },
        {
          "seconds": 1.7,
          "returncode": 0,
          "bytes": 0
        },
        {
          "seconds": 2.75,
          "returncode": 0,
          "bytes": 0
        }
      ],
      "attempts": [
        {
          "attempt": 1,
          "startedAt": "2026-09-24T14:53:04Z",
          "seconds": 82.78,
          "exitCode": 0,
          "state": "READY",
          "indexStatus": "COMPLETED",
          "corpusStatus": "COMPLETED",
          "stderr": null
        }
      ]
    },
    "indexStatus": {
      "endpoint": "/api/v1/projects/cf0e7dee-bfa4-4f54-b8fa-8391afefbcfd/index/status",
      "run_id": "c27a2f54-e3d0-48e2-a4cc-93a8bc41821e",
      "project_id": "cf0e7dee-bfa4-4f54-b8fa-8391afefbcfd",
      "repository_head_sha": "ad4fdf81c0f8cde59671bbe2252eb48f86784eff",
      "git_branch": "isoryn-wo-0002-architecture-toolchain-discovery",
      "status": "COMPLETED",
      "started_at": "2026-09-24T14:53:23.773535Z",
      "completed_at": "2026-09-24T14:53:24.097680Z",
      "discovered_file_count": 131,
      "indexed_file_count": 0,
      "reused_file_count": 131,
      "changed_file_count": 0,
      "added_file_count": 0,
      "removed_file_count": 0,
      "unchanged_file_count": 131,
      "parsed_file_count": 0,
      "symbol_count": 69,
      "error": null,
      "repositoryHeadMatchesProofHead": true
    },
    "corpusStatus": {
      "endpoint": "/api/v1/projects/cf0e7dee-bfa4-4f54-b8fa-8391afefbcfd/retrieval/corpus",
      "state": "CURRENT",
      "lastSuccessfulSync": "2026-09-24T14:54:03.423274Z",
      "latestRunStatus": "COMPLETED"
    },
    "mcpSession": {
      "protocolVersion": "2025-06-18",
      "serverInfo": {
        "name": "hive-mcp",
        "version": "mcp-core-surface-v1"
      },
      "tools": [
        "project.list",
        "project.status",
        "context.build",
        "context.search",
        "memory.search",
        "memory.get",
        "checkpoint.read"
      ],
      "toolsAreExactlyTheGovernedSeven": true,
      "allReadOnly": true,
      "launcherExit": 0,
      "sessionAttempts": [
        {
          "attempt": 1,
          "startedAt": "2026-09-24T14:55:39Z",
          "launcherExit": 0,
          "unavailableCalls": []
        }
      ],
      "perCallVerdicts": {
        "project.list": "PASS",
        "project.status": "PASS",
        "checkpoint.read": "PASS",
        "context.search": "PASS",
        "memory.search": "NOT_AVAILABLE",
        "memory.get": "NOT_AVAILABLE",
        "context.build": "NOT_AVAILABLE"
      }
    },
    "retrieval": {
      "queries": [
        {
          "query": "official release policy",
          "expectedCanonicalFile": "docs/adr/ADR-0001-godot-baseline-and-repository-topology.md",
          "targetReached": true,
          "candidatePool": 8,
          "hybridState": "LEXICAL_FALLBACK_SEMANTIC_UNAVAILABLE",
          "rerankState": "RERANK_FALLBACK_DISABLED"
        },
        {
          "query": "Godot 4.5 security and platform-support fixes only 4.4 no longer supported",
          "expectedCanonicalFile": "docs/project-brain/08-GODOT-BASELINE-AND-TOPOLOGY.md",
          "targetReached": true,
          "candidatePool": 3,
          "hybridState": "LEXICAL_FALLBACK_SEMANTIC_UNAVAILABLE",
          "rerankState": "RERANK_FALLBACK_DISABLED"
        },
        {
          "query": "ISORYN Checkpoint STATUS",
          "expectedCanonicalFile": "docs/project-brain/13-CHECKPOINT.md",
          "targetReached": true,
          "candidatePool": 8,
          "hybridState": "LEXICAL_FALLBACK_SEMANTIC_UNAVAILABLE",
          "rerankState": "RERANK_FALLBACK_DISABLED"
        },
        {
          "query": "architecture module boundaries",
          "expectedCanonicalFile": "docs/project-brain/04-ARCHITECTURE.md",
          "targetReached": true,
          "candidatePool": 6,
          "hybridState": "LEXICAL_FALLBACK_SEMANTIC_UNAVAILABLE",
          "rerankState": "RERANK_FALLBACK_DISABLED"
        },
        {
          "query": "Bootstrap completes only when Source Pack passes deterministic validation",
          "expectedCanonicalFile": "docs/project-brain/15-DEFINITION-OF-DONE.md",
          "targetReached": true,
          "candidatePool": 1,
          "hybridState": "LEXICAL_FALLBACK_SEMANTIC_UNAVAILABLE",
          "rerankState": "RERANK_FALLBACK_DISABLED"
        },
        {
          "query": "reviewerCorrectionReconciliation baselineStillCurrent expensiveReceiptsRepeated",
          "expectedCanonicalFile": ".engineering/evidence/wo-0002/godot-c01-upstream-reverification.json",
          "targetReached": true,
          "candidatePool": 1,
          "hybridState": "LEXICAL_FALLBACK_SEMANTIC_UNAVAILABLE",
          "rerankState": "RERANK_FALLBACK_DISABLED"
        }
      ],
      "canonicalFilesReached": [
        ".engineering/evidence/wo-0002/godot-c01-upstream-reverification.json",
        "docs/adr/ADR-0001-godot-baseline-and-repository-topology.md",
        "docs/project-brain/04-ARCHITECTURE.md",
        "docs/project-brain/08-GODOT-BASELINE-AND-TOPOLOGY.md",
        "docs/project-brain/13-CHECKPOINT.md",
        "docs/project-brain/15-DEFINITION-OF-DONE.md"
      ],
      "canonicalFilesMissed": [],
      "correctedSupportPolicyMaterialSeen": [
        "adr0001-historical-supersede",
        "adr0001-support-bullet",
        "checkpoint-correction-status",
        "dod-no-defect-promotion",
        "evidence-bundle-corrected-why"
      ],
      "snippetWindowNote": "HIVE returns a truncated window of each matched chunk, so a corrected phrase deeper than that window is invisible in the snippet even when the right chunk matched. Markers are therefore reported per query and per result index, and the full canonical checkpoint text is reported separately under checkpoint.read.",
      "lexicalFallbackRecorded": "Every query answered with LEXICAL_FALLBACK_SEMANTIC_UNAVAILABLE and rerank RERANK_FALLBACK_DISABLED on this stack; the receipt states that as a fact rather than describing the results as semantic."
    },
    "notAvailable": {
      "memory.search": "An unfiltered memory.search (project_id and limit 5, no query) returned zero entries without error on the pinned stack. That is recorded as NOT_AVAILABLE for the memory-retrieval capability rather than as a pass: the call shows nothing was returned for this project, and the call shape cannot establish anything about memories it did not surface.",
      "memory.get": "Called with a syntactically valid UUID whose existence is not asserted; HIVE answers category not_found, code resource_not_found, which is recorded as NOT_AVAILABLE. Independently, the unfiltered memory.search above returned no entries for this project, so the stack surfaced no real memory_id to read - neither response identifies which resource the not_found refers to.",
      "context.build": "Observed literally: category stale, code source_not_current, message 'project source is not current'. HIVE refused the call at its source-currency guard, so this response says nothing about the task_id: it neither establishes that the task is registered nor that it is absent, and it does not demonstrate the happy path either. Recorded as NOT_AVAILABLE and not reclassified. The explanation previously held in this field was inherited from the WO-0002 receipt, whose captured answer was a different one (not_found / resource_not_found), so the inheritance was not supported by the bytes recorded above. Creating a task would mutate HIVE state and is outside a read-only proof."
    },
    "expensiveReceiptsRepeated": false,
    "receipt": ".engineering/evidence/wo-0002/hive-mcp-proof-c01.json",
    "oneLineSummary": "HIVE v1.0.0 and the seven-tool read-only MCP surface were re-proved against the reviewer-corrected canonical text at head ad4fdf81c, on the pinned isolated stack, with retrieval that returns the corrected support-policy material."
  },
  "cd01ContextBuildReread": {
    "purpose": "CD01 corrected the explanation; this re-read establishes what the same arguments answer when the source is demonstrably current, so the record stops leaving the two refusals mixed together.",
    "head": "24485b1c3e579a7c1f7be699087c5be069a03a0c",
    "branch": "isoryn-wo-0002-architecture-toolchain-discovery",
    "cleanTrackedTreeBeforeCapture": true,
    "stack": {
      "baseUrl": "http://127.0.0.1:18199",
      "composeProject": "isoryn-c02-v100",
      "healthVersion": "1.0.0"
    },
    "containerHeadProbe": {
      "before": "24485b1c3e579a7c1f7be699087c5be069a03a0c",
      "after": "24485b1c3e579a7c1f7be699087c5be069a03a0c",
      "matchesHead": true
    },
    "canonicalRefresh": {
      "command": "C:\\Users\\csn19\\AppData\\Local\\Programs\\Python\\Python312\\python.exe scripts/hive_bootstrap.py --base-url http://127.0.0.1:18199 --relative-path isoryn-engine",
      "returncode": 0
    },
    "sourceState": {
      "indexBefore": "COMPLETED",
      "indexRepositoryHeadSha": "24485b1c3e579a7c1f7be699087c5be069a03a0c",
      "corpusBefore": "CURRENT",
      "indexAfter": "COMPLETED",
      "corpusAfter": "CURRENT"
    },
    "governedCallsIssued": 1,
    "request": {
      "method": "tools/call",
      "name": "context.build",
      "arguments": {
        "project_id": "cf0e7dee-bfa4-4f54-b8fa-8391afefbcfd",
        "task_id": "0f4c1a86-2f3b-4f5a-9c1d-7b0e2f1a3d4c",
        "top_k": 5,
        "disclosure_level": "L2"
      },
      "requestSha256": "4b359ef1412d8f8f55d19cada2934e839c0631746e0a9f3a23772278a352f087"
    },
    "c01Answer": {
      "category": "stale",
      "code": "source_not_current",
      "message": "project source is not current"
    },
    "cd01Answer": {
      "category": "not_found",
      "code": "resource_not_found",
      "message": "resource not found"
    },
    "answersTheSameWay": false,
    "whatThisDemonstrates": "The same schema-valid arguments answered differently once the source had just been re-indexed at a clean committed head, so the C01 refusal was state-dependent.",
    "whatItDoesNotDemonstrate": "This response is about the call being refused, not about the task. It does not establish that the task_id is registered, and it does not establish that it is absent: proving the second would need a lookup this guard never reaches, and proving the first would need a write to HIVE, which a read-only proof may not perform. The context.build happy path therefore remains NOT_AVAILABLE.",
    "happyPathResult": "NOT_AVAILABLE",
    "receipt": ".engineering/evidence/wo-0002/context-build-cd01.json"
  },
  "cd02HeadRebinding": {
    "finding": "Independent review of the delivered head found that the record still described the previous delivery head: headSha, candidateHeadSha, commandsExecutedAtHead and github.deliveredHeadSha named the head the CD01 correction was pushed at, and ci.json carried no check-run for the head that was actually current, so the bundle could not be read as covering the candidate.",
    "corrected": [
      "The four delivery-semantics fields now name the head whose completed Governance observation ci.json carries, and the prose above the payload uses the same head.",
      "ci.json gained the check-run for that head, read from the GitHub API, with every earlier observation left byte-identical.",
      "headRoleTable, historicalHeadsDeclared and checkExecutionHeads separate the delivery head from the historical proof heads and from the head each command ran at."
    ],
    "deliberatelyNotChanged": [
      "proofHeadSha, reviewerCorrectionHeadSha, c01ProofHeadSha and the CD01 re-read head, each still taken from its own receipt.",
      "capturedAt of every receipt, and the raw HIVE/MCP captures.",
      "the CD01 interpretation, verdicts and the NOT_AVAILABLE inventory rows."
    ],
    "deliveryHead": {
      "sha": "bd5aba1883daee0a9e1825c2f2f385b7ab401cf4",
      "governanceStatus": "completed",
      "governanceConclusion": "success",
      "run": "https://github.com/KayzenRoot/isoryn-engine/actions/runs/36032284927/job/107743734657",
      "capturedAt": "2026-09-24T18:44:36Z",
      "requiredChecksOutput": "Governance\tpass\t10s\thttps://github.com/KayzenRoot/isoryn-engine/actions/runs/36032284927/job/107743734657"
    },
    "observationsCarriedFromBefore": [
      "7a12df9243b54fd9ac5e5dd7dfcf7f2bbb47e1e0",
      "2d567f97d5e3affa32bf190b8393a3e6d20d6327",
      "ec1f419ec04be2bc1759a010b86306c63d496500",
      "3d442fb8f17b0de2079073ea01883c4d3d69dfdf",
      "db613904a2ed9c4f7db36022ca07726a3898aa83",
      "81f605c2b7074a8ac403bd000c5aa1010eb89d96"
    ],
    "receiptsRewritten": [],
    "captureCommand": "python D:\\Hive\\scratch\\c01_capture_ci.py bd5aba1883daee0a9e1825c2f2f385b7ab401cf4",
    "selfReferenceLimit": "The commit that carries this sentence is a descendant of the head it certifies. Its own check-run is read from GitHub with `gh pr checks 5 --required`; no field in this record claims it."
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
      "path": ".engineering/evidence/wo-0002/ci.json",
      "change": "added"
    },
    {
      "path": ".engineering/evidence/wo-0002/context-build-cd01.json",
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
      "path": ".engineering/evidence/wo-0002/godot-c01-upstream-reverification.json",
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
      "path": ".engineering/evidence/wo-0002/hive-mcp-proof-c01.json",
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
      "path": ".engineering/evidence/wo-0002/ci.json",
      "bytes": 4041,
      "sha256": "8e9f4682136b3583028503ab10800c82e7c6a0bb21c23cb5cfa6e3807b980c88"
    },
    {
      "path": ".engineering/evidence/wo-0002/context-build-cd01.json",
      "bytes": 9372,
      "sha256": "bc55a0853ce0fd40f4dc4e29baa54489a6099e0f7b37b3e7f8b0c3fdcb5ea576"
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
      "path": ".engineering/evidence/wo-0002/godot-c01-upstream-reverification.json",
      "bytes": 5915,
      "sha256": "cca54347eef3d154ebe1909a8386357a6deade71d018420bb6b30af0677e686d"
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
      "path": ".engineering/evidence/wo-0002/hive-mcp-proof-c01.json",
      "bytes": 29924,
      "sha256": "e360f48da3ddbb457138081be1ecf6f577ff0dcc43cc2223007ff103b749a8b2"
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
    "mcp_proof_wo0002_historical": "PASS",
    "godot_official_source_verification": "PASS",
    "c01_official_godot_reverification": "PASS",
    "c01_hive_rebind_at_reviewer_corrected_head": "PASS",
    "c01_retrieval_sees_reviewer_correction": "PASS",
    "cd01_context_build_reread_at_current_source": "PASS",
    "reviewer_correction_preserved": "PASS",
    "toolchain_inventory": "PASS",
    "godot_current_stable_build": "PASS",
    "benchmark_baseline": "PASS",
    "governance_validator": "PASS",
    "unittest_suite": "PASS",
    "governance_ci": "PASS",
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
    "mcp_context_build_happy_path": "NOT_AVAILABLE",
    "context_build_interpretation_matches_raw_response": "PASS",
    "head_rebinding_fields_match_governance_observation": "PASS"
  },
  "governanceRun": {
    "schemaVersion": "isoryn-gef-evidence-v1",
    "workOrder": "ISORYN-WO-0002",
    "repository": "KayzenRoot/isoryn-engine",
    "branch": "isoryn-wo-0002-architecture-toolchain-discovery",
    "capturedAt": "2026-09-24T18:44:36Z",
    "localHead": "bd5aba1883daee0a9e1825c2f2f385b7ab401cf4",
    "remoteHead": "bd5aba1883daee0a9e1825c2f2f385b7ab401cf4",
    "requiredChecksCommand": "gh pr checks 5 --required",
    "requiredChecksOutput": "Governance\tpass\t10s\thttps://github.com/KayzenRoot/isoryn-engine/actions/runs/36032284927/job/107743734657",
    "observations": [
      {
        "head": "7a12df9243b54fd9ac5e5dd7dfcf7f2bbb47e1e0",
        "context": "Governance",
        "status": "completed",
        "conclusion": "success",
        "result": "PASS",
        "run": "https://github.com/KayzenRoot/isoryn-engine/actions/runs/35937813544/job/107438732251",
        "job": "107438732251",
        "detail": "GitHub check-run for this exact commit, read through the API."
      },
      {
        "head": "2d567f97d5e3affa32bf190b8393a3e6d20d6327",
        "context": "Governance",
        "status": "completed",
        "conclusion": "success",
        "result": "PASS",
        "run": "https://github.com/KayzenRoot/isoryn-engine/actions/runs/35894586565/job/107295219344",
        "job": "107295219344",
        "detail": "GitHub check-run for this exact commit, read through the API."
      },
      {
        "head": "ec1f419ec04be2bc1759a010b86306c63d496500",
        "context": "Governance",
        "status": "completed",
        "conclusion": "success",
        "result": "PASS",
        "run": "https://github.com/KayzenRoot/isoryn-engine/actions/runs/35894231988/job/107294031650",
        "job": "107294031650",
        "detail": "GitHub check-run for this exact commit, read through the API."
      },
      {
        "head": "3d442fb8f17b0de2079073ea01883c4d3d69dfdf",
        "context": "Governance",
        "status": "completed",
        "conclusion": "success",
        "result": "PASS",
        "run": "https://github.com/KayzenRoot/isoryn-engine/actions/runs/36017729211/job/107694443843",
        "job": "107694443843",
        "startedAt": "2026-09-24T15:06:42Z",
        "completedAt": "2026-09-24T15:06:46Z",
        "detail": "GitHub check-run for this exact commit, read through the API."
      },
      {
        "head": "db613904a2ed9c4f7db36022ca07726a3898aa83",
        "context": "Governance",
        "status": "completed",
        "conclusion": "success",
        "result": "PASS",
        "run": "https://github.com/KayzenRoot/isoryn-engine/actions/runs/36019148911/job/107699282758",
        "job": "107699282758",
        "startedAt": "2026-09-24T15:18:03Z",
        "completedAt": "2026-09-24T15:18:08Z",
        "detail": "GitHub check-run for this exact commit, read through the API."
      },
      {
        "head": "81f605c2b7074a8ac403bd000c5aa1010eb89d96",
        "context": "Governance",
        "status": "completed",
        "conclusion": "success",
        "result": "PASS",
        "run": "https://github.com/KayzenRoot/isoryn-engine/actions/runs/36032079943/job/107743044652",
        "job": "107743044652",
        "startedAt": "2026-09-24T17:07:20Z",
        "completedAt": "2026-09-24T17:07:27Z",
        "detail": "GitHub check-run for this exact commit, read through the API."
      },
      {
        "head": "bd5aba1883daee0a9e1825c2f2f385b7ab401cf4",
        "context": "Governance",
        "status": "completed",
        "conclusion": "success",
        "result": "PASS",
        "run": "https://github.com/KayzenRoot/isoryn-engine/actions/runs/36032284927/job/107743734657",
        "job": "107743734657",
        "startedAt": "2026-09-24T17:09:08Z",
        "completedAt": "2026-09-24T17:09:18Z",
        "detail": "GitHub check-run for this exact commit, read through the API."
      }
    ],
    "note": "Each observation names the commit GitHub evaluated. A record can carry this file only in a later commit than the one it describes, so the delivered head's own run is read back through the API and through `gh pr checks 5 --required` rather than asserted here.",
    "observationsAppendedFor": "bd5aba1883daee0a9e1825c2f2f385b7ab401cf4",
    "deliveredHeadObservations": 1,
    "governanceCiForDeliveredHead": "PASS"
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
      "result": "PASS - Ran 34 tests in 0.880s, OK"
    },
    {
      "command": "git diff --check (unstaged and staged) + git status --porcelain=v1 empty",
      "result": "PASS - no whitespace errors in either index"
    },
    {
      "command": "repository secret scan (pattern sweep over every tracked and untracked file, plus credential-scanning state read from the GitHub API)",
      "result": "PASS - 129 text files and 4 binary files reported by name out of 133 listed, 0 pattern matches; platform side, 0 secret scanning alerts with push protection enabled"
    },
    {
      "command": "HIVE health/inspect/index/corpus/retrieval + MCP initialize/tools/list/project.status/checkpoint.read/context.search through scripts/hive_mcp.py",
      "result": "HISTORICAL at proofHead 958d5ed0bfb74be40eec5f7b3ef0f57fee76b9f4; superseded as the current proof by the C01 row below. The container's own git rev-parse HEAD returned 958d5ed0bfb74be40eec5f7b3ef0f57fee76b9f4 and the bootstrap that refreshed the index exited 0 with state READY"
    },
    {
      "command": "python scripts/hive_bootstrap.py --base-url http://127.0.0.1:18199 --relative-path isoryn-engine, then a governed MCP session (initialize, tools/list, project.list, project.status, checkpoint.read, six context.search queries, memory.search, memory.get, context.build) through scripts/hive_mcp.py with HIVE_COMPOSE_PROJECT=isoryn-c02-v100",
      "result": "PASS at proofHead ad4fdf81c (reviewer-corrected descendant of e481b3376): bootstrap exit 0 in 1 attempt(s) with state READY, index COMPLETED at the proof head, corpus CURRENT, tools/list exactly the governed seven with readOnlyHint true, launcher exit 0, memory.search/memory.get/context.build NOT_AVAILABLE for their recorded reasons"
    },
    {
      "command": "CD01 bounded re-read: scripts/hive_bootstrap.py against http://127.0.0.1:18199 at a clean tracked tree, then one governed context.build call with the C01 argument set through scripts/hive_mcp.py",
      "result": "executed at head 24485b1c3 - bootstrap exit 0, index COMPLETED at that head, corpus CURRENT, container git head 24485b1c3, answer not_found / resource_not_found (was stale / source_not_current at the C01 head), recorded in .engineering/evidence/wo-0002/context-build-cd01.json"
    },
    {
      "command": "git ls-remote of refs/tags on the official repository, gh api releases/latest, and curl of the official release-policy page (bytes and sha256 recorded)",
      "result": "PASS - 4.7.2-stable is still the newest published stable tag (noNewerStableTagExists True), the admitted baseline commit matches (True), and the official page reproduces the reviewer's support rows (CONFIRMED)"
    },
    {
      "command": "git grep -F for each reviewer-corrected sentence at HEAD (the gate against a regeneration quietly reverting a hand-applied review correction)",
      "result": "PASS - 4 of 4 corrected sentences present in the committed files"
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
      "result": "PASS - Governance check-run for the pushed head, captured per-commit in .engineering/evidence/wo-0002/ci.json"
    }
  ],
  "securityChecks": {
    "credentialPatternSweep": {
      "filesListed": 133,
      "textFilesScanned": 129,
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
    "context.build was first called with a query argument that the governed schema rejects (additionalProperties false) and was re-called with schema-valid arguments. The WO-0002 re-call answered not_found / resource_not_found and the C01 re-call answered stale / source_not_current; neither answer says why, and the claim this record carried - that the refusal proved the task was absent from the stack - was an inference, not an observation.",
    "CD01 found that inference in three places and removed it. The C01 receipt's derived detail described a not_found answer caused by an unregistered task_id while the bytes it captured were a source-currency refusal, an explanation inherited from the WO-0002 receipt whose captured answer was a different one. The raw JSON of every governed call is untouched (verdict, isError, response_sha256, error and argumentsUsed compared field-by-field against the committed receipt); the detail is corrected, the superseded wording is kept verbatim beside it under detailCorrection.supersededDetail, and context.build stays NOT_AVAILABLE because the happy path is still unproven and the task_id's status is still unknown.",
    "CD01 then re-read the same call rather than only re-wording it: canonical bootstrap at a clean tracked tree, index COMPLETED and corpus CURRENT at head 24485b1c3, then exactly one governed read. The answer changed to not_found / resource_not_found, which is evidence that the C01 refusal came from the source-currency guard and not from anything about the task. Recording the second answer is what makes the corrected interpretation measured instead of merely better-phrased; it still does not buy the happy path, so the inventory row did not move.",
    "C01's first proof run asserted retrieval quality by matching loose keywords ('release policy', 'platform-support') against whole serialized responses and never checked whether each query reached its intended canonical file. It therefore reported a missed Definition-of-Done target and zero correction markers on the same run that had just returned the reviewer's corrected ADR-0001 bullet and the corrected Evidence Bundle sentence. Fixed by matching the reviewer's own sentences per result snippet with whitespace collapsed, and by redesigning the queries against executed probes: the Definition-of-Done query was rewritten from the literal phrase 'definition of done', which WO-0001's own evidence chunks quote and which therefore captured the candidate pool, to a sentence only that file contains.",
    "The same first run recorded a snippet as absent evidence when it was only truncated. context.search returns a window of each matched chunk, so a corrected phrase deeper than that window is invisible even when the right chunk matched; the receipt now states the window limitation and reports markers per query and per result index instead of inferring absence from one.",
    "Four of six searches in one C01 session answered database_unavailable ('durable store is unavailable', HIVE v1.0.0 mapping any psycopg error to it) while twelve of twelve identical searches in the next run returned data, so the condition is transient runtime state. Reading those answers as empty results would have produced a receipt claiming the corpus was quiet. The assembler now distinguishes the two, re-runs the session a bounded number of times, and records every attempt with which calls were unavailable.",
    "The pinned stack's indexer failed with git_timeout and then git_status_unavailable because HIVE gives every git call five seconds and the workspace reaches the container over a read-only 9p mount that cannot refresh .git/index, so a cold status re-stats the whole tree. Root-caused with a timed in-container git probe and fixed inside the pinned stack by repacking the host repository's loose objects (299 to 7) and warming the container's cache before the bootstrap, with the cold and warm timings and the failed attempts recorded rather than hidden.",
    "The official release-policy page returns HTTP 403 to urllib's default user agent, so the re-verification fetches it with an identified user agent through curl and records the exact command, the byte count and the SHA-256 of the page it parsed; the support rows quoted in the reviewer correction are read out of that captured page rather than restated.",
    "CD02 found the delivery fields lagging the delivered head: after the CI-binding commits, headSha, candidateHeadSha, commandsExecutedAtHead and github.deliveredHeadSha still named the head the CD01 correction was pushed at, and ci.json carried no check-run for the head that was current, so nothing in the versioned record tied the checks to the candidate under review. The binding was repaired by capturing the current head's run from the GitHub API and by giving every head in the record exactly one declared role. No receipt was re-dated, no proof head moved, and no check is claimed at a head where it did not run: the deterministic commands in `tests` ran against this working tree at the head recorded in commandsExecutedAtHead."
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
      "detail": "Read from the C01 receipt rather than inherited: the unfiltered memory.search returned 0 entries without error, memory.get answered not_found / resource_not_found, and context.build answered stale / source_not_current ('project source is not current'). CD01 re-read that call with the source freshly re-indexed and CURRENT at head 24485b1c3 and got not_found / resource_not_found, so the currency guard, not the task, produced the C01 answer. Each row is a bounded refusal, so each is NOT_AVAILABLE: none of them demonstrates the happy path, and none identifies which resource the refusal refers to, so the task_id's registration status stays unknown rather than proven absent. All used schema-valid arguments and none is recorded as a pass. Creating a task or writing a memory would mutate HIVE state, which is outside a read-only proof."
    }
  ],
  "residualRisks": [
    "The built binary's early Vulkan segfault is not reproduced by upstream's published binary and is not attributed. Until it is explained the frozen command line is a measurement build, not a CI reference build (backlog row 10, ADR-0002).",
    "One mobile-APU Windows host is not a hardware class; every number here is single-host and labelled.",
    "Retrieval on the pinned HIVE stack is lexical (hybrid_state LEXICAL_FALLBACK_SEMANTIC_UNAVAILABLE), so HIVE results are keyword recall, not semantic evidence.",
    "The machine still runs a drifted HIVE v1.0.2 on port 8000; only HIVE_COMPOSE_PROJECT plus the -p flag keeps proofs pointed at the pinned v1.0.0 stack.",
    "The pinned v1.0.0 stack intermittently answers governed reads with database_unavailable while its postgres and redis containers report healthy. The condition is reproduced and bounded but not attributed: any future proof has to distinguish it from an empty result set rather than record it as recall, and a proof that cannot do so should be treated as BLOCKED_HIVE_ISOLATION rather than as a pass.",
    "HIVE v1.0.0 gives every git call five seconds and the canonical workspace reaches the container over a read-only 9p mount, so indexing this tree is fragile on this host class. The mitigation used here (repacked objects plus a warmed container cache) is host state, not a repository guarantee: another machine standing up the same stack can need it too, and the bootstrap attempt counts recorded in the C01 receipt are what make that visible.",
    "context.search returns a truncated window of each matched chunk, so a phrase that exists in a matched file can still be absent from the returned snippet. Absence from a snippet is recorded as absence from the snippet, never as absence from the corpus.",
    "context.build is refused on the pinned stack and neither refusal names the resource it is about. CD01 re-read it once with the source freshly re-indexed and CURRENT at the captured head, and the answer changed from stale/source_not_current to not_found/resource_not_found - which shows the first refusal was a currency guard, not a statement about the task. What stays unknown is the happy path itself: no governed read-only call has produced a built context from this stack, and the registration status of the probe task_id is unknown rather than proven absent. Establishing either would need a write to HIVE, which the read-only boundary forbids without its own admission.",
    "A record cannot carry the check-run of the commit that carries it, so the delivery head named here is always at least one commit behind the branch tip. CD02 closed the part that was a defect - the fields named a head older than the one under review without saying so - and what remains is the structural limit: the carrier commit's own status is platform state, read with `gh pr checks 5 --required`, and no field in this bundle asserts it. A regeneration whose delivery fields do not agree with a completed Governance observation in ci.json now turns a check red instead of quietly re-labelling a head.",
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
    "reviewerCorrectionHeadSha": "e481b3376c13cdbdfae243d945d10789d39a23fc",
    "c01ProofHeadSha": "ad4fdf81c0f8cde59671bbe2252eb48f86784eff",
    "deliveredHeadSha": "bd5aba1883daee0a9e1825c2f2f385b7ab401cf4",
    "deliveryHeadBasis": "the head ci.json carries a completed Governance check-run for; see deliveryHeadSemantics and cd02HeadRebinding",
    "mergeAttempted": false,
    "promotionAttempted": false,
    "note": "Merging and checkpoint/ADR promotion are hard stops for both WO-0002 and C01; the PR is delivered open, and the exact-head Governance result is in governanceRun."
  },
  "proposedCheckpointDelta": {
    "status": "PROPOSED_ONLY_CORRECTION_REQUIRED",
    "path": ".engineering/evidence/ISORYN-WO-0002-CHECKPOINT-DELTA.md",
    "note": "Executor proposes; only the reviewer promotes through the governed flow. C01 does not promote anything: the checkpoint still reads ARCHITECTURE DISCOVERY CORRECTION REQUIRED until the re-review says otherwise."
  },
  "productionCodeConfirmation": "No engine, runtime, editor or module implementation was written in WO-0002 or in its C01 correction. The only executable content is the committed measurement fixture (.engineering/evidence/wo-0002/bench/, a GDScript harness inside the evidence namespace), the governance validator's two new repository-shape gates, and their tests. C01 added two evidence receipts and this bundle; it changed no canonical decision, no pin and no build input.",
  "wo0002StopCondition": "READY_FOR_ARCHITECTURE_TOOLCHAIN_AUDIT",
  "stopCondition": "READY_FOR_WO0002_C01_INDEPENDENT_REVIEW",
  "verdict": "DELIVERED_FOR_INDEPENDENT_REREVIEW",
  "cd01InterpretationGate": {
    "rawResponseStillInReceipt": true,
    "supersededWordingKeptBesideCorrection": true,
    "verdictStillNotAvailable": true,
    "forbiddenPhrasesFoundInRecord": [],
    "rereadReceiptHeadBindsToCapture": true,
    "happyPathStillNotAvailable": true,
    "derivedTextScanned": "c01HiveRebind.notAvailable + unsupportedPlatformFeatures + errorsFoundAndCorrected + checks"
  },
  "cd02HeadRebindingGate": {
    "deliveryFieldsAgree": true,
    "deliveryHead": "bd5aba1883daee0a9e1825c2f2f385b7ab401cf4",
    "deliveryHeadGovernanceObservation": {
      "status": "completed",
      "conclusion": "success",
      "run": "https://github.com/KayzenRoot/isoryn-engine/actions/runs/36032284927/job/107743734657"
    },
    "observationsPresentBeforeRebinding": [
      "7a12df9243b54fd9ac5e5dd7dfcf7f2bbb47e1e0",
      "2d567f97d5e3affa32bf190b8393a3e6d20d6327",
      "ec1f419ec04be2bc1759a010b86306c63d496500",
      "3d442fb8f17b0de2079073ea01883c4d3d69dfdf",
      "db613904a2ed9c4f7db36022ca07726a3898aa83",
      "81f605c2b7074a8ac403bd000c5aa1010eb89d96"
    ],
    "observationsDropped": [],
    "receiptsModifiedInWorkingTree": [],
    "proofHeadsStillBoundToTheirReceipts": true,
    "deliveryHeadAlsoClaimedAsProofHead": false,
    "cd01InterpretationPreserved": true
  }
}
```
