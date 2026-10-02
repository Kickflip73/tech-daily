import json

D = '/mnt/openclaw/.openclaw/workspace/tech-daily/data/'
prev = {r['name']: r['stars'] for r in json.load(open(D+'github_trending_2026-09-25.json'))['repositories']}
today = json.load(open(D+'github_repos_2026-09-26.json'))

news = [r for r in today if r['full_name'] not in prev]
news.sort(key=lambda x: -(x['stargazers_count'] or 0))
print(f"=== NEW repos today (not in yesterday's 122): {len(news)} ===")
for r in news[:40]:
    print(f"{r['stargazers_count']:5d}  {r['full_name']} [{r['language']}] created {r['created_at'][:10]}")
    desc = (r['description'] or '')[:100]
    print(f"       {desc}")
