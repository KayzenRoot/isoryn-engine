"""Deterministic ISORYN governance validation.

Every check here is a semantic gate derived from the canonical sources in
.engineering/SOURCE-HIERARCHY.md, not a filename survey: an artifact is required
only because a canonical rule or acceptance gate depends on it, and content is
asserted where an empty or wrong file would let an unproven claim pass.
"""
from __future__ import annotations
import json, re, sys
from pathlib import Path, PurePosixPath, PureWindowsPath

ROOT = Path(__file__).resolve().parents[1]
GEF_PIN = "866fe3af8cccc65c929aaf6a47a924401fa448b3"
HIVE_PIN = "a53b5b9fcf55c32a5696180fb1b1ef80ccd1edcf"

# GEF v1.0.0 MCP core surface: exactly these read-only tools are documented by the pinned HIVE source.
MCP_TOOLS = ("project.list", "project.status", "context.build", "context.search",
             "memory.search", "memory.get", "checkpoint.read")

RESULT_VOCABULARY = {"PASS", "FAIL", "NOT_AVAILABLE", "DEFERRED_BY_WO", "UNKNOWN"}
SHA = re.compile(r"^[0-9a-f]{40}$")
# The delivery-head contract a record declares for itself: `deliveryHeadSemantics` states what the head
# fields mean, `deliveryHeadCiReceipt` names the versioned CI ledger, and the named fields have to resolve
# through it. Enforcing the contract is offline by design — the validator reads the record and the ledger,
# never GitHub — so this gate cannot claim a check-run is still live. Confirming the carrier head against
# the API is a separate step whose result is written into the ledger, not asserted here.
GATE_HEAD_REBINDING = "head_rebinding_fields_match_governance_observation"
CERTIFIED_HEAD_FIELDS = ("headSha", "candidateHeadSha", "github.deliveredHeadSha")
EXECUTION_HEAD_FIELD = "commandsExecutedAtHead"
TREE_STATES = {"CLEAN", "WORKING_TREE_DIRTY"}
# The only directory a versioned receipt may live in, so a record can never point the gate at a file the reviewer
# has not seen.
EVIDENCE_DIR = ".engineering/evidence"
# Drive-letter or foreign-home paths are machine state; they must not live in portable config.
MACHINE_PATH = re.compile(r"(?<![A-Za-z0-9])[A-Za-z]:[\\/]|/(?:home|Users|mnt|var/folders)/")

REQUIRED = (
    "AGENTS.md", "README.md", "CONTRIBUTING.md", "SECURITY.md", ".gitignore", ".gitattributes",
    ".env.example", ".codex/config.toml", ".mcp.json",
    ".github/CODEOWNERS", ".github/pull_request_template.md", ".github/dependabot.yml",
    ".github/workflows/governance.yml", ".github/prompts/implement-work-order.prompt.md",
    ".engineering/SOURCE-HIERARCHY.md", ".engineering/PROJECT-OVERVIEW.md",
    ".engineering/CHECKPOINT.md", ".engineering/CHECKPOINT.json",
    ".engineering/BOOTSTRAP-MANIFEST.json", ".engineering/REVIEW-AUTOFIX-POLICY.md",
    ".engineering/gef/GEF-ADOPTION.md", ".engineering/gef/GEF-PROJECT-PROFILE.json",
    ".engineering/gef/GEF-SOURCE-BRIDGE.json", ".engineering/gef/GEF-POLICY.md",
    ".engineering/gef/GEF-EXECUTION-PROTOCOL.md", ".engineering/gef/GEF-REVIEW-PROTOCOL.md",
    ".engineering/gef/GEF-EVIDENCE-SPEC.md",
    ".engineering/github/repository-settings.json", ".engineering/github/ruleset-main-governance.json",
    "docs/project-brain/00-README-UPLOAD-ORDER.md", "docs/project-brain/01-PROJECT-OVERVIEW.md",
    "docs/project-brain/02-REQUIREMENTS.md", "docs/project-brain/03-SCOPE.md",
    "docs/project-brain/04-ARCHITECTURE.md", "docs/project-brain/05-INTEGRATION-CONTRACTS.md",
    "docs/project-brain/06-MASTER-MODULE-INDEX.md", "docs/project-brain/07-PROPRIETARY-TECHNOLOGY-REGISTRY.md",
    "docs/project-brain/08-GODOT-BASELINE-AND-TOPOLOGY.md", "docs/project-brain/09-TOOLCHAIN-AND-BENCHMARK-BASELINE.md",
    "docs/project-brain/10-SECURITY-GOVERNANCE.md", "docs/project-brain/11-TEST-PLAN.md",
    "docs/project-brain/12-LOCAL-DEPLOYMENT.md", "docs/project-brain/13-CHECKPOINT.md",
    "docs/project-brain/14-BACKLOG.md", "docs/project-brain/15-DEFINITION-OF-DONE.md",
    "docs/project-brain/16-DECISIONS-LEDGER.md",
    "docs/adr/ADR-0001-godot-baseline-and-repository-topology.md",
    "docs/adr/ADR-0002-build-toolchain-and-upstream-sync.md",
    "docs/adr/ADR-0003-extension-seam-policy.md",
    "docs/GEF-BOOTSTRAP.md", "docs/HIVE-INTEGRATION.md", "docs/BOOTSTRAP-RUNBOOK.md",
    "scripts/validate_governance.py", "scripts/hive_mcp.py", "scripts/hive_bootstrap.py",
    "scripts/bootstrap-local.ps1", "scripts/hive-bootstrap.ps1", "scripts/configure-github.ps1",
    "tests/test_hive_bootstrap.py", "tests/test_hive_mcp.py", "tests/test_governance.py",
)

