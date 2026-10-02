#!/usr/bin/env python3
"""Parse arXiv XML and extract paper info."""
import xml.etree.ElementTree as ET
import json

with open("/root/.openclaw/workspace/tech-daily/data/arxiv_2026-08-25.xml", "rb") as f:
    tree = ET.parse(f)

ns = {"atom": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}

papers = []
for entry in tree.findall("atom:entry", ns):
    title = entry.find("atom:title", ns)
    title_text = title.text.strip().replace("\n", " ") if title.text else ""
    
    summary = entry.find("atom:summary", ns)
    abstract = summary.text.strip().replace("\n", " ")[:300] if summary.text else ""
    
    id_elem = entry.find("atom:id", ns)
    arxiv_id = id_elem.text.split("/")[-1] if id_elem is not None else ""
    
    authors = [a.find("atom:name", ns).text for a in entry.findall("atom:author", ns) if a.find("atom:name", ns) is not None]
    
    categories = [cat.get("term", "") for cat in entry.findall("atom:category", ns)]
    
    published = entry.find("atom:published", ns)
    
    papers.append({
        "title": title_text,
        "arxiv_id": arxiv_id,
        "abstract": abstract,
        "authors": authors[:5],
        "categories": categories,
        "published": published.text if published is not None else ""
    })

# Save parsed
with open("/root/.openclaw/workspace/tech-daily/data/arxiv_2026-08-25.json", "w") as f:
    json.dump({"date": "2026-08-25", "count": len(papers), "papers": papers}, f, indent=2, ensure_ascii=False)

print(f"Parsed {len(papers)} papers")
# Print by category
from collections import Counter
cat_counter = Counter()
for p in papers:
    for c in p["categories"]:
        cat_counter[c] += 1
print("Top categories:")
for cat, cnt in cat_counter.most_common(15):
    print(f"  {cat}: {cnt}")
