#!/usr/bin/env python3
"""检查 Isaac Sim 文档覆盖率
使用项目本地的 source/reference_urls.txt 而非桌面文件。
"""
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent  # 项目根目录
REF_URLS_FILE = BASE_DIR / "source" / "reference_urls.txt"
RAW_DIR = BASE_DIR / "source" / "raw"

if not REF_URLS_FILE.exists():
    print(f"❌ 未找到 {REF_URLS_FILE}")
    print("生成方法:")
    print("  python3 -c \"import re; content = open('~/Desktop/Isaac_Sim_Main_Docs.md').read();")
    print("  urls = sorted(set(re.findall(r'https://docs[.^\\\\s)+', content)))")
    print("  open('source/reference_urls.txt','w').write('\\\\n'.join(urls))\"")
    exit(1)

urls_in_docs = set(REF_URLS_FILE.read_text().splitlines())
urls_in_docs.discard("")

collected_urls = set()
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
                collected_urls.add(url_match.group(1).strip())

def norm(u):
    return u.rstrip("/").split("?")[0].split("#")[0]

norm_docs = {norm(u) for u in urls_in_docs}
norm_coll = {norm(u) for u in collected_urls}
covered = norm_docs & norm_coll
missing = norm_docs - norm_coll

print(f"Reference URLs: {len(norm_docs)}")
print(f"Collected:      {len(norm_coll)}")
pct = int(100 * len(covered) / len(norm_docs)) if norm_docs else 0
print(f"Covered:        {len(covered)} ({pct}%)")
print(f"Missing:        {len(missing)}")