HIVE_GOV = ("docs/project-brain/13-CHECKPOINT.md", "docs/project-brain/03-SCOPE.md",
            "docs/project-brain/15-DEFINITION-OF-DONE.md", "docs/project-brain/04-ARCHITECTURE.md",
            "docs/project-brain/16-DECISIONS-LEDGER.md")
HEADINGS = ("## STATUS", "## VERSION", "## PHASE", "## OBJECTIVE", "## IN PROGRESS", "## BLOCKERS", "## NEXT STEP")
SHARED = {"status": "## STATUS", "version": "## VERSION", "phase": "## PHASE", "nextStep": "## NEXT STEP"}
PORTABLE_CONFIG = (".env.example", ".codex/config.toml", ".gitignore",
                   ".engineering/github/repository-settings.json",
                   ".engineering/github/ruleset-main-governance.json")
PORTABLE_CONFIG_GLOBS = ("scripts/*.ps1", "scripts/*.py", ".engineering/context-locks/*.json",
                         ".github/*.yml", ".github/*.md", ".github/workflows/*.yml")
VENDORED_TREES = ("hive", "gef-bootstrap", "core", "iris", "backend", "node_modules")
# ADR-0001/0002 keep the engine external: build products and engine-tree fingerprints are never repository state.
BINARY_ARTIFACTS = (".exe", ".dll", ".lib", ".obj", ".pdb", ".so", ".dylib", ".a", ".o", ".class", ".jar")
ENGINE_TREE_MARKERS = ("SConstruct", "SCsub")
ENGINE_TREE_SUFFIXES = (".gen.h", ".gen.cpp")
SCOPE_DOC = "docs/project-brain/03-SCOPE.md"
MODULE_INDEX_DOC = "docs/project-brain/06-MASTER-MODULE-INDEX.md"
# HIVE indexes from a Linux container that performs no line-ending conversion, so a CRLF working
# tree reads as an entirely modified repository and its staleness guard refuses canonical retrieval.
TEXT_SUFFIXES = (".md", ".py", ".ps1", ".json", ".yml", ".yaml", ".toml", ".txt", ".ini", ".cfg",
                 ".example", ".prompt.md", ".agent.md")


def fail(m):
    raise SystemExit("GOVERNANCE VALIDATION FAILED: " + m)


def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


def load_json(rel):
    try:
        return json.loads(read(rel))
    except json.JSONDecodeError as exc:
        fail(f"{rel} is not valid JSON: {exc}")


def bundle_payload(rel, wo_id):
    """The machine payload of an Evidence Bundle: one fenced json block, parsed or fatal."""
    bundle = ROOT / rel
    if not bundle.is_file():
        fail("missing Evidence Bundle for " + wo_id)
    block = re.search(r"(?m)^```json\n(.*?)\n```", bundle.read_text(encoding="utf-8"), re.S)
    if not block:
        fail(wo_id + " Evidence Bundle carries no machine-readable json payload block")
    try:
        payload = json.loads(block.group(1))
    except json.JSONDecodeError as exc:
        fail(wo_id + " Evidence Bundle payload is not valid JSON: " + str(exc))
    if not isinstance(payload, dict):
        fail(wo_id + " Evidence Bundle payload is not a json object")
    return payload


