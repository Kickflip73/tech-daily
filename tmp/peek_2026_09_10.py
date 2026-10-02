#!/usr/bin/env python3
import json, sys

DATE = "2026-09-10"
D = "/root/.openclaw/workspace/tech-daily/data"

hn = json.load(open(f"{D}/hackernews_{DATE}.json"))
print("=== HN TOP 35 ===")
for s in hn:
    print(f"{s.get('score',0)}pts {s.get('descendants',0)}c | {s.get('title')} | {(s.get('url') or 'https://news.ycombinator.com/item?id='+str(s.get('id')))}")

print()
gh = json.load(open(f"{D}/github_trending_{DATE}.json"))["repositories"]
# dedupe by name, keep max stars
seen = {}
for r in gh:
    n = r["name"]
    if n not in seen or r["stars"] > seen[n]["stars"]:
        seen[n] = r
repos = sorted(seen.values(), key=lambda x: -x["stars"])
print(f"=== GITHUB TRENDING ({len(repos)} deduped) ===")
for r in repos[:40]:
    desc = (r.get("description") or "")[:110]
    print(f"{r['stars']}* [{r.get('language')}] {r['name']} — {desc} | {r['url']}")

print()
hf = json.load(open(f"{D}/huggingface_papers_{DATE}.json"))
print(f"=== HF PAPERS ({len(hf)}) ===")
items = hf if isinstance(hf, list) else hf.get("papers", [])
for p in items[:20]:
    if isinstance(p, dict):
        title = p.get("title") or p.get("paper", {}).get("title", "")
        likes = p.get("likes") or p.get("paper", {}).get("likes", 0)
        summary = (p.get("summary") or p.get("paper", {}).get("summary", "") or "")[:150]
        pid = p.get("id") or p.get("paper", {}).get("id", "")
        print(f"{likes}👍 {title} ({pid})\n    {summary}")
