import copy, io, json, re, unittest
from contextlib import redirect_stdout
from pathlib import Path

import scripts.validate_governance as vg

ROOT = Path(__file__).resolve().parents[1]


def load(rel):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def set_path(obj, path, value):
    parts = path.split(".")
    for part in parts[:-1]:
        obj = obj[part]
    obj[parts[-1]] = value


def drop_path(obj, path):
    parts = path.split(".")
    for part in parts[:-1]:
        obj = obj[part]
    del obj[parts[-1]]


class ValidatorGateTests(unittest.TestCase):
    def test_full_tree_passes(self):
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            self.assertEqual(vg.main(), 0)
        self.assertIn("ISORYN governance validation: PASS", buffer.getvalue())

    def test_required_list_has_no_duplicates(self):
        self.assertEqual(len(vg.REQUIRED), len(set(vg.REQUIRED)))

    def test_every_required_artifact_resolves_to_a_file(self):
        for rel in vg.REQUIRED:
            self.assertTrue((ROOT / rel).is_file(), rel)

    def test_working_tree_is_container_readable(self):
        self.assertIn(".gitattributes", vg.REQUIRED)
        self.assertIn("* text=auto eol=lf", (ROOT / ".gitattributes").read_text(encoding="utf-8"))
        vg.check_line_endings()

    def test_missing_checkpoint_heading_fails_closed(self):
        text = "## STATUS\nBOOTSTRAP ACTIVE\n"
        with self.assertRaises(SystemExit) as ctx:
            vg.section(text, "## NEXT STEP")
        self.assertIn("missing heading", str(ctx.exception))

    def test_empty_checkpoint_heading_fails_closed(self):
        text = "## STATUS\n## VERSION\n1.0\n"
        with self.assertRaises(SystemExit) as ctx:
            vg.section(text, "## STATUS")
        self.assertIn("no value", str(ctx.exception))

    def test_checkpoint_bridge_drift_is_detected(self):
        canonical = "## STATUS\nBOOTSTRAP ACTIVE\n\n## VERSION\n1\n"
        bridge = "## STATUS\nSOMETHING ELSE\n\n## VERSION\n1\n"
        with self.assertRaises(SystemExit) as ctx:
            for field, heading in vg.SHARED.items():
                value = vg.section(canonical, heading)
                if vg.section(bridge, heading) != value:
                    vg.fail("checkpoint bridge drift for " + field)
        self.assertIn("drift for status", str(ctx.exception))


