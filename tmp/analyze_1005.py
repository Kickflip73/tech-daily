import json
repos = json.load(open('/root/.openclaw/workspace/tech-daily/data/github_repos_2026-10-05.json'))
print("=== TOP DELTA ===")
rs = [r for r in repos if r['prev_stars'] is not None]
rs.sort(key=lambda r: r['stargazers_count'] - r['prev_stars'], reverse=True)
for r in rs[:40]:
    print(f"{r['stargazers_count']-r['prev_stars']:+6d} total {r['stargazers_count']:6d} [{r['language']}] {r['full_name']} :: {(r['description'] or '')[:110]}")
print()
print("=== NEW sorted by stars ===")
ns = [r for r in repos if r['prev_stars'] is None]
ns.sort(key=lambda r: r['stargazers_count'], reverse=True)
for r in ns[:40]:
    print(f"  NEW total {r['stargazers_count']:6d} [{r['language']}] {r['full_name']} :: {(r['description'] or '')[:110]}")
