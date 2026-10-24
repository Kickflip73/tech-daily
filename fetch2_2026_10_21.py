#!/usr/bin/env python3
import json, ssl, urllib.request, time, base64
ctx = ssl.create_default_context(); ctx.check_hostname=False; ctx.verify_mode=ssl.CERT_NONE
def fj(url, timeout=25):
    try:
        req = urllib.request.Request(url, headers={"User-Agent":"tech-daily-bot/1.0"})
        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as r:
            return json.loads(r.read().decode())
    except Exception as e:
        print("ERR", url, e); return None

y = fj("https://api.github.com/search/repositories?q=created:%3E2026-10-10+created:%3C2026-10-21&sort=stars&order=desc&per_page=100")
if y:
    prev = {it["full_name"]: it["stargazers_count"] for it in y.get("items", [])}
    json.dump(prev, open("data/gh_prev_2026-10-21.json","w"))
    print("prev snapshot:", len(prev))

targets = ["deepseek-ai/DeepInfer","Gathin23/cleanyourtv","chenglou/handwired","rohit267/net-merge",
           "Caho1/open-claude-ui","zhuyansen/new-term-radar","Zfinix/eleven","juliobsz/skills",
           "datalab-to/indra","outcrawlai/scout","LiCinCan/blender-ai-mcp-addon","threerocks/sweety-handdraw-video",
           "MyLuxy/overdrive","humblemuzzu/dumbtv","Ansub/tv-detox","yeyuxin777/baoyan-agent-benchmark",
           "CoolkHz/gptibo","xscreensaver-official/xscreensaver"]
out = {}
for t in targets:
    rd = fj(f"https://api.github.com/repos/{t}/readme")
    if rd and rd.get("content"):
        txt = base64.b64decode(rd["content"]).decode("utf-8","ignore")
        out[t] = txt[:6000]
        print("OK readme:", t, len(txt))
    time.sleep(0.3)
json.dump(out, open("data/gh_readmes_2026-10-21.json","w"), ensure_ascii=False)
print("DONE")
