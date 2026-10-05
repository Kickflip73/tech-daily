import json
D = '/root/.openclaw/workspace/tech-daily/data/'
ax = json.load(open(D + 'arxiv_2026-10-05.json'))
for p in ax:
    cats = ','.join(p.get('categories', [])[:2])
    print(f"[{cats}] {p['title'][:105]}")