def work_order_bundles():
    """(wo_id, work order path, bundle path) for every canonical Work Order in the namespace."""
    entries = []
    for order in sorted((ROOT / ".engineering/work-orders").glob("*.md")):
        match = re.match(r"([A-Z]+-[A-Z]+-\d+)", order.stem)
        if not match:
            fail("Work Order filename must start with a stable ID: " + order.name)
        wo_id = match.group(1)
        entries.append((wo_id, order.relative_to(ROOT).as_posix(),
                        ".engineering/evidence/" + wo_id + "-EVIDENCE.md"))
    if not entries:
        fail("no canonical Work Order under .engineering/work-orders/")
    return entries


def declared(obj, path, wo_id):
    """Field lookup by dotted path that fails closed instead of letting an absent claim pass."""
    value = obj
    for part in path.split("."):
        if not isinstance(value, dict) or part not in value:
            fail(f"{wo_id} declares the delivery-head contract but has no {path}")
        value = value[part]
    return value


def ci_ledger(text, rel):
    """Parse a versioned CI ledger: a json object whose observations are a list of objects."""
    try:
        ledger = json.loads(text)
    except json.JSONDecodeError as exc:
        fail(f"{rel} is not valid JSON: {exc}")
    if not isinstance(ledger, dict):
        fail(f"{rel} is not a json object")
    observations = ledger.get("observations")
    if not isinstance(observations, list) or not observations:
        fail(f"{rel} carries no observations list; a ledger with no check-run cannot certify a head")
    if any(not isinstance(o, dict) for o in observations):
        fail(f"{rel} carries an observation that is not a json object")
    return ledger


def read_ci_ledger(rel, wo_id):
    """Resolve a `deliveryHeadCiReceipt` to a regular file inside the evidence directory, or fail closed.

    The value is a portable repository path, so it is judged with canonical separators before anything touches the
    filesystem: a backslash is a separator on Windows and an ordinary character on POSIX, which is precisely the pair
    of facts a `split("/")` guard cannot see, and a drive or network share resolves over a relative root. Prefix
    matching alone is still not containment, because a link inside the directory can name a target outside it, so the
    decision is made on resolved paths and every resolution failure refuses rather than falling through.
    """
    posix, windows = PurePosixPath(rel), PureWindowsPath(rel)
    if windows.drive or windows.is_absolute() or posix.is_absolute() or rel.startswith("~"):
        fail(f"{wo_id} points its delivery-head CI receipt outside {EVIDENCE_DIR}/: {rel} is an absolute path, a "
             "drive letter or a network share, and a versioned receipt is always repository-relative")
    if "\\" in rel:
        fail(f"{wo_id} names its CI receipt with a Windows separator: {rel}; the contract is a portable path "
             "written with / separators")
    if ".." in posix.parts:
        fail(f"{wo_id} points its delivery-head CI receipt outside {EVIDENCE_DIR}/: {rel} climbs out of it with "
             "a .. segment")
    if not rel.startswith(EVIDENCE_DIR + "/"):
        fail(f"{wo_id} points its delivery-head CI receipt outside {EVIDENCE_DIR}/: {rel}")
    try:
        repo_root = ROOT.resolve(strict=True)
        evidence_path = repo_root / EVIDENCE_DIR
        evidence_root = evidence_path.resolve(strict=True)
        if evidence_root != evidence_path:
            fail(f"{wo_id} evidence directory {EVIDENCE_DIR}/ resolves through a link to {evidence_root}; "
                 "receipts must remain in the canonical repository evidence directory")
        target = (repo_root / rel).resolve(strict=True)
    except FileNotFoundError:
        fail(f"{wo_id} names CI receipt {rel} which is not in the repository")
    except (OSError, RuntimeError, ValueError) as exc:
        # pathlib raises RuntimeError for a symlink loop and ValueError for an unrepresentable path, neither of
        # which is an OSError, and both of which would otherwise escape as a traceback instead of a refusal.
        fail(f"{wo_id} cannot resolve CI receipt {rel}: {getattr(exc, 'strerror', None) or type(exc).__name__}")
    if not target.is_relative_to(evidence_root):
        fail(f"{wo_id} points its delivery-head CI receipt outside {EVIDENCE_DIR}/: {rel} resolves to {target}, "
             "which leaves the directory the contract confines receipts to")
    if not target.is_file():
        fail(f"{wo_id} CI receipt {rel} resolves to {target}, which is not a regular file")
    try:
        text = target.read_text(encoding="utf-8")
    except OSError as exc:
        fail(f"{wo_id} cannot read CI receipt {rel}: {exc.strerror or type(exc).__name__}")
    except UnicodeDecodeError as exc:
        fail(f"{wo_id} CI receipt {rel} is not utf-8 text: {exc}")
    return ci_ledger(text, rel)


