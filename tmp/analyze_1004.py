import json

gh = json.load(open('data/github_repos_2026-10-04.json'))
rows = []
for r in gh:
    cur = r.get('stargazers_count') or 0
    prev = r.get('prev_stars')
    if prev is None:
        rows.append((None, cur, 'NEW', r))
    else:
        rows.append((cur - prev, cur, 'OLD', r))

print("=== TOP DELTA ===")
old = sorted([x for x in rows if x[2] == 'OLD'], key=lambda x: -x[0])[:25]
for d, cur, t, r in old:
    print(f"+{d}  total={cur}  {r['full_name']}  [{r['language']}]  {(r['description'] or '')[:110]}")

print()
print("=== TOP NEW ===")
new = sorted([x for x in rows if x[2] == 'NEW'], key=lambda x: -x[1])[:20]
for d, cur, t, r in new:
    print(f"NEW total={cur}  created={r['created_at'][:10]}  {r['full_name']}  [{r['language']}]  {(r['description'] or '')[:110]}")

print()
print("=== HN TOP 40 ===")
hn = json.load(open('data/hackernews_2026-10-04.json'))
for s in hn:
    print(f"{s.get('score')}pts {s.get('descendants')}c  {s.get('title')}  || {(s.get('url') or '')[:90]}")
