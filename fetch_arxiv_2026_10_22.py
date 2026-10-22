#!/usr/bin/env python3
"""Retry arXiv fetch for 2026-10-22 (rate-limited in main run)."""
import ssl, urllib.request, re, json, time
import xml.etree.ElementTree as ET

ctx = ssl.create_default_context(); ctx.check_hostname = False; ctx.verify_mode = ssl.CERT_NONE

def ft(url, timeout=90):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 tech-daily"})
    with urllib.request.urlopen(req, timeout=timeout, context=ctx) as r:
        return r.read().decode("utf-8", "ignore")

ns = {"a": "http://www.w3.org/2005/Atom"}
papers = []
seen = set()
for cat in ["cs.AI", "cs.LG", "cs.CL", "cs.CR", "cs.SE"]:
    try:
        xml = ft(f"http://export.arxiv.org/api/query?search_query=cat:{cat}&sortBy=submittedDate&sortOrder=descending&max_results=25")
        root = ET.fromstring(xml.encode())
        for e in root.findall("a:entry", ns):
            title = e.find("a:title", ns)
            summ = e.find("a:summary", ns)
            aid = e.find("a:id", ns)
            pub = e.find("a:published", ns)
            link = e.find("a:link[@rel='alternate']", ns)
            pid = aid.text if aid is not None else ""
            if pid in seen:
                continue
            seen.add(pid)
            authors = [a.find("a:name", ns).text for a in e.findall("a:author", ns)
                       if a.find("a:name", ns) is not None and a.find("a:name", ns).text]
            papers.append({
                "title": re.sub(r"\s+", " ", title.text).strip() if title is not None and title.text else "",
                "summary": re.sub(r"\s+", " ", summ.text).strip() if summ is not None and summ.text else "",
                "id": pid,
                "published": pub.text if pub is not None else "",
                "link": link.get("href", "") if link is not None else "",
                "authors": authors[:6],
                "categories": [c.get("term") for c in e.findall("a:category", ns)],
            })
        print(cat, "ok, unique total:", len(papers))
        time.sleep(4)
    except Exception as ex:
        print(cat, "ERR", ex)
        time.sleep(6)

json.dump(papers, open("data/arxiv_2026-10-22.json", "w"), indent=2, ensure_ascii=False)
print("saved", len(papers))
