import json

hn = json.load(open('data/hackernews_2026-10-10.json'))
print("=== HN TOP 40 ===")
for s in hn:
    print(f"{s.get('score')}pt {s.get('descendants',0)}c | {s.get('title')} | {s.get('url','')}")

print()
repos = json.load(open('data/github_repos_2026-10-10.json'))
print("=== GITHUB repos with delta ===")
# sort by delta then stars
rows = [r for r in repos if r.get('prev_stars') is not None]
new = [r for r in repos if r.get('prev_stars') is None]
rows.sort(key=lambda r: (r['stargazers_count'] - r['prev_stars']), reverse=True)
for r in rows[:45]:
    print(f"+{r['stargazers_count']-r['prev_stars']} total {r['stargazers_count']} | {r['full_name']} [{r.get('language')}] {(r.get('description') or '')[:110]}")
print()
print(f"--- {len(new)} NEW repos (top by stars) ---")
new.sort(key=lambda r: r['stargazers_count'] or 0, reverse=True)
for r in new[:45]:
    print(f"NEW {r['stargazers_count']} | {r['full_name']} [{r.get('language')}] {(r.get('description') or '')[:110]}")
