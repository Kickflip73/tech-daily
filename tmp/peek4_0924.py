import json, urllib.request, ssl, time
hn = json.load(open('data/hackernews_2026-09-24.json'))
targets = ["Jev in 25 Lines", "AGENTS.md", "Tokens too cheap", "Sol and Luna", "enzyme", "Stripe's Knowledge"]
ctx = ssl.create_default_context(); ctx.check_hostname=False; ctx.verify_mode=ssl.CERT_NONE
def gj(u):
    req = urllib.request.Request(u, headers={"User-Agent":"t/1.0"})
    return json.loads(urllib.request.urlopen(req, timeout=20, context=ctx).read().decode())
for s in hn:
    t = s.get('title','')
    if any(k.lower() in t.lower() for k in targets):
        print("="*80)
        print(t, "| score", s.get('score'), "| id", s.get('id'))
        kids = s.get('kids', [])[:3]
        for k in kids:
            try:
                c = gj(f"https://hacker-news.firebaseio.com/v0/item/{k}.json")
                txt = (c.get('text') or '').replace('<p>','\n')[:600]
                print(f"--- comment by {c.get('by')}: {txt}")
            except Exception as e:
                print("err", e)
            time.sleep(0.05)
