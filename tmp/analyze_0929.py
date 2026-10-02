#!/usr/bin/env python3
import json
d = "/mnt/openclaw/.openclaw/workspace/tech-daily/data/"
gh = json.load(open(d + "github_repos_2026-09-29.json"))
prev = {r["full_name"]: r for r in json.load(open(d + "github_repos_2026-09-28.json"))}
rows = []
for r in gh:
    fn = r["full_name"]
    cur = r["stargazers_count"]
    p = prev.get(fn)
    d24 = (cur - p["stargazers_count"]) if p else None
    rows.append((cur, d24 if d24 is not None else 0, fn, r.get("language"), (r.get("description") or "")[:110], fn in prev))
rows.sort(key=lambda x: -x[0])
print("=== TOP 45 by stars (24h delta vs 9/28 snapshot) ===")
for cur, d24, fn, lang, desc, isold in rows[:45]:
    tag = ("NEW " if not isold else f"+{d24}")
    print(f"{cur:>7} {tag:>7} {fn} [{lang}] {desc}")
print()
newcomers = [r for r in gh if r["full_name"] not in prev]
print(f"newcomers: {len(newcomers)} / {len(gh)}")
print()
print("=== TOP NEWCOMERS ===")
newc = [x for x in rows if not x[5]][:25]
for cur, d24, fn, lang, desc, _ in newc:
    print(f"{cur:>7}       {fn} [{lang}] {desc}")
