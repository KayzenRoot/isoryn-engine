import unittest
from scripts.hive_bootstrap import resolve_registered_project

class HiveProjectResolutionTests(unittest.TestCase):
    def test_exact_relative_path_wins(self):
        p=[{"name":"ISORYN","relative_path":"isoryn-engine","project_id":"1"}]
        self.assertEqual(resolve_registered_project(p,name="ISORYN",relative_path="isoryn-engine")["project_id"],"1")
    def test_name_collision_fails(self):
        p=[{"name":"ISORYN","relative_path":"old/isoryn","project_id":"1"}]
        with self.assertRaises(RuntimeError):
            resolve_registered_project(p,name="ISORYN",relative_path="isoryn-engine")
    def test_absent_returns_none(self):
        self.assertIsNone(resolve_registered_project([],name="ISORYN",relative_path="isoryn-engine"))

if __name__=="__main__": unittest.main()
