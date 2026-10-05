import json
D = '/root/.openclaw/workspace/tech-daily/data/'
hn = json.load(open(D + 'hackernews_2026-10-05.json'))
print("=== HN TOP 40 ===")
for s in hn:
    if not s: continue
    print(f"{s.get('score',0):5d} pts {s.get('descendants',0):4d} cmt | {s.get('title','')[:95]} | {s.get('url','')[:80]}")
print()
hf = json.load(open(D + 'hfpapers_2026-10-05.json'))
print("=== HF PAPERS ===")
for p in hf:
    pp = p.get('paper', p)
    title = pp.get('title','')
    up = pp.get('upvotes', p.get('upvotes', '?'))
    print(f"{up} 👍 | {title[:110]}")
