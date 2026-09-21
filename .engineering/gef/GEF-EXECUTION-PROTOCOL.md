# ISORYN GEF Execution Protocol

Every implementation Work Order contains: OBJECTIVE; HIVE PREFLIGHT; CANONICAL BASIS; CONTEXT BUDGET; RISK/ASSURANCE; SCOPE; OUT OF SCOPE; FILES/SOURCES TO READ; REQUIREMENTS; ARCHITECTURE RULES; CONSTRAINTS; ACCEPTANCE CRITERIA; TESTS; EVIDENCE; DELIVERABLES; REVIEW FORMAT PT-BR; STOP CONDITION.

Resolve Git first. Use HIVE progressively. Execute only admitted scope. Preserve valid independent evidence. Repair causal failures at the smallest invalidated surface. Stop at the Work Order stop condition.

## ISORYN namespaces
- Work Order: `.engineering/work-orders/<WO-ID>-<slug>.md`.
- Context Lock: `.engineering/context-locks/<WO-ID>.json`, recording admitted scope, out-of-scope, base SHA, canonical
  sources, upstream pins and the `staleWhen` conditions that invalidate it.
- Evidence: see `GEF-EVIDENCE-SPEC.md`. A Context Lock is only current while its base is an ancestor of the candidate
  head and none of its `staleWhen` conditions has fired; a stale lock is re-admitted, not silently reused.

