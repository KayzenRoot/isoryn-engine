# GEF Bootstrap in ISORYN

ISORYN targets the production-accepted GEF Bootstrap v1.0.0 release at upstream commit 866fe3af8cccc65c929aaf6a47a924401fa448b3.

GEF v1.0.0 is distributed as a source workspace, not a published global npm CLI. ISORYN therefore does not vendor the whole gef-bootstrap repository. It materializes the target-project governance contract required for a new GEF-native project.

Installed surfaces:
- canonical Source Pack under docs/project-brain;
- source hierarchy and checkpoint bridges;
- GEF adoption/profile/policy/protocol records;
- Work Order, Context Lock and Evidence namespaces;
- deterministic governance validation;
- GitHub CI and review scaffolding;
- HIVE-first executor integration.

To validate GEF upstream separately:
git clone https://github.com/KayzenRoot/gef-bootstrap.git
cd gef-bootstrap
git checkout v1.0.0
npm ci
npm run validate