class HeadRebindingGateTests(unittest.TestCase):
    """CD03: a record may name a certified head only its own versioned CI ledger proves, and statically.

    The fixtures are the shipped WO-0002 record and ledger, mutated one claim at a time, so every negative
    exercises the gate's real refusal instead of restating its arithmetic.
    """

    WO = "ISORYN-WO-0002"
    BUNDLE = ".engineering/evidence/ISORYN-WO-0002-EVIDENCE.md"

    def record(self):
        evidence = vg.bundle_payload(self.BUNDLE, self.WO)
        receipt = evidence["deliveryHeadCiReceipt"]
        return copy.deepcopy(evidence), load(receipt), receipt

    def assert_refuses(self, evidence, ledger, receipt, fragment):
        with self.assertRaises(SystemExit) as ctx:
            vg.verify_delivery_head(evidence, ledger, receipt, self.WO)
        self.assertIn(fragment, str(ctx.exception))

    def matching(self, ledger, head):
        return [o for o in ledger["observations"]
                if o.get("context") == "Governance" and o.get("head") == head]

    def test_shipped_record_passes_the_gate_it_declares(self):
        evidence, ledger, receipt = self.record()
        certified, execution = vg.verify_delivery_head(evidence, ledger, receipt, self.WO)
        self.assertEqual(certified, evidence["headSha"])
        self.assertEqual(execution, evidence["commandsExecutedAtHead"])
        self.assertEqual(len(self.matching(ledger, certified)), 1)

    def test_validator_flow_binds_the_declaring_record(self):
        bound = {wo: (certified, execution) for wo, certified, execution in vg.check_head_rebinding()}
        self.assertIn(self.WO, bound)
        evidence, _ledger, _receipt = self.record()
        self.assertEqual(bound[self.WO], (evidence["headSha"], evidence["commandsExecutedAtHead"]))

    def test_gate_symbol_is_called_from_the_validator_flow(self):
        source = (ROOT / "scripts/validate_governance.py").read_text(encoding="utf-8")
        self.assertIn("def check_head_rebinding(", source)
        self.assertIn("bound = check_head_rebinding()", source.split("def main()")[1])

    def test_every_certified_field_must_name_the_same_head(self):
        for path in vg.CERTIFIED_HEAD_FIELDS:
            evidence, ledger, receipt = self.record()
            set_path(evidence, path, "0" * 40)
            self.assert_refuses(evidence, ledger, receipt, path + "=" + "0" * 9)

    def test_certified_head_must_be_an_exact_commit(self):
        evidence, ledger, receipt = self.record()
        set_path(evidence, "headSha", evidence["headSha"][:9])
        self.assert_refuses(evidence, ledger, receipt, "headSha is not an exact commit")

    def test_absent_certified_field_fails_closed(self):
        evidence, ledger, receipt = self.record()
        drop_path(evidence, "github.deliveredHeadSha")
        self.assert_refuses(evidence, ledger, receipt, "has no github.deliveredHeadSha")

    def test_contract_must_declare_every_field_it_enforces(self):
        evidence, ledger, receipt = self.record()
        evidence["deliveryHeadSemantics"] = evidence["deliveryHeadSemantics"].replace(
            "commandsExecutedAtHead", "someOtherHeadField")
        self.assert_refuses(evidence, ledger, receipt, "does not name commandsExecutedAtHead")

    def test_missing_governance_observation_certifies_nothing(self):
        evidence, ledger, receipt = self.record()
        head = evidence["headSha"]
        ledger["observations"] = [o for o in ledger["observations"] if o.get("head") != head]
        self.assert_refuses(evidence, ledger, receipt, "no Governance observation for that exact commit")

    def test_duplicated_observation_is_ambiguous_not_stronger(self):
        evidence, ledger, receipt = self.record()
        ledger["observations"].append(dict(self.matching(ledger, evidence["headSha"])[0]))
        self.assert_refuses(evidence, ledger, receipt, "an ambiguous ledger certifies nothing")

    def test_unfinished_run_is_not_a_certification(self):
        evidence, ledger, receipt = self.record()
        self.matching(ledger, evidence["headSha"])[0]["status"] = "in_progress"
        self.assert_refuses(evidence, ledger, receipt, "incomplete Governance run")

    def test_failed_run_is_never_reported_as_certified(self):
        evidence, ledger, receipt = self.record()
        observed = self.matching(ledger, evidence["headSha"])[0]
        observed["conclusion"] = "failure"
        self.assert_refuses(evidence, ledger, receipt, "a failure is never a certification")

    def test_ledger_that_contradicts_its_own_result_fails_closed(self):
        evidence, ledger, receipt = self.record()
        self.matching(ledger, evidence["headSha"])[0]["result"] = "FAIL"
        self.assert_refuses(evidence, ledger, receipt, "the ledger contradicts itself")

    def test_embedded_copy_must_agree_with_the_versioned_ledger(self):
        evidence, ledger, receipt = self.record()
        evidence["governanceRun"]["observations"] = [
            dict(o, run="https://example.invalid/actions/runs/1/job/1")
            if o.get("head") == evidence["headSha"] else o
            for o in evidence["governanceRun"]["observations"]]
        self.assert_refuses(evidence, ledger, receipt, "embeds a different Governance run")

    def test_ledger_from_another_branch_or_work_order_is_rejected(self):
        evidence, ledger, receipt = self.record()
        ledger["branch"] = "isoryn-some-other-branch"
        self.assert_refuses(evidence, ledger, receipt, "declaring branch")
        evidence, ledger, receipt = self.record()
        ledger["workOrder"] = "ISORYN-WO-0001"
        self.assert_refuses(evidence, ledger, receipt, "declaring workOrder")

    def test_malformed_ledgers_fail_closed(self):
        with self.assertRaises(SystemExit) as bad_json:
            vg.ci_ledger('{"observations": [', ".engineering/evidence/wo-0002/ci.json")
        self.assertIn("is not valid JSON", str(bad_json.exception))
        with self.assertRaises(SystemExit) as empty:
            vg.ci_ledger('{"observations": []}', ".engineering/evidence/wo-0002/ci.json")
        self.assertIn("carries no observations list", str(empty.exception))

    def test_a_copy_that_cannot_certify_fails_closed(self):
        evidence, ledger, receipt = self.record()
        evidence["governanceRun"] = {"workOrder": self.WO, "branch": evidence["branch"]}
        self.assert_refuses(evidence, ledger, receipt, "carries no observations list")

    def test_receipt_must_point_inside_the_evidence_tree(self):
        for escape in ("../../Windows/win.ini", "/etc/passwd", ".engineering/work-orders/x.json"):
            with self.assertRaises(SystemExit) as ctx:
                vg.read_ci_ledger(escape, self.WO)
            self.assertIn("outside .engineering/evidence/", str(ctx.exception))
        with self.assertRaises(SystemExit) as missing:
            vg.read_ci_ledger(".engineering/evidence/wo-0002/not-recorded.json", self.WO)
        self.assertIn("is not in the repository", str(missing.exception))

    def test_execution_head_must_state_the_tree_it_ran_on(self):
        evidence, ledger, receipt = self.record()
        set_path(evidence, "commandsExecutedAtTreeState", "NOT_RECORDED")
        self.assert_refuses(evidence, ledger, receipt, "tree state")
        evidence, ledger, receipt = self.record()
        set_path(evidence, "commandsExecutedAtTreeState", "CLEAN")
        self.assert_refuses(evidence, ledger, receipt, "while its commandsExecutedAtNote")
        evidence, ledger, receipt = self.record()
        set_path(evidence, "commandsExecutedAtTreeState", "WORKING_TREE_DIRTY")
        set_path(evidence, "commandsExecutedAtNote", "ran against a committed tree")
        self.assert_refuses(evidence, ledger, receipt, "while its commandsExecutedAtNote")

    def test_execution_head_must_match_the_declared_execution_row(self):
        evidence, ledger, receipt = self.record()
        set_path(evidence, "checkExecutionHeads.deterministicCommands.head", "f" * 40)
        self.assert_refuses(evidence, ledger, receipt, "checkExecutionHeads names")

    def test_command_rows_cannot_be_credited_to_a_tree_they_did_not_run_on(self):
        for mutate, fragment in (({"head": "e" * 40}, "commandsExecutedAtHead claims"),
                                 ({"treeState": "CLEAN"}, "cannot be credited"),
                                 ({"head": "not-a-commit"}, "not an exact commit")):
            evidence, ledger, receipt = self.record()
            row = next(r for r in evidence["tests"] if "treeState" in r)
            row.update(mutate)
            self.assert_refuses(evidence, ledger, receipt, fragment)

    def test_heads_under_the_contract_need_a_declared_role(self):
        evidence, ledger, receipt = self.record()
        del evidence["headRoleTable"][evidence["headSha"]]
        self.assert_refuses(evidence, ledger, receipt, "holds no row in headRoleTable")
        evidence, ledger, receipt = self.record()
        del evidence["headRoleTable"][evidence["commandsExecutedAtHead"]]
        self.assert_refuses(evidence, ledger, receipt, "execution head")

    def test_report_row_must_agree_with_the_validator(self):
        evidence, ledger, receipt = self.record()
        set_path(evidence, "checks." + vg.GATE_HEAD_REBINDING, "UNKNOWN")
        self.assert_refuses(evidence, ledger, receipt, "the report and the code must agree")

    def test_records_under_a_different_convention_stay_outside_this_gate(self):
        wo1 = vg.bundle_payload(".engineering/evidence/ISORYN-WO-0001-EVIDENCE.md", "ISORYN-WO-0001")
        self.assertNotIn("deliveryHeadSemantics", wo1)
        ledger = load(".engineering/evidence/ci.json")
        self.assertFalse(self.matching(ledger, wo1["headSha"]),
                         "WO-0001's head is a code head, not a ledger-certified delivery head")
        self.assertEqual([wo for wo, _c, _e in vg.check_head_rebinding()], [self.WO])


