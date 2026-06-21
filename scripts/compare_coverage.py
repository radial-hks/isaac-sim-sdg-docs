#!/usr/bin/env python3
"""Compare Isaac_Sim_Main_Docs.md URLs vs collected URLs in isaac-sim-sdg-docs/source/raw/"""
import re
from pathlib import Path
from collections import defaultdict

DESKTOP = Path.home() / "Desktop"
DOCS_FILE = DESKTOP / "Isaac_Sim_Main_Docs.md"
RAW_DIR = DESKTOP / "isaac-sim-sdg-docs" / "source" / "raw"

# Read Main Docs
raw = DOCS_FILE.read_text(encoding="utf-8")
urls_in_docs = set(re.findall(r'https://docs\.isaacsim\.omniverse\.nvidia\.com[^\s\)\]]*', raw))
print(f"Main_Docs URLs: {len(urls_in_docs)}")

# Read collected
collected_urls = {}
for mdir in sorted(RAW_DIR.iterdir()):
    if not mdir.is_dir():
        continue
    for f in sorted(mdir.iterdir()):
        if f.suffix != ".md":
            continue
        text = f.read_text(encoding="utf-8")
        m = re.search(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
        if m:
            url_match = re.search(r"url:\s*(.+)", m.group(1))
            if url_match:
                collected_urls[url_match.group(1).strip()] = f"{mdir.name}/{f.name}"
print(f"Collected URLs: {len(collected_urls)}")

def norm(u):
    return u.rstrip("/").split("?")[0].split("#")[0]

norm_docs = {norm(u): u for u in urls_in_docs}
norm_coll = {norm(u): u for u in collected_urls}

covered = set(norm_docs) & set(norm_coll)
missing = set(norm_docs) - set(norm_coll)

pct = int(100 * len(covered) / len(norm_docs)) if norm_docs else 0
print(f"\nMain Docs unique: {len(norm_docs)}")
print(f"Covered:          {len(covered)} ({pct}%)")
print(f"Missing:          {len(missing)}")

def get_cat(u):
    m2 = re.search(r"/latest/([^/]+)", u)
    return m2.group(1) if m2 else "root"

missing_by_cat = defaultdict(list)
for k in sorted(norm_docs):
    if k not in norm_coll:
        cat = get_cat(norm_docs[k])
        page = norm_docs[k].split("/")[-1].replace(".html", "").replace("_", " ")
        missing_by_cat[cat].append(page)

print("\n" + "=" * 60)
print("Missing pages by module (" + str(len(missing)) + " total)")
print("=" * 60)
for cat in sorted(missing_by_cat):
    pages = missing_by_cat[cat]
    print(f"\n  [{cat}] {len(pages)} pages missing")
    for p in pages:
        print(f"    - {p}")

# Also show covered summary
print("\n" + "=" * 60)
print("Covered pages breakdown")
print("=" * 60)
covered_by_cat = defaultdict(list)
for k in sorted(norm_docs):
    if k in norm_coll:
        cat = get_cat(norm_docs[k])
        page = norm_docs[k].split("/")[-1].replace(".html", "").replace("_", " ")
        covered_by_cat[cat].append(page)

for cat in sorted(covered_by_cat):
    pages = covered_by_cat[cat]
    print(f"\n  [{cat}] {len(pages)} pages collected")
    for p in pages:
        print(f"    + {p}")
