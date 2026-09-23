import io, json, re, unittest
from contextlib import redirect_stdout
from pathlib import Path

import scripts.validate_governance as vg

ROOT = Path(__file__).resolve().parents[1]


def load(rel):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


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
