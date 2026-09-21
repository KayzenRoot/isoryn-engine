# ISORYN-WO-0001 - Evidence Bundle

Generated 2026-09-21T17:26:21Z by the executor of `ISORYN-WO-0001` (GEF v1.0.0 adoption, HIVE v1.0.0
integration, professional GitHub foundation) for pull request
[ISORYN-WO-0001/#2](https://github.com/KayzenRoot/isoryn-engine/pull/2) at exact head `ac858e0c4c67c5eb3dc21697cbfe3f2e13f0b54a`.

This bundle is machine-readable: the JSON block at the end is the payload
`scripts/validate_governance.py` gates. Prose here only points at it.

## Binding

| Field | Value |
| --- | --- |
| Admission base (origin/main at WO admission) | `dfe6b0547f0c46c6f0afb14cb4cfa6b3c8a17362` |
| PR base (`main` at branch cut) | `5fb0179b9c0a9a8f94f170dc299f199a7c7c883d` |
| Head executed against | `ac858e0c4c67c5eb3dc21697cbfe3f2e13f0b54a` |
| Branch | `isoryn-wo-0001-foundation` |
| GEF pin | v1.0.0 `866fe3af8cccc65c929aaf6a47a924401fa448b3` |
| HIVE pin | v1.0.0 `a53b5b9fcf55c32a5696180fb1b1ef80ccd1edcf` |

Every entry in checks was executed against this exact tree by a capture tool that runs outside the repository and installs its receipts into this directory afterwards, so no measurement was taken of a tree the capture itself had dirtied. The governance_validator and unittest_suite gates read this bundle, so they cannot be satisfied by the code head alone: they execute against the head that contains this file, and GitHub Actions re-executes them on that head, which is the authority for the reviewed commit. See ciObservations.

The 11 commits between the admission base and the PR base are the earlier
direct-to-`main` bootstrap of this same Work Order, permitted before branch protection existed;
they are listed in `priorWorkOrderCommits` rather than presented as this PR's delta.

## Result vocabulary

`PASS` executed and satisfied the gate, `FAIL` executed and did not, `NOT_AVAILABLE` the platform or
runtime refused the capability and the exact response is recorded, `DEFERRED_BY_WO` the Work Order
itself excluded it and the authorizing clause is quoted.

## Executed checks at `ac858e0c4c67c5eb3dc21697cbfe3f2e13f0b54a`

| `clean_worktree_for_hive` | PASS |
| `git_diff_check` | PASS |
| `governance_ci` | NOT_AVAILABLE |
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

## Stop condition

`READY_FOR_BOOTSTRAP_AUDIT` - AWAITING_INDEPENDENT_REVIEW. The Work Order forbids merging and forbids starting engine implementation;
the checkpoint delta is `PROPOSED_ONLY` and promotion belongs to an independent audit.

```json
{
  "schemaVersion": "isoryn-gef-evidence-bundle-v1",
  "workOrder": "ISORYN-WO-0001",
  "role": "EXECUTOR_DELIVERY",
  "generatedAt": "2026-09-21T17:26:21Z",
  "repository": "KayzenRoot/isoryn-engine",
  "branch": "isoryn-wo-0001-foundation",
  "pr": {
    "number": 2,
    "url": "https://github.com/KayzenRoot/isoryn-engine/pull/2",
    "state": "OPEN",
    "baseSha": "5fb0179b9c0a9a8f94f170dc299f199a7c7c883d",
    "headSha": "3de6fa11ed5dda13a31a9b7abe6591de6a34bf0f",
    "merged": false,
    "autoMergeRequest": null,
    "headShaNote": "Recorded from the remote when this bundle was generated, so it names the last pushed head, not the evidence commit itself - a pull request receipt cannot contain its own SHA. The follow-up evidence commit refreshes it alongside ciObservations.",
    "note": "Open for independent review. The Work Order forbids merging, and the executor does not merge or self-approve."
  },
  "baseSha": "5fb0179b9c0a9a8f94f170dc299f199a7c7c883d",
  "headSha": "ac858e0c4c67c5eb3dc21697cbfe3f2e13f0b54a",
  "candidateHeadSha": "ac858e0c4c67c5eb3dc21697cbfe3f2e13f0b54a",
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
    ".engineering/evidence/github/after-repository.json",
    ".engineering/evidence/github/after-ruleset.json",
    ".engineering/evidence/github/before-repository.json",
    ".engineering/evidence/github/before-rulesets.json",
    ".engineering/evidence/github/ruleset-check-main.txt",
    ".engineering/evidence/github/ruleset-list.json",
    ".engineering/evidence/github/ruleset-view.txt",
    ".engineering/evidence/github/security-endpoints.txt",
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
    "governance_ci": "NOT_AVAILABLE",
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
      "git_head_sha": "ac858e0c4c67c5eb3dc21697cbfe3f2e13f0b54a",
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
      "last_successful_sync": "2026-09-21T17:22:25.734460Z",
      "latest_run": {
        "status": "COMPLETED",
        "repository_source_count": 124,
        "chunk_count": 133,
        "current_reference_count": 135
      }
    },
    "queries": {
      "Definition of Done": {
        "paths": [
          ".engineering/evidence/ISORYN-WO-0001-CHECKPOINT-DELTA.md",
          "docs/project-brain/15-DEFINITION-OF-DONE.md",
          "scripts/validate_governance.py",
          "AGENTS.md",
          ".engineering/work-orders/ISORYN-WO-0001-GEF-HIVE-BOOTSTRAP.md",
          "docs/project-brain/00-README-UPLOAD-ORDER.md"
        ],
        "canonical_paths": [
          "docs/project-brain/00-README-UPLOAD-ORDER.md",
          "docs/project-brain/15-DEFINITION-OF-DONE.md"
        ]
      },
      "Godot engine foundation": {
        "paths": [
          "docs/project-brain/05-INTEGRATION-CONTRACTS.md",
          ".engineering/work-orders/ISORYN-WO-0001-GEF-HIVE-BOOTSTRAP.md",
          ".engineering/github/repository-settings.json",
          "README.md",
          "docs/project-brain/01-PROJECT-OVERVIEW.md",
          ".engineering/evidence/github/after-repository.json"
        ],
        "canonical_paths": [
          "docs/project-brain/01-PROJECT-OVERVIEW.md",
          "docs/project-brain/05-INTEGRATION-CONTRACTS.md"
        ]
      }
    },
    "canonical_paths": [
      "docs/project-brain/00-README-UPLOAD-ORDER.md",
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
              "text": "{\"limit\":32,\"projects\":[{\"detached_head\":false,\"git_branch\":\"isoryn-wo-0001-foundation\",\"git_head_sha\":\"ac858e0c4c67c5eb3dc21697cbfe3f2e13f0b54a\",\"language_stack\":[],\"name\":\"ISORYN\",\"project_id\":\"8696b773-8554-4f27-9cb0-77ddfaf98deb\",\"relative_path\":\"isoryn-engine\",\"repository_accessible\":true,\"state\":\"READY\",\"working_tree_clean\":true},{\"detached_head\":false,\"git_branch\":\"main\",\"git_head_sha\":\"8e995cf4fe66d6da185fd1540d84069d836a5525\",\"language_stack\":[],\"name\":\"FORGE\",\"project_id\":\"08d8ac6c-eedb-42d5-a03c-d699eea6fc85\",\"relative_path\":\"forge\",\"repository_accessible\":true,\"state\":\"READY\",\"working_tree_clean\":true},{\"detached_head\":false,\"git_branch\":\"feat/m01-core-runtime\",\"git_head_sha\":\"0eafc1682f31edadca935d1d47d9cf4baf2bf82f\",\"language_stack\":[\"rust\"],\"name\":\"CORE\",\"project_id\":\"220151cb-0e6e-43b3-845e-faec9c5a851b\",\"relative_path\":\"core\",\"repository_accessible\":true,\"state\":\"READY\",\"working_tree_clean\":false},{\"detached_head\":false,\"git_branch\":\"codex/cp-02r-hive-mcp-corrective\",\"git_head_sha\":\"79fd8c709ea73fb017545b835f9073288ce2af10\",\"language_stack\":[\"typescript\",\"javascript\"],\"name\":\"NEXLABS-WEB\",\"project_id\":\"85efae57-a5f4-44c8-aa0a-f63412fabaa5\",\"relative_path\":\"nexlabs-web\",\"repository_accessible\":true,\"state\":\"READY\",\"working_tree_clean\":true}],\"returned_count\":4,\"truncated\":false,\"version\":\"mcp-project-list-v1\"}"
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
                "git_head_sha": "ac858e0c4c67c5eb3dc21697cbfe3f2e13f0b54a",
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
              "text": "{\"project\":{\"detached_head\":false,\"git_branch\":\"isoryn-wo-0001-foundation\",\"git_head_sha\":\"ac858e0c4c67c5eb3dc21697cbfe3f2e13f0b54a\",\"language_stack\":[],\"name\":\"ISORYN\",\"project_id\":\"8696b773-8554-4f27-9cb0-77ddfaf98deb\",\"relative_path\":\"isoryn-engine\",\"repository_accessible\":true,\"state\":\"READY\",\"working_tree_clean\":true},\"version\":\"mcp-project-status-v1\"}"
            }
          ],
          "structuredContent": {
            "version": "mcp-project-status-v1",
            "project": {
              "project_id": "8696b773-8554-4f27-9cb0-77ddfaf98deb",
              "name": "ISORYN",
              "relative_path": "isoryn-engine",
              "git_branch": "isoryn-wo-0001-foundation",
              "git_head_sha": "ac858e0c4c67c5eb3dc21697cbfe3f2e13f0b54a",
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
              "text": "{\"checkpoint\":{\"content\":\"# ISORYN Checkpoint\\n\\n## STATUS\\nBOOTSTRAP ACTIVE\\n\\n## VERSION\\nISORYN 0.0 - Clean Foundation\\n\\n## PHASE\\n0 - GEF/HIVE Repository Foundation\\n\\n## OBJECTIVE\\nEstablish the professional Source Pack, GEF v1.0.0 governance, HIVE v1.0.0 integration, Codex MCP bridge and exact-head governance CI before engine implementation begins.\\n\\n## IN PROGRESS\\nISORYN-WO-0001-GEF-HIVE-BOOTSTRAP.\\n\\n## BLOCKERS\\nLocal HIVE runtime registration/indexing cannot be proven from GitHub alone and requires execution in the canonical Windows workspace. Repository administrative protection also requires settings/gh access if not already configured.\\n\\n## NEXT STEP\\nValidate local HIVE registration from D:\\\\Hive\\\\Projects\\\\isoryn-engine, configure professional main ruleset, collect exact-head CI/evidence, audit, then promote this checkpoint before engine module discovery.\\n\",\"content_characters\":837,\"git_blob_sha\":\"eda40e734a2c9f5e4fdf9cd8d559758f3ef93aba\",\"git_head_sha\":\"ac858e0c4c67c5eb3dc21697cbfe3f2e13f0b54a\",\"path\":\"docs/project-brain/13-CHECKPOINT.md\",\"registered_head_sha\":\"ac858e0c4c67c5eb3dc21697cbfe3f2e13f0b54a\",\"section_count\":7,\"sections\":[{\"end_char\":49,\"end_line\":5,\"heading\":\"STATUS\",\"start_char\":21,\"start_line\":3},{\"end_char\":91,\"end_line\":8,\"heading\":\"VERSION\",\"start_char\":49,\"start_line\":6},{\"end_char\":136,\"end_line\":11,\"heading\":\"PHASE\",\"start_char\":91,\"start_line\":9},{\"end_char\":321,\"end_line\":14,\"heading\":\"OBJECTIVE\",\"start_char\":136,\"start_line\":12},{\"end_char\":372,\"end_line\":17,\"heading\":\"IN PROGRESS\",\"start_char\":321,\"start_line\":15},{\"end_char\":617,\"end_line\":20,\"heading\":\"BLOCKERS\",\"start_char\":372,\"start_line\":18},{\"end_char\":837,\"end_line\":22,\"heading\":\"NEXT STEP\",\"start_char\":617,\"start_line\":21}],\"source_content_sha256\":\"e80d974e32e7d6da04e2cd35a5ff16c8c7f60e71f09ed4ddc4c2cf39484e0188\"},\"project_id\":\"8696b773-8554-4f27-9cb0-77ddfaf98deb\",\"version\":\"mcp-checkpoint-read-v1\"}"
            }
          ],
          "structuredContent": {
            "version": "mcp-checkpoint-read-v1",
            "project_id": "8696b773-8554-4f27-9cb0-77ddfaf98deb",
            "checkpoint": {
              "path": "docs/project-brain/13-CHECKPOINT.md",
              "git_head_sha": "ac858e0c4c67c5eb3dc21697cbfe3f2e13f0b54a",
              "registered_head_sha": "ac858e0c4c67c5eb3dc21697cbfe3f2e13f0b54a",
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
              "text": "{\"candidate_pool\":5,\"fallback_reason\":\"rerank_disabled\",\"hybrid_state\":\"LEXICAL_FALLBACK_SEMANTIC_UNAVAILABLE\",\"normalized_query\":\"definition of done\",\"project_id\":\"8696b773-8554-4f27-9cb0-77ddfaf98deb\",\"query\":\"Definition of Done\",\"rerank_state\":\"RERANK_FALLBACK_DISABLED\",\"results\":[{\"chunk_content_sha256\":\"84172922aa8aadc46e4a0758dabdfab599d23cec94dfcffc808ebc24fc1e5ea0\",\"chunk_id\":\"f3b56f23-3bb4-40e4-be35-29116be52a18\",\"chunker_version\":\"line-window-v1\",\"corpus_run_id\":\"2ebde07b-af29-4db4-84e1-7254b94614d1\",\"end_char\":3292,\"end_line\":40,\"hybrid_score\":0.01639344262295082,\"lexical_contribution\":0.01639344262295082,\"lexical_rank\":1,\"lexical_score\":0.5059567093849182,\"path\":\".engineering/evidence/ISORYN-WO-0001-CHECKPOINT-DELTA.md\",\"pre_rerank_rank\":1,\"project_id\":\"8696b773-8554-4f27-9cb0-77ddfaf98deb\",\"qualified_symbol\":null,\"reference_id\":\"495ed92d-d8d9-4a04-ad75-114affc45aed\",\"repository_file_id\":\"7e16afb3-8b4e-4311-8b92-b69abe72e86c\",\"repository_symbol_id\":null,\"rerank_rank\":1,\"rerank_score\":null,\"semantic_contribution\":0.0,\"semantic_distance\":null,\"semantic_rank\":null,\"semantic_score\":null,\"snippet\":\"...P.` | `NONE. ISORYN-WO-0001 delivered and awaiting independent audit.` | Work Order: stop for independent review, do not advance to the next increment |\\n| NEXT STEP | validate local HIVE registration, configure professional main ruleset, collect exact-head CI/evidence, audit, promote | `Audit ISORYN-WO-0001 at the exact PR head; on APPROVED, promote this delta and open the architecture/toolchain discovery Work Order` | Definition of Done and the review-first policy |\\n| BLOCKERS | as recorded | `NONE for Work Order scope. Product/engine implementation remains unauthorized; deferred gates are toolchain, benchmark and performance ev\",\"snippet_characters\":646,\"snippet_truncated\":true,\"source_content_sha256\":\"84172922aa8aadc46e4a0758dabdfab599d23cec94dfcffc808ebc24fc1e5ea0\",\"source_kind\":\"REPOSITORY_FILE\",\"start_char\":0,\"start_line\":1,\"task_id\":null,\"title\":null},{\"chunk_content_sha256\":\"e43d43dfc34b76e742c66b5b0c322a790e014b6811613a21222f78ccd3683b03\",\"chunk_id\":\"93406231-d493-4a56-b95c-176b722188ab\",\"chunker_version\":\"line-window-v1\",\"corpus_run_id\":\"2ebde07b-af29-4db4-84e1-7254b94614d1\",\"end_char\":638,\"end_line\":5,\"hybrid_score\":0.016129032258064516,\"lexical_contribution\":0.016129032258064516,\"lexical_rank\":2,\"lexical_score\":0.3524390272796154,\"path\":\"docs/project-brain/15-DEFINITION-OF-DONE.md\",\"pre_rerank_rank\":2,\"project_id\":\"8696b773-8554-4f27-9cb0-77ddfaf98deb\",\"qualified_symbol\":null,\"reference_id\":\"add6a580-c7af-469f-8bd4-7a2396f31a4e\",\"repository_file_id\":\"cb44c3a2-b555-4e3e-a13d-47242dcf922b\",\"repository_symbol_id\":null,\"rerank_rank\":2,\"rerank_score\":null,\"semantic_contribution\":0.0,\"semantic_distance\":null,\"semantic_rank\":null,\"semantic_score\":null,\"snippet\":\"# ISORYN Definition of Done\\n\\nBootstrap completes only when: Source Pack passes deterministic validation; GEF target-project artifacts exist; HIVE MCP/registration tooling exists and is unit-tested; exact-head governance CI passes; local HIVE registration/index/corpus sync is evidenced; main protection/ruleset is evidenced or explicitly BLOCKED by capability gap; audit returns APPROVED; checkpoint is promoted after audit.\\n\\nProduct increments require admitted acceptance criteria plus functional, test, documentation, security, performance and deployment evidence at exact candidate head. No known HIGH/CRITICAL defect may be promoted.\\n\",\"snippet_characters\":638,\"snippet_truncated\":false,\"source_content_sha256\":\"e43d43dfc34b76e742c66b5b0c322a790e014b6811613a21222f78ccd3683b03\",\"source_kind\":\"REPOSITORY_FILE\",\"start_char\":0,\"start_line\":1,\"task_id\":null,\"title\":null},{\"chunk_content_sha256\":\"7a0b0c5a1483bd20077d2021883b186ca55a3d7719a7196f5f377535ad064d4d\",\"chunk_id\":\"df6ff7d3-eb97-4ae7-a194-163db71cfc5c\",\"chunker_version\":\"line-window-v1\",\"corpus_run_id\":\"2ebde07b-af29-4db4-84e1-7254b94614d1\",\"end_char\":4668,\"end_line\":80,\"hybrid_score\":0.015873015873015872,\"lexical_contribution\":0.015873015873015872,\"lexical_rank\":3,\"lexical_score\":0.20250000059604645,\"path\":\"scripts/validate_governance.py\",\"pre_rerank_rank\":3,\"project_id\":\"8696b773-8554-4f27-9cb0-77ddfaf98deb\",\"qualified_symbol\":null,\"reference_id\":\"7fdb4b5f-e7c6-4699-9c22-b4f0a1e29b8f\",\"repository_file_id\":\"9ec170ca-ec02-4ce0-9521-e090b883e6bc\",\"repository_symbol_id\":null,\"rerank_rank\":3,\"rerank_score\":null,\"semantic_contribution\":0.0,\"semantic_distance\":null,\"semantic_rank\":null,\"semantic_score\":null,\"snippet\":\"...\\\",\\n    \\\".engineering/SOURCE-HIERARCHY.md\\\", \\\".engineering/PROJECT-OVERVIEW.md\\\",\\n    \\\".engineering/CHECKPOINT.md\\\", \\\".engineering/CHECKPOINT.json\\\",\\n    \\\".engineering/BOOTSTRAP-MANIFEST.json\\\", \\\".engineering/REVIEW-AUTOFIX-POLICY.md\\\",\\n    \\\".engineering/gef/GEF-ADOPTION.md\\\", \\\".engineering/gef/GEF-PROJECT-PROFILE.json\\\",\\n    \\\".engineering/gef/GEF-SOURCE-BRIDGE.json\\\", \\\".engineering/gef/GEF-POLICY.md\\\",\\n    \\\".engineering/gef/GEF-EXECUTION-PROTOCOL.md\\\", \\\".engineering/gef/GEF-REVIEW-PROTOCOL.md\\\",\\n    \\\".engineering/gef/GEF-EVIDENCE-SPEC.md\\\",\\n    \\\".engineering/github/repository-settings.json\\\", \\\".engineering/github/ruleset-main-governance.json\\\",\",\"snippet_characters\":646,\"snippet_truncated\":true,\"source_content_sha256\":\"08809102e97f9c08c2cfc6b208768e0d3dfdc9420165db8f233dd69a1afdef9b\",\"source_kind\":\"REPOSITORY_FILE\",\"start_char\":0,\"start_line\":1,\"task_id\":null,\"title\":null},{\"chunk_content_sha256\":\"1a111c8b528b56f5474af1ef27f5cdee42fdd1fbf5c0b57f66141635649f2596\",\"chunk_id\":\"cd9db84f-d164-4d3e-b631-ae004b51810f\",\"chunker_version\":\"line-window-v1\",\"corpus_run_id\":\"2ebde07b-af29-4db4-84e1-7254b94614d1\",\"end_char\":5975,\"end_line\":63,\"hybrid_score\":0.015625,\"lexical_contribution\":0.015625,\"lexical_rank\":4,\"lexical_score\":0.2002783715724945,\"path\":\"AGENTS.md\",\"pre_rerank_rank\":4,\"project_id\":\"8696b773-8554-4f27-9cb0-77ddfaf98deb\",\"qualified_symbol\":null,\"reference_id\":\"4e7cb5dd-d93f-4ab8-bc6b-9d62bd67ed19\",\"repository_file_id\":\"2dea9964-7aa2-4fbd-9762-c617bdf57f07\",\"repository_symbol_id\":null,\"rerank_rank\":4,\"rerank_score\":null,\"semantic_contribution\":0.0,\"semantic_distance\":null,\"semantic_rank\":null,\"semantic_score\":null,\"snippet\":\"...ontract\\n\\nISORYN is governed by GEF and is HIVE-first.\\n\\n## Authority\\n1. Resolve authority through .engineering/SOURCE-HIERARCHY.md.\\n2. Read docs/project-brain/13-CHECKPOINT.md first.\\n3. Then read Decisions, Scope, Definition of Done, Architecture and Requirements as required by the active Work Order.\\n4. Git and exact executable evidence outrank derived summaries and chat memory.\\n5. Product implementation requires an admitted Work Order.\\n\\n## HIVE-first preflight\\nBefore product edits resolve repository root, branch, HEAD and cleanliness; verify HIVE v1.0.0; resolve ISORYN through HIVE's read-only MCP; retrieve only minimum sufficien\",\"snippet_characters\":646,\"snippet_truncated\":true,\"source_content_sha256\":\"1a111c8b528b56f5474af1ef27f5cdee42fdd1fbf5c0b57f66141635649f2596\",\"source_kind\":\"REPOSITORY_FILE\",\"start_char\":0,\"start_line\":1,\"task_id\":null,\"title\":null},{\"chunk_content_sha256\":\"c6b3b0730db2a74ab07e6d8618c127018fed4005b50433258701ae25e74c0844\",\"chunk_id\":\"4076c6ab-5c3d-48e6-b8bc-2b9f22189d7b\",\"chunker_version\":\"line-window-v1\",\"corpus_run_id\":\"2ebde07b-af29-4db4-84e1-7254b94614d1\",\"end_char\":5952,\"end_line\":76,\"hybrid_score\":0.015384615384615385,\"lexical_contribution\":0.015384615384615385,\"lexical_rank\":5,\"lexical_score\":0.20012837648391724,\"path\":\".engineering/work-orders/ISORYN-WO-0001-GEF-HIVE-BOOTSTRAP.md\",\"pre_rerank_rank\":5,\"project_id\":\"8696b773-8554-4f27-9cb0-77ddfaf98deb\",\"qualified_symbol\":null,\"reference_id\":\"9c957e14-547b-4187-b43d-ab3713ede9c6\",\"repository_file_id\":\"d84342fa-4c91-4b17-adeb-6b2251596c3a\",\"repository_symbol_id\":null,\"rerank_rank\":5,\"rerank_score\":null,\"semantic_contribution\":0.0,\"semantic_distance\":null,\"semantic_rank\":null,\"semantic_score\":null,\"snippet\":\"...hronize the clean ISORYN repository into the canonical local workspace, complete and validate the\\nGEF/GEFI + HIVE bootstrap, configure project-scoped Codex/CLI HIVE MCP integration, harden the GitHub repository\\nprofessionally through authenticated gh, create objective evidence, push a governed branch, open one PR, wait for\\nrequired CI, and stop for independent review. No engine or product feature is implemented by this Work Order.\\n\\nHIVE PREFLIGHT: repository root, branch, HEAD and cleanliness must be known before any product edit; ISORYN must\\nresolve to a registered HIVE project through the read-only MCP surface; retrieval may on\",\"snippet_characters\":646,\"snippet_truncated\":true,\"source_content_sha256\":\"adb8b3f590786b115ea86974426c619d61df3da6d396875455eb2c5807c99921\",\"source_kind\":\"REPOSITORY_FILE\",\"start_char\":0,\"start_line\":1,\"task_id\":null,\"title\":null}],\"semantic_state\":\"UNAVAILABLE\",\"top_k\":5,\"version\":\"mcp-context-search-v1\"}"
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
                "reference_id": "495ed92d-d8d9-4a04-ad75-114affc45aed",
                "chunk_id": "f3b56f23-3bb4-40e4-be35-29116be52a18",
                "corpus_run_id": "2ebde07b-af29-4db4-84e1-7254b94614d1",
                "source_kind": "REPOSITORY_FILE",
                "hybrid_score": 0.01639344262295082,
                "lexical_score": 0.5059567093849182,
                "semantic_score": null,
                "semantic_distance": null,
                "lexical_rank": 1,
                "semantic_rank": null,
                "lexical_contribution": 0.01639344262295082,
                "semantic_contribution": 0.0,
                "snippet": "...P.` | `NONE. ISORYN-WO-0001 delivered and awaiting independent audit.` | Work Order: stop for independent review, do not advance to the next increment |\n| NEXT STEP | validate local HIVE registration, configure professional main ruleset, collect exact-head CI/evidence, audit, promote | `Audit ISORYN-WO-0001 at the exact PR head; on APPROVED, promote this delta and open the architecture/toolchain discovery Work Order` | Definition of Done and the review-first policy |\n| BLOCKERS | as recorded | `NONE for Work Order scope. Product/engine implementation remains unauthorized; deferred gates are toolchain, benchmark and performance ev",
                "path": ".engineering/evidence/ISORYN-WO-0001-CHECKPOINT-DELTA.md",
                "title": null,
                "qualified_symbol": null,
                "repository_file_id": "7e16afb3-8b4e-4311-8b92-b69abe72e86c",
                "repository_symbol_id": null,
                "task_id": null,
                "source_content_sha256": "84172922aa8aadc46e4a0758dabdfab599d23cec94dfcffc808ebc24fc1e5ea0",
                "chunk_content_sha256": "84172922aa8aadc46e4a0758dabdfab599d23cec94dfcffc808ebc24fc1e5ea0",
                "chunker_version": "line-window-v1",
                "start_line": 1,
                "end_line": 40,
                "start_char": 0,
                "end_char": 3292,
                "pre_rerank_rank": 1,
                "rerank_rank": 1,
                "rerank_score": null,
                "snippet_characters": 646,
                "snippet_truncated": true
              },
              {
                "project_id": "8696b773-8554-4f27-9cb0-77ddfaf98deb",
                "reference_id": "add6a580-c7af-469f-8bd4-7a2396f31a4e",
                "chunk_id": "93406231-d493-4a56-b95c-176b722188ab",
                "corpus_run_id": "2ebde07b-af29-4db4-84e1-7254b94614d1",
                "source_kind": "REPOSITORY_FILE",
                "hybrid_score": 0.016129032258064516,
                "lexical_score": 0.3524390272796154,
                "semantic_score": null,
                "semantic_distance": null,
                "lexical_rank": 2,
                "semantic_rank": null,
                "lexical_contribution": 0.016129032258064516,
                "semantic_contribution": 0.0,
                "snippet": "# ISORYN Definition of Done\n\nBootstrap completes only when: Source Pack passes deterministic validation; GEF target-project artifacts exist; HIVE MCP/registration tooling exists and is unit-tested; exact-head governance CI passes; local HIVE registration/index/corpus sync is evidenced; main protection/ruleset is evidenced or explicitly BLOCKED by capability gap; audit returns APPROVED; checkpoint is promoted after audit.\n\nProduct increments require admitted acceptance criteria plus functional, test, documentation, security, performance and deployment evidence at exact candidate head. No known HIGH/CRITICAL defect may be promoted.\n",
                "path": "docs/project-brain/15-DEFINITION-OF-DONE.md",
                "title": null,
                "qualified_symbol": null,
                "repository_file_id": "cb44c3a2-b555-4e3e-a13d-47242dcf922b",
                "repository_symbol_id": null,
                "task_id": null,
                "source_content_sha256": "e43d43dfc34b76e742c66b5b0c322a790e014b6811613a21222f78ccd3683b03",
                "chunk_content_sha256": "e43d43dfc34b76e742c66b5b0c322a790e014b6811613a21222f78ccd3683b03",
                "chunker_version": "line-window-v1",
                "start_line": 1,
                "end_line": 5,
                "start_char": 0,
                "end_char": 638,
                "pre_rerank_rank": 2,
                "rerank_rank": 2,
                "rerank_score": null,
                "snippet_characters": 638,
                "snippet_truncated": false
              },
              {
                "project_id": "8696b773-8554-4f27-9cb0-77ddfaf98deb",
                "reference_id": "7fdb4b5f-e7c6-4699-9c22-b4f0a1e29b8f",
                "chunk_id": "df6ff7d3-eb97-4ae7-a194-163db71cfc5c",
                "corpus_run_id": "2ebde07b-af29-4db4-84e1-7254b94614d1",
                "source_kind": "REPOSITORY_FILE",
                "hybrid_score": 0.015873015873015872,
                "lexical_score": 0.20250000059604645,
                "semantic_score": null,
                "semantic_distance": null,
                "lexical_rank": 3,
                "semantic_rank": null,
                "lexical_contribution": 0.015873015873015872,
                "semantic_contribution": 0.0,
                "snippet": "...\",\n    \".engineering/SOURCE-HIERARCHY.md\", \".engineering/PROJECT-OVERVIEW.md\",\n    \".engineering/CHECKPOINT.md\", \".engineering/CHECKPOINT.json\",\n    \".engineering/BOOTSTRAP-MANIFEST.json\", \".engineering/REVIEW-AUTOFIX-POLICY.md\",\n    \".engineering/gef/GEF-ADOPTION.md\", \".engineering/gef/GEF-PROJECT-PROFILE.json\",\n    \".engineering/gef/GEF-SOURCE-BRIDGE.json\", \".engineering/gef/GEF-POLICY.md\",\n    \".engineering/gef/GEF-EXECUTION-PROTOCOL.md\", \".engineering/gef/GEF-REVIEW-PROTOCOL.md\",\n    \".engineering/gef/GEF-EVIDENCE-SPEC.md\",\n    \".engineering/github/repository-settings.json\", \".engineering/github/ruleset-main-governance.json\",",
                "path": "scripts/validate_governance.py",
                "title": null,
                "qualified_symbol": null,
                "repository_file_id": "9ec170ca-ec02-4ce0-9521-e090b883e6bc",
                "repository_symbol_id": null,
                "task_id": null,
                "source_content_sha256": "08809102e97f9c08c2cfc6b208768e0d3dfdc9420165db8f233dd69a1afdef9b",
                "chunk_content_sha256": "7a0b0c5a1483bd20077d2021883b186ca55a3d7719a7196f5f377535ad064d4d",
                "chunker_version": "line-window-v1",
                "start_line": 1,
                "end_line": 80,
                "start_char": 0,
                "end_char": 4668,
                "pre_rerank_rank": 3,
                "rerank_rank": 3,
                "rerank_score": null,
                "snippet_characters": 646,
                "snippet_truncated": true
              },
              {
                "project_id": "8696b773-8554-4f27-9cb0-77ddfaf98deb",
                "reference_id": "4e7cb5dd-d93f-4ab8-bc6b-9d62bd67ed19",
                "chunk_id": "cd9db84f-d164-4d3e-b631-ae004b51810f",
                "corpus_run_id": "2ebde07b-af29-4db4-84e1-7254b94614d1",
                "source_kind": "REPOSITORY_FILE",
                "hybrid_score": 0.015625,
                "lexical_score": 0.2002783715724945,
                "semantic_score": null,
                "semantic_distance": null,
                "lexical_rank": 4,
                "semantic_rank": null,
                "lexical_contribution": 0.015625,
                "semantic_contribution": 0.0,
                "snippet": "...ontract\n\nISORYN is governed by GEF and is HIVE-first.\n\n## Authority\n1. Resolve authority through .engineering/SOURCE-HIERARCHY.md.\n2. Read docs/project-brain/13-CHECKPOINT.md first.\n3. Then read Decisions, Scope, Definition of Done, Architecture and Requirements as required by the active Work Order.\n4. Git and exact executable evidence outrank derived summaries and chat memory.\n5. Product implementation requires an admitted Work Order.\n\n## HIVE-first preflight\nBefore product edits resolve repository root, branch, HEAD and cleanliness; verify HIVE v1.0.0; resolve ISORYN through HIVE's read-only MCP; retrieve only minimum sufficien",
                "path": "AGENTS.md",
                "title": null,
                "qualified_symbol": null,
                "repository_file_id": "2dea9964-7aa2-4fbd-9762-c617bdf57f07",
                "repository_symbol_id": null,
                "task_id": null,
                "source_content_sha256": "1a111c8b528b56f5474af1ef27f5cdee42fdd1fbf5c0b57f66141635649f2596",
                "chunk_content_sha256": "1a111c8b528b56f5474af1ef27f5cdee42fdd1fbf5c0b57f66141635649f2596",
                "chunker_version": "line-window-v1",
                "start_line": 1,
                "end_line": 63,
                "start_char": 0,
                "end_char": 5975,
                "pre_rerank_rank": 4,
                "rerank_rank": 4,
                "rerank_score": null,
                "snippet_characters": 646,
                "snippet_truncated": true
              },
              {
                "project_id": "8696b773-8554-4f27-9cb0-77ddfaf98deb",
                "reference_id": "9c957e14-547b-4187-b43d-ab3713ede9c6",
                "chunk_id": "4076c6ab-5c3d-48e6-b8bc-2b9f22189d7b",
                "corpus_run_id": "2ebde07b-af29-4db4-84e1-7254b94614d1",
                "source_kind": "REPOSITORY_FILE",
                "hybrid_score": 0.015384615384615385,
                "lexical_score": 0.20012837648391724,
                "semantic_score": null,
                "semantic_distance": null,
                "lexical_rank": 5,
                "semantic_rank": null,
                "lexical_contribution": 0.015384615384615385,
                "semantic_contribution": 0.0,
                "snippet": "...hronize the clean ISORYN repository into the canonical local workspace, complete and validate the\nGEF/GEFI + HIVE bootstrap, configure project-scoped Codex/CLI HIVE MCP integration, harden the GitHub repository\nprofessionally through authenticated gh, create objective evidence, push a governed branch, open one PR, wait for\nrequired CI, and stop for independent review. No engine or product feature is implemented by this Work Order.\n\nHIVE PREFLIGHT: repository root, branch, HEAD and cleanliness must be known before any product edit; ISORYN must\nresolve to a registered HIVE project through the read-only MCP surface; retrieval may on",
                "path": ".engineering/work-orders/ISORYN-WO-0001-GEF-HIVE-BOOTSTRAP.md",
                "title": null,
                "qualified_symbol": null,
                "repository_file_id": "d84342fa-4c91-4b17-adeb-6b2251596c3a",
                "repository_symbol_id": null,
                "task_id": null,
                "source_content_sha256": "adb8b3f590786b115ea86974426c619d61df3da6d396875455eb2c5807c99921",
                "chunk_content_sha256": "c6b3b0730db2a74ab07e6d8618c127018fed4005b50433258701ae25e74c0844",
                "chunker_version": "line-window-v1",
                "start_line": 1,
                "end_line": 76,
                "start_char": 0,
                "end_char": 5952,
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
    "repositoryReceipts": [
      ".engineering/evidence/github/before-repository.json",
      ".engineering/evidence/github/after-repository.json"
    ],
    "repositoryReceiptsIdentical": true,
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
        }
      ]
    },
    "rulesetCheckMain": "5 rules apply to branch main in repo KayzenRoot/isoryn-engine\n\n- deletion\n  (configured in ruleset 23776080 from repository KayzenRoot/isoryn-engine)\n\n- non_fast_forward\n  (configured in ruleset 23776080 from repository KayzenRoot/isoryn-engine)\n\n- pull_request: [allowed_merge_methods: [squash]] [dismiss_stale_reviews_on_push: true] [require_code_owner_review: false] [require_extra_approval_for_unattributed_changes: true] [require_last_push_approval: false] [required_approving_review_count: 0] [required_review_thread_resolution: true] [required_reviewers: []] \n  (configured in ruleset 23776080 from repository KayzenRoot/isoryn-engine)\n\n- required_linear_history\n  (configured in ruleset 23776080 from repository KayzenRoot/isoryn-engine)\n\n- update\n  (configured in ruleset 23776080 from repository KayzenRoot/isoryn-engine)\n",
    "rulesetView": "\nmain-governance\nID: 23776080\nSource: KayzenRoot/isoryn-engine (Repository)\nEnforcement: Active\nYou can bypass: never\n\nBypass List\nThis ruleset cannot be bypassed\n\nConditions\n- ref_name: [exclude: []] [include: [refs/heads/main]] \n\nRules\n- deletion\n- non_fast_forward\n- pull_request: [allowed_merge_methods: [squash]] [dismiss_stale_reviews_on_push: true] [require_code_owner_review: false] [require_extra_approval_for_unattributed_changes: true] [require_last_push_approval: false] [required_approving_review_count: 0] [required_review_thread_resolution: true] [required_reviewers: []] \n- required_linear_history\n- update\n",
    "securityEndpointProbe": "vulnerability_alerts => gh api --method PUT repos/KayzenRoot/isoryn-engine/vulnerability_alerts failed with exit 1\nNo D:\\HIVE\\projects\\isoryn-engine\\scripts\\configure-github.ps1:41 caractere:30\n+ ... DE -ne 0) { throw \"gh $($CliArgs -join ' ') failed with exit $LASTEXI ...\n+                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n    + CategoryInfo          : OperationStopped: (gh api --method...led with exit 1:String) [], RuntimeException\n    + FullyQualifiedErrorId : gh api --method PUT repos/KayzenRoot/isoryn-engine/vulnerability_alerts failed with exit \n    1\nautomated_security_fixes => gh api --method PUT repos/KayzenRoot/isoryn-engine/automated_security_fixes failed with exit 1\nNo D:\\HIVE\\projects\\isoryn-engine\\scripts\\configure-github.ps1:41 caractere:30\n+ ... DE -ne 0) { throw \"gh $($CliArgs -join ' ') failed with exit $LASTEXI ...\n+                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n    + CategoryInfo          : OperationStopped: (gh api --method...led with exit 1:String) [], RuntimeException\n    + FullyQualifiedErrorId : gh api --method PUT repos/KayzenRoot/isoryn-engine/automated_security_fixes failed with  \n   exit 1\n",
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
      "head": "ac858e0c4c67c5eb3dc21697cbfe3f2e13f0b54a",
      "context": "Governance",
      "result": "FAIL",
      "run": "https://github.com/KayzenRoot/isoryn-engine/actions/runs/35627653055",
      "detail": "GOVERNANCE VALIDATION FAILED: missing Evidence Bundle for ISORYN-WO-0001. This bundle is the gate's own subject, so it cannot exist in the code head it evidences; the failing run is kept visible instead of being hidden by rewriting history."
    }
  ],
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
    "ISORYN-WO-0001 omitted the EVIDENCE, HIVE PREFLIGHT, CANONICAL BASIS, CONTEXT BUDGET and RISK/ASSURANCE sections that GEF-EXECUTION-PROTOCOL.md requires of every implementation Work Order.",
    "CONTRIBUTING.md still described the one-time direct-to-main bootstrap as available after the ruleset would make it impossible, and its branch convention contradicted the branch this Work Order designates.",
    "No test exercised scripts/validate_governance.py, so the governance gate itself was unverified.",
    "A capture pass reported hive_retrieval_canonical PASS while the index run for that head had actually failed, because the corpus was still CURRENT from an earlier sync. Both retrieval assertions are now gated on the pipeline result for this head, so a stale-but-current corpus can no longer pass.",
    "Windows git rewriting .git/index while HIVE's container reads the same file over the mount made a single status read fail with git_status_unavailable at a clean head, and checkpoint.read then answered source_not_current. The exact container command was reproduced and succeeds, so the capture retries the pipeline (3 attempts, 20s apart) and records every attempt instead of publishing one race as truth.",
    "MCP responses were keyed by request id rather than tool name, so mcp-proof.json would have published {\"3\": null} in place of the calls it claimed to prove; the launcher thread also awaited without a bound. Receipts now carry each tool's raw response behind its name under a per-call timeout.",
    "The preflight receipt was built by slicing between the first '{' and the last '}' of the bootstrap script's stdout. That text opens with a Python-repr health line, so nothing parsed and every successful run was filed under an 'error' key with its proof truncated to the last 800 characters - including the head HIVE had inspected. The summary is now parsed as the trailing JSON object it is, and the captured head is compared with the local HEAD under its own check.",
    "clean_worktree_for_hive asserted a fully empty 'git status', which the Evidence Bundle's own untracked artifacts violate, and it was written from an assumption rather than HIVE's rule. The guard HIVE actually applies is 'git status --porcelain=v1 --untracked-files=no': modified tracked paths fail its reads, untracked paths do not - confirmed in this run, where every HIVE/MCP check passed with the receipts untracked. The check now mirrors that contract and logs the untracked set as an observation."
  ],
  "residualRisks": [
    "One sibling workspace could not be relinked at its previous path because an unrelated service holds a lock on the empty directory. No data was lost: the working tree, index and history all live at the new canonical path, and the leftover is an empty directory. Retrying the link needs the owning process to release it.",
    "The sibling project registrations predate this Work Order; one reports an inspection head older than its current head. Refreshing them is outside ISORYN's scope and is recorded rather than silently done.",
    "required_status_checks is applied only after the exact 'Governance' context has been observed on a real check run for this head. Until then the ruleset is complete except for that rule, and this is stated, not hidden.",
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
  "stopCondition": "READY_FOR_BOOTSTRAP_AUDIT",
  "verdict": "AWAITING_INDEPENDENT_REVIEW"
}
```
