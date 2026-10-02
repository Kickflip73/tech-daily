import json
D = "2026-09-22"
hf = json.load(open(f"/root/.openclaw/workspace/tech-daily/data/huggingface_papers_{D}.json"))
print(json.dumps(hf[0], ensure_ascii=False)[:600])
print("----")
for p in hf[:20]:
    paper = p.get("paper") or {}
    print(f'{paper.get("upvotes", 0):>5}  {paper.get("title","")[:110]} | {paper.get("url") or paper.get("id","")}')
print("---- arxiv top")
ax = json.load(open(f"/root/.openclaw/workspace/tech-daily/data/arxiv_{D}.json"))
for p in ax[:15]:
    print(f'[{p.get("primary_category","")}] {p.get("title","")[:110]}')
