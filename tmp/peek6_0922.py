import json
D = "2026-09-22"
hf = json.load(open(f"/root/.openclaw/workspace/tech-daily/data/huggingface_papers_{D}.json"))
ids = ["2609.20519","2609.20511","2609.21346","2609.22068","2609.20804","2609.22000","2609.20800","2609.20784","2609.22086","2609.21465","2609.20816","2609.21749","2609.20942"]
for p in hf:
    if p.get("id") in ids:
        print(f'--- {p["id"]} [{p.get("organization","")}] 👍{p.get("upvotes")} {p.get("title")}')
        print((p.get("summary") or "")[:500])
        print()
