from __future__ import annotations
import os, re, subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]

# Docker Compose resolves a project name from --project-name, then COMPOSE_PROJECT_NAME, then the
# compose file's own `name:` key. A machine that runs several HIVE stacks exports
# COMPOSE_PROJECT_NAME for whichever stack the operator last used, so cwd alone does not select the
# target and only the -p flag outranks that ambient value.
COMPOSE_PROJECT = re.compile(r"^[a-z0-9][a-z0-9_.-]{0,127}$")

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

def resolve_compose_project() -> str | None:
    configured=os.getenv("HIVE_COMPOSE_PROJECT","").strip()
    if not configured: return None
    if not COMPOSE_PROJECT.fullmatch(configured):
        raise RuntimeError("HIVE_COMPOSE_PROJECT must be a lowercase Docker Compose project name "
                           "(letters, digits, underscore, dot or hyphen) so it cannot inject compose arguments.")
    return configured

def build_mcp_command():
    command=["docker","compose"]
    project=resolve_compose_project()
    if project: command.extend(("-p",project))
    command.extend(("exec","-T","api","python","-m","app.mcp_server"))
    return resolve_hive_repo(), command

def main():
    hive_repo, command=build_mcp_command()
    try: return subprocess.run(command,cwd=hive_repo,check=False).returncode
    except FileNotFoundError as exc: raise RuntimeError("Docker CLI is not available on PATH.") from exc

if __name__=="__main__":
    try: raise SystemExit(main())
    except Exception as exc:
        print(f"HIVE MCP bootstrap failed: {exc}",file=sys.stderr)
        raise SystemExit(1)
