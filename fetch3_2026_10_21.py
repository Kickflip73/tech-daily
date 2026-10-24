#!/usr/bin/env python3
import ssl, urllib.request, json, re
ctx = ssl.create_default_context(); ctx.check_hostname=False; ctx.verify_mode=ssl.CERT_NONE
def ft(url, timeout=30):
    req = urllib.request.Request(url, headers={"User-Agent":"Mozilla/5.0 tech-daily"})
    with urllib.request.urlopen(req, timeout=timeout, context=ctx) as r:
        return r.read().decode("utf-8","ignore")

# arXiv latest
try:
    xml = ft("http://export.arxiv.org/api/query?search_query=cat:cs.AI&sortBy=submittedDate&sortOrder=descending&max_results=30", timeout=60)
    open("data/arxiv_2026-10-21.xml","w").write(xml)
    import xml.etree.ElementTree as ET
    ns={"a":"http://www.w3.org/2005/Atom"}
    root=ET.fromstring(xml.encode())
    for e in root.findall("a:entry",ns):
        t=e.find("a:title",ns).text.strip().replace("\n"," ")
        i=e.find("a:id",ns).text
        print(t[:100],"|",i)
except Exception as ex:
    print("arxiv ERR", ex)
