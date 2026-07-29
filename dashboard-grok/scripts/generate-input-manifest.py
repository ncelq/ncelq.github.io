#!/usr/bin/env python3
"""Scan repo input/**/*.json (read-only) and write dashboard-grok/manifest.json."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

# dashboard-grok/scripts/ → repo root
ROOT_DEFAULT = Path(__file__).resolve().parents[2]
PKG_DIR = Path(__file__).resolve().parents[1]  # dashboard-grok/
MANIFEST_NAME = "manifest.json"


def collect_files(input_dir: Path) -> list[str]:
    """List prediction JSON paths relative to repo root. Does not write to input_dir."""
    files: list[str] = []
    if not input_dir.is_dir():
        return files
    skip_names = {MANIFEST_NAME, "qqq-ohlc.json"}
    for path in sorted(input_dir.rglob("*.json")):
        if path.name in skip_names:
            continue
        rel = path.relative_to(input_dir.parent).as_posix()
        files.append(rel)
    return files


def build_manifest(files: list[str], generated_at: str | None = None) -> dict:
    return {
        "generated_at": generated_at or datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "files": files,
    }


def write_manifest(repo_root: Path, generated_at: str | None = None) -> Path:
    input_dir = repo_root / "input"
    out = repo_root / "dashboard-grok" / MANIFEST_NAME
    payload = build_manifest(collect_files(input_dir), generated_at=generated_at)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=ROOT_DEFAULT,
        help="Repository root (default: two levels above this script)",
    )
    args = parser.parse_args()
    path = write_manifest(args.root.resolve())
    data = json.loads(path.read_text(encoding="utf-8"))
    print(f"Wrote {path} ({len(data['files'])} files)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
