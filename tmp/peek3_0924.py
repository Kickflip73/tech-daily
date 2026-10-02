import json
hf = json.load(open('data/huggingface_papers_2026-09-24.json'))
for p in hf[25:50]:
    pid = p.get('paper',{}).get('id','') if isinstance(p.get('paper'),dict) else p.get('id','')
    print(f"{p.get('upvotes',0):>5}  {p.get('title','')[:110]} | {pid}")
print()
arx = json.load(open('data/arxiv_2026-09-24.json'))
print("=== arXiv (50) ===")
for p in arx[:50]:
    print(f"- {p['title'][:110]} | {p['id'].split('/abs/')[-1]}")
