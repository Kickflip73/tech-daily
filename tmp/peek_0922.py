import json
D = "2026-09-22"
gh = json.load(open(f"/root/.openclaw/workspace/tech-daily/data/github_trending_{D}.json"))["repositories"]
seen = set()
print("=== GITHUB TOP ===")
n = 0
for r in sorted(gh, key=lambda x: -(x["stars"] or 0)):
    if r["name"] in seen:
        continue
    seen.add(r["name"])
    n += 1
    if n > 25:
        break
    print(f'{r["stars"]:>6}  {r["name"]} [{r["language"]}] {(r["description"] or "")[:110]}')

print()
print("=== HN TOP ===")
hn = json.load(open(f"/root/.openclaw/workspace/tech-daily/data/hackernews_{D}.json"))
hn.sort(key=lambda x: -(x.get("score") or 0))
for s in hn[:25]:
    print(f'{s.get("score"):>5}  {s.get("title","")[:100]} | {s.get("url") or "HN:"+str(s.get("id"))}')

print()
print("=== HF PAPERS TOP ===")
hf = json.load(open(f"/root/.openclaw/workspace/tech-daily/data/huggingface_papers_{D}.json"))
for p in hf[:20]:
    print(f'{p.get("paper",{}).get("upvotes",0):>5}  {p.get("paper",{}).get("title","")[:110]}')
