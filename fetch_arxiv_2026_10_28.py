#!/usr/bin/env python3
"""Fetch arxiv for 2026-10-28 with retry."""
import json, re, time, urllib.request, xml.etree.ElementTree as ET
DATE = "2026-10-28"
DATA_DIR = "/root/.openclaw/workspace/tech-daily/data"

def fetch_text(url, timeout=90):
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "tech-daily-bot/1.0"})
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read().decode()
        except Exception as e:
            print(f"attempt {attempt+1}: {e}")
            time.sleep(10)
    return None

xml_txt = fetch_text("https://export.arxiv.org/api/query?search_query=cat:cs.AI+OR+cat:cs.CL+OR+cat:cs.LG+OR+cat:cs.CR+OR+cat:cs.SE&sortBy=submittedDate&sortOrder=descending&max_results=60")
if xml_txt:
    ns = {"atom": "http://www.w3.org/2005/Atom"}
    papers = []
    root = ET.fromstring(xml_txt.encode())
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
    print(f"Fetched {len(papers)} arxiv papers")
else:
    print("arXiv STILL FAILED")
