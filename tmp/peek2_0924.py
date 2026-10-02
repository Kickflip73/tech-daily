import json
hn = json.load(open('data/hackernews_2026-09-24.json'))
print("=== HN TOP ===")
for s in hn[:35]:
    print(f"{s.get('score',0):>5}  {s.get('title','')[:100]}  | {s.get('url','')[:80]} | c:{s.get('descendants',0)}")
print()
print("=== HF Papers ===")
hf = json.load(open('data/huggingface_papers_2026-09-24.json'))
for p in hf[:25]:
    print(f"{p.get('upvotes',0):>5}  {p.get('title','')[:110]} | {p.get('paper',{}).get('id','') if isinstance(p.get('paper'),dict) else p.get('id','')}")