def certified_observation(ledger, head, wo_id, source):
    """The one completed, successful Governance observation for `head`, or a closed failure."""
    observations = ledger.get("observations")
    if not isinstance(observations, list) or not observations:
        fail(f"{source} for {wo_id} carries no observations list; a ledger with no check-run cannot certify a head")
    if any(not isinstance(o, dict) for o in observations):
        fail(f"{source} for {wo_id} carries an observation that is not a json object")
    matches = [o for o in observations
               if o.get("context") == "Governance" and o.get("head") == head]
    if not matches:
        fail(f"{wo_id} names {head[:9]} as its certified head but {source} has no Governance observation "
             "for that exact commit")
    if len(matches) > 1:
        fail(f"{wo_id} certified head {head[:9]} matches {len(matches)} Governance observations in {source}; "
             "an ambiguous ledger certifies nothing")
    observed = matches[0]
    if observed.get("status") != "completed":
        fail(f"{wo_id} certified head {head[:9]} has an incomplete Governance run in {source}: "
             f"{observed.get('status')!r}")
    if observed.get("conclusion") != "success":
        fail(f"{wo_id} certified head {head[:9]} Governance run concluded {observed.get('conclusion')!r} "
             f"in {source}; a failure is never a certification")
    if observed.get("result") not in (None, "PASS"):
        fail(f"{wo_id} certified head {head[:9]} carries result {observed.get('result')!r} beside a "
             f"{observed.get('conclusion')!r} conclusion in {source}; the ledger contradicts itself")
    return observed


def section(text, heading):
    lines = text.splitlines()
    try:
        start = lines.index(heading) + 1
    except ValueError:
        fail("checkpoint missing heading: " + heading)
    vals = []
    for line in lines[start:]:
        if line.startswith("## "):
            break
        if line.strip():
            vals.append(line.strip())
    if not vals:
        fail("checkpoint heading has no value: " + heading)
    return "\n".join(vals)


def check_artifacts():
    for rel in REQUIRED:
        if not (ROOT / rel).is_file():
            fail("missing required file: " + rel)
        if (ROOT / rel).stat().st_size == 0:
            fail("required file is empty: " + rel)


def check_no_vendoring():
    for name in VENDORED_TREES:
        path = ROOT / name
        if path.is_dir():
            fail(f"vendored external workspace present at repository root: {name}/ (AGENTS.md forbids it)")
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(ROOT)
        if any(part in {".git", "__pycache__", "node_modules"} for part in rel.parts):
            continue
        suffix = path.suffix.lower()
        if suffix in BINARY_ARTIFACTS:
            fail(f"generated/executable artifact committed at {rel.as_posix()}; "
                 "engine builds and binaries stay outside the repository (ADR-0001/ADR-0002)")
        if path.name in ENGINE_TREE_MARKERS or suffix in ENGINE_TREE_SUFFIXES:
            fail(f"engine-tree fingerprint committed at {rel.as_posix()}; "
                 "the Godot source tree is an external pinned clone, never vendored (WO-0002 out of scope)")


def check_scope_coverage():
    scope = read(SCOPE_DOC)
    block = re.search(r"## Product scope to plan\n(.*?)\n\n", scope, re.S)
    if not block:
        fail(f"{SCOPE_DOC} no longer carries the 'Product scope to plan' block the module index is derived from")
    families = [f.strip() for f in block.group(1).strip().rstrip(".").split(";") if f.strip()]
    if len(families) < 2:
        fail("scope product list is unparsable; the coverage gate would pass on nothing")
    index = read(MODULE_INDEX_DOC)
    missing = [f for f in families if f not in index]
    if missing:
        fail("Master Module Index does not cover scope families: " + ", ".join(missing))


def check_line_endings():
    if "* text=auto eol=lf" not in read(".gitattributes"):
        fail(".gitattributes must pin text to LF: a CRLF working tree makes HIVE's container report every "
             "tracked file as modified, and its staleness guard then refuses canonical retrieval")
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path.suffix not in TEXT_SUFFIXES:
            continue
        if any(part in {".git", "__pycache__", "node_modules"} for part in path.relative_to(ROOT).parts):
            continue
        if b"\r\n" in path.read_bytes():
            fail("working tree carries CRLF in " + path.relative_to(ROOT).as_posix()
                 + "; check out with .gitattributes honoured (core.autocrlf must not override it)")


