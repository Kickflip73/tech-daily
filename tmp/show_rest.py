import json

D = "/root/.openclaw/workspace/tech-daily/data"

hf = json.load(open(f"{D}/hfpapers_2026-10-28.json"))
print("=== HF Daily Papers (top by upvotes) ===")
for p in sorted(hf, key=lambda x: -(x.get("paper", {}).get("upvotes") or 0))[:25]:
    pap = p.get("paper", {})
    print(f"{pap.get('upvotes',0):>4} | {pap.get('title','')[:95]}")
    print(f"      {pap.get('summary','')[:200]}")

print()
arx = json.load(open(f"{D}/arxiv_2026-10-28.json"))
print("=== arXiv 60 titles ===")
for p in arx:
    print(f"- [{','.join(p['categories'][:3])}] {p['title'][:90]}")
