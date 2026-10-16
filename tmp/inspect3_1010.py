import json

print("=== HF papers ===")
hf = json.load(open('data/hfpapers_2026-10-10.json'))
for p in hf:
    pp = p.get('paper', p)
    likes = pp.get('upvotes', pp.get('likes', 0)) or 0
    title = pp.get('title','').replace('\n',' ')
    print(f"{likes}👍 | {title} | {pp.get('id','')}")

print()
print("=== arXiv latest 50 ===")
ax = json.load(open('data/arxiv_2026-10-10.json'))
for p in ax:
    cats = ','.join(p.get('categories', [])[:2])
    print(f"[{cats}] {p['title']} | {p['id']}")