def check_checkpoint_bridge():
    cp = read(HIVE_GOV[0])
    for h in HEADINGS:
        section(cp, h)
    bridge = read(".engineering/CHECKPOINT.md")
    machine = load_json(".engineering/CHECKPOINT.json")
    if machine.get("canonicalCheckpoint") != HIVE_GOV[0]:
        fail("machine checkpoint canonical path mismatch")
    if machine.get("viewStatus") != "DERIVED_VIEW":
        fail("checkpoint bridge must declare viewStatus DERIVED_VIEW; Git and the canonical checkpoint outrank it")
    for field, h in SHARED.items():
        value = section(cp, h)
        if section(bridge, h) != value or machine.get(field) != value:
            fail("checkpoint bridge drift for " + field)
    if not re.search(r"ISORYN-WO-\d{4}", section(cp, "## IN PROGRESS")):
        fail("canonical checkpoint IN PROGRESS does not name an active Work Order")


def check_pins():
    profile = load_json(".engineering/gef/GEF-PROJECT-PROFILE.json")
    if profile.get("gefVersion") != "1.0.0":
        fail("GEF version mismatch")
    manifest = load_json(".engineering/BOOTSTRAP-MANIFEST.json")
    if manifest.get("gef", {}).get("releaseCommit") != GEF_PIN:
        fail("GEF pin mismatch")
    if manifest.get("hive", {}).get("releaseCommit") != HIVE_PIN:
        fail("HIVE pin mismatch")
    bridge = load_json(".engineering/gef/GEF-SOURCE-BRIDGE.json")
    if bridge.get("canonicalCheckpoint") != HIVE_GOV[0]:
        fail("GEF source bridge does not point at the canonical checkpoint")
    if not bridge.get("domains"):
        fail("GEF source bridge declares no governed domains")


def check_machine_paths():
    targets = [p for glob in PORTABLE_CONFIG_GLOBS for p in sorted(ROOT.glob(glob))]
    targets += [(ROOT / rel) for rel in PORTABLE_CONFIG]
    for path in targets:
        if not path.is_file():
            continue
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if MACHINE_PATH.search(line) and not line.lstrip().startswith("#"):
                rel = path.relative_to(ROOT).as_posix()
                fail(f"portable config carries a machine path ({rel}:{number}); keep it in .env or documentation")


def check_mcp_surface():
    config = read(".codex/config.toml")
    enabled = re.search(r"enabled_tools\s*=\s*\[(.*?)\]", config, re.S)
    if not enabled:
        fail(".codex/config.toml does not declare an enabled_tools allowlist for the HIVE MCP server")
    tools = tuple(re.findall(r'"([^"]+)"', enabled.group(1)))
    if set(tools) != set(MCP_TOOLS):
        fail(f"MCP allowlist drifted from the pinned HIVE core surface: {sorted(tools)}")
    if "required = true" not in config:
        fail("HIVE MCP server must be required so a missing bridge cannot be silently ignored")
    launcher = read("scripts/hive_mcp.py")
    if "app.mcp_server" not in launcher:
        fail("HIVE MCP launcher no longer starts the pinned HIVE MCP server module")
    agents = read("AGENTS.md")
    for tool in MCP_TOOLS:
        if tool not in agents:
            fail("AGENTS.md omits stable MCP tool " + tool)
    for invented in ("code.search", "run.record", "decision.list", "telemetry.", "project.open"):
        if invented in agents or invented in config:
            fail(f"unsupported HIVE v1.0.0 MCP tool advertised: {invented}")


def check_governance_policies():
    agents = read("AGENTS.md")
    if "downloadable PDF artifacts" not in agents:
        fail("AGENTS.md prompt artifact policy was removed or rewritten")
    if "Review-first direct correction policy" not in agents:
        fail("AGENTS.md review-first correction policy was removed")
    autofix = read(".engineering/REVIEW-AUTOFIX-POLICY.md")
    for token in ("CHAT_FIXABLE", "EXECUTOR_REQUIRED", "residual"):
        if token not in autofix:
            fail("review-autofix policy lost its " + token + " classification")


def check_workflow():
    text = read(".github/workflows/governance.yml")
    job = re.search(r"(?m)^  [A-Za-z0-9_.-]+:\n(?:.*\n)*?    name: (.+)$", text)
    if not job or job.group(1).strip().strip('"') != "Governance":
        fail("no job named Governance; the ruleset requires the exact check context 'Governance'")
    if not re.search(r"(?m)^name: Governance$", text):
        fail("workflow display name must be Governance")
    if "permissions:" not in text or "contents: read" not in text:
        fail("workflow must declare least-privilege GITHUB_TOKEN permissions (contents: read)")
    for action, ref in re.findall(r"uses: ([^@\s]+)@([^\s#]+)", text):
        if not re.fullmatch(r"[0-9a-f]{40}", ref):
            fail(f"action {action} is not pinned to an immutable commit SHA")
    for command in ("validate_governance.py", "unittest discover"):
        if command not in text:
            fail("governance workflow no longer runs " + command)


