import sys
from pathlib import Path

import collect


def test_assemble_only_dry_run_does_not_write_output(tmp_path, monkeypatch):
    manifests_dir = tmp_path / "manifests"
    raw_dir = tmp_path / "source" / "raw"
    output_dir = tmp_path / "output"
    manifests_dir.mkdir()

    manifest = manifests_dir / "01-demo.json"
    manifest.write_text(
        """
{
  "module": "01-demo",
  "title": "Demo",
  "output": "output/demo.md",
  "pages": [
    {"url": "/demo.html", "title": "Demo Page", "section": "Intro"}
  ]
}
""".strip(),
        encoding="utf-8",
    )

    module_dir = raw_dir / "01-demo"
    module_dir.mkdir(parents=True)
    (module_dir / "demo.md").write_text(
        """---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/demo.html
title: "Demo Page"
section: "Intro"
module: "01-demo"
checksum: "abc"
fetched: "2026-06-21T00:00:00"
---

# Demo body
""",
        encoding="utf-8",
    )

    monkeypatch.setattr(collect, "BASE_DIR", tmp_path)
    monkeypatch.setattr(collect, "MANIFESTS_DIR", manifests_dir)
    monkeypatch.setattr(collect, "RAW_DIR", raw_dir)
    monkeypatch.setattr(collect, "OUTPUT_DIR", output_dir)
    monkeypatch.setattr(collect, "CACHE_DIR", tmp_path / "source" / "cache")
    monkeypatch.setattr(collect, "CACHE_FILE", tmp_path / "source" / "cache" / ".collect_cache.json")
    monkeypatch.setattr(sys, "argv", ["collect.py", "--assemble-only", "--dry-run"])

    collect.main()

    assert not (output_dir / "demo.md").exists()


def test_plain_dry_run_does_not_create_raw_dirs_or_cache(tmp_path, monkeypatch):
    manifests_dir = tmp_path / "manifests"
    raw_dir = tmp_path / "source" / "raw"
    cache_dir = tmp_path / "source" / "cache"
    output_dir = tmp_path / "output"
    manifests_dir.mkdir()

    (manifests_dir / "01-demo.json").write_text(
        """
{
  "module": "01-demo",
  "title": "Demo",
  "output": "output/demo.md",
  "pages": [
    {"url": "/demo.html", "title": "Demo Page", "section": "Intro"}
  ]
}
""".strip(),
        encoding="utf-8",
    )

    monkeypatch.setattr(collect, "BASE_DIR", tmp_path)
    monkeypatch.setattr(collect, "MANIFESTS_DIR", manifests_dir)
    monkeypatch.setattr(collect, "RAW_DIR", raw_dir)
    monkeypatch.setattr(collect, "OUTPUT_DIR", output_dir)
    monkeypatch.setattr(collect, "CACHE_DIR", cache_dir)
    monkeypatch.setattr(collect, "CACHE_FILE", cache_dir / ".collect_cache.json")
    monkeypatch.setattr(sys, "argv", ["collect.py", "--dry-run"])

    collect.main()

    assert not raw_dir.exists()
    assert not cache_dir.exists()
    assert not output_dir.exists()
