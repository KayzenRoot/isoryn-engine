from __future__ import annotations
import argparse, json, os, sys, urllib.error, urllib.request
from pathlib import Path
from typing import Any

def request(base_url:str, method:str, path:str, payload:dict[str,Any]|None=None)->Any:
    data=None if payload is None else json.dumps(payload).encode()
    req=urllib.request.Request(base_url.rstrip("/")+path,data=data,method=method,headers={"Content-Type":"application/json"})
    try:
        with urllib.request.urlopen(req,timeout=15) as response:
            raw=response.read()
            return json.loads(raw.decode()) if raw else None
    except urllib.error.HTTPError as exc:
        body=exc.read().decode(errors="replace")
        raise RuntimeError(f"{method} {path} -> HTTP {exc.code}: {body}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"HIVE unavailable at {base_url}: {exc.reason}") from exc

def resolve_registered_project(projects:list[dict[str,Any]],*,name:str,relative_path:str):
    exact=next((x for x in projects if x.get("relative_path")==relative_path),None)
    if exact is not None: return exact
    collisions=[x for x in projects if x.get("name")==name and x.get("relative_path")!=relative_path]
    if collisions:
        raise RuntimeError(f'HIVE already has project name "{name}" at a different path: '+", ".join(sorted(str(x.get("relative_path")) for x in collisions)))
    return None

def main()->int:
    p=argparse.ArgumentParser(description="Register and prepare ISORYN in HIVE v1.0.0")
    p.add_argument("--base-url",default=os.getenv("HIVE_API_URL","http://localhost:8000"))
    p.add_argument("--name",default="ISORYN")
    p.add_argument("--relative-path",default=os.getenv("HIVE_ISORYN_RELATIVE_PATH") or Path.cwd().name)
    a=p.parse_args()
    print("HIVE health:",request(a.base_url,"GET","/api/v1/health"))
    projects=request(a.base_url,"GET","/api/v1/projects")
    if not isinstance(projects,list): raise RuntimeError("HIVE project list returned unexpected payload")
    target=resolve_registered_project(projects,name=a.name,relative_path=a.relative_path)
    if target is None:
        target=request(a.base_url,"POST","/api/v1/projects",{"name":a.name,"relative_path":a.relative_path})
        print("Registered ISORYN in HIVE.")
    else: print("Resolved existing ISORYN registration by exact relative path.")
    project_id=target.get("project_id")
    if not project_id: raise RuntimeError("HIVE did not return project_id")
    inspected=request(a.base_url,"POST",f"/api/v1/projects/{project_id}/inspect")
    if inspected.get("state")!="READY": raise RuntimeError(f"ISORYN is not READY in HIVE: {inspected}")
    if inspected.get("relative_path")!=a.relative_path: raise RuntimeError("HIVE inspection resolved a different canonical path.")
    index=request(a.base_url,"POST",f"/api/v1/projects/{project_id}/index")
    if index.get("status")!="COMPLETED": raise RuntimeError(f"ISORYN indexing did not complete: {index}")
    corpus=request(a.base_url,"POST",f"/api/v1/projects/{project_id}/retrieval/corpus/sync")
    if corpus.get("status") not in {"COMPLETED","CURRENT"}: raise RuntimeError(f"ISORYN retrieval corpus is not current: {corpus}")
    print(json.dumps({"project_id":project_id,"relative_path":inspected.get("relative_path"),"git_head_sha":inspected.get("git_head_sha"),"state":inspected.get("state"),"index_status":index.get("status"),"corpus_status":corpus.get("status")},indent=2))
    return 0

if __name__=="__main__":
    try: raise SystemExit(main())
    except Exception as exc:
        print(f"HIVE bootstrap failed: {exc}",file=sys.stderr)
        raise SystemExit(1)
