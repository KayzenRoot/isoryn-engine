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
                repo,cmd=hm.build_mcp_command()
                self.assertEqual(repo,root.resolve())
                self.assertEqual(cmd,["docker","compose","exec","-T","api","python","-m","app.mcp_server"])

if __name__=="__main__": unittest.main()
