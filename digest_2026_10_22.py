#!/usr/bin/env python3
"""Digest data for 2026-10-22 report."""
import json

D = "/root/.openclaw/workspace/tech-daily/data"

print("=" * 30, "GITHUB TOP 40 by stars", "=" * 30)
repos = json.load(open(f"{D}/github_repos_2026-10-22.json"))
repos.sort(key=lambda r: r.get("stargazers_count") or 0, reverse=True)
for r in repos[:40]:
    print(f"{r['stargazers_count']:>7} | {(r.get('language') or '-'):<12} | {r['full_name']:<45} | {(r.get('description') or '')[:110]}")

print()
print("=" * 30, "HN TOP 40", "=" * 30)
hn = json.load(open(f"{D}/hackernews_2026-10-22.json"))
hn.sort(key=lambda s: s.get("score") or 0, reverse=True)
for s in hn:
    print(f"{s.get('score'):>5}pt | {s.get('descendants',0):>4}c | {(s.get('title') or '')[:100]} | {s.get('url','')[:90]}")

print()
print("=" * 30, "HF PAPERS", "=" * 30)
hf = json.load(open(f"{D}/hfpapers_2026-10-22.json"))
for p in hf:
    pp = p.get("paper", p)
    likes = p.get("paper", {}).get("upvotes", "?")
    title = pp.get("title", "")
    pid = pp.get("id", "")
    print(f"{likes:>5} | {title[:110]} | {pid}")

print()
print("=" * 30, "arXiv sample titles", "=" * 30)
ax = json.load(open(f"{D}/arxiv_2026-10-22.json"))
for p in ax[:60]:
    print(f"{p['published'][:10]} | {p['title'][:120]} | {p['id']}")
