#!/usr/bin/env python3
import json
DATE = "2026-10-09"

hn = json.load(open(f"data/hackernews_{DATE}.json"))
print("=== HN TOP 40 ===")
for s in hn:
    if s:
        print(f"{s.get('score',0)}pts | {s.get('descendants',0)}c | {s.get('title','')[:110]} | {s.get('url','') or 'HN:'+str(s.get('id'))}")

repos = json.load(open(f"data/github_repos_{DATE}.json"))
matched = [r for r in repos if r["prev_stars"] is not None]
matched.sort(key=lambda r: (r["stargazers_count"] - r["prev_stars"]), reverse=True)
print("\n=== GH TOP DELTA ===")
for r in matched[:40]:
    print(f"+{r['stargazers_count']-r['prev_stars']} (total {r['stargazers_count']}) | {r['language']} | {r['full_name']} | {(r['description'] or '')[:90]}")
news = [r for r in repos if r["prev_stars"] is None]
news.sort(key=lambda r: r["stargazers_count"] or 0, reverse=True)
print("\n=== GH NEW FACES ===")
for r in news[:25]:
    print(f"{r['stargazers_count']} stars | {r['language']} | {r['full_name']} | {(r['description'] or '')[:90]}")

print("\n=== HF PAPERS ===")
hf = json.load(open(f"data/hfpapers_{DATE}.json"))
for p in hf[:30]:
    pp = p.get("paper", {})
    print(f"{pp.get('upvotes','?')}likes | {pp.get('title','')[:110]}")

print("\n=== ARXIV ===")
ax = json.load(open(f"data/arxiv_{DATE}.json"))
for p in ax[:50]:
    print(f"{p['published'][:10]} | {','.join(p['categories'][:2])} | {p['title'][:120]}")
