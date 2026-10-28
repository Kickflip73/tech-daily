import json, urllib.request

def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "tech-daily-bot/1.0"})
    return json.loads(urllib.request.urlopen(req, timeout=30).read().decode())

names = ['unclebob/crapper','unclebob/dryer','unclebob/mutator','unclebob/uml-viewer','Motionsites-AI/claude-skill','stormydayy/halo-overlay','NVIDIA/local-inference']
for n in names:
    try:
        r = get(f"https://api.github.com/repos/{n}")
        print(f"{n}: {r['stargazers_count']} | created={r['created_at'][:10]} | lang={r.get('language')} | {(r.get('description') or '')[:100]}")
    except Exception as e:
        print(f"{n}: ERR {e}")
