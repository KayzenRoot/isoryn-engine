# ISORYN Review Autofix Policy

Status: ADOPTED_POLICY
Source: GEF v1.0.0 review-first correction model, materialized for ISORYN as a stable repository rule.

This file is the canonical repository source for the review-first direct correction rule restated in
`AGENTS.md`. When the two disagree, this file governs the policy and `AGENTS.md` governs executor behavior.

## Core rule
The reviewer or chat fixes small, causal, safe, in-scope findings directly whenever the current tools can
implement and objectively validate them. Codex/Coder/Qoder receives only residual `EXECUTOR_REQUIRED` work.

## Classification
- `CHAT_FIXABLE`: repository files, governance or documentation drift, bounded configuration defects,
  test and evidence defects repairable from the current environment, and any correction that can be
  validated here without new local state.
- `EXECUTOR_REQUIRED`: local-machine or runtime state, unavailable administrative capability, broader
  implementation needing the executor environment, dependency or toolchain execution the reviewer does
  not have, or a correction that cannot be objectively validated from here.

## Constraints
1. Presence of a defect is never by itself a reason to delegate.
2. A correction Work Order carries only residual `EXECUTOR_REQUIRED` findings.
3. Every direct correction creates a new exact head; re-run the applicable validation and CI and bind the
   review to the corrected SHA.
4. Never hide, downgrade or bypass a failure in order to avoid using an executor.
5. No promotion while the current increment is `CORRECTION REQUIRED` or `BLOCKED`, or while a known
   HIGH/CRITICAL defect remains.
6. Executor-facing prompt handoffs follow the `AGENTS.md` prompt artifact policy: downloadable PDF, never
   a canonical copyable prompt box.
