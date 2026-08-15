# build-manifest.ps1 — OPTIONAL helper for dashboard-kimi/dashboard.html
# Regenerates dashboard-kimi/manifest.json, which dashboard.html uses ONLY as a
# last-resort file listing fallback (primary: GitHub API, secondary: jsDelivr).
# Run this before pushing if you want the fallback to stay fresh. Not required.
$ErrorActionPreference = "Stop"
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$root = Split-Path -Parent $scriptDir          # repo root (parent of dashboard-kimi)
$inputDir = Join-Path $root "input"
if (-not (Test-Path $inputDir)) { Write-Error "input/ folder not found at $inputDir"; exit 1 }

$files = Get-ChildItem -Path $inputDir -Recurse -Filter *.json |
  Where-Object { $_.FullName -match "input[\\/][^\\/]+[\\/][^\\/]+[\\/][^\\/]+\.json$" } |
  ForEach-Object { $_.FullName.Substring($root.Length + 1).Replace("\", "/") } |
  Sort-Object

$manifest = @{
  generated = (Get-Date).ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ssZ")
  count     = $files.Count
  files     = $files
}
$out = Join-Path $scriptDir "manifest.json"
$manifest | ConvertTo-Json -Depth 3 | Set-Content -Path $out -Encoding UTF8
Write-Host "Wrote $out with $($files.Count) files"
