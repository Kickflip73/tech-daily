#!/usr/bin/env python3
import json

with open('data/github_repos_2026-10-07.json') as f:
    repos = json.load(f)
rows = []
for r in repos:
    if r.get('prev_stars') is not None:
        d = r['stargazers_count'] - r['prev_stars']
        rows.append((d, r))
    else:
        rows.append((None, r))
known = sorted([x for x in rows if x[0] is not None], key=lambda x: -x[0])
new = [x for x in rows if x[0] is None]
new = sorted(new, key=lambda x: -(x[1]['stargazers_count'] or 0))
print("=== TOP 40 by 24h delta ===")
for d, r in known[:40]:
    print(f"{d:+5d} | {r['stargazers_count']:5d} | {r['language'] or '-':12} | {r['full_name']} | {(r['description'] or '')[:90]}")
print()
print("=== TOP 25 NEW (no prev) ===")
for d, r in new[:25]:
    print(f"  NEW | {r['stargazers_count']:5d} | {r['language'] or '-':12} | {r['full_name']} | {(r['description'] or '')[:90]}")
