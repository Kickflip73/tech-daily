import json
D = "2026-09-22"
hf = json.load(open(f"/root/.openclaw/workspace/tech-daily/data/huggingface_papers_{D}.json"))
rows = []
for p in hf:
    paper = p.get("paper") or {}
    rows.append((paper.get("upvotes", 0) or 0, paper.get("title", ""), paper.get("publishedAt", ""), [a.get("name") for a in (paper.get("authors") or [])[:3]], paper.get("id", "")))
rows.sort(reverse=True)
for u, t, d, a, i in rows[:25]:
    print(f'{u:>4}  {t[:100]} | {d[:10]} | {a} | {i}')
