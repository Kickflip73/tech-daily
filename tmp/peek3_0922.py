import json
D = "2026-09-22"
base = "/root/.openclaw/workspace/tech-daily/data"

hn = json.load(open(f"{base}/hackernews_{D}.json"))
hn.sort(key=lambda x: -(x.get("score") or 0))
print("=== HN full list (40) ===")
for s in hn:
    print(f'{s.get("score"):>5}  {(s.get("title") or "")[:120]} | {(s.get("url") or "")[:90]}')

print()
print("=== GITHUB all (dedup, by stars) ===")
gh = json.load(open(f"{base}/github_trending_{D}.json"))["repositories"]
seen = {}
for r in gh:
    if r["name"] not in seen or (r["stars"] or 0) > seen[r["name"]]["stars"]:
        seen[r["name"]] = r
for r in sorted(seen.values(), key=lambda x: -(x["stars"] or 0)):
    print(f'{r["stars"]:>6}  {r["name"]} [{r["language"]}] {(r["description"] or "")[:130]}')
