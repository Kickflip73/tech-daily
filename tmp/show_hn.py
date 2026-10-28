import json
hn = json.load(open("/root/.openclaw/workspace/tech-daily/data/hackernews_2026-10-28.json"))
hn.sort(key=lambda s: s.get("score", 0), reverse=True)
print("=== HN TOP 30 ===")
for s in hn[:30]:
    print(f"{s.get('score',0):>4} | {s.get('title','')[:95]} | {s.get('url','')[:85]} | c:{s.get('descendants',0)}")
