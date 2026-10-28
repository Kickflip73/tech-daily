#!/usr/bin/env python3
"""Parse raw arxiv XML fetched via web_fetch for 2026-10-28."""
import json, re, xml.etree.ElementTree as ET

DATA_DIR = "/root/.openclaw/workspace/tech-daily/data"
DATE = "2026-10-28"

with open(f"{DATA_DIR}/arxiv_raw_{DATE}.xml", "r") as f:
    txt = f.read()
# Strip security wrapper if present
m = re.search(r"(<\?xml.*?</feed>)", txt, re.DOTALL)
if m:
    txt = m.group(1)

ns = {"atom": "http://www.w3.org/2005/Atom"}
papers = []
root = ET.fromstring(txt.encode())
for entry in root.findall("atom:entry", ns):
    p = {}
    t = entry.find("atom:title", ns)
    p["title"] = re.sub(r"\s+", " ", t.text).strip() if t is not None and t.text else ""
    s = entry.find("atom:summary", ns)
    p["summary"] = re.sub(r"\s+", " ", s.text).strip() if s is not None and s.text else ""
    i = entry.find("atom:id", ns)
    p["id"] = i.text if i is not None else ""
    pub = entry.find("atom:published", ns)
    p["published"] = pub.text if pub is not None else ""
    authors = [a.find("atom:name", ns).text for a in entry.findall("atom:author", ns) if a.find("atom:name", ns) is not None]
    p["authors"] = authors
    cats = [c.get("term") for c in entry.findall("atom:category", ns)]
    p["categories"] = cats
    papers.append(p)

with open(f"{DATA_DIR}/arxiv_{DATE}.json", "w") as f:
    json.dump(papers, f, indent=2, ensure_ascii=False)
print(f"Parsed {len(papers)} arxiv papers")
for p in papers[:40]:
    print("-", p["title"][:90], "|", ",".join(p["categories"][:3]))
