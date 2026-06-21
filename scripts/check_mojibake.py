#!/usr/bin/env python3
"""Check generated docs and raw pages for mojibake artifacts."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent

MOJIBAKE_PATTERNS = (
    "\u00e2\u0080\u0099",  # right single quote
    "\u00e2\u0080\u0094",  # em dash
    "\u00e2\u0080\u009c",  # left double quote
    "\u00e2\u0080\u009d",  # right double quote
    "\u00e2\u0080\u0098",  # left single quote
    "\u00e2\u0080\u0091",  # non-breaking hyphen
    "\u00e2\u0080\u0093",  # en dash
    "\u00e2\u0080\u00a6",  # ellipsis
    "\u00e2\u0084\u00a2",  # trademark
    "\u00e2\u0086\u0090",  # left arrow
    "\u00e2\u0086\u0092",  # right arrow
    "\u00e2\u0088\u0092",  # minus sign
    "\u00e2\u008c\u0098",  # command key
    "\u00e2\u0094",        # box drawing prefix
    "\u00e2\u0096",        # block/triangle prefix
    "\u00e2",              # any remaining UTF-8 double-encoding lead byte
    "\u00c2",              # Latin-1 artifact prefix
    "\u00c3",              # Latin-1 artifact prefix
    "\ufffd",              # replacement character
)


@dataclass(frozen=True)
class MojibakeFinding:
    path: Path
    count: int


def iter_markdown_files(base: Path) -> list[Path]:
    roots = [base / "source" / "raw", base / "output"]
    files: list[Path] = []
    for root in roots:
        if root.exists():
            files.extend(sorted(root.rglob("*.md")))
    return files


def count_mojibake(text: str) -> int:
    count = 0
    remaining = text
    for pattern in sorted(MOJIBAKE_PATTERNS, key=len, reverse=True):
        pattern_count = remaining.count(pattern)
        if pattern_count:
            count += pattern_count
            remaining = remaining.replace(pattern, "")
    return count


def find_mojibake(base: Path = BASE) -> list[MojibakeFinding]:
    findings: list[MojibakeFinding] = []
    for path in iter_markdown_files(base):
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            findings.append(MojibakeFinding(path, 1))
            continue
        count = count_mojibake(content)
        if count:
            findings.append(MojibakeFinding(path, count))
    return findings


def main() -> int:
    findings = find_mojibake(BASE)
    total = sum(finding.count for finding in findings)

    print("Checked roots: source/raw, output")
    print(f"Files with mojibake: {len(findings)}")
    print(f"Total mojibake occurrences: {total}")

    if findings:
        print("\nTop 20 affected:")
        for finding in sorted(findings, key=lambda item: -item.count)[:20]:
            rel_path = finding.path.relative_to(BASE)
            print(f"  {finding.count:6d}  {rel_path}")
        return 1

    print("\nAll clean - no mojibake found")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
