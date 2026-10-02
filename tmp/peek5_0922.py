import json
D = "2026-09-22"
hf = json.load(open(f"/root/.openclaw/workspace/tech-daily/data/huggingface_papers_{D}.json"))
print("keys of first:", list(hf[0].keys()))
rows = []
for p in hf:
    q = p.get("paper") or p
    rows.append((q.get("upvotes", 0) or 0, q.get("title", ""), q.get("publishedAt", ""), q.get("id", "")))
rows.sort(reverse=True)
for u, t, d, i in rows[:25]:
    print(f'{u:>4}  {t[:100]} | {d[:10]} | {i}')
