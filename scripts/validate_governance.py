from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
REQUIRED=("AGENTS.md",".codex/config.toml",".engineering/SOURCE-HIERARCHY.md",".engineering/PROJECT-OVERVIEW.md",".engineering/CHECKPOINT.md",".engineering/CHECKPOINT.json",".engineering/BOOTSTRAP-MANIFEST.json",".engineering/gef/GEF-ADOPTION.md",".engineering/gef/GEF-PROJECT-PROFILE.json",".engineering/gef/GEF-SOURCE-BRIDGE.json",".engineering/gef/GEF-POLICY.md",".engineering/gef/GEF-EXECUTION-PROTOCOL.md",".engineering/gef/GEF-REVIEW-PROTOCOL.md",".engineering/gef/GEF-EVIDENCE-SPEC.md","docs/project-brain/01-PROJECT-OVERVIEW.md","docs/project-brain/02-REQUIREMENTS.md","docs/project-brain/03-SCOPE.md","docs/project-brain/04-ARCHITECTURE.md","docs/project-brain/10-SECURITY-GOVERNANCE.md","docs/project-brain/11-TEST-PLAN.md","docs/project-brain/12-LOCAL-DEPLOYMENT.md","docs/project-brain/13-CHECKPOINT.md","docs/project-brain/14-BACKLOG.md","docs/project-brain/15-DEFINITION-OF-DONE.md","docs/project-brain/16-DECISIONS-LEDGER.md","docs/HIVE-INTEGRATION.md","scripts/hive_mcp.py")
HIVE_GOV=("docs/project-brain/13-CHECKPOINT.md","docs/project-brain/03-SCOPE.md","docs/project-brain/15-DEFINITION-OF-DONE.md","docs/project-brain/04-ARCHITECTURE.md","docs/project-brain/16-DECISIONS-LEDGER.md")
HEADINGS=("## STATUS","## VERSION","## PHASE","## OBJECTIVE","## IN PROGRESS","## BLOCKERS","## NEXT STEP")
SHARED={"status":"## STATUS","version":"## VERSION","phase":"## PHASE","nextStep":"## NEXT STEP"}
def fail(m): raise SystemExit("GOVERNANCE VALIDATION FAILED: "+m)
def section(text,heading):
    lines=text.splitlines()
    try: start=lines.index(heading)+1
    except ValueError: fail("checkpoint missing heading: "+heading)
    vals=[]
    for line in lines[start:]:
        if line.startswith("## "): break
        if line.strip(): vals.append(line.strip())
    if not vals: fail("checkpoint heading has no value: "+heading)
    return "\n".join(vals)
for rel in REQUIRED:
    if not (ROOT/rel).is_file(): fail("missing required file: "+rel)
cp=(ROOT/HIVE_GOV[0]).read_text(encoding="utf-8")
for h in HEADINGS: section(cp,h)
bridge=(ROOT/".engineering/CHECKPOINT.md").read_text(encoding="utf-8")
machine=json.loads((ROOT/".engineering/CHECKPOINT.json").read_text(encoding="utf-8"))
if machine.get("canonicalCheckpoint")!=HIVE_GOV[0]: fail("machine checkpoint canonical path mismatch")
for field,h in SHARED.items():
    value=section(cp,h)
    if section(bridge,h)!=value or machine.get(field)!=value: fail("checkpoint bridge drift for "+field)
profile=json.loads((ROOT/".engineering/gef/GEF-PROJECT-PROFILE.json").read_text(encoding="utf-8"))
if profile.get("gefVersion")!="1.0.0": fail("GEF version mismatch")
manifest=json.loads((ROOT/".engineering/BOOTSTRAP-MANIFEST.json").read_text(encoding="utf-8"))
if manifest.get("gef",{}).get("releaseCommit")!="866fe3af8cccc65c929aaf6a47a924401fa448b3": fail("GEF pin mismatch")
if manifest.get("hive",{}).get("releaseCommit")!="a53b5b9fcf55c32a5696180fb1b1ef80ccd1edcf": fail("HIVE pin mismatch")
print("ISORYN governance validation: PASS")
print("GEF: v1.0.0 @ 866fe3af8cccc65c929aaf6a47a924401fa448b3")
print("HIVE: v1.0.0 @ a53b5b9fcf55c32a5696180fb1b1ef80ccd1edcf")
print(f"Required artifacts: {len(REQUIRED)}")