class PortableConfigTests(unittest.TestCase):
    def test_machine_path_pattern(self):
        for hit in (r'path = "D:\Hive\projects\x"', 'root=/home/dev/x', 'root=/Users/dev/x'):
            self.assertTrue(vg.MACHINE_PATH.search(hit), hit)
        for miss in ('canonicalCheckpoint: docs/project-brain/13-CHECKPOINT.md',
                     'HIVE_API_URL=http://127.0.0.1:8000', 'relative-path isoryn-engine',
                     '$Repository = "https://github.com/KayzenRoot/isoryn-engine.git"'):
            self.assertIsNone(vg.MACHINE_PATH.search(miss), miss)

    def test_no_machine_path_in_scripts_or_env_example(self):
        vg.check_machine_paths()


class McpContractTests(unittest.TestCase):
    def test_documented_surface_is_the_pinned_core_surface(self):
        self.assertEqual(len(vg.MCP_TOOLS), 7)
        self.assertEqual(set(vg.MCP_TOOLS), {
            "project.list", "project.status", "context.build", "context.search",
            "memory.search", "memory.get", "checkpoint.read"})

    def test_codex_config_allowlist_matches(self):
        config = (ROOT / ".codex/config.toml").read_text(encoding="utf-8")
        declared = set(re.findall(r'"([^"]+)"', re.search(r"enabled_tools\s*=\s*\[(.*?)\]", config, re.S).group(1)))
        self.assertEqual(declared, set(vg.MCP_TOOLS))
        self.assertIn("required = true", config)

    def test_launcher_targets_the_pinned_module_and_no_proxy_binary(self):
        launcher = (ROOT / "scripts/hive_mcp.py").read_text(encoding="utf-8")
        self.assertIn("app.mcp_server", launcher)
        self.assertNotIn("npx", launcher)

    def test_agents_md_does_not_advertise_unsupported_tools(self):
        agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        for invented in ("code.search", "run.record", "decision.list", "telemetry.", "project.open"):
            self.assertNotIn(invented, agents)


