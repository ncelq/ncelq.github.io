import importlib.util
import json
import subprocess
import sys
from pathlib import Path

PKG = Path(__file__).resolve().parents[1]  # dashboard-grok/
REPO = PKG.parents[0]
SCRIPT = PKG / "scripts" / "generate-input-manifest.py"


def _load():
    spec = importlib.util.spec_from_file_location("gen_manifest", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def test_collect_excludes_manifest_and_sorts(tmp_path: Path):
    mod = _load()
    input_dir = tmp_path / "input"
    (input_dir / "eng-a" / "model-x").mkdir(parents=True)
    (input_dir / "eng-b" / "model-y").mkdir(parents=True)
    (input_dir / "eng-a" / "model-x" / "a.json").write_text("{}", encoding="utf-8")
    (input_dir / "eng-b" / "model-y" / "b.json").write_text("{}", encoding="utf-8")
    (input_dir / "manifest.json").write_text("{}", encoding="utf-8")
    (input_dir / "qqq-ohlc.json").write_text("{}", encoding="utf-8")

    files = mod.collect_files(input_dir)
    assert files == [
        "input/eng-a/model-x/a.json",
        "input/eng-b/model-y/b.json",
    ]
    assert "input/manifest.json" not in files
    assert "input/qqq-ohlc.json" not in files


def test_build_manifest_shape():
    mod = _load()
    payload = mod.build_manifest(["input/a.json"], generated_at="2026-07-29T00:00:00Z")
    assert payload == {
        "generated_at": "2026-07-29T00:00:00Z",
        "files": ["input/a.json"],
    }


def test_write_manifest_to_dashboard_grok(tmp_path: Path):
    mod = _load()
    (tmp_path / "input" / "e" / "m").mkdir(parents=True)
    (tmp_path / "input" / "e" / "m" / "x.json").write_text('{"signal":"HOLD"}', encoding="utf-8")
    (tmp_path / "dashboard-grok").mkdir()
    out = mod.write_manifest(tmp_path, generated_at="2026-07-29T12:00:00Z")
    assert out == tmp_path / "dashboard-grok" / "manifest.json"
    assert not (tmp_path / "input" / "manifest.json").exists()
    data = json.loads(out.read_text(encoding="utf-8"))
    assert data["generated_at"] == "2026-07-29T12:00:00Z"
    assert data["files"] == ["input/e/m/x.json"]


def test_cli_writes_dashboard_manifest_not_input():
    result = subprocess.run(
        [sys.executable, str(SCRIPT), "--root", str(REPO)],
        check=True,
        capture_output=True,
        text=True,
    )
    assert "Wrote" in result.stdout
    out = PKG / "manifest.json"
    assert out.is_file()
    assert not (REPO / "input" / "manifest.json").exists()
    data = json.loads(out.read_text(encoding="utf-8"))
    assert "files" in data
    assert all(f.startswith("input/") and f.endswith(".json") for f in data["files"])
    assert len(data["files"]) > 0
