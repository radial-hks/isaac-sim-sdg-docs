#!/usr/bin/env python3
"""Check for remaining mojibake in active raw files (fixed paths)."""
import os
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
raw_dir = BASE / "source" / "raw"

active_modules = [
    "01-concepts", "02-fundamentals-dev", "03-extension-dev",
    "04-headless-deploy", "05-python-api-quickref", "06-sim2real-ue5",
    "07-robot-setup", "08-omnigraph-robot-sim", "09-advanced-optionals"
]

text_patterns = [
    '\u00e2\u0080\u0099', '\u00e2\u0080\u0094', '\u00e2\u0080\u009c',
    '\u00e2\u0080\u009d', '\u00e2\u0080\u0098', '\u00e2\u0080\u0093',
]

total = 0
affected_files = {}
for module_dir in sorted(os.listdir(raw_dir)):
    if module_dir not in active_modules:
        continue
    mpath = raw_dir / module_dir
    if not mpath.is_dir():
        continue
    for f in sorted(os.listdir(mpath)):
        if not f.endswith('.md'):
            continue
        fpath = mpath / f
        try:
            content = fpath.read_text(encoding='utf-8')
        except Exception:
            continue
        count = sum(content.count(p) for p in text_patterns)
        if count > 0:
            affected_files[str(fpath)] = count
            total += count

print(f"Active modules checked: {len(active_modules)}")
print(f"Files with mojibake: {len(affected_files)}")
print(f"Total mojibake occurrences: {total}")

if affected_files:
    print("\nTop 20 affected:")
    for fpath, count in sorted(affected_files.items(), key=lambda x: -x[1])[:20]:
        print(f"  {count:6d}  {fpath}")
else:
    print("\nAll clean - no mojibake found")