def check_desired_state():
    settings = load_json(".engineering/github/repository-settings.json")
    for key, want in (("allow_merge_commit", False), ("allow_rebase_merge", False),
                      ("allow_squash_merge", True), ("delete_branch_on_merge", True),
                      ("allow_update_branch", True)):
        if settings.get(key) != want:
            fail(f"repository-settings.json must fix {key} to {want}")
    ruleset = load_json(".engineering/github/ruleset-main-governance.json")
    if ruleset.get("name") != "main-governance" or ruleset.get("enforcement") != "active":
        fail("ruleset manifest must define an active main-governance ruleset")
    if ruleset.get("conditions", {}).get("ref_name", {}).get("include") != ["refs/heads/main"]:
        fail("main-governance must target only refs/heads/main")
    if ruleset.get("bypass_actors") != []:
        fail("main-governance must not grant bypass actors without an approved policy")
    rules = {rule["type"]: rule.get("parameters", {}) for rule in ruleset.get("rules", [])}
    for missing in ("deletion", "non_fast_forward", "required_linear_history", "pull_request",
                    "required_status_checks"):
        if missing not in rules:
            fail("main-governance is missing the " + missing + " rule")
    if "update" in rules:
        fail("main-governance must not use the restrict-updates rule without an approved bypass actor; "
             "that combination blocks pull-request merges into main")
    pr = rules["pull_request"]
    if pr.get("required_review_thread_resolution") is not True:
        fail("main-governance must require resolved review threads")
    if pr.get("require_code_owner_review") or pr.get("require_last_push_approval") \
            or pr.get("required_approving_review_count", 0) > 0:
        fail("main-governance must not require a human approval that a single-owner repository cannot satisfy")
    contexts = [c.get("context") for c in rules["required_status_checks"].get("required_status_checks", [])]
    if contexts != ["Governance"]:
        fail("required status checks must name exactly the Governance context")
    dependabot = read(".github/dependabot.yml")
    if "github-actions" not in dependabot:
        fail("dependabot.yml must track github-actions")


def check_governance_namespaces():
    for wo_id, order_rel, bundle_rel in work_order_bundles():
        body = read(order_rel)
        for heading in ("OBJECTIVE", "HIVE PREFLIGHT", "CANONICAL BASIS", "CONTEXT BUDGET", "RISK/ASSURANCE",
                        "SCOPE", "OUT OF SCOPE", "ACCEPTANCE CRITERIA", "TESTS", "EVIDENCE", "DELIVERABLES",
                        "REVIEW FORMAT", "STOP CONDITION"):
            if not re.search(r"(?m)^" + re.escape(heading) + r":", body):
                fail(f"{wo_id} omits the {heading} section required by GEF-EXECUTION-PROTOCOL.md")
        lock = ROOT / ".engineering/context-locks" / (wo_id + ".json")
        if not lock.is_file():
            fail("missing Context Lock for " + wo_id)
        locked = json.loads(lock.read_text(encoding="utf-8"))
        for field in ("schemaVersion", "workOrder", "baseSha", "branch", "canonicalSources", "staleWhen"):
            if not locked.get(field):
                fail(f"{wo_id} Context Lock has no {field}")
        if not SHA.match(str(locked["baseSha"])):
            fail(f"{wo_id} Context Lock baseSha is not an exact commit")
        evidence = bundle_payload(bundle_rel, wo_id)
        for field in ("schemaVersion", "workOrder", "baseSha", "headSha", "candidateHeadSha", "branch",
                      "hivePreflight", "checks", "unsupportedPlatformFeatures", "residualRisks",
                      "proposedCheckpointDelta", "stopCondition"):
            if field not in evidence:
                fail(f"{wo_id} Evidence Bundle has no {field}")
        for sha in ("baseSha", "headSha", "candidateHeadSha"):
            if not SHA.match(str(evidence[sha])):
                fail(f"{wo_id} Evidence Bundle {sha} is not an exact commit")
        for name, result in evidence["checks"].items():
            if result not in RESULT_VOCABULARY:
                fail(f"{wo_id} Evidence Bundle check '{name}' uses undocumented result '{result}'")
        for deferred in [d for d in evidence["unsupportedPlatformFeatures"]
                         if d.get("result") == "DEFERRED_BY_WO"]:
            if "'" not in deferred.get("detail", ""):
                fail(f"{wo_id} defers '{deferred.get('capability')}' without quoting the authorizing clause")
        delta = ROOT / ".engineering/evidence" / (wo_id + "-CHECKPOINT-DELTA.md")
        if evidence.get("proposedCheckpointDelta", {}).get("status") == "PROPOSED_ONLY" and not delta.is_file():
            fail(wo_id + " proposes a checkpoint delta but the delta file is absent")
        if not str(evidence.get("pr", {}).get("url", "")).startswith("https://github.com/"):
            fail(wo_id + " Evidence Bundle does not name the open pull request it belongs to")


