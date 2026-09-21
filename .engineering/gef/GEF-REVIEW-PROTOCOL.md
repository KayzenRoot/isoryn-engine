# ISORYN GEF Review Protocol

Review exact candidate/head against Scope, Architecture, Requirements, acceptance criteria and DoD.

Order: confirm authorized base/head; confirm Context Lock; inspect semantic delta; verify exact-head tests/evidence; check scope/architecture/security/integrity regressions; classify findings; return APPROVED, CORRECTION REQUIRED or BLOCKED.

After findings, attempt bounded direct correction first when it remains in frozen scope, adds no unapproved dependency/architecture, current tools can perform it, and exact-head revalidation is available. Otherwise delegate only residual executor-required corrections. No checkpoint promotion with unresolved HIGH/CRITICAL findings.
