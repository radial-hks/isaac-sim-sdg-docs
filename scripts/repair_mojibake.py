#!/usr/bin/env python3
"""Repair mojibake artifacts in existing raw and output Markdown files."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from collect import fix_mojibake  # noqa: E402
from check_mojibake import iter_markdown_files  # noqa: E402


def repair_mojibake(base: Path = ROOT) -> list[Path]:
    changed: list[Path] = []
    for path in iter_markdown_files(base):
        content = path.read_text(encoding="utf-8")
        repaired = fix_mojibake(content)
        if repaired != content:
            path.write_text(repaired, encoding="utf-8")
            changed.append(path)
    return changed


def main() -> int:
    changed = repair_mojibake(ROOT)
    print(f"Repaired files: {len(changed)}")
    for path in changed[:50]:
        print(f"  {path.relative_to(ROOT)}")
    if len(changed) > 50:
        print(f"  ... {len(changed) - 50} more")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