def verify_delivery_head(evidence, ledger, ledger_source, wo_id):
    """Check a record against one parsed CI ledger. Pure so a test can hand it a contradicting pair."""
    semantics = evidence.get("deliveryHeadSemantics")
    if not isinstance(semantics, str) or not semantics.strip():
        fail(f"{wo_id} has delivery-head fields without deliveryHeadSemantics stating what they mean")
    for path in CERTIFIED_HEAD_FIELDS + (EXECUTION_HEAD_FIELD,):
        if path not in semantics:
            fail(f"{wo_id} deliveryHeadSemantics does not name {path}; a field under the contract must be "
                 "declared with the role it carries")

    heads = {}
    for path in CERTIFIED_HEAD_FIELDS:
        value = declared(evidence, path, wo_id)
        if not SHA.match(str(value)):
            fail(f"{wo_id} {path} is not an exact commit: {value!r}")
        heads[path] = str(value)
    certified = set(heads.values())
    if len(certified) > 1:
        fail(f"{wo_id} certified-head fields disagree: "
             + ", ".join(f"{k}={v[:9]}" for k, v in sorted(heads.items()))
             + "; the certified head is one commit, so a rebind moves every field or redefines them")
    certified_head = certified.pop()

    for key in ("workOrder", "branch"):
        if ledger.get(key) and ledger[key] != evidence.get(key):
            fail(f"{wo_id} certifies its head through {ledger_source} declaring {key}={ledger[key]!r}, "
                 f"not {evidence.get(key)!r}")
    observed = certified_observation(ledger, certified_head, wo_id, ledger_source)
    embedded = evidence.get("governanceRun")
    if isinstance(embedded, dict):
        mirror = certified_observation(embedded, certified_head, wo_id, "the run embedded in the bundle")
        if mirror.get("run") != observed.get("run"):
            fail(f"{wo_id} embeds a different Governance run for {certified_head[:9]} than its CI ledger: "
                 f"{mirror.get('run')!r} against {observed.get('run')!r}")

    execution = str(declared(evidence, EXECUTION_HEAD_FIELD, wo_id))
    if not SHA.match(execution):
        fail(f"{wo_id} {EXECUTION_HEAD_FIELD} is not an exact commit: {execution!r}")
    state = declared(evidence, "commandsExecutedAtTreeState", wo_id)
    if state not in TREE_STATES:
        fail(f"{wo_id} {EXECUTION_HEAD_FIELD} tree state {state!r} is not "
             + " or ".join(sorted(TREE_STATES)))
    admits_dirty = "uncommitted" in str(declared(evidence, "commandsExecutedAtNote", wo_id)).lower()
    if (state == "WORKING_TREE_DIRTY") != admits_dirty:
        fail(f"{wo_id} declares {EXECUTION_HEAD_FIELD} tree state {state!r} while its commandsExecutedAtNote "
             + ("describes uncommitted files" if admits_dirty else "does not describe the tree it used"))
    execution_rows = evidence.get("checkExecutionHeads")
    if isinstance(execution_rows, dict):
        row = execution_rows.get("deterministicCommands")
        if isinstance(row, dict) and row.get("head") and str(row["head"]) != execution:
            fail(f"{wo_id} ran deterministic commands at {execution[:9]} but checkExecutionHeads names "
                 f"{str(row['head'])[:9]}")
    for row in evidence.get("tests", []) if isinstance(evidence.get("tests"), list) else []:
        if not isinstance(row, dict) or "treeState" not in row:
            continue
        named = str(row.get("command", "?"))[:48]
        if not SHA.match(str(row.get("head"))):
            fail(f"{wo_id} test row {named!r} names a head that is not an exact commit: {row.get('head')!r}")
        if row["head"] != execution or row["treeState"] != state:
            fail(f"{wo_id} test row {named!r} claims {str(row.get('head'))[:9]}/{row['treeState']} while "
                 f"{EXECUTION_HEAD_FIELD} claims {execution[:9]}/{state}; a command cannot be credited to a "
                 "tree it did not run against")
    roles = evidence.get("headRoleTable")
    if isinstance(roles, dict):
        for label, value in (("execution head", execution), ("certified head", certified_head)):
            if value not in roles:
                fail(f"{wo_id} {label} {value[:9]} holds no row in headRoleTable; every SHA in this record "
                     "must declare exactly one role")
    reported = declared(evidence, "checks." + GATE_HEAD_REBINDING, wo_id)
    if reported != "PASS":
        fail(f"{wo_id} reports {GATE_HEAD_REBINDING} as {reported!r} in a record whose binding this "
             "validator just enforced; the report and the code must agree")
    return certified_head, execution


