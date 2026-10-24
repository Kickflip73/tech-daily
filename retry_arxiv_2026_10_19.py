#!/usr/bin/env python3
"""Retry arXiv fetch for 2026-10-19."""
import json, re, time, urllib.request
import xml.etree.ElementTree as ET

DATE = "2026-10-19"
DATA_DIR = "/root/.openclaw/workspace/tech-daily/data"

def fetch_text(url, timeout=90):
    req = urllib.request.Request(url, headers={"User-Agent": "tech-daily-bot/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode()

xml_text = None
for attempt in range(3):
    try:
        xml_text = fetch_text("https://export.arxiv.org/api/query?search_query=cat:cs.*&sortBy=submittedDate&sortOrder=descending&max_results=50")
        break
    except Exception as e:
        print("retry", attempt, e)
        time.sleep(20)

if xml_text:
    ns = {"atom": "http://www.w3.org/2005/Atom"}
    root = ET.fromstring(xml_text.encode())
    papers = []
    for e in root.findall("atom:entry", ns):
        def g(t):
            el = e.find(f"atom:{t}", ns)
            return re.sub(r"\s+", " ", el.text).strip() if el is not None and el.text else ""
        p = {
            "title": g("title"), "summary": g("summary"), "id": g("id"), "published": g("published"),
            "authors": [a.find("atom:name", ns).text for a in e.findall("atom:author", ns) if a.find("atom:name", ns) is not None and a.find("atom:name", ns).text],
            "link": (e.find("atom:link[@rel='alternate']", ns).get("href", "") if e.find("atom:link[@rel='alternate']", ns) is not None else ""),
            "categories": [c.get("term") for c in e.findall("atom:category", ns)],
        }
        papers.append(p)
    json.dump(papers, open(f"{DATA_DIR}/arxiv_{DATE}.json", "w"), indent=2, ensure_ascii=False)
    print("arxiv ok:", len(papers))
else:
    print("arxiv FAILED")
