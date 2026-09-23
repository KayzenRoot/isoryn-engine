import os, tempfile, unittest
from pathlib import Path
from unittest.mock import patch
import scripts.hive_mcp as hm

class HiveMcpTests(unittest.TestCase):
    def test_configured_hive_checkout_resolves(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td)
            (root/"docker-compose.yml").write_text("services: {}\n",encoding="utf-8")
            (root/"backend").mkdir()
            with patch.dict(os.environ,{"HIVE_REPO_PATH":str(root)},clear=False):
                self.assertEqual(hm.resolve_hive_repo(),root.resolve())
    def test_command_is_stable_stdio_server(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td)
            (root/"docker-compose.yml").write_text("services: {}\n",encoding="utf-8")
            (root/"backend").mkdir()
            with patch.dict(os.environ,{"HIVE_REPO_PATH":str(root)},clear=False):
                os.environ.pop("HIVE_COMPOSE_PROJECT",None)
                repo,cmd=hm.build_mcp_command()
                self.assertEqual(repo,root.resolve())
                self.assertEqual(cmd,["docker","compose","exec","-T","api","python","-m","app.mcp_server"])
    def test_compose_project_selects_the_target_stack(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td)
            (root/"docker-compose.yml").write_text("services: {}\n",encoding="utf-8")
            (root/"backend").mkdir()
            with patch.dict(os.environ,{"HIVE_REPO_PATH":str(root),"HIVE_COMPOSE_PROJECT":"isoryn-c01-v100",
                                        "COMPOSE_PROJECT_NAME":"another-stack"},clear=False):
                _,cmd=hm.build_mcp_command()
                # -p must precede the subcommand and must beat an ambient COMPOSE_PROJECT_NAME.
                self.assertEqual(cmd[:4],["docker","compose","-p","isoryn-c01-v100"])
                self.assertEqual(cmd[4:],["exec","-T","api","python","-m","app.mcp_server"])
    def test_compose_project_rejects_argument_injection(self):
        with patch.dict(os.environ,{"HIVE_COMPOSE_PROJECT":"--profile evil"},clear=False):
            with self.assertRaises(RuntimeError):
                hm.resolve_compose_project()
    def test_blank_compose_project_keeps_the_default(self):
        with patch.dict(os.environ,{"HIVE_COMPOSE_PROJECT":"   "},clear=False):
            self.assertIsNone(hm.resolve_compose_project())

if __name__=="__main__": unittest.main()