def delivery_head_binding(evidence, wo_id):
    """Enforce a record's delivery-head contract against the CI ledger it names. Reads no network.

    A record that does not declare `deliveryHeadSemantics` is outside this contract: WO-0001's headSha names
    a code head whose bundle commit carries the run, which is what its own headBindingNote documents. The
    gate validates the semantics a record declares instead of forcing one shape onto every Work Order, and it
    keeps the certified head separate from the execution head because those are different commits as soon as
    evidence-only commits follow the bundle.
    """
    receipt = str(declared(evidence, "deliveryHeadCiReceipt", wo_id))
    return verify_delivery_head(evidence, read_ci_ledger(receipt, wo_id), receipt, wo_id)


def check_head_rebinding():
    """Apply the delivery-head contract to every bundle that declares it. Static receipt check, no API call."""
    bound = []
    for wo_id, _order, bundle_rel in work_order_bundles():
        evidence = bundle_payload(bundle_rel, wo_id)
        if "deliveryHeadSemantics" not in evidence:
            continue
        certified_head, execution_head = delivery_head_binding(evidence, wo_id)
        bound.append((wo_id, certified_head, execution_head))
    return bound


def check_stale_claims():
    bootstrap = read("docs/GEF-BOOTSTRAP.md")
    if "Installed surfaces" not in bootstrap:
        fail("docs/GEF-BOOTSTRAP.md no longer states which GEF surfaces are installed")
    for surface in ("work-orders", "context-locks", "evidence"):
        if not (ROOT / ".engineering" / surface).is_dir():
            fail("docs/GEF-BOOTSTRAP.md claims the " + surface + " namespace but it does not exist")
        if surface + "/" not in bootstrap:
            fail("docs/GEF-BOOTSTRAP.md must document the " + surface + " namespace it claims")
    deployment = read("docs/project-brain/12-LOCAL-DEPLOYMENT.md")
    if "deferred" not in deployment:
        fail("deployment doc must keep its deferred-toolchain boundary explicit")
    if "No engine implementation is authorized yet" not in read("docs/project-brain/01-PROJECT-OVERVIEW.md"):
        fail("project overview must keep the current no-implementation boundary")
    if "unmeasured performance/quality claims" not in read("docs/project-brain/03-SCOPE.md"):
        fail("scope must keep the ban on unmeasured performance and quality claims")
    if "No shared-database coupling" not in read("docs/project-brain/04-ARCHITECTURE.md"):
        fail("architecture must keep the no-shared-database boundary with HIVE/CORE/IRIS")


def main() -> int:
    check_artifacts()
    check_no_vendoring()
    check_scope_coverage()
    check_line_endings()
    check_checkpoint_bridge()
    check_pins()
    check_machine_paths()
    check_mcp_surface()
    check_governance_policies()
    check_workflow()
    check_desired_state()
    check_governance_namespaces()
    bound = check_head_rebinding()
    check_stale_claims()
    print("ISORYN governance validation: PASS")
    print("GEF: v1.0.0 @ " + GEF_PIN)
    print("HIVE: v1.0.0 @ " + HIVE_PIN)
    print(f"Required artifacts: {len(REQUIRED)}")
    print(f"Governed MCP tools: {len(MCP_TOOLS)}")
    for wo_id, certified_head, execution_head in bound:
        print(f"{GATE_HEAD_REBINDING}: {wo_id} certified @ {certified_head[:9]}, "
              f"commands ran @ {execution_head[:9]}")
    if not bound:
        print(f"{GATE_HEAD_REBINDING}: no bundle declares the delivery-head contract")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except SystemExit as exc:
        if isinstance(exc.code, str):
            print(exc.code, file=sys.stderr)
            raise SystemExit(1)
        raise
