import json

D = '/mnt/openclaw/.openclaw/workspace/tech-daily/data/'
DATE = '2026-09-26'

print("===== HACKER NEWS TOP 40 =====")
hn = json.load(open(D + f'hackernews_{DATE}.json'))
for s in hn:
    if not s:
        continue
    print(f"[{s.get('score',0):4d}pts {s.get('descendants',0):4d}c] {s.get('title','')} | {s.get('url','') or 'https://news.ycombinator.com/item?id='+str(s.get('id'))}")

print()
print("===== HUGGINGFACE DAILY PAPERS (top 30) =====")
try:
    hf = json.load(open(D + f'hfpapers_{DATE}.json'))
    items = hf if isinstance(hf, list) else hf.get('recentlyTrendingPapers', hf)
    for p in items:
        if not isinstance(p, dict): continue
        paper = p.get('paper', p)
        title = paper.get('title','')
        ups = p.get('paper', {}).get('upvotes', p.get('upvotes', 0)) if isinstance(p, dict) else 0
        aid = paper.get('id','')
        print(f"[{ups:3d}👍] {title} (arxiv {aid})")
except Exception as e:
    print("HF parse error:", e)

print()
print("===== ARXIV latest cs (titles only) =====")
ax = json.load(open(D + f'arxiv_{DATE}.json'))
for p in ax[:50]:
    t = p['title'].replace('\n',' ')[:110]
    print(f"- {t} ({p['id'].split('/abs/')[-1]})")
