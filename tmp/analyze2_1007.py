#!/usr/bin/env python3
import json

# HN top stories
with open('data/hackernews_2026-10-07.json') as f:
    hn = json.load(f)
print("=== HN TOP 40 ===")
for s in hn[:40]:
    print(f"{s.get('score',0):4d}pts {s.get('descendants',0):4d}c | {s.get('title','')[:110]} | {s.get('url','')[:80]}")

# arxiv cats
with open('data/arxiv_2026-10-07.json') as f:
    arx = json.load(f)
print()
print(f"=== ARXIV {len(arx)} papers, categories ===")
from collections import Counter
cats = Counter()
for p in arx:
    for c in p.get('categories', []):
        cats[c] += 1
print(cats.most_common(15))
print()
print("=== ARXIV sample titles ===")
for p in arx[:20]:
    print(f"- {p['title'][:100]} [{','.join(p.get('categories',[])[:2])}]")

# HF papers
with open('data/hfpapers_2026-10-07.json') as f:
    hf = json.load(f)
print()
print(f"=== HF PAPERS {len(hf)} ===")
for item in hf[:25]:
    p = item.get('paper', item)
    t = p.get('title', '')
    up = item.get('paper', {}).get('upvotes', '')
    print(f"- {t[:100]} (upvotes: {up})")
