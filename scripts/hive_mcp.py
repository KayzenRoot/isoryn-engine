from __future__ import annotations
import os, subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]

def resolve_hive_repo() -> Path:
    candidates=[]
    for var in ("HIVE_REPO_PATH", "HIVE_HOME"):
        configured=os.getenv(var)
        if configured:
            base=Path(configured).expanduser()
            candidates.extend((base, base / "app"))
    candidates.extend((ROOT.parents[1] / "hive", ROOT.parent / "hive", ROOT.parent / "Hive"))
    seen=set()
    for candidate in candidates:
        try: resolved=candidate.resolve()
        except OSError: continue
        if resolved in seen: continue
        seen.add(resolved)
        if (resolved/"docker-compose.yml").is_file() and (resolved/"backend").is_dir():
            return resolved
    raise RuntimeError("HIVE v1.0.0 checkout not found. Set HIVE_REPO_PATH or HIVE_HOME to the stable HIVE checkout.")

def build_mcp_command():
    return resolve_hive_repo(), ["docker","compose","exec","-T","api","python","-m","app.mcp_server"]

def main():
    hive_repo, command=build_mcp_command()
    try: return subprocess.run(command,cwd=hive_repo,check=False).returncode
    except FileNotFoundError as exc: raise RuntimeError("Docker CLI is not available on PATH.") from exc

if __name__=="__main__":
    try: raise SystemExit(main())
    except Exception as exc:
        print(f"HIVE MCP bootstrap failed: {exc}",file=sys.stderr)
        raise SystemExit(1)
