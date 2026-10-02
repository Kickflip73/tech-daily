#!/usr/bin/env python3
import json
d = "/mnt/openclaw/.openclaw/workspace/tech-daily/data/"
print("=== HACKER NEWS TOP 40 ===")
hn = json.load(open(d + "hackernews_2026-09-29.json"))
for s in hn:
    print(f"{s.get('score',0):>5} {s.get('descendants',0):>4}c  {s.get('title','')[:100]}  | {s.get('url','')[:80]}")
print()
print("=== HUGGINGFACE DAILY PAPERS ===")
hf = json.load(open(d + "hfpapers_2026-09-29.json"))
for p in hf:
    pp = p.get("paper", {})
    print(f"upvotes={p.get('paper',{}).get('upvotes', p.get('upvotes','?'))}  {pp.get('title','')[:110]}")
    auth = pp.get('authors', [])
    print("   ", (pp.get('summary','') or '')[:220].replace("\n"," "))
print()
print("=== ARXIV (latest 50 cs) ===")
ax = json.load(open(d + "arxiv_2026-09-29.json"))
for p in ax:
    print("-", p["published"][:10], p["title"][:100].replace("\n", " "))
    print("   ", p["summary"][:180].replace("\n", " "))
