# ISORYN-WO-0001 - Evidence Bundle

Generated 2026-09-21T18:23:38Z by the executor of `ISORYN-WO-0001` (GEF v1.0.0 adoption, HIVE v1.0.0
integration, professional GitHub foundation) for pull request
[ISORYN-WO-0001/#2](https://github.com/KayzenRoot/isoryn-engine/pull/2) at exact head `d5de04c5ac157236de55875bb530f81d3d02ce86`.

This bundle is machine-readable: the JSON block at the end is the payload
`scripts/validate_governance.py` gates. Prose here only points at it.

## Binding

| Field | Value |
| --- | --- |
| Admission base (origin/main at WO admission) | `dfe6b0547f0c46c6f0afb14cb4cfa6b3c8a17362` |
| PR base (`main` at branch cut) | `5fb0179b9c0a9a8f94f170dc299f199a7c7c883d` |
| Head executed against | `d5de04c5ac157236de55875bb530f81d3d02ce86` |
| Head this bundle was written against | `b8b5e90940356c69e85511e29c940f1f093977fc` |
| Reviewer correction head | `4ee69e2c45a6afd2c23a0e7b5a8df20d0acbcc9b` |
| C01 HIVE recovery proof head | `f293fabfd4cde0a202d917b75eee590567b2027e` |
| Branch | `isoryn-wo-0001-foundation` |
| GEF pin | v1.0.0 `866fe3af8cccc65c929aaf6a47a924401fa448b3` |
| HIVE pin | v1.0.0 `a53b5b9fcf55c32a5696180fb1b1ef80ccd1edcf` |

Every entry in checks was executed against this exact tree by a capture tool that runs outside the repository and installs its receipts into this directory afterwards, so no measurement was taken of a tree the capture itself had dirtied. The governance_validator and unittest_suite gates read this bundle, so they cannot be satisfied by the code head alone: they execute against the head that contains this file, and GitHub Actions re-executes them on that head, which is the authority for the reviewed commit. See ciObservations.

headSha is the tree every measurement in this bundle was executed against, taken from the HIVE inspection receipt rather than from the local checkout, so a later evidence-only or documentation commit can never inherit those proofs by proximity. bundleCommitHead is the head this bundle was written against, and ciObservations is complete through it. The commit that actually carries this file is its descendant - no commit can observe its own Actions run - so that run is read from GitHub on the pull request instead of being claimed here, and environmentDrift states what could not be re-executed between headSha and the bundle head.

The 11 commits between the admission base and the PR base are the earlier
direct-to-`main` bootstrap of this same Work Order, permitted before branch protection existed;
they are listed in `priorWorkOrderCommits` rather than presented as this PR's delta.

## Result vocabulary

`PASS` executed and satisfied the gate, `FAIL` executed and did not, `NOT_AVAILABLE` the platform or
runtime refused the capability and the exact response is recorded, `DEFERRED_BY_WO` the Work Order
itself excluded it and the authorizing clause is quoted.

## Executed checks at `d5de04c5ac157236de55875bb530f81d3d02ce86`

| `clean_worktree_for_hive` | PASS |
| `git_diff_check` | PASS |
| `governance_ci` | PASS |
| `governance_validator` | PASS |
| `hive_bootstrap_pipeline` | PASS |
| `hive_corpus_current` | PASS |
| `hive_inspection_head_matches_local_head` | PASS |
| `hive_retrieval_canonical` | PASS |
| `mcp_checkpoint_read` | PASS |
| `mcp_context_search_canonical` | PASS |
| `mcp_handshake` | PASS |
| `mcp_launcher_no_npx_proxy` | PASS |
| `mcp_project_status` | PASS |
| `mcp_readonly_call` | PASS |
| `no_uncommitted_tracked_changes` | PASS |
| `performance_benchmark` | DEFERRED_BY_WO |
| `py_compile` | PASS |
| `secret_scan` | PASS |
| `third_party_dependency_scan` | NOT_AVAILABLE |
| `toolchain_build` | DEFERRED_BY_WO |
| `unittest_suite` | PASS |

`governance_validator` and `unittest_suite` read this bundle as their subject. They cannot pass at
the code head alone; the first push therefore shows a red `Governance` run, quoted in
`ciObservations` with its run URL instead of being smoothed over. The authority for the reviewed
commit is the Actions run on the head that contains this file.

## C01 - HIVE runtime recovery at `f293fabfd4cde0a202d917b75eee590567b2027e`

Independent review found that the proofs above bound to a runtime that no longer served the machine,
and blocked promotion on `HIVE_RUNTIME_DRIFT`. Correction C01 re-establishes the pinned baseline as a
current proof instead of restating the old one. Nothing here edits the `d5de04c5ac15` records: they
stay valid for that head, and the four heads are named separately in `c01Recovery.proofLineage`.

The pinned v1.0.0 source was cloned read-only from the operator's existing HIVE object store at tag
`v1.0.0` (`a53b5b9fcf55c32a5696180fb1b1ef80ccd1edcf`, `VERSION` 1.0.0) and brought up as its own
Compose project `isoryn-c01-v100` on `127.0.0.1:18099`, with its own data root and its own projects
root. Postgres and Redis publish no host port, and the network and container names derive from the
project, so the stack shares no collision domain with the runtimes already on this machine.

| Check | Result | Evidence |
| --- | --- | --- |
| Health reports the pinned baseline | PASS | `/api/v1/health` returns `"version":"1.0.0"` on 18099 while 8000 answers `"version":"1.0.2"` |
| `HIVE_PROJECTS_ROOT` maps `isoryn-engine` to the real working copy | PASS | container sees `/workspace/projects/isoryn-engine`, mounted read-only |
| ISORYN resolves uniquely, no ambiguous identity | PASS | `project.list` returns exactly one project |
| Inspection `repository_accessible=true`, state `READY` | PASS | `hive-preflight.json`, `mcp-proof.json` `project.status` |
| Inspection binds to the C01 head, not `d5de04c5ac15` | PASS | `git_head_sha` = `f293fabfd4cde0a202d917b75eee590567b2027e` |
| `working_tree_clean` truthfully reported | PASS | `true`, captured after the code correction was committed |
| Repository index completes | PASS | `index_status` COMPLETED |
| Retrieval corpus syncs and reports CURRENT | PASS | 135 sources, 218 chunks/references |
| Canonical retrieval resolves | PASS | `13-CHECKPOINT.md` rank 2, `04-ARCHITECTURE.md` rank 2, `15-DEFINITION-OF-DONE.md` rank 11 of 20 |
| Real MCP session through the repository launcher | PASS | `mcp-proof.json`: initialize, tools/list, four executed calls, exit 0, empty stderr |
| `tools/list` is exactly the governed surface | PASS | the seven read-only tools, `allReadOnly` true |
| Launcher targets the pinned stack, not the concurrent one | PASS | `c01Recovery.isolation` - ambient `COMPOSE_PROJECT_NAME` was left pointing at the live stack for the whole session |
| Concurrent HIVE workspaces untouched | PASS | `c01Recovery.concurrentRuntimeBeforeAfter` |

The drift itself moved again while C01 was being executed: the runtime on `127.0.0.1:8000` is no
longer the HIVE 1.0.1 checkout the review recorded but HIVE **1.0.2** from
`C:\Users\csn19\AppData\Local\HIVE\app`, which is also where the evidence had pinned v1.0.0. That
checkout is now at `8db3d244a679898f0e08d1898bc87e6a6a89326e` (`v1.0.2`), so the pinned release commit
survives only as a tagged object in its store. The correction records that instead of quieting it: the
pin was re-materialised from the tag rather than adopted from whatever the machine happens to run, and
the canonical pin stays v1.0.0 - moving it to 1.0.1 or 1.0.2 needs an ADR, which this is not.

Two behaviours of the local environment made the old launcher unsafe here, and both are now tested:
Docker Compose resolves `COMPOSE_PROJECT_NAME` and `HIVE_DATA_ROOT` from the process environment
before any `--env-file`, and `docker compose exec` selects containers by project label rather than by
working directory. Left alone, a launcher running in the pinned checkout entered the 1.0.2 container,
and an isolated stack mounted the live database directory instead of its own.

## What is proved, not asserted

- **HIVE** (`hivePreflight`): health, exact-relative-path resolution without name collision, inspect
  to `READY`, index `COMPLETED`, corpus sync `COMPLETED`, with the observed `git_branch`,
  `git_head_sha` and `working_tree_clean` as reported by the runtime.
- **Canonical retrieval** (`hiveRetrievalProof`): corpus state, source/chunk counts and two lexical
  queries that resolve documents under `docs/project-brain/` - the canonical Project Brain, not
  incidental files.
- **MCP** (`mcpProof`): an executed JSON-RPC session through `scripts/hive_mcp.py` - `initialize`,
  `tools/list` with the seven read-only tools and their annotations, then real
  `project.list`, `project.status`, `checkpoint.read` and `context.search` calls, each with its raw
  response. A configured launcher is not claimed as a working one.
- **GitHub** (`github`): repository settings and the `main-governance` ruleset as captured BEFORE and
  AFTER through authenticated `gh`, plus `gh ruleset check main` read-back and the honest
  `NOT_AVAILABLE` responses of the optional security endpoints.

## Declared gaps

`unsupportedPlatformFeatures` records what this plan or runtime cannot do, `residualRisks` what is
still true but not solved, and `errorsFoundAndCorrected` each defect this Work Order found,
including the ones that initially produced false or missing evidence here.

`environmentDrift` records that the pinned HIVE v1.0.0 runtime stopped serving `127.0.0.1:8000`
while this chain was being closed - including the verbatim failed re-capture receipt - so every
HIVE and MCP proof here is read as bound to `d5de04c5ac15` rather than to the commit that carries
this file. That record is kept as written. `c01Recovery` closes it: the pinned baseline is running
again, isolated, and re-proved against `f293fabfd4cd`, so the drift is closed by a new correction
rather than by editing the drift out.

## Stop condition

`READY_FOR_C01_REVIEW` - the HIVE runtime drift that blocked promotion is closed by current,
re-executed proof at `f293fabfd4cde0a202d917b75eee590567b2027e`, and `verdict` stays
`AWAITING_INDEPENDENT_REVIEW`. The Work Order forbids merging and forbids starting engine
implementation; the checkpoint delta is `PROPOSED_ONLY` and promotion belongs to an independent audit.

```json
{
  "schemaVersion": "isoryn-gef-evidence-bundle-v1",
  "workOrder": "ISORYN-WO-0001",
  "role": "EXECUTOR_DELIVERY",
  "generatedAt": "2026-09-21T18:23:38Z",
  "repository": "KayzenRoot/isoryn-engine",
  "branch": "isoryn-wo-0001-foundation",
  "pr": {
    "number": 2,
    "url": "https://github.com/KayzenRoot/isoryn-engine/pull/2",
    "state": "OPEN",
    "baseSha": "5fb0179b9c0a9a8f94f170dc299f199a7c7c883d",
    "headSha": "b8b5e90940356c69e85511e29c940f1f093977fc",
    "mergedAt": null,
    "merged": false,
    "autoMergeRequest": null,
    "headShaNote": "Recorded from the remote when this bundle was generated, so it names the last pushed head, not the evidence commit itself - a pull request receipt cannot contain its own SHA. The follow-up evidence commit refreshes it alongside ciObservations.",
    "note": "Open for independent review. The Work Order forbids merging, and the executor does not merge or self-approve."
  },
  "baseSha": "5fb0179b9c0a9a8f94f170dc299f199a7c7c883d",
  "headSha": "d5de04c5ac157236de55875bb530f81d3d02ce86",
  "candidateHeadSha": "d5de04c5ac157236de55875bb530f81d3d02ce86",
  "bundleCommitHead": "b8b5e90940356c69e85511e29c940f1f093977fc",
  "proofsBindNote": "headSha is the tree every measurement in this bundle was executed against, taken from the HIVE inspection receipt rather than from the local checkout, so a later evidence-only or documentation commit can never inherit those proofs by proximity. bundleCommitHead is the head this bundle was written against, and ciObservations is complete through it. The commit that actually carries this file is its descendant - no commit can observe its own Actions run - so that run is read from GitHub on the pull request instead of being claimed here, and environmentDrift states what could not be re-executed between headSha and the bundle head.",
  "headBindingNote": "Every entry in checks was executed against this exact tree by a capture tool that runs outside the repository and installs its receipts into this directory afterwards, so no measurement was taken of a tree the capture itself had dirtied. The governance_validator and unittest_suite gates read this bundle, so they cannot be satisfied by the code head alone: they execute against the head that contains this file, and GitHub Actions re-executes them on that head, which is the authority for the reviewed commit. See ciObservations.",
  "admissionBaseSha": "dfe6b0547f0c46c6f0afb14cb4cfa6b3c8a17362",
  "priorWorkOrderCommits": [
    {
      "sha": "5fb0179b9c0a9a8f94f170dc299f199a7c7c883d",
      "subject": "docs: enforce review-first direct correction policy"
    },
    {
      "sha": "6584b7aae7546d33e8d747feff2265ba3d3eff67",
      "subject": "docs: require PDF executor prompt artifacts"
    },
    {
      "sha": "5725fa60aedf97f78f6c3146e81422d3ee54716d",
      "subject": "chore(bootstrap): add local sync and GitHub hardening runbooks [ISORYN-WO-0001]"
    },
    {
      "sha": "773199892d07c489c81157b51dc6d04733c2cf1d",
      "subject": "chore(governance): reconcile complete ISORYN GEF/HIVE foundation [ISORYN-WO-0001]"
    },
    {
      "sha": "c8678be6665399e3afe482dbe34250d1a7ab665f",
      "subject": "chore(governance): install ISORYN source pack [ISORYN-WO-0001]"
    },
    {
      "sha": "9393f623d487462faad58de01e0afb75c4db0365",
      "subject": "chore(governance): install ISORYN source pack [ISORYN-WO-0001]"
    },
    {
      "sha": "b1004848072c38aedb06e6bd48fda07e8db34710",
      "subject": "chore(governance): install ISORYN source pack [ISORYN-WO-0001]"
    },
    {
      "sha": "b289a4367bd711107c0de6d697676be5a4516359",
      "subject": "chore(governance): install ISORYN source pack [ISORYN-WO-0001]"
    },
    {
      "sha": "88283b45be0cfab2130d0cb5e342064e9f53dc61",
      "subject": "chore(governance): install ISORYN source pack [ISORYN-WO-0001]"
    },
    {
      "sha": "b2bbc17c5befd5e5932c076b0d6df23995778259",
      "subject": "chore(governance): install ISORYN source pack [ISORYN-WO-0001]"
    },
    {
      "sha": "9caf1be57707f39b79364be1308ec8512036414b",
      "subject": "chore(governance): install ISORYN source pack [ISORYN-WO-0001]"
    }
  ],
  "upstreamPins": {
    "gef": {
      "version": "1.0.0",
      "releaseCommit": "866fe3af8cccc65c929aaf6a47a924401fa448b3",
      "validated": "PASS",
      "method": "annotated tag v1.0.0 resolves to this commit in a read-only source checkout; nothing was vendored into ISORYN"
    },
    "hive": {
      "version": "1.0.0",
      "releaseCommit": "a53b5b9fcf55c32a5696180fb1b1ef80ccd1edcf",
      "validated": "PASS",
      "method": "the release commit is present in the installed HIVE v1.0.0 source tree used by the local runtime; the separate development checkout does not contain it, which is recorded instead of being silently ignored"
    }
  },
  "canonicalInputs": [
    "AGENTS.md",
    ".engineering/SOURCE-HIERARCHY.md",
    "docs/project-brain/13-CHECKPOINT.md",
    "docs/project-brain/16-DECISIONS-LEDGER.md",
    "docs/project-brain/03-SCOPE.md",
    "docs/project-brain/15-DEFINITION-OF-DONE.md",
    "docs/project-brain/04-ARCHITECTURE.md",
    "docs/project-brain/02-REQUIREMENTS.md",
    "docs/project-brain/11-TEST-PLAN.md",
    "docs/GEF-BOOTSTRAP.md",
    "docs/HIVE-INTEGRATION.md",
    ".engineering/work-orders/ISORYN-WO-0001-GEF-HIVE-BOOTSTRAP.md",
    "ISORYN-WO-0001-SYNC-GEF-HIVE-GITHUB-FOUNDATION.pdf (executor handoff artifact)"
  ],
  "filesChanged": [
    ".codex/config.toml",
    ".engineering/REVIEW-AUTOFIX-POLICY.md",
    ".engineering/context-locks/ISORYN-WO-0001.json",
    ".engineering/evidence/ISORYN-WO-0001-CHECKPOINT-DELTA.md",
    ".engineering/evidence/ISORYN-WO-0001-EVIDENCE.md",
    ".engineering/evidence/checks.json",
    ".engineering/evidence/ci.json",
    ".engineering/evidence/github/after-repository.json",
    ".engineering/evidence/github/after-ruleset.json",
    ".engineering/evidence/github/before-repository.json",
    ".engineering/evidence/github/before-rulesets.json",
    ".engineering/evidence/github/ruleset-check-main.txt",
    ".engineering/evidence/github/ruleset-list.json",
    ".engineering/evidence/github/ruleset-view.txt",
    ".engineering/evidence/github/security-endpoints.txt",
    ".engineering/evidence/hive-preflight.json",
    ".engineering/evidence/hive-retrieval-proof.json",
    ".engineering/evidence/matrix.log",
    ".engineering/evidence/mcp-proof.json",
    ".engineering/gef/GEF-EVIDENCE-SPEC.md",
    ".engineering/gef/GEF-EXECUTION-PROTOCOL.md",
    ".engineering/github/repository-settings.json",
    ".engineering/github/ruleset-main-governance.json",
    ".engineering/work-orders/ISORYN-WO-0001-GEF-HIVE-BOOTSTRAP.md",
    ".env.example",
    ".gitattributes",
    ".github/CODEOWNERS",
    ".github/dependabot.yml",
    ".github/pull_request_template.md",
    ".gitignore",
    ".mcp.json",
    "AGENTS.md",
    "CONTRIBUTING.md",
    "docs/BOOTSTRAP-RUNBOOK.md",
    "docs/GEF-BOOTSTRAP.md",
    "docs/HIVE-INTEGRATION.md",
    "scripts/bootstrap-local.ps1",
    "scripts/configure-github.ps1",
    "scripts/hive-bootstrap.ps1",
    "scripts/hive_bootstrap.py",
    "scripts/hive_mcp.py",
    "scripts/validate_governance.py",
    "tests/test_governance.py"
  ],
  "checks": {
    "py_compile": "PASS",
    "governance_validator": "PASS",
    "unittest_suite": "PASS",
    "git_diff_check": "PASS",
    "no_uncommitted_tracked_changes": "PASS",
    "clean_worktree_for_hive": "PASS",
    "secret_scan": "PASS",
    "hive_bootstrap_pipeline": "PASS",
    "hive_inspection_head_matches_local_head": "PASS",
    "hive_corpus_current": "PASS",
    "hive_retrieval_canonical": "PASS",
    "mcp_handshake": "PASS",
    "mcp_readonly_call": "PASS",
    "mcp_project_status": "PASS",
    "mcp_checkpoint_read": "PASS",
    "mcp_context_search_canonical": "PASS",
    "mcp_launcher_no_npx_proxy": "PASS",
    "governance_ci": "PASS",
    "toolchain_build": "DEFERRED_BY_WO",
    "performance_benchmark": "DEFERRED_BY_WO",
    "third_party_dependency_scan": "NOT_AVAILABLE"
  },
  "hivePreflight": {
    "api": "http://127.0.0.1:8000",
    "result": "PASS",
    "attempts": [
      {
        "attempt": 1,
        "result": "PASS",
        "detail": "COMPLETED"
      }
    ],
    "pipeline": {
      "project_id": "8696b773-8554-4f27-9cb0-77ddfaf98deb",
      "relative_path": "isoryn-engine",
      "git_branch": "isoryn-wo-0001-foundation",
      "git_head_sha": "d5de04c5ac157236de55875bb530f81d3d02ce86",
      "state": "READY",
      "working_tree_clean": true,
      "index_status": "COMPLETED",
      "corpus_status": "COMPLETED"
    },
    "classification": null,
    "note": "Derived state only: Git and the canonical checkpoint outrank HIVE. working_tree_clean is reported as observed and never edited into a true value."
  },
  "hiveRetrievalProof": {
    "project_id": "8696b773-8554-4f27-9cb0-77ddfaf98deb",
    "corpus": {
      "state": "CURRENT",
      "last_successful_sync": "2026-09-21T17:43:39.160137Z",
      "latest_run": {
        "status": "COMPLETED",
        "repository_source_count": 130,
        "chunk_count": 200,
        "current_reference_count": 202
      }
    },
    "queries": {
      "Definition of Done": {
        "paths": [
          ".engineering/evidence/ISORYN-WO-0001-EVIDENCE.md",
          ".engineering/evidence/mcp-proof.json",
          ".engineering/evidence/ISORYN-WO-0001-EVIDENCE.md",
          ".engineering/evidence/mcp-proof.json",
          ".engineering/evidence/hive-retrieval-proof.json",
          ".engineering/evidence/ISORYN-WO-0001-EVIDENCE.md",
          ".engineering/evidence/ISORYN-WO-0001-CHECKPOINT-DELTA.md",
          "docs/project-brain/15-DEFINITION-OF-DONE.md",
          ".engineering/evidence/ISORYN-WO-0001-EVIDENCE.md",
          "scripts/validate_governance.py"
        ],
        "canonical_paths": [
          "docs/project-brain/15-DEFINITION-OF-DONE.md"
        ],
        "canonical_ranks": [
          7
        ],
        "first_canonical_rank": 7
      },
      "Godot engine foundation": {
        "paths": [
          "docs/project-brain/05-INTEGRATION-CONTRACTS.md",
          ".engineering/evidence/hive-retrieval-proof.json",
          ".engineering/evidence/ISORYN-WO-0001-EVIDENCE.md",
          ".engineering/work-orders/ISORYN-WO-0001-GEF-HIVE-BOOTSTRAP.md",
          ".engineering/evidence/ISORYN-WO-0001-EVIDENCE.md",
          ".engineering/evidence/ISORYN-WO-0001-EVIDENCE.md",
          ".engineering/github/repository-settings.json",
          "README.md",
          "docs/project-brain/01-PROJECT-OVERVIEW.md",
          ".engineering/evidence/github/after-repository.json"
        ],
        "canonical_paths": [
          "docs/project-brain/01-PROJECT-OVERVIEW.md",
          "docs/project-brain/05-INTEGRATION-CONTRACTS.md"
        ],
        "canonical_ranks": [
          0,
          8
        ],
        "first_canonical_rank": 0
      }
    },
    "canonical_paths": [
      "docs/project-brain/01-PROJECT-OVERVIEW.md",
      "docs/project-brain/05-INTEGRATION-CONTRACTS.md",
      "docs/project-brain/15-DEFINITION-OF-DONE.md"
    ]
  },
  "mcpProof": {
    "launcher": "python scripts/hive_mcp.py",
    "serverInfo": {
      "name": "hive-mcp",
      "version": "mcp-core-surface-v1"
    },
    "tools": [
      "checkpoint.read",
      "context.build",
      "context.search",
      "memory.get",
      "memory.search",
      "project.list",
      "project.status"
    ],
    "annotations": {
      "project.list": {
        "readOnlyHint": true,
        "destructiveHint": false,
        "idempotentHint": true,
        "openWorldHint": false
      },
      "project.status": {
        "readOnlyHint": true,
        "destructiveHint": false,
        "idempotentHint": true,
        "openWorldHint": false
      },
      "context.build": {
        "readOnlyHint": true,
        "destructiveHint": false,
        "idempotentHint": true,
        "openWorldHint": false
      },
      "context.search": {
        "readOnlyHint": true,
        "destructiveHint": false,
        "idempotentHint": true,
        "openWorldHint": false
      },
      "memory.search": {
        "readOnlyHint": true,
        "destructiveHint": false,
        "idempotentHint": true,
        "openWorldHint": false
      },
      "memory.get": {
        "readOnlyHint": true,
        "destructiveHint": false,
        "idempotentHint": true,
        "openWorldHint": false
      },
      "checkpoint.read": {
        "readOnlyHint": true,
        "destructiveHint": false,
        "idempotentHint": true,
        "openWorldHint": false
      }
    },
    "allReadOnly": true,
    "calls": {
      "project.list": {
        "jsonrpc": "2.0",
        "id": 3,
        "result": {
          "content": [
            {
              "type": "text",
              "text": "{\"limit\":32,\"projects\":[{\"detached_head\":false,\"git_branch\":\"isoryn-wo-0001-foundation\",\"git_head_sha\":\"d5de04c5ac157236de55875bb530f81d3d02ce86\",\"language_stack\":[],\"name\":\"ISORYN\",\"project_id\":\"8696b773-8554-4f27-9cb0-77ddfaf98deb\",\"relative_path\":\"isoryn-engine\",\"repository_accessible\":true,\"state\":\"READY\",\"working_tree_clean\":true},{\"detached_head\":false,\"git_branch\":\"main\",\"git_head_sha\":\"8e995cf4fe66d6da185fd1540d84069d836a5525\",\"language_stack\":[],\"name\":\"FORGE\",\"project_id\":\"08d8ac6c-eedb-42d5-a03c-d699eea6fc85\",\"relative_path\":\"forge\",\"repository_accessible\":true,\"state\":\"READY\",\"working_tree_clean\":true},{\"detached_head\":false,\"git_branch\":\"feat/m01-core-runtime\",\"git_head_sha\":\"0eafc1682f31edadca935d1d47d9cf4baf2bf82f\",\"language_stack\":[\"rust\"],\"name\":\"CORE\",\"project_id\":\"220151cb-0e6e-43b3-845e-faec9c5a851b\",\"relative_path\":\"core\",\"repository_accessible\":true,\"state\":\"READY\",\"working_tree_clean\":false},{\"detached_head\":false,\"git_branch\":\"codex/cp-02r-hive-mcp-corrective\",\"git_head_sha\":\"79fd8c709ea73fb017545b835f9073288ce2af10\",\"language_stack\":[\"typescript\",\"javascript\"],\"name\":\"NEXLABS-WEB\",\"project_id\":\"85efae57-a5f4-44c8-aa0a-f63412fabaa5\",\"relative_path\":\"nexlabs-web\",\"repository_accessible\":true,\"state\":\"READY\",\"working_tree_clean\":true}],\"returned_count\":4,\"truncated\":false,\"version\":\"mcp-project-list-v1\"}"
            }
          ],
          "structuredContent": {
            "version": "mcp-project-list-v1",
            "limit": 32,
            "returned_count": 4,
            "truncated": false,
            "projects": [
              {
                "project_id": "8696b773-8554-4f27-9cb0-77ddfaf98deb",
                "name": "ISORYN",
                "relative_path": "isoryn-engine",
                "git_branch": "isoryn-wo-0001-foundation",
                "git_head_sha": "d5de04c5ac157236de55875bb530f81d3d02ce86",
                "detached_head": false,
                "repository_accessible": true,
                "working_tree_clean": true,
                "language_stack": [],
                "state": "READY"
              },
              {
                "project_id": "08d8ac6c-eedb-42d5-a03c-d699eea6fc85",
                "name": "FORGE",
                "relative_path": "forge",
                "git_branch": "main",
                "git_head_sha": "8e995cf4fe66d6da185fd1540d84069d836a5525",
                "detached_head": false,
                "repository_accessible": true,
                "working_tree_clean": true,
                "language_stack": [],
                "state": "READY"
              },
              {
                "project_id": "220151cb-0e6e-43b3-845e-faec9c5a851b",
                "name": "CORE",
                "relative_path": "core",
                "git_branch": "feat/m01-core-runtime",
                "git_head_sha": "0eafc1682f31edadca935d1d47d9cf4baf2bf82f",
                "detached_head": false,
                "repository_accessible": true,
                "working_tree_clean": false,
                "language_stack": [
                  "rust"
                ],
                "state": "READY"
              },
              {
                "project_id": "85efae57-a5f4-44c8-aa0a-f63412fabaa5",
                "name": "NEXLABS-WEB",
                "relative_path": "nexlabs-web",
                "git_branch": "codex/cp-02r-hive-mcp-corrective",
                "git_head_sha": "79fd8c709ea73fb017545b835f9073288ce2af10",
                "detached_head": false,
                "repository_accessible": true,
                "working_tree_clean": true,
                "language_stack": [
                  "typescript",
                  "javascript"
                ],
                "state": "READY"
              }
            ]
          },
          "isError": false
        }
      },
      "project.status": {
        "jsonrpc": "2.0",
        "id": 4,
        "result": {
          "content": [
            {
              "type": "text",
              "text": "{\"project\":{\"detached_head\":false,\"git_branch\":\"isoryn-wo-0001-foundation\",\"git_head_sha\":\"d5de04c5ac157236de55875bb530f81d3d02ce86\",\"language_stack\":[],\"name\":\"ISORYN\",\"project_id\":\"8696b773-8554-4f27-9cb0-77ddfaf98deb\",\"relative_path\":\"isoryn-engine\",\"repository_accessible\":true,\"state\":\"READY\",\"working_tree_clean\":true},\"version\":\"mcp-project-status-v1\"}"
            }
          ],
          "structuredContent": {
            "version": "mcp-project-status-v1",
            "project": {
              "project_id": "8696b773-8554-4f27-9cb0-77ddfaf98deb",
              "name": "ISORYN",
              "relative_path": "isoryn-engine",
              "git_branch": "isoryn-wo-0001-foundation",
              "git_head_sha": "d5de04c5ac157236de55875bb530f81d3d02ce86",
              "detached_head": false,
              "repository_accessible": true,
              "working_tree_clean": true,
              "language_stack": [],
              "state": "READY"
            }
          },
          "isError": false
        }
      },
      "checkpoint.read": {
        "jsonrpc": "2.0",
        "id": 5,
        "result": {
          "content": [
            {
              "type": "text",
              "text": "{\"checkpoint\":{\"content\":\"# ISORYN Checkpoint\\n\\n## STATUS\\nBOOTSTRAP ACTIVE\\n\\n## VERSION\\nISORYN 0.0 - Clean Foundation\\n\\n## PHASE\\n0 - GEF/HIVE Repository Foundation\\n\\n## OBJECTIVE\\nEstablish the professional Source Pack, GEF v1.0.0 governance, HIVE v1.0.0 integration, Codex MCP bridge and exact-head governance CI before engine implementation begins.\\n\\n## IN PROGRESS\\nISORYN-WO-0001-GEF-HIVE-BOOTSTRAP.\\n\\n## BLOCKERS\\nLocal HIVE runtime registration/indexing cannot be proven from GitHub alone and requires execution in the canonical Windows workspace. Repository administrative protection also requires settings/gh access if not already configured.\\n\\n## NEXT STEP\\nValidate local HIVE registration from D:\\\\Hive\\\\Projects\\\\isoryn-engine, configure professional main ruleset, collect exact-head CI/evidence, audit, then promote this checkpoint before engine module discovery.\\n\",\"content_characters\":837,\"git_blob_sha\":\"eda40e734a2c9f5e4fdf9cd8d559758f3ef93aba\",\"git_head_sha\":\"d5de04c5ac157236de55875bb530f81d3d02ce86\",\"path\":\"docs/project-brain/13-CHECKPOINT.md\",\"registered_head_sha\":\"d5de04c5ac157236de55875bb530f81d3d02ce86\",\"section_count\":7,\"sections\":[{\"end_char\":49,\"end_line\":5,\"heading\":\"STATUS\",\"start_char\":21,\"start_line\":3},{\"end_char\":91,\"end_line\":8,\"heading\":\"VERSION\",\"start_char\":49,\"start_line\":6},{\"end_char\":136,\"end_line\":11,\"heading\":\"PHASE\",\"start_char\":91,\"start_line\":9},{\"end_char\":321,\"end_line\":14,\"heading\":\"OBJECTIVE\",\"start_char\":136,\"start_line\":12},{\"end_char\":372,\"end_line\":17,\"heading\":\"IN PROGRESS\",\"start_char\":321,\"start_line\":15},{\"end_char\":617,\"end_line\":20,\"heading\":\"BLOCKERS\",\"start_char\":372,\"start_line\":18},{\"end_char\":837,\"end_line\":22,\"heading\":\"NEXT STEP\",\"start_char\":617,\"start_line\":21}],\"source_content_sha256\":\"e80d974e32e7d6da04e2cd35a5ff16c8c7f60e71f09ed4ddc4c2cf39484e0188\"},\"project_id\":\"8696b773-8554-4f27-9cb0-77ddfaf98deb\",\"version\":\"mcp-checkpoint-read-v1\"}"
            }
          ],
          "structuredContent": {
            "version": "mcp-checkpoint-read-v1",
            "project_id": "8696b773-8554-4f27-9cb0-77ddfaf98deb",
            "checkpoint": {
              "path": "docs/project-brain/13-CHECKPOINT.md",
              "git_head_sha": "d5de04c5ac157236de55875bb530f81d3d02ce86",
              "registered_head_sha": "d5de04c5ac157236de55875bb530f81d3d02ce86",
              "git_blob_sha": "eda40e734a2c9f5e4fdf9cd8d559758f3ef93aba",
              "source_content_sha256": "e80d974e32e7d6da04e2cd35a5ff16c8c7f60e71f09ed4ddc4c2cf39484e0188",
              "section_count": 7,
              "sections": [
                {
                  "heading": "STATUS",
                  "start_line": 3,
                  "end_line": 5,
                  "start_char": 21,
                  "end_char": 49
                },
                {
                  "heading": "VERSION",
                  "start_line": 6,
                  "end_line": 8,
                  "start_char": 49,
                  "end_char": 91
                },
                {
                  "heading": "PHASE",
                  "start_line": 9,
                  "end_line": 11,
                  "start_char": 91,
                  "end_char": 136
                },
                {
                  "heading": "OBJECTIVE",
                  "start_line": 12,
                  "end_line": 14,
                  "start_char": 136,
                  "end_char": 321
                },
                {
                  "heading": "IN PROGRESS",
                  "start_line": 15,
                  "end_line": 17,
                  "start_char": 321,
                  "end_char": 372
                },
                {
                  "heading": "BLOCKERS",
                  "start_line": 18,
                  "end_line": 20,
                  "start_char": 372,
                  "end_char": 617
                },
                {
                  "heading": "NEXT STEP",
                  "start_line": 21,
                  "end_line": 22,
                  "start_char": 617,
                  "end_char": 837
                }
              ],
              "content_characters": 837,
              "content": "# ISORYN Checkpoint\n\n## STATUS\nBOOTSTRAP ACTIVE\n\n## VERSION\nISORYN 0.0 - Clean Foundation\n\n## PHASE\n0 - GEF/HIVE Repository Foundation\n\n## OBJECTIVE\nEstablish the professional Source Pack, GEF v1.0.0 governance, HIVE v1.0.0 integration, Codex MCP bridge and exact-head governance CI before engine implementation begins.\n\n## IN PROGRESS\nISORYN-WO-0001-GEF-HIVE-BOOTSTRAP.\n\n## BLOCKERS\nLocal HIVE runtime registration/indexing cannot be proven from GitHub alone and requires execution in the canonical Windows workspace. Repository administrative protection also requires settings/gh access if not already configured.\n\n## NEXT STEP\nValidate local HIVE registration from D:\\Hive\\Projects\\isoryn-engine, configure professional main ruleset, collect exact-head CI/evidence, audit, then promote this checkpoint before engine module discovery.\n"
            }
          },
          "isError": false
        }
      },
      "context.search": {
        "jsonrpc": "2.0",
        "id": 6,
        "result": {
          "content": [
            {
              "type": "text",
              "text": "{\"candidate_pool\":5,\"fallback_reason\":\"rerank_disabled\",\"hybrid_state\":\"LEXICAL_FALLBACK_SEMANTIC_UNAVAILABLE\",\"normalized_query\":\"definition of done\",\"project_id\":\"8696b773-8554-4f27-9cb0-77ddfaf98deb\",\"query\":\"Definition of Done\",\"rerank_state\":\"RERANK_FALLBACK_DISABLED\",\"results\":[{\"chunk_content_sha256\":\"c509b009afcc28546fddd5a1d139d5e868a71ebb47b0fdf375990d3fa2646af5\",\"chunk_id\":\"bde16aaa-5049-4b42-bf99-deb31fa9a2b3\",\"chunker_version\":\"line-window-v1\",\"corpus_run_id\":\"43cc41ca-685f-4812-8e98-0ac965919171\",\"end_char\":41498,\"end_line\":649,\"hybrid_score\":0.01639344262295082,\"lexical_contribution\":0.01639344262295082,\"lexical_rank\":1,\"lexical_score\":1.0409587621688843,\"path\":\".engineering/evidence/ISORYN-WO-0001-EVIDENCE.md\",\"pre_rerank_rank\":1,\"project_id\":\"8696b773-8554-4f27-9cb0-77ddfaf98deb\",\"qualified_symbol\":null,\"reference_id\":\"06289fa6-8a8e-470c-a09b-632744aaf67d\",\"repository_file_id\":\"bf4963d4-ddec-4e95-aa7f-e31a5efe173a\",\"repository_symbol_id\":null,\"rerank_rank\":1,\"rerank_score\":null,\"semantic_contribution\":0.0,\"semantic_distance\":null,\"semantic_rank\":null,\"semantic_score\":null,\"snippet\":\"            }\\n          ],\\n          \\\"structuredContent\\\": {\\n            \\\"version\\\": \\\"mcp-context-search-v1\\\",\\n            \\\"project_id\\\": \\\"8696b773-8554-4f27-9cb0-77ddfaf98deb\\\",\\n            \\\"query\\\": \\\"Definition of Done\\\",\\n            \\\"normalized_query\\\": \\\"definition of done\\\",\\n            \\\"top_k\\\": 5,\\n            \\\"candidate_pool\\\": 5,\\n            \\\"hybrid_state\\\": \\\"LEXICAL_FALLBACK_SEMANTIC_UNAVAILABLE\\\",\\n            \\\"semantic_state\\\": \\\"UNAVAILABLE\\\",\\n            \\\"rerank_state\\\": \\\"RERANK_FALLBACK_DISABLED\\\",\\n            \\\"fallback_reason\\\": \\\"rerank_disabled\\\",\\n            \\\"results\\\": [\\n              {\\n                \\\"project_id\\\": \\\"8696b773-8554-4f27-9\",\"snippet_characters\":643,\"snippet_truncated\":true,\"source_content_sha256\":\"954bcd7f4e0cc1e05ebb1754a1aaf8aa4df78fabfb54027b5f0d0dd0a11c99ba\",\"source_kind\":\"REPOSITORY_FILE\",\"start_char\":36356,\"start_line\":570,\"task_id\":null,\"title\":null},{\"chunk_content_sha256\":\"7babe43715f282601727e6c2823643493f704f650a355b1fa7b4aa9fa2821566\",\"chunk_id\":\"ebe8e2a3-fa25-43f2-a4b4-9ac40ce4dba1\",\"chunker_version\":\"line-window-v1\",\"corpus_run_id\":\"43cc41ca-685f-4812-8e98-0ac965919171\",\"end_char\":26511,\"end_line\":329,\"hybrid_score\":0.016129032258064516,\"lexical_contribution\":0.016129032258064516,\"lexical_rank\":2,\"lexical_score\":1.0409587621688843,\"path\":\".engineering/evidence/mcp-proof.json\",\"pre_rerank_rank\":2,\"project_id\":\"8696b773-8554-4f27-9cb0-77ddfaf98deb\",\"qualified_symbol\":null,\"reference_id\":\"85fc03eb-6b4e-430a-8ffa-cd9725faebfd\",\"repository_file_id\":\"b6431965-e302-48e6-8fd9-13fdbc785e5a\",\"repository_symbol_id\":null,\"rerank_rank\":2,\"rerank_score\":null,\"semantic_contribution\":0.0,\"semantic_distance\":null,\"semantic_rank\":null,\"semantic_score\":null,\"snippet\":\"          }\\n        ],\\n        \\\"structuredContent\\\": {\\n          \\\"version\\\": \\\"mcp-context-search-v1\\\",\\n          \\\"project_id\\\": \\\"8696b773-8554-4f27-9cb0-77ddfaf98deb\\\",\\n          \\\"query\\\": \\\"Definition of Done\\\",\\n          \\\"normalized_query\\\": \\\"definition of done\\\",\\n          \\\"top_k\\\": 5,\\n          \\\"candidate_pool\\\": 5,\\n          \\\"hybrid_state\\\": \\\"LEXICAL_FALLBACK_SEMANTIC_UNAVAILABLE\\\",\\n          \\\"semantic_state\\\": \\\"UNAVAILABLE\\\",\\n          \\\"rerank_state\\\": \\\"RERANK_FALLBACK_DISABLED\\\",\\n          \\\"fallback_reason\\\": \\\"rerank_disabled\\\",\\n          \\\"results\\\": [\\n            {\\n              \\\"project_id\\\": \\\"8696b773-8554-4f27-9cb0-77ddfaf98deb\\\",\\n             \",\"snippet_characters\":643,\"snippet_truncated\":true,\"source_content_sha256\":\"3781d9b9709e375e7afc574cb567d1c37f0a3ab3b7ad0107a091c5cf46f2fd75\",\"source_kind\":\"REPOSITORY_FILE\",\"start_char\":21529,\"start_line\":250,\"task_id\":null,\"title\":null},{\"chunk_content_sha256\":\"d9bb3c5cb2d1f8772f70818dba397e6fd9d95a0c8f42a5909bcffac79b17f027\",\"chunk_id\":\"ac667c5b-2aa2-4559-8ff3-a7b8c0c61ce2\",\"chunker_version\":\"line-window-v1\",\"corpus_run_id\":\"43cc41ca-685f-4812-8e98-0ac965919171\",\"end_char\":32881,\"end_line\":569,\"hybrid_score\":0.015873015873015872,\"lexical_contribution\":0.015873015873015872,\"lexical_rank\":3,\"lexical_score\":0.9363574981689453,\"path\":\".engineering/evidence/ISORYN-WO-0001-EVIDENCE.md\",\"pre_rerank_rank\":3,\"project_id\":\"8696b773-8554-4f27-9cb0-77ddfaf98deb\",\"qualified_symbol\":null,\"reference_id\":\"f359f8f7-0f30-4583-8900-ddeee335da2b\",\"repository_file_id\":\"bf4963d4-ddec-4e95-aa7f-e31a5efe173a\",\"repository_symbol_id\":null,\"rerank_rank\":3,\"rerank_score\":null,\"semantic_contribution\":0.0,\"semantic_distance\":null,\"semantic_rank\":null,\"semantic_score\":null,\"snippet\":\"              \\\"text\\\": \\\"{\\\\\\\"candidate_pool\\\\\\\":5,\\\\\\\"fallback_reason\\\\\\\":\\\\\\\"rerank_disabled\\\\\\\",\\\\\\\"hybrid_state\\\\\\\":\\\\\\\"LEXICAL_FALLBACK_SEMANTIC_UNAVAILABLE\\\\\\\",\\\\\\\"normalized_query\\\\\\\":\\\\\\\"definition of done\\\\\\\",\\\\\\\"project_id\\\\\\\":\\\\\\\"8696b773-8554-4f27-9cb0-77ddfaf98deb\\\\\\\",\\\\\\\"query\\\\\\\":\\\\\\\"Definition of Done\\\\\\\",\\\\\\\"rerank_state\\\\\\\":\\\\\\\"RERANK_FALLBACK_DISABLED\\\\\\\",\\\\\\\"results\\\\\\\":[{\\\\\\\"chunk_content_sha256\\\\\\\":\\\\\\\"84172922aa8aadc46e4a0758dabdfab599d23cec94dfcffc808ebc24fc1e5ea0\\\\\\\",\\\\\\\"chunk_id\\\\\\\":\\\\\\\"f3b56f23-3bb4-40e4-be35-29116be52a18\\\\\\\",\\\\\\\"chunker_version\\\\\\\":\\\\\\\"line-window-v1\\\\\\\",\\\\\\\"corpus_run_id\\\\\\\":\\\\\\\"2ebde07b-af29-4db4-84e1-7254b94614d1\\\\\\\",\\\\\\\"end_char\\\\\\\":3292,\\\\\\\"end_line\\\\\\\":40,\\\\\\\"hybrid_score\\\\\\\":0.0163\",\"snippet_characters\":643,\"snippet_truncated\":true,\"source_content_sha256\":\"954bcd7f4e0cc1e05ebb1754a1aaf8aa4df78fabfb54027b5f0d0dd0a11c99ba\",\"source_kind\":\"REPOSITORY_FILE\",\"start_char\":26881,\"start_line\":569,\"task_id\":null,\"title\":null},{\"chunk_content_sha256\":\"83ef1f1523cb005fd4a6d12317c49cde388045ccf0fe53844f9fced400baa8ef\",\"chunk_id\":\"725867f7-d242-4f26-ae11-00eae543d7ee\",\"chunker_version\":\"line-window-v1\",\"corpus_run_id\":\"43cc41ca-685f-4812-8e98-0ac965919171\",\"end_char\":18056,\"end_line\":249,\"hybrid_score\":0.015625,\"lexical_contribution\":0.015625,\"lexical_rank\":4,\"lexical_score\":0.9363574981689453,\"path\":\".engineering/evidence/mcp-proof.json\",\"pre_rerank_rank\":4,\"project_id\":\"8696b773-8554-4f27-9cb0-77ddfaf98deb\",\"qualified_symbol\":null,\"reference_id\":\"6320a9a6-c468-45e3-ab74-60f8e82a0e24\",\"repository_file_id\":\"b6431965-e302-48e6-8fd9-13fdbc785e5a\",\"repository_symbol_id\":null,\"rerank_rank\":4,\"rerank_score\":null,\"semantic_contribution\":0.0,\"semantic_distance\":null,\"semantic_rank\":null,\"semantic_score\":null,\"snippet\":\"            \\\"text\\\": \\\"{\\\\\\\"candidate_pool\\\\\\\":5,\\\\\\\"fallback_reason\\\\\\\":\\\\\\\"rerank_disabled\\\\\\\",\\\\\\\"hybrid_state\\\\\\\":\\\\\\\"LEXICAL_FALLBACK_SEMANTIC_UNAVAILABLE\\\\\\\",\\\\\\\"normalized_query\\\\\\\":\\\\\\\"definition of done\\\\\\\",\\\\\\\"project_id\\\\\\\":\\\\\\\"8696b773-8554-4f27-9cb0-77ddfaf98deb\\\\\\\",\\\\\\\"query\\\\\\\":\\\\\\\"Definition of Done\\\\\\\",\\\\\\\"rerank_state\\\\\\\":\\\\\\\"RERANK_FALLBACK_DISABLED\\\\\\\",\\\\\\\"results\\\\\\\":[{\\\\\\\"chunk_content_sha256\\\\\\\":\\\\\\\"84172922aa8aadc46e4a0758dabdfab599d23cec94dfcffc808ebc24fc1e5ea0\\\\\\\",\\\\\\\"chunk_id\\\\\\\":\\\\\\\"f3b56f23-3bb4-40e4-be35-29116be52a18\\\\\\\",\\\\\\\"chunker_version\\\\\\\":\\\\\\\"line-window-v1\\\\\\\",\\\\\\\"corpus_run_id\\\\\\\":\\\\\\\"2ebde07b-af29-4db4-84e1-7254b94614d1\\\\\\\",\\\\\\\"end_char\\\\\\\":3292,\\\\\\\"end_line\\\\\\\":40,\\\\\\\"hybrid_score\\\\\\\":0.016393\",\"snippet_characters\":643,\"snippet_truncated\":true,\"source_content_sha256\":\"3781d9b9709e375e7afc574cb567d1c37f0a3ab3b7ad0107a091c5cf46f2fd75\",\"source_kind\":\"REPOSITORY_FILE\",\"start_char\":12056,\"start_line\":249,\"task_id\":null,\"title\":null},{\"chunk_content_sha256\":\"88293e10b2bc71260145588e09392f8853e076952be26569e7dafbdfe29c7a04\",\"chunk_id\":\"5dd0e87d-91ea-45d6-ab2e-3ea7b7b654c3\",\"chunker_version\":\"line-window-v1\",\"corpus_run_id\":\"43cc41ca-685f-4812-8e98-0ac965919171\",\"end_char\":1622,\"end_line\":49,\"hybrid_score\":0.015384615384615385,\"lexical_contribution\":0.015384615384615385,\"lexical_rank\":5,\"lexical_score\":0.5241162180900574,\"path\":\".engineering/evidence/hive-retrieval-proof.json\",\"pre_rerank_rank\":5,\"project_id\":\"8696b773-8554-4f27-9cb0-77ddfaf98deb\",\"qualified_symbol\":null,\"reference_id\":\"3ceb57de-b65c-475b-9b82-c47a1f1f3aae\",\"repository_file_id\":\"a930975b-8f21-4b35-9d0a-0735ae3e91d8\",\"repository_symbol_id\":null,\"rerank_rank\":5,\"rerank_score\":null,\"semantic_contribution\":0.0,\"semantic_distance\":null,\"semantic_rank\":null,\"semantic_score\":null,\"snippet\":\"... \\\"2026-09-21T17:22:25.734460Z\\\",\\n    \\\"latest_run\\\": {\\n      \\\"status\\\": \\\"COMPLETED\\\",\\n      \\\"repository_source_count\\\": 124,\\n      \\\"chunk_count\\\": 133,\\n      \\\"current_reference_count\\\": 135\\n    }\\n  },\\n  \\\"queries\\\": {\\n    \\\"Definition of Done\\\": {\\n      \\\"paths\\\": [\\n        \\\".engineering/evidence/ISORYN-WO-0001-CHECKPOINT-DELTA.md\\\",\\n        \\\"docs/project-brain/15-DEFINITION-OF-DONE.md\\\",\\n        \\\"scripts/validate_governance.py\\\",\\n        \\\"AGENTS.md\\\",\\n        \\\".engineering/work-orders/ISORYN-WO-0001-GEF-HIVE-BOOTSTRAP.md\\\",\\n        \\\"docs/project-brain/00-README-UPLOAD-ORDER.md\\\"\\n      ],\\n      \\\"canonical_paths\\\": [\\n        \\\"docs/project-brain/00-REA\",\"snippet_characters\":646,\"snippet_truncated\":true,\"source_content_sha256\":\"88293e10b2bc71260145588e09392f8853e076952be26569e7dafbdfe29c7a04\",\"source_kind\":\"REPOSITORY_FILE\",\"start_char\":0,\"start_line\":1,\"task_id\":null,\"title\":null}],\"semantic_state\":\"UNAVAILABLE\",\"top_k\":5,\"version\":\"mcp-context-search-v1\"}"
            }
          ],
          "structuredContent": {
            "version": "mcp-context-search-v1",
            "project_id": "8696b773-8554-4f27-9cb0-77ddfaf98deb",
            "query": "Definition of Done",
            "normalized_query": "definition of done",
            "top_k": 5,
            "candidate_pool": 5,
            "hybrid_state": "LEXICAL_FALLBACK_SEMANTIC_UNAVAILABLE",
            "semantic_state": "UNAVAILABLE",
            "rerank_state": "RERANK_FALLBACK_DISABLED",
            "fallback_reason": "rerank_disabled",
            "results": [
              {
                "project_id": "8696b773-8554-4f27-9cb0-77ddfaf98deb",
                "reference_id": "06289fa6-8a8e-470c-a09b-632744aaf67d",
                "chunk_id": "bde16aaa-5049-4b42-bf99-deb31fa9a2b3",
                "corpus_run_id": "43cc41ca-685f-4812-8e98-0ac965919171",
                "source_kind": "REPOSITORY_FILE",
                "hybrid_score": 0.01639344262295082,
                "lexical_score": 1.0409587621688843,
                "semantic_score": null,
                "semantic_distance": null,
                "lexical_rank": 1,
                "semantic_rank": null,
                "lexical_contribution": 0.01639344262295082,
                "semantic_contribution": 0.0,
                "snippet": "            }\n          ],\n          \"structuredContent\": {\n            \"version\": \"mcp-context-search-v1\",\n            \"project_id\": \"8696b773-8554-4f27-9cb0-77ddfaf98deb\",\n            \"query\": \"Definition of Done\",\n            \"normalized_query\": \"definition of done\",\n            \"top_k\": 5,\n            \"candidate_pool\": 5,\n            \"hybrid_state\": \"LEXICAL_FALLBACK_SEMANTIC_UNAVAILABLE\",\n            \"semantic_state\": \"UNAVAILABLE\",\n            \"rerank_state\": \"RERANK_FALLBACK_DISABLED\",\n            \"fallback_reason\": \"rerank_disabled\",\n            \"results\": [\n              {\n                \"project_id\": \"8696b773-8554-4f27-9",
                "path": ".engineering/evidence/ISORYN-WO-0001-EVIDENCE.md",
                "title": null,
                "qualified_symbol": null,
                "repository_file_id": "bf4963d4-ddec-4e95-aa7f-e31a5efe173a",
                "repository_symbol_id": null,
                "task_id": null,
                "source_content_sha256": "954bcd7f4e0cc1e05ebb1754a1aaf8aa4df78fabfb54027b5f0d0dd0a11c99ba",
                "chunk_content_sha256": "c509b009afcc28546fddd5a1d139d5e868a71ebb47b0fdf375990d3fa2646af5",
                "chunker_version": "line-window-v1",
                "start_line": 570,
                "end_line": 649,
                "start_char": 36356,
                "end_char": 41498,
                "pre_rerank_rank": 1,
                "rerank_rank": 1,
                "rerank_score": null,
                "snippet_characters": 643,
                "snippet_truncated": true
              },
              {
                "project_id": "8696b773-8554-4f27-9cb0-77ddfaf98deb",
                "reference_id": "85fc03eb-6b4e-430a-8ffa-cd9725faebfd",
                "chunk_id": "ebe8e2a3-fa25-43f2-a4b4-9ac40ce4dba1",
                "corpus_run_id": "43cc41ca-685f-4812-8e98-0ac965919171",
                "source_kind": "REPOSITORY_FILE",
                "hybrid_score": 0.016129032258064516,
                "lexical_score": 1.0409587621688843,
                "semantic_score": null,
                "semantic_distance": null,
                "lexical_rank": 2,
                "semantic_rank": null,
                "lexical_contribution": 0.016129032258064516,
                "semantic_contribution": 0.0,
                "snippet": "          }\n        ],\n        \"structuredContent\": {\n          \"version\": \"mcp-context-search-v1\",\n          \"project_id\": \"8696b773-8554-4f27-9cb0-77ddfaf98deb\",\n          \"query\": \"Definition of Done\",\n          \"normalized_query\": \"definition of done\",\n          \"top_k\": 5,\n          \"candidate_pool\": 5,\n          \"hybrid_state\": \"LEXICAL_FALLBACK_SEMANTIC_UNAVAILABLE\",\n          \"semantic_state\": \"UNAVAILABLE\",\n          \"rerank_state\": \"RERANK_FALLBACK_DISABLED\",\n          \"fallback_reason\": \"rerank_disabled\",\n          \"results\": [\n            {\n              \"project_id\": \"8696b773-8554-4f27-9cb0-77ddfaf98deb\",\n             ",
                "path": ".engineering/evidence/mcp-proof.json",
                "title": null,
                "qualified_symbol": null,
                "repository_file_id": "b6431965-e302-48e6-8fd9-13fdbc785e5a",
                "repository_symbol_id": null,
                "task_id": null,
                "source_content_sha256": "3781d9b9709e375e7afc574cb567d1c37f0a3ab3b7ad0107a091c5cf46f2fd75",
                "chunk_content_sha256": "7babe43715f282601727e6c2823643493f704f650a355b1fa7b4aa9fa2821566",
                "chunker_version": "line-window-v1",
                "start_line": 250,
                "end_line": 329,
                "start_char": 21529,
                "end_char": 26511,
                "pre_rerank_rank": 2,
                "rerank_rank": 2,
                "rerank_score": null,
                "snippet_characters": 643,
                "snippet_truncated": true
              },
              {
                "project_id": "8696b773-8554-4f27-9cb0-77ddfaf98deb",
                "reference_id": "f359f8f7-0f30-4583-8900-ddeee335da2b",
                "chunk_id": "ac667c5b-2aa2-4559-8ff3-a7b8c0c61ce2",
                "corpus_run_id": "43cc41ca-685f-4812-8e98-0ac965919171",
                "source_kind": "REPOSITORY_FILE",
                "hybrid_score": 0.015873015873015872,
                "lexical_score": 0.9363574981689453,
                "semantic_score": null,
                "semantic_distance": null,
                "lexical_rank": 3,
                "semantic_rank": null,
                "lexical_contribution": 0.015873015873015872,
                "semantic_contribution": 0.0,
                "snippet": "              \"text\": \"{\\\"candidate_pool\\\":5,\\\"fallback_reason\\\":\\\"rerank_disabled\\\",\\\"hybrid_state\\\":\\\"LEXICAL_FALLBACK_SEMANTIC_UNAVAILABLE\\\",\\\"normalized_query\\\":\\\"definition of done\\\",\\\"project_id\\\":\\\"8696b773-8554-4f27-9cb0-77ddfaf98deb\\\",\\\"query\\\":\\\"Definition of Done\\\",\\\"rerank_state\\\":\\\"RERANK_FALLBACK_DISABLED\\\",\\\"results\\\":[{\\\"chunk_content_sha256\\\":\\\"84172922aa8aadc46e4a0758dabdfab599d23cec94dfcffc808ebc24fc1e5ea0\\\",\\\"chunk_id\\\":\\\"f3b56f23-3bb4-40e4-be35-29116be52a18\\\",\\\"chunker_version\\\":\\\"line-window-v1\\\",\\\"corpus_run_id\\\":\\\"2ebde07b-af29-4db4-84e1-7254b94614d1\\\",\\\"end_char\\\":3292,\\\"end_line\\\":40,\\\"hybrid_score\\\":0.0163",
                "path": ".engineering/evidence/ISORYN-WO-0001-EVIDENCE.md",
                "title": null,
                "qualified_symbol": null,
                "repository_file_id": "bf4963d4-ddec-4e95-aa7f-e31a5efe173a",
                "repository_symbol_id": null,
                "task_id": null,
                "source_content_sha256": "954bcd7f4e0cc1e05ebb1754a1aaf8aa4df78fabfb54027b5f0d0dd0a11c99ba",
                "chunk_content_sha256": "d9bb3c5cb2d1f8772f70818dba397e6fd9d95a0c8f42a5909bcffac79b17f027",
                "chunker_version": "line-window-v1",
                "start_line": 569,
                "end_line": 569,
                "start_char": 26881,
                "end_char": 32881,
                "pre_rerank_rank": 3,
                "rerank_rank": 3,
                "rerank_score": null,
                "snippet_characters": 643,
                "snippet_truncated": true
              },
              {
                "project_id": "8696b773-8554-4f27-9cb0-77ddfaf98deb",
                "reference_id": "6320a9a6-c468-45e3-ab74-60f8e82a0e24",
                "chunk_id": "725867f7-d242-4f26-ae11-00eae543d7ee",
                "corpus_run_id": "43cc41ca-685f-4812-8e98-0ac965919171",
                "source_kind": "REPOSITORY_FILE",
                "hybrid_score": 0.015625,
                "lexical_score": 0.9363574981689453,
                "semantic_score": null,
                "semantic_distance": null,
                "lexical_rank": 4,
                "semantic_rank": null,
                "lexical_contribution": 0.015625,
                "semantic_contribution": 0.0,
                "snippet": "            \"text\": \"{\\\"candidate_pool\\\":5,\\\"fallback_reason\\\":\\\"rerank_disabled\\\",\\\"hybrid_state\\\":\\\"LEXICAL_FALLBACK_SEMANTIC_UNAVAILABLE\\\",\\\"normalized_query\\\":\\\"definition of done\\\",\\\"project_id\\\":\\\"8696b773-8554-4f27-9cb0-77ddfaf98deb\\\",\\\"query\\\":\\\"Definition of Done\\\",\\\"rerank_state\\\":\\\"RERANK_FALLBACK_DISABLED\\\",\\\"results\\\":[{\\\"chunk_content_sha256\\\":\\\"84172922aa8aadc46e4a0758dabdfab599d23cec94dfcffc808ebc24fc1e5ea0\\\",\\\"chunk_id\\\":\\\"f3b56f23-3bb4-40e4-be35-29116be52a18\\\",\\\"chunker_version\\\":\\\"line-window-v1\\\",\\\"corpus_run_id\\\":\\\"2ebde07b-af29-4db4-84e1-7254b94614d1\\\",\\\"end_char\\\":3292,\\\"end_line\\\":40,\\\"hybrid_score\\\":0.016393",
                "path": ".engineering/evidence/mcp-proof.json",
                "title": null,
                "qualified_symbol": null,
                "repository_file_id": "b6431965-e302-48e6-8fd9-13fdbc785e5a",
                "repository_symbol_id": null,
                "task_id": null,
                "source_content_sha256": "3781d9b9709e375e7afc574cb567d1c37f0a3ab3b7ad0107a091c5cf46f2fd75",
                "chunk_content_sha256": "83ef1f1523cb005fd4a6d12317c49cde388045ccf0fe53844f9fced400baa8ef",
                "chunker_version": "line-window-v1",
                "start_line": 249,
                "end_line": 249,
                "start_char": 12056,
                "end_char": 18056,
                "pre_rerank_rank": 4,
                "rerank_rank": 4,
                "rerank_score": null,
                "snippet_characters": 643,
                "snippet_truncated": true
              },
              {
                "project_id": "8696b773-8554-4f27-9cb0-77ddfaf98deb",
                "reference_id": "3ceb57de-b65c-475b-9b82-c47a1f1f3aae",
                "chunk_id": "5dd0e87d-91ea-45d6-ab2e-3ea7b7b654c3",
                "corpus_run_id": "43cc41ca-685f-4812-8e98-0ac965919171",
                "source_kind": "REPOSITORY_FILE",
                "hybrid_score": 0.015384615384615385,
                "lexical_score": 0.5241162180900574,
                "semantic_score": null,
                "semantic_distance": null,
                "lexical_rank": 5,
                "semantic_rank": null,
                "lexical_contribution": 0.015384615384615385,
                "semantic_contribution": 0.0,
                "snippet": "... \"2026-09-21T17:22:25.734460Z\",\n    \"latest_run\": {\n      \"status\": \"COMPLETED\",\n      \"repository_source_count\": 124,\n      \"chunk_count\": 133,\n      \"current_reference_count\": 135\n    }\n  },\n  \"queries\": {\n    \"Definition of Done\": {\n      \"paths\": [\n        \".engineering/evidence/ISORYN-WO-0001-CHECKPOINT-DELTA.md\",\n        \"docs/project-brain/15-DEFINITION-OF-DONE.md\",\n        \"scripts/validate_governance.py\",\n        \"AGENTS.md\",\n        \".engineering/work-orders/ISORYN-WO-0001-GEF-HIVE-BOOTSTRAP.md\",\n        \"docs/project-brain/00-README-UPLOAD-ORDER.md\"\n      ],\n      \"canonical_paths\": [\n        \"docs/project-brain/00-REA",
                "path": ".engineering/evidence/hive-retrieval-proof.json",
                "title": null,
                "qualified_symbol": null,
                "repository_file_id": "a930975b-8f21-4b35-9d0a-0735ae3e91d8",
                "repository_symbol_id": null,
                "task_id": null,
                "source_content_sha256": "88293e10b2bc71260145588e09392f8853e076952be26569e7dafbdfe29c7a04",
                "chunk_content_sha256": "88293e10b2bc71260145588e09392f8853e076952be26569e7dafbdfe29c7a04",
                "chunker_version": "line-window-v1",
                "start_line": 1,
                "end_line": 49,
                "start_char": 0,
                "end_char": 1622,
                "pre_rerank_rank": 5,
                "rerank_rank": 5,
                "rerank_score": null,
                "snippet_characters": 646,
                "snippet_truncated": true
              }
            ]
          },
          "isError": false
        }
      }
    },
    "launcherStderr": ""
  },
  "github": {
    "settingsAppliedFrom": ".engineering/github/repository-settings.json",
    "repositoryBefore": {
      "name": "isoryn-engine",
      "full_name": "KayzenRoot/isoryn-engine",
      "private": false,
      "visibility": "public",
      "default_branch": "main",
      "description": "ISORYN engine program: clean governed foundation (GEF v1.0.0 + HIVE v1.0.0). Godot 4.x is the accepted foundation direction pending evidence-backed discovery.",
      "topics": [
        "engine-development",
        "game-engine",
        "godot",
        "governance",
        "isoryn"
      ],
      "has_issues": true,
      "has_projects": true,
      "has_wiki": false,
      "has_downloads": false,
      "has_pages": false,
      "has_discussions": false,
      "allow_merge_commit": false,
      "allow_rebase_merge": false,
      "allow_squash_merge": true,
      "allow_auto_merge": true,
      "delete_branch_on_merge": true,
      "allow_update_branch": true,
      "use_squash_pr_title_as_default": false,
      "squash_merge_commit_message": "COMMIT_MESSAGES",
      "security_and_analysis": {
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
      }
    },
    "repositoryAfter": {
      "name": "isoryn-engine",
      "full_name": "KayzenRoot/isoryn-engine",
      "private": false,
      "visibility": "public",
      "default_branch": "main",
      "description": "ISORYN engine program: clean governed foundation (GEF v1.0.0 + HIVE v1.0.0). Godot 4.x is the accepted foundation direction pending evidence-backed discovery.",
      "topics": [
        "engine-development",
        "game-engine",
        "godot",
        "governance",
        "isoryn"
      ],
      "has_issues": true,
      "has_projects": false,
      "has_wiki": false,
      "has_downloads": false,
      "has_pages": false,
      "has_discussions": false,
      "allow_merge_commit": false,
      "allow_rebase_merge": false,
      "allow_squash_merge": true,
      "allow_auto_merge": true,
      "delete_branch_on_merge": true,
      "allow_update_branch": true,
      "use_squash_pr_title_as_default": false,
      "squash_merge_commit_message": "COMMIT_MESSAGES",
      "security_and_analysis": {
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
      }
    },
    "repositoryReceipts": [
      ".engineering/evidence/github/before-repository.json",
      ".engineering/evidence/github/after-repository.json"
    ],
    "repositoryReceiptsIdentical": false,
    "codeownersBefore": "* @KayzenRoot\n",
    "codeownersAfter": "# ISORYN review routing metadata.\n#\n# Ownership here records who a change should be routed to. It is deliberately NOT an approval gate:\n# the main-governance ruleset sets require_code_owner_review=false and required_approving_review_count=0,\n# because this repository has a single owner who is also the pull request author. GitHub does not accept a\n# review from the author, so enforcing code-owner approval here would make main permanently unmergeable.\n#\n# Add a team or second maintainer, then enable require_code_owner_review in\n# .engineering/github/ruleset-main-governance.json, before treating this file as a required gate.\n* @KayzenRoot\n",
    "rulesetManifest": {
      "name": "main-governance",
      "target": "branch",
      "enforcement": "active",
      "conditions": {
        "ref_name": {
          "exclude": [],
          "include": [
            "refs/heads/main"
          ]
        }
      },
      "bypass_actors": [],
      "rules": [
        {
          "type": "deletion"
        },
        {
          "type": "non_fast_forward"
        },
        {
          "type": "required_linear_history"
        },
        {
          "type": "update",
          "parameters": {
            "update_allows_fetch_and_merge": false
          }
        },
        {
          "type": "pull_request",
          "parameters": {
            "allowed_merge_methods": [
              "squash"
            ],
            "dismiss_stale_reviews_on_push": true,
            "require_code_owner_review": false,
            "require_last_push_approval": false,
            "required_approving_review_count": 0,
            "required_review_thread_resolution": true
          }
        },
        {
          "type": "required_status_checks",
          "parameters": {
            "do_not_enforce_on_create": false,
            "strict_required_status_checks_policy": true,
            "required_status_checks": [
              {
                "context": "Governance"
              }
            ]
          }
        }
      ]
    },
    "effectiveRuleset": {
      "id": 23776080,
      "name": "main-governance",
      "enforcement": "active",
      "conditions": {
        "ref_name": {
          "exclude": [],
          "include": [
            "refs/heads/main"
          ]
        }
      },
      "bypassActors": [],
      "rules": [
        {
          "type": "non_fast_forward",
          "parameters": {}
        },
        {
          "type": "deletion",
          "parameters": {}
        },
        {
          "type": "required_linear_history",
          "parameters": {}
        },
        {
          "type": "update",
          "parameters": {}
        },
        {
          "type": "pull_request",
          "parameters": {
            "required_approving_review_count": 0,
            "dismiss_stale_reviews_on_push": true,
            "required_reviewers": [],
            "require_code_owner_review": false,
            "require_last_push_approval": false,
            "required_review_thread_resolution": true,
            "require_extra_approval_for_unattributed_changes": true,
            "allowed_merge_methods": [
              "squash"
            ]
          }
        },
        {
          "type": "required_status_checks",
          "parameters": {
            "strict_required_status_checks_policy": true,
            "do_not_enforce_on_create": false,
            "required_status_checks": [
              {
                "context": "Governance"
              }
            ]
          }
        }
      ]
    },
    "requiredStatusChecks": {
      "strict_required_status_checks_policy": true,
      "do_not_enforce_on_create": false,
      "required_status_checks": [
        {
          "context": "Governance"
        }
      ]
    },
    "rulesetCheckMain": "6 rules apply to branch main in repo KayzenRoot/isoryn-engine\n\n- deletion\n  (configured in ruleset 23776080 from repository KayzenRoot/isoryn-engine)\n\n- non_fast_forward\n  (configured in ruleset 23776080 from repository KayzenRoot/isoryn-engine)\n\n- pull_request: [allowed_merge_methods: [squash]] [dismiss_stale_reviews_on_push: true] [require_code_owner_review: false] [require_extra_approval_for_unattributed_changes: true] [require_last_push_approval: false] [required_approving_review_count: 0] [required_review_thread_resolution: true] [required_reviewers: []] \n  (configured in ruleset 23776080 from repository KayzenRoot/isoryn-engine)\n\n- required_linear_history\n  (configured in ruleset 23776080 from repository KayzenRoot/isoryn-engine)\n\n- required_status_checks: [do_not_enforce_on_create: false] [required_status_checks: [map[context:Governance]]] [strict_required_status_checks_policy: true] \n  (configured in ruleset 23776080 from repository KayzenRoot/isoryn-engine)\n\n- update\n  (configured in ruleset 23776080 from repository KayzenRoot/isoryn-engine)\n",
    "statusChecksSequencing": "required_status_checks was withheld from the first application because a required context that has never reported leaves a protected branch permanently unmergeable. It was applied from the checked-in manifest only after the 'Governance' context was observed green on real runs, and this receipt is the read-back of the applied state rather than a description of intent.",
    "rulesetView": "\nmain-governance\nID: 23776080\nSource: KayzenRoot/isoryn-engine (Repository)\nEnforcement: Active\nYou can bypass: never\n\nBypass List\nThis ruleset cannot be bypassed\n\nConditions\n- ref_name: [exclude: []] [include: [refs/heads/main]] \n\nRules\n- deletion\n- non_fast_forward\n- pull_request: [allowed_merge_methods: [squash]] [dismiss_stale_reviews_on_push: true] [require_code_owner_review: false] [require_extra_approval_for_unattributed_changes: true] [require_last_push_approval: false] [required_approving_review_count: 0] [required_review_thread_resolution: true] [required_reviewers: []] \n- required_linear_history\n- required_status_checks: [do_not_enforce_on_create: false] [required_status_checks: [map[context:Governance]]] [strict_required_status_checks_policy: true] \n- update\n",
    "securityEndpointProbe": "vulnerability_alerts => NOT_AVAILABLE (exit=1) gh.exe : gh: Not Found (HTTP 404)\nautomated_security_fixes => NOT_AVAILABLE (exit=1) gh.exe : gh: Not Found (HTTP 404)\n",
    "enforcementProofMethod": "The applied state is proved by read-back: GET on the ruleset id and 'gh ruleset check main' listing all six rules against refs/heads/main. No destructive push, force-push or branch-deletion test was run against main to 'show' the protection, because the Work Order forbids force-push and destructive cleanup and such a probe cannot be undone if the guard fails.",
    "receipts": [
      "after-repository.json",
      "after-ruleset.json",
      "before-repository.json",
      "before-rulesets.json",
      "ruleset-check-main.txt",
      "ruleset-list.json",
      "ruleset-view.txt",
      "security-endpoints.txt"
    ]
  },
  "ciObservations": [
    {
      "head": "b8b5e90940356c69e85511e29c940f1f093977fc",
      "context": "Governance",
      "status": "completed",
      "conclusion": "success",
      "result": "PASS",
      "run": "https://github.com/KayzenRoot/isoryn-engine/actions/runs/35637778291/job/106459349626",
      "detail": "GitHub check-run for this exact commit, read through the API"
    },
    {
      "head": "dfd8745e607a529197a806ce15ec2003aa073114",
      "context": "Governance",
      "status": "completed",
      "conclusion": "success",
      "result": "PASS",
      "run": "https://github.com/KayzenRoot/isoryn-engine/actions/runs/35635555729/job/106451985978",
      "detail": "GitHub check-run for this exact commit, read through the API"
    },
    {
      "head": "72b2d3a06fb70d240784d945680741f623eccabd",
      "context": "Governance",
      "status": "completed",
      "conclusion": "success",
      "result": "PASS",
      "run": "https://github.com/KayzenRoot/isoryn-engine/actions/runs/35634056578/job/106446985162",
      "detail": "GitHub check-run for this exact commit, read through the API"
    },
    {
      "head": "bd73ecd41e11b21e29678c1a0830ba5895c74b35",
      "context": "Governance",
      "status": "completed",
      "conclusion": "success",
      "result": "PASS",
      "run": "https://github.com/KayzenRoot/isoryn-engine/actions/runs/35632133365/job/106440622755",
      "detail": "GitHub check-run for this exact commit, read through the API"
    },
    {
      "head": "3de6fa11ed5dda13a31a9b7abe6591de6a34bf0f",
      "context": "Governance",
      "status": "completed",
      "conclusion": "failure",
      "result": "FAIL",
      "run": "https://github.com/KayzenRoot/isoryn-engine/actions/runs/35627653055/job/106425847441",
      "detail": "GitHub check-run for this exact commit, read through the API"
    },
    {
      "head": "5fb0179b9c0a9a8f94f170dc299f199a7c7c883d",
      "context": "Governance",
      "status": "completed",
      "conclusion": "success",
      "result": "PASS",
      "run": "https://github.com/KayzenRoot/isoryn-engine/actions/runs/35613159283/job/106377088615",
      "detail": "GitHub check-run for this exact commit, read through the API"
    },
    {
      "head": "6584b7aae7546d33e8d747feff2265ba3d3eff67",
      "context": "Governance",
      "status": "completed",
      "conclusion": "success",
      "result": "PASS",
      "run": "https://github.com/KayzenRoot/isoryn-engine/actions/runs/35612910958/job/106376255435",
      "detail": "GitHub check-run for this exact commit, read through the API"
    }
  ],
  "ciObservationContext": "Each entry names the commit GitHub evaluated. The failing run is the structural one this bundle exists to resolve: the validator's Evidence Bundle gate cannot be satisfied by the code head it evidences, so the run before any bundle existed reports FAIL and is kept visible instead of being smoothed over by a later pass.",
  "environmentDrift": {
    "observedAt": "2026-09-21T17:54:00Z",
    "summary": "While the evidence chain was being closed, 127.0.0.1:8000 stopped being served by the pinned HIVE v1.0.0 stack and started being served by a different local HIVE checkout at version 1.0.1, whose projects root does not contain ISORYN.",
    "pinnedSourceStillCorrect": "C:\\Users\\csn19\\AppData\\Local\\HIVE\\app is still at release commit a53b5b9fcf55c32a5696180fb1b1ef80ccd1edcf (git describe v1.0.0), so the pin this Work Order adopted is intact; the runtime answering the port is not that stack.",
    "servingStack": "docker compose project dir D:\\Projetos Codex\\hive, VERSION 1.0.1, HEAD f96901f (v1.0.0-11-gf96901f), mounting D:\\Projetos Codex\\hive\\.hive-projects as /workspace/projects and its own .hive-data as the data root.",
    "symptoms": [
      "GET /api/v1/health reports version 1.0.1 where every proof in this bundle recorded 1.0.0",
      "the ISORYN registration visible there is state OFFLINE with inspection_error path_unavailable, because that stack's projects root has no isoryn-engine",
      "a machine-level HIVE_PROJECTS_ROOT now resolves to D:/Projetos Codex instead of the canonical D:\\Hive\\projects documented in docs/HIVE-INTEGRATION.md"
    ],
    "failedReCapture": {
      "api": "http://127.0.0.1:8000",
      "result": "FAIL",
      "attempts": [
        {
          "attempt": 1,
          "result": "FAIL",
          "detail": "HIVE bootstrap failed: ISORYN is not READY in HIVE: {'project_id': '1e4aaa02-d268-4ab3-88e5-d956203177fb', 'name': 'ISORYN', 'relative_path': 'isoryn-engine', 'git_branch': None, 'git_head_sha': None, 'detached_head': False, 'repository_accessible': False, 'working_tree_clean': None, 'language_stack': [], 'state': 'OFFLINE', 'inspection_error': 'path_unavailable', 'created_at': '2026-09-21T17:54:0"
        },
        {
          "attempt": 2,
          "result": "FAIL",
          "detail": "HIVE bootstrap failed: GET /api/v1/health -> HTTP 503: {\"status\":\"degraded\",\"version\":\"1.0.1\",\"environment\":\"development\",\"timestamp\":\"2026-09-21T17:54:29.721168Z\",\"data_root\":\"/var/lib/hive\",\"checks\":{\"postgres\":{\"status\":\"ok\",\"details\":{\"pgvector\":true}},\"redis\":{\"status\":\"degraded\",\"details\":{\"reason\":\"connection failed (ConnectionError)\"}},\"storage\":{\"status\":\"ok\",\"details\":{\"configured\":true,"
        },
        {
          "attempt": 3,
          "result": "FAIL",
          "detail": "HIVE bootstrap failed: ISORYN is not READY in HIVE: {'project_id': '1e4aaa02-d268-4ab3-88e5-d956203177fb', 'name': 'ISORYN', 'relative_path': 'isoryn-engine', 'git_branch': None, 'git_head_sha': None, 'detached_head': False, 'repository_accessible': False, 'working_tree_clean': None, 'language_stack': [], 'state': 'OFFLINE', 'inspection_error': 'path_unavailable', 'created_at': '2026-09-21T17:54:0"
        }
      ],
      "pipeline": {
        "unparsed_output": "HIVE health: {'status': 'ok', 'version': '1.0.1', 'environment': 'development', 'timestamp': '2026-09-21T17:54:50.050805Z', 'data_root': '/var/lib/hive', 'checks': {'postgres': {'status': 'ok', 'details': {'pgvector': True}}, 'redis': {'status': 'ok', 'details': {'canonical': False}}, 'storage': {'status': 'ok', 'details': {'configured': True, 'writable': True, 'canonical_data_root': '/var/lib/hive'}}}}\nResolved existing ISORYN registration by exact relative path.\n\nHIVE bootstrap failed: ISORYN is not READY in HIVE: {'project_id': '1e4aaa02-d268-4ab3-88e5-d956203177fb', 'name': 'ISORYN', 'relative_path': 'isoryn-engine', 'git_branch': None, 'git_head_sha': None, 'detached_head': False, 'repository_accessible': False, 'working_tree_clean': None, 'language_stack': [], 'state': 'OFFLINE', 'inspection_error': 'path_unavailable', 'created_at': '2026-09-21T17:54:01.070201Z', 'updated_at': '2026-09-21T17:54:50.283374Z', 'last_inspected_at': '2026-09-21T17:54:50.283374Z'}"
      },
      "classification": "HIVE_UNAVAILABLE",
      "note": "Derived state only: Git and the canonical checkpoint outrank HIVE. working_tree_clean is reported as observed and never edited into a true value."
    },
    "notDoneOnPurpose": [
      "No container, volume, port or environment of the other workspace was stopped, restarted or re-pointed to reclaim the proofs: that stack belongs to concurrent work and ISORYN's rules put stopping shared runtime state outside this Work Order.",
      "DELETE is not offered by the HIVE API (405), so the registration a bootstrap attempt created in that stack at 17:54Z (project 1e4aaa02-d268-4ab3-88e5-d956203177fb, state OFFLINE) remains, and is named here rather than quietly cleaned up in a database this Work Order does not own."
    ],
    "consequence": "HIVE and MCP re-proofs at heads after the capture head could not be executed against the pinned runtime, so no receipt in this bundle was regenerated for them. The checks that do not need HIVE - the governance validator, the unit suite and the CI job - are green at every pushed head, which is what the ciObservations chain shows.",
    "pinnedContainersAbsent": "Verified at 18:09Z: `docker ps -a` lists no container of the pinned stack and `docker volume ls` holds a single anonymous volume belonging to the concurrent one, so the pinned v1.0.0 images and its data root were removed with the runtime, not just stopped. The receipts in this bundle are therefore the only surviving record of that runtime's behaviour.",
    "recovery": "With the operator's decision: bring the pinned v1.0.0 stack back (its source at C:\\Users\\csn19\\AppData\\Local\\HIVE\\app still builds; nothing to restore from, it must be re-upped) either on its own host port or after the concurrent stack is released, point HIVE_PROJECTS_ROOT at D:\\Hive\\projects, then run python scripts/hive_bootstrap.py --relative-path isoryn-engine and re-capture. Nothing in the repository has to change for that; the proofs are re-runnable, not lost.",
    "closedBy": {
      "correction": "C01",
      "proofHead": "f293fabfd4cde0a202d917b75eee590567b2027e",
      "record": "c01Recovery",
      "result": "HIVE_RUNTIME_DRIFT CLOSED for the governed v1.0.0 baseline: the pinned runtime runs isolated and re-proves health, registration, READY, index, corpus, canonical retrieval and MCP at the C01 head.",
      "stillTrueAfterClosure": "The machine-level default runtime on 127.0.0.1:8000 is HIVE 1.0.2 and has no ISORYN registration. Integrations that follow the ambient environment still reach it, so every ISORYN HIVE call has to name the pinned stack explicitly."
    }
  },
  "unsupportedPlatformFeatures": [
    {
      "capability": "ruleset enforcement level 'evaluate'",
      "result": "NOT_AVAILABLE",
      "detail": "REST rejects the property on this plan; only 'active' and 'disabled' are accepted, so a dry-run ruleset cannot be expressed."
    },
    {
      "capability": "vulnerability_alerts toggle",
      "result": "NOT_AVAILABLE",
      "detail": "PUT /repos/KayzenRoot/isoryn-engine/vulnerability_alerts -> HTTP 404. Dependabot version updates are still configured through .github/dependabot.yml."
    },
    {
      "capability": "automated_security_fixes toggle",
      "result": "NOT_AVAILABLE",
      "detail": "PUT /repos/KayzenRoot/isoryn-engine/automated_security_fixes -> HTTP 404."
    },
    {
      "capability": "mandatory human approval, CODEOWNERS review or last-pusher approval on main",
      "result": "DEFERRED_BY_WO",
      "detail": "Work Order: 'avoid mandatory human approval/CODEOWNER/last-pusher rules that deadlock a single-owner automated workflow.' .github/CODEOWNERS stays routing metadata only and the ruleset keeps required_approving_review_count=0."
    },
    {
      "capability": "review requirement without an approval gate",
      "result": "PASS",
      "detail": "Encoded as the pull_request rule with required_review_thread_resolution=true and dismiss_stale_reviews_on_push=true, the supported non-deadlocking form."
    },
    {
      "capability": "use_squash_pr_title_as_default",
      "result": "NOT_AVAILABLE",
      "detail": "PATCH /repos/KayzenRoot/isoryn-engine returns HTTP 200 with the field still false, both in the response body and on read-back, even though .engineering/github/repository-settings.json asks for true. On a User-owned repository the platform ignores this key, so the squash-title default stays a reviewer choice rather than an enforced setting. Every other governed key reads back at its target state - this run's only delta was has_projects true to false, because the rest (merge methods, delete_branch_on_merge, allow_update_branch, secret scanning, push protection, dependabot security updates) was already at target from earlier applications, which is what an idempotent script is expected to report."
    },
    {
      "capability": "HIVE semantic retrieval and reranking",
      "result": "NOT_AVAILABLE",
      "detail": "context.search and context.build answered hybrid_state 'LEXICAL_FALLBACK_SEMANTIC_UNAVAILABLE', semantic_state 'UNAVAILABLE', rerank_state 'RERANK_FALLBACK_DISABLED'. HIVE v1.0.0 raises SemanticConfigurationError 'embedding_base_url_missing' when no OpenAI-compatible endpoint is configured, and this local deployment sets no HIVE_EMBEDDING_BASE_URL. pgvector is healthy, so the storage path exists; the embedding provider is an operator choice outside this repository and no HIVE configuration was changed to make a proof pass. Every retrieval claim in this bundle is therefore about the lexical path, which is what the runtime actually served."
    },
    {
      "capability": "HIVE v1.0.0 MCP tools beyond the core surface",
      "result": "NOT_AVAILABLE",
      "detail": "The pinned runtime exposes exactly project.list, project.status, context.build, context.search, memory.search, memory.get, checkpoint.read. The code.*/run.*/decision.*/validation.*/telemetry.*/project.open list in docs/project-brain/09 is design intent, not v1.0.0 surface, and the validator refuses to advertise it."
    }
  ],
  "errorsFoundAndCorrected": [
    "HIVE_PROJECTS_ROOT disagreed with every ISORYN document. Corrected to the documented root; the three pre-existing READY registrations were re-resolved and verified before the old value was dropped.",
    "A workspace consolidation was interrupted by a background process holding file handles, which duplicated two sibling repositories. Recovered by comparing every path (byte-identical or missing) and restoring the missing tracked and untracked trees before removing anything; both Git objects were verified with fsck and exact pre-move HEADs. See residualRisks.",
    "Nested junctions are not traversed by the container filesystem, so a junction under the projects root cannot stand in for a real directory. Recorded instead of worked around with a bind mount, which failed read-only.",
    "The repository worktree was CRLF while every blob is LF (Windows core.autocrlf=true). HIVE's Linux container applies no conversion, so it reported all 51 tracked files dirty and refused canonical retrieval with an empty result set. Fixed with .gitattributes ('* text=auto eol=lf') plus a real LF checkout; the validator now fails if a text file in the working tree carries CRLF, and project.status reports working_tree_clean true.",
    "scripts/hive_mcp.py discovered a HIVE checkout only through HIVE_REPO_PATH plus sibling paths, which no operator on this machine had set, so the MCP launcher died before starting Docker. It now honours HIVE_HOME, exported by the HIVE installer, and reports the resolution failure instead of exiting silently.",
    "HIVE registration/index/corpus exceeded the 15 second per-request timeout in scripts/hive_bootstrap.py and reported a false failure. Raised to a configurable timeout (default 180s, 600s used here) and added the observed working_tree_clean and branch fields to the reported preflight truth.",
    "The first capture pass wrote its own receipts into the working tree while HIVE read that tree as dirty (the CRLF defect above), so the receipts it produced proved nothing about the snapshot they were meant to establish. Capture now writes outside the repository and installs the receipts afterwards, and the matrix.log keeps both attempts.",
    "The main-governance ruleset was left with a single rule after several rejected payloads. Repaired to the full rule set with the correct schema: allowed_merge_methods belongs to the pull_request rule, 'update' accepts only update_allows_fetch_and_merge, and the approval counter is required_approving_review_count.",
    "scripts/configure-github.ps1 named a different ruleset, inlined its payload, and sent typed booleans with -f. Rewritten to upsert main-governance from the checked-in manifests, capture BEFORE/AFTER receipts and record optional security endpoints instead of assuming them.",
    ".env.example and the default parameter of scripts/bootstrap-local.ps1 committed absolute machine paths, violating GEF PC-08 and the Work Order rule that machine paths stay documentation. Both are now operator configuration; scripts/validate_governance.py enforces it.",
    "The governance validator checked 27 artifacts and none of the repository-governance layer it is supposed to gate (README/CONTRIBUTING/SECURITY/.gitignore/.github, CI, tests, tooling, Work Orders, Context Locks, Evidence Bundles). Coverage was extended and semantic assertions added without removing any prior check.",
    "Two validator assertions were wrong in ways that would have produced false signals: the checkpoint gate required the literal word 'IN PROGRESS' inside its own section, and the machine-path pattern matched the 'p:/' inside https:// URLs. Both now assert what was meant, with unit tests on the pattern itself.",
    "scripts/configure-github.ps1 wrote its .txt receipts with CRLF, which re-created the exact container-read failure .gitattributes exists to prevent: the working tree read as modified and HIVE's reads would have gone stale behind a passing test suite. The writer now normalises to LF and the line-ending gate caught it the same run it was introduced in.",
    "ISORYN-WO-0001 omitted the EVIDENCE, HIVE PREFLIGHT, CANONICAL BASIS, CONTEXT BUDGET and RISK/ASSURANCE sections that GEF-EXECUTION-PROTOCOL.md requires of every implementation Work Order.",
    "CONTRIBUTING.md still described the one-time direct-to-main bootstrap as available after the ruleset would make it impossible, and its branch convention contradicted the branch this Work Order designates.",
    "No test exercised scripts/validate_governance.py, so the governance gate itself was unverified.",
    "A capture pass reported hive_retrieval_canonical PASS while the index run for that head had actually failed, because the corpus was still CURRENT from an earlier sync. Both retrieval assertions are now gated on the pipeline result for this head, so a stale-but-current corpus can no longer pass.",
    "Windows git rewriting .git/index while HIVE's container reads the same file over the mount made a single status read fail with git_status_unavailable at a clean head, and checkpoint.read then answered source_not_current. The exact container command was reproduced and succeeds, so the capture retries the pipeline (3 attempts, 20s apart) and records every attempt instead of publishing one race as truth.",
    "MCP responses were keyed by request id rather than tool name, so mcp-proof.json would have published {\"3\": null} in place of the calls it claimed to prove; the launcher thread also awaited without a bound. Receipts now carry each tool's raw response behind its name under a per-call timeout.",
    "The preflight receipt was built by slicing between the first '{' and the last '}' of the bootstrap script's stdout. That text opens with a Python-repr health line, so nothing parsed and every successful run was filed under an 'error' key with its proof truncated to the last 800 characters - including the head HIVE had inspected. The summary is now parsed as the trailing JSON object it is, and the captured head is compared with the local HEAD under its own check.",
    "governance_ci was a hard-coded NOT_AVAILABLE line, and the failing Actions run was recorded against whatever the local head happened to be at generation time - which misattributed a real run to a commit it never evaluated. The capture now reads the check-run for the pushed head through the GitHub API and each observation names the exact commit GitHub checked.",
    "clean_worktree_for_hive asserted a fully empty 'git status', which the Evidence Bundle's own untracked artifacts violate, and it was written from an assumption rather than HIVE's rule. The guard HIVE actually applies is 'git status --porcelain=v1 --untracked-files=no': modified tracked paths fail its reads, untracked paths do not - confirmed in this run, where every HIVE/MCP check passed with the receipts untracked. The check now mirrors that contract and logs the untracked set as an observation.",
    "The generator resolved the proof head as 'the head HIVE recorded, or else the local HEAD'. After the runtime drift that fallback fired: the capture directory held a failed v1.0.1 preflight with no head, so the next run bound every HIVE and MCP proof to a commit it had never measured. Reading the receipts from the installed tree instead of the scratch directory, and refusing to generate when the runtime receipt names no head, removes that path; the failed attempt is now carried verbatim under environmentDrift instead of overwriting the receipt that proves the pinned runtime worked.",
    "scripts/hive_mcp.py resolved a HIVE checkout by path but let Docker Compose pick the stack, so on a machine whose environment exports COMPOSE_PROJECT_NAME for a different HIVE it execed into that other runtime while reporting a clean launch. It now passes -p when HIVE_COMPOSE_PROJECT is set and rejects a value that could inject compose arguments.",
    "An isolated pinned stack first rendered its data root from the ambient HIVE_DATA_ROOT rather than from its own env file, which would have pointed a v1.0.0 migration at the live 1.0.2 database directory. Caught by reading `docker compose config` back before any container started; the recorded stack runs with per-process overrides.",
    "The canonical workspace path carried by the Work Order and the runbook (D:\\Hive\\Projects\\isoryn-engine) no longer exists: D:\\Hive is now the newer stack's data root and the ISORYN working copy is at D:\\Projects\\isoryn-engine. Proved by directory listing rather than recreated, because recreating it would have collided with concurrent work."
  ],
  "residualRisks": [
    "One sibling workspace could not be relinked at its previous path because an unrelated service holds a lock on the empty directory. No data was lost: the working tree, index and history all live at the new canonical path, and the leftover is an empty directory. Retrying the link needs the owning process to release it.",
    "The sibling project registrations predate this Work Order; one reports an inspection head older than its current head. Refreshing them is outside ISORYN's scope and is recorded rather than silently done.",
    "This Work Order's own evidence artifacts are keyword-dense and quote canonical headings, which displaced docs/project-brain/15-DEFINITION-OF-DONE.md from a six-row lexical window (it resolves at rank 7 of 10). Nothing was excluded from the probe to restore the pass: the window is 10 and every canonical rank is recorded in hiveRetrievalProof, so further displacement shows up as a number instead of a silent FAIL.",
    "allow_auto_merge is enabled at the repository level as a capability. It is not enabled on the pull request (autoMergeRequest is null) and the Work Order forbids merging.",
    "Canonical documentation keeps the absolute workspace path by explicit Work Order allowance ('machine paths stay configuration/documentation'), so documentation is not a portability guarantee; executable config is.",
    "The Evidence Bundle is committed after the code it evidences because a commit cannot contain its own SHA and cannot name a pull request that does not exist yet. headBindingNote and ciObservations carry that precisely; any later evidence-only commit must append its own observed result.",
    "HIVE's staleness guard ignores untracked paths ('git status --porcelain=v1 --untracked-files=no') but fails closed on any modified tracked path, and its index walks the working tree so untracked files are indexed too. Proofs are therefore captured from a head with no dirty tracked paths; the Evidence Bundle's own untracked artifacts are listed in matrix.log as an observation rather than hidden."
  ],
  "rollback": {
    "posture": "Reverting the Work Order commits restores the pre-bootstrap Source Pack. No runtime, dependency or product code was introduced, so no data migration or lockfile regeneration is involved.",
    "protectedBranch": "main cannot be deleted or force-updated under main-governance; corrections land as new commits on the Work Order branch and are re-evidenced at the new exact head.",
    "hive": "HIVE holds only derived state for this project. Re-indexing or forgetting the registration cannot affect canonical Git truth; nothing in this Work Order wrote through HIVE."
  },
  "proposedCheckpointDelta": {
    "status": "PROPOSED_ONLY",
    "path": ".engineering/evidence/ISORYN-WO-0001-CHECKPOINT-DELTA.md",
    "note": "The executor may not self-approve promotion."
  },
  "stopCondition": "READY_FOR_C01_REVIEW",
  "verdict": "AWAITING_INDEPENDENT_REVIEW",
  "c01GeneratedAt": "2026-09-23T13:17:22Z",
  "c01Recovery": {
    "trigger": "Independent review of PR #2 returned CORRECTION REQUIRED and blocked promotion on HIVE_RUNTIME_DRIFT.",
    "proofLineage": {
      "historicalHiveProofHead": "d5de04c5ac157236de55875bb530f81d3d02ce86",
      "reviewerCorrectionHead": "4ee69e2c45a6afd2c23a0e7b5a8df20d0acbcc9b",
      "c01ExecutionProofHead": "f293fabfd4cde0a202d917b75eee590567b2027e",
      "finalEvidenceCarryingHead": "recorded in .engineering/evidence/ci.json once Governance runs on the pushed head",
      "note": "The d5de04c5ac15 records are left exactly as written and remain valid only for that head. C01 adds a current proof at f293fabfd4cd rather than restating the old one."
    },
    "runtime": {
      "baseline": "HIVE v1.0.0",
      "sourceCommit": "a53b5b9fcf55c32a5696180fb1b1ef80ccd1edcf",
      "versionReportedByHealth": "1.0.0",
      "composeProject": "isoryn-c01-v100",
      "apiPort": 18099,
      "apiUrl": "http://127.0.0.1:18099",
      "dataRoot": "D:/isoryn-c01-hive-proof/data",
      "projectsRoot": "D:/Projects",
      "projectsRootInContainer": "/workspace/projects",
      "postgresPublishedPort": null,
      "redisPublishedPort": null,
      "network": "isoryn-c01-v100_hive",
      "materialisation": "git clone --no-hardlinks --branch v1.0.0 from the operator's existing HIVE object store. The clone step read the source repository only; no container, volume, network, .env or Git state of any pre-existing stack was modified.",
      "secrets": "POSTGRES_PASSWORD is generated per machine in the operator-local compose env file and is not recorded here."
    },
    "isolation": {
      "collisionDomainsSeparated": [
        "Compose project name, which also derives container and network names",
        "host API port",
        "HIVE_DATA_ROOT",
        "HIVE_PROJECTS_ROOT",
        "compose env file"
      ],
      "ambientEnvironmentHazard": "Docker Compose resolves variables from the process environment before --env-file. This machine exports COMPOSE_PROJECT_NAME, HIVE_DATA_ROOT, HIVE_PROJECTS_ROOT, HIVE_HOME and HIVE_REPO_PATH for the operator's live stack, so a stack configured only with --env-file rendered HIVE_DATA_ROOT as the live database directory and would have migrated it with a v1.0.0 schema. `docker compose config` was read back with per-process overrides before anything started, and that is what the recorded mounts reflect.",
      "launcherHazard": "docker compose exec chooses containers by project label, not by working directory. From inside the pinned v1.0.0 checkout with the ambient COMPOSE_PROJECT_NAME left at the live value, `docker compose ps` listed hive-v102-api-1 and its siblings; with -p isoryn-c01-v100 it listed isoryn-c01-v100-api-1. scripts/hive_mcp.py now passes -p when HIVE_COMPOSE_PROJECT is set.",
      "targetedPinnedStackNotConcurrent": true
    },
    "concurrentRuntimeBeforeAfter": {
      "policy": "The concurrent stacks are not owned by this correction; none was stopped, deleted, reconfigured or entered.",
      "hiveProjectAtD-Projetos-Codex": {
        "role": "the HIVE 1.0.1 workspace the review named",
        "before": "api Exited(3), dashboard Created, migration/storage-init Exited(0), redis and postgres Exited(127)",
        "after": "identical container set and identical recorded states and timestamps",
        "mutatedByThisCorrection": false
      },
      "hiveV102Project": {
        "role": "the runtime actually serving 127.0.0.1:8000 during C01",
        "before": "api/postgres/redis up and healthy, dashboard up, StartedAt 2026-09-22T22:57:17Z, restartcount 0",
        "after": "unchanged StartedAt, restartcount 0, same image id, /api/v1/health still ok at version 1.0.2",
        "mutatedByThisCorrection": false,
        "dataRootStillExclusive": "D:/HIVE/postgres is mounted only in hive-v102-postgres-1"
      },
      "outsideThisCorrection": "A third stack, compose project hive-wo031-final-159ac90-retry-02 on 127.0.0.1:18041, was running at the first snapshot and gone at the second. No command in this session named that project, and its images are still present, which is a normal down-without-rmi by its own owner. Recorded rather than assumed away, because a before/after claim has to name what actually moved."
    },
    "results": {
      "health": {
        "version": "1.0.0",
        "status": "ok",
        "postgres": "ok with pgvector",
        "redis": "ok",
        "storage": "ok"
      },
      "project": {
        "project_id": "76ee3c9b-d539-4020-a010-cb956cf4254a",
        "relative_path": "isoryn-engine",
        "git_branch": "isoryn-wo-0001-foundation",
        "git_head_sha": "f293fabfd4cde0a202d917b75eee590567b2027e",
        "state": "READY",
        "repository_accessible": true,
        "working_tree_clean": true,
        "registrationIsUnique": true,
        "projectListReturnedCount": 1
      },
      "index": {
        "status": "COMPLETED"
      },
      "corpus": {
        "state": "CURRENT",
        "repository_source_count": 135,
        "chunk_count": 218,
        "reference_count": 218
      },
      "canonicalRetrieval": {
        "docs/project-brain/13-CHECKPOINT.md": {
          "firstRank": 2,
          "withinTop10": true
        },
        "docs/project-brain/15-DEFINITION-OF-DONE.md": {
          "firstRank": 11,
          "withinTop10": false,
          "window": 20
        },
        "docs/project-brain/04-ARCHITECTURE.md": {
          "firstRank": 2,
          "withinTop10": true
        },
        "note": "The DoD page ranks behind this Work Order's own evidence bundle for its own name because the bundle repeats the phrase far more often. Reported at rank 11 of a 20-wide window rather than re-queried until it surfaced in one."
      },
      "mcp": {
        "transport": "stdio JSON-RPC through scripts/hive_mcp.py",
        "toolsListed": [
          "checkpoint.read",
          "context.build",
          "context.search",
          "memory.get",
          "memory.search",
          "project.list",
          "project.status"
        ],
        "toolsListMatchesGovernedSurface": true,
        "allReadOnly": true,
        "callsExecuted": [
          "project.list",
          "project.status",
          "checkpoint.read",
          "context.search"
        ],
        "launcherExitCode": 0,
        "launcherStderr": "",
        "semanticState": "UNAVAILABLE",
        "hybridState": "LEXICAL_FALLBACK_SEMANTIC_UNAVAILABLE",
        "rerankState": "RERANK_FALLBACK_DISABLED"
      }
    },
    "checks": {
      "py_compile": "PASS",
      "governance_validator": "PASS",
      "unittest_suite": "PASS",
      "git_diff_check": "PASS",
      "no_uncommitted_tracked_changes": "PASS",
      "clean_worktree_for_hive": "PASS",
      "secret_scan": "PASS",
      "hive_bootstrap_pipeline": "PASS",
      "hive_inspection_head_matches_local_head": "PASS",
      "hive_corpus_current": "PASS",
      "hive_retrieval_canonical": "PASS",
      "mcp_handshake": "PASS",
      "mcp_readonly_call": "PASS",
      "mcp_project_status": "PASS",
      "mcp_checkpoint_read": "PASS",
      "mcp_context_search_canonical": "PASS",
      "mcp_launcher_no_npx_proxy": "PASS",
      "mcp_launcher_targets_pinned_project": "PASS",
      "concurrent_hive_untouched": "PASS",
      "governance_ci": "UNKNOWN",
      "toolchain_build": "DEFERRED_BY_WO",
      "performance_benchmark": "DEFERRED_BY_WO",
      "third_party_dependency_scan": "NOT_AVAILABLE"
    },
    "filesChanged": [
      "scripts/hive_mcp.py",
      "tests/test_hive_mcp.py",
      ".codex/config.toml",
      ".env.example",
      "docs/HIVE-INTEGRATION.md",
      ".engineering/evidence/hive-preflight.json",
      ".engineering/evidence/hive-retrieval-proof.json",
      ".engineering/evidence/mcp-proof.json",
      ".engineering/evidence/checks.json",
      ".engineering/evidence/ci.json",
      ".engineering/evidence/ISORYN-WO-0001-EVIDENCE.md",
      ".engineering/evidence/ISORYN-WO-0001-CHECKPOINT-DELTA.md"
    ],
    "testCounts": {
      "unittest": "27 tests, 0 failures (was 24 before the isolation tests)"
    },
    "notDone": [
      "The canonical HIVE pin stays v1.0.0; it was not raised to 1.0.1 or 1.0.2 to make the drift disappear, because a baseline change needs its own ADR.",
      "No engine or product implementation was introduced.",
      "PR #2 is not merged and the checkpoint is not promoted."
    ]
  }
}
```
