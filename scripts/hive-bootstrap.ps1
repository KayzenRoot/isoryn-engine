param(
  [string]$BaseUrl = $env:HIVE_API_URL,
  [string]$RelativePath = $env:HIVE_ISORYN_RELATIVE_PATH
)
if (-not $BaseUrl) { $BaseUrl = "http://127.0.0.1:8000" }
if (-not $RelativePath) { $RelativePath = (Split-Path -Leaf (Resolve-Path "$PSScriptRoot\..")) }
python "$PSScriptRoot\hive_bootstrap.py" --base-url $BaseUrl --relative-path $RelativePath
exit $LASTEXITCODE