class DesiredStateTests(unittest.TestCase):
    def test_configurator_reads_rules_before_applying_them(self):
        script = (ROOT / "scripts/configure-github.ps1").read_text(encoding="utf-8")
        self.assertIn("before-ruleset-$", script)
        self.assertLess(script.index("before-ruleset-$"), script.index("Upserting ruleset"))

    def test_configurator_refuses_a_self_locking_ruleset(self):
        script = (ROOT / "scripts/configure-github.ps1").read_text(encoding="utf-8")
        self.assertIn('-contains "update"', script)
        self.assertIn("make main unmergeable", script)

    def test_ruleset_manifest_shape(self):
        ruleset = load(".engineering/github/ruleset-main-governance.json")
        self.assertEqual(ruleset["name"], "main-governance")
        self.assertEqual(ruleset["conditions"]["ref_name"]["include"], ["refs/heads/main"])
        self.assertEqual(ruleset["bypass_actors"], [])
        rules = {r["type"]: r.get("parameters", {}) for r in ruleset["rules"]}
        self.assertEqual(
            set(rules),
            {"deletion", "non_fast_forward", "required_linear_history", "pull_request",
             "required_status_checks"})
        self.assertNotIn("update", rules)
        self.assertEqual([c["context"] for c in rules["required_status_checks"]["required_status_checks"]],
                         ["Governance"])
        self.assertIs(rules["pull_request"]["required_review_thread_resolution"], True)
        self.assertIs(rules["pull_request"]["require_code_owner_review"], False)
        self.assertEqual(rules["pull_request"]["required_approving_review_count"], 0)

    def test_workflow_emits_the_required_status_context(self):
        text = (ROOT / ".github/workflows/governance.yml").read_text(encoding="utf-8")
        self.assertIn("name: Governance", text)
        for _action, ref in re.findall(r"uses: ([^@\s]+)@([^\s#]+)", text):
            self.assertRegex(ref, r"^[0-9a-f]{40}$")

    def test_governance_namespaces_exist_for_every_work_order(self):
        for order in sorted((ROOT / ".engineering/work-orders").glob("*.md")):
            wo_id = re.match(r"([A-Z]+-[A-Z]+-\d+)", order.stem).group(1)
            self.assertTrue((ROOT / ".engineering/context-locks" / (wo_id + ".json")).is_file(), wo_id)
            bundle = ROOT / ".engineering/evidence" / (wo_id + "-EVIDENCE.md")
            self.assertTrue(bundle.is_file(), wo_id)
            block = re.search(r"(?m)^```json\n(.*?)\n```", bundle.read_text(encoding="utf-8"), re.S)
            self.assertIsNotNone(block, wo_id)
            payload = json.loads(block.group(1))
            self.assertTrue(set(payload["checks"].values()) <= vg.RESULT_VOCABULARY, payload["checks"])
            self.assertEqual(payload["workOrder"], wo_id)


