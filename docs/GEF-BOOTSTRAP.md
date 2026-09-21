# GEF Bootstrap in ISORYN

ISORYN targets GEF Bootstrap v1.0.0 at upstream commit 866fe3af8cccc65c929aaf6a47a924401fa448b3. GEF v1.0.0 is a source workspace, not a published global npm CLI, so ISORYN materializes the target-project governance contract instead of vendoring the whole repository.

Installed surfaces: canonical Source Pack, source hierarchy/checkpoint bridges, GEF adoption/profile/policy/protocol records, Work Order/Context Lock/Evidence namespaces, deterministic governance validation, GitHub CI/review scaffolding and HIVE-first executor integration.

Upstream validation:
git clone https://github.com/KayzenRoot/gef-bootstrap.git
cd gef-bootstrap
git checkout v1.0.0
npm ci
npm run validate
