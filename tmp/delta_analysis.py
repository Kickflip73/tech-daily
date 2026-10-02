import json

prev = {r['name']: r['stars'] for r in json.load(open('/mnt/openclaw/.openclaw/workspace/tech-daily/data/github_trending_2026-09-25.json'))['repositories']}
today = json.load(open('/mnt/openclaw/.openclaw/workspace/tech-daily/data/github_repos_2026-09-26.json'))
matched = []
for r in today:
    if r['full_name'] in prev:
        delta = r['stargazers_count'] - prev[r['full_name']]
        matched.append((delta, r['stargazers_count'], r['full_name'], r['language']))
matched.sort(reverse=True)
print(f"Matched {len(matched)} repos with yesterday snapshot. Top 30 by delta:")
for d, s, n, l in matched[:30]:
    print(f"+{d:5d}  {s:6d}  {n}  [{l}]")
print()
print("Top 20 by total stars (all 300):")
for r in sorted(today, key=lambda x: -(x['stargazers_count'] or 0))[:20]:
    if r['full_name'] in prev:
        d = r['stargazers_count'] - prev[r['full_name']]
        mark = f"(+{d})"
    else:
        mark = "(new)"
    print(f"{r['stargazers_count']:6d} {mark:9s} {r['full_name']} [{r['language']}]")