class DiscoveryBaselineTests(unittest.TestCase):
    def test_every_scope_family_has_an_index_row(self):
        vg.check_scope_coverage()
        scope = (ROOT / vg.SCOPE_DOC).read_text(encoding="utf-8")
        block = re.search(r"## Product scope to plan\n(.*?)\n\n", scope, re.S).group(1)
        families = [f.strip() for f in block.strip().rstrip(".").split(";") if f.strip()]
        index = (ROOT / vg.MODULE_INDEX_DOC).read_text(encoding="utf-8")
        rows = re.findall(r"(?m)^\| (M-\d\d) \|", index)
        self.assertEqual(len(families), len(rows), "one index row per scope family")
        self.assertEqual(len(rows), len(set(rows)), "duplicate module index row")

    def test_coverage_gate_uses_the_documented_vocabulary(self):
        self.assertTrue(hasattr(vg, "check_scope_coverage"))
        self.assertIn(vg.MODULE_INDEX_DOC, vg.REQUIRED)
        self.assertTrue(".exe" in vg.BINARY_ARTIFACTS and "SConstruct" in vg.ENGINE_TREE_MARKERS)

    def test_repository_carries_no_engine_binary_or_tree_fingerprint(self):
        vg.check_no_vendoring()

    def test_adrs_are_proposals_not_self_promotions(self):
        adrs = sorted((ROOT / "docs/adr").glob("ADR-*.md"))
        self.assertEqual(len(adrs), 3, "ADR-0001/0002/0003 are the WO-0002 deliverables")
        for adr in adrs:
            text = adr.read_text(encoding="utf-8")
            self.assertIn("Status:", text, adr.name)
            self.assertIn("PROPOSED", text, adr.name)
            self.assertNotIn("Status: ACCEPTED", text, adr.name)

    def test_pinned_upstream_commit_is_consistent_across_the_baseline_set(self):
        receipt = load(".engineering/evidence/wo-0002/godot-official-state.json")
        commit = receipt["currentStable"]["commitShaVerifiedByLocalClone"]
        self.assertRegex(commit, r"^[0-9a-f]{40}$")
        for rel in ("docs/project-brain/06-MASTER-MODULE-INDEX.md",
                    "docs/project-brain/08-GODOT-BASELINE-AND-TOPOLOGY.md",
                    "docs/adr/ADR-0001-godot-baseline-and-repository-topology.md"):
            self.assertIn(commit, (ROOT / rel).read_text(encoding="utf-8"), rel)


class PolicyPreservationTests(unittest.TestCase):
    def test_pdf_prompt_policy_survives(self):
        agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        self.assertIn("downloadable PDF artifacts", agents)
        self.assertIn("not as copyable prompt boxes", agents)

    def test_autonomy_rule_does_not_authorize_destructive_actions(self):
        agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        self.assertIn("Autonomous Work Order execution", agents)
        block = agents.split("## Autonomous Work Order execution", 1)[1].split("## Review", 1)[0]
        flat = re.sub(r"\s+", " ", block)
        for forbidden in ("merging a pull request", "force-push", "history rewrite",
                          "deleting or overwriting uncommitted user work"):
            self.assertIn(forbidden, flat)
        self.assertIn("never overrides a hard stop", flat)

    def test_review_autofix_policy_is_canonical(self):
        text = (ROOT / ".engineering/REVIEW-AUTOFIX-POLICY.md").read_text(encoding="utf-8")
        for token in ("CHAT_FIXABLE", "EXECUTOR_REQUIRED", "copyable prompt box"):
            self.assertIn(token, text)


if __name__ == "__main__":
    unittest.main()
