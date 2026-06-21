#!/usr/bin/env python3
import re
from pathlib import Path

DOCS_FILE = Path.home() / "Desktop" / "Isaac_Sim_Main_Docs.md"
RAW_DIR = Path("source/raw")

urls_in_docs = set(re.findall(r'https://docs\.isaacsim\.omniverse\.nvidia\.com[^\s\)\]]*', DOCS_FILE.read_text()))
collected_urls = set()
for mdir in RAW_DIR.iterdir():
    if not mdir.is_dir():
        continue
    for f in mdir.iterdir():
        if f.suffix != ".md":
            continue
        text = f.read_text(encoding="utf-8")
        m = re.search(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
        if m:
            url_match = re.search(r"url:\s*(.+)", m.group(1))
            if url_match:
                collected_urls.add(url_match.group(1).strip())

def norm(u):
    return u.rstrip("/").split("?")[0].split("#")[0]

norm_docs = {norm(u) for u in urls_in_docs}
norm_coll = {norm(u) for u in collected_urls}
covered = norm_docs & norm_coll
missing = norm_docs - norm_coll

print(f"Main Docs unique: {len(norm_docs)}")
print(f"Collected unique: {len(norm_coll)}")
pct = int(100*len(covered)/len(norm_docs)) if norm_docs else 0
print(f"Covered:          {len(covered)} ({pct}%)")
print(f"Missing:          {len(missing)}")
