import json

# HF papers
hf = json.load(open('data/hfpapers_2026-10-04.json'))
print("=== HF PAPERS ===")
for p in hf:
    paper = p.get('paper', p)
    pid = paper.get('id', '')
    title = paper.get('title', '')
    upvotes = p.get('paper', {}).get('upvotes', p.get('upvotes', 0))
    print(f"{upvotes}up  {title}  || {pid}")

print()
print("=== ARXIV ===")
ax = json.load(open('data/arxiv_2026-10-04.json'))
for p in ax:
    cats = ','.join(p.get('categories', [])[:2])
    print(f"{p['published'][:10]} [{cats}] {p['title']} || {p['id']}")
