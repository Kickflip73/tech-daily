import json, urllib.request, time, re

def getj(url):
    req = urllib.request.Request(url, headers={'User-Agent':'tech-daily-bot/1.0'})
    return json.loads(urllib.request.urlopen(req, timeout=30).read())

out = {}
for i, name in [(50664325,'claude_sabotage'), (50667989,'djb_false_proofs'), (50665968,'disclog_algo'), (50661646,'harddrives')]:
    item = getj(f'https://hacker-news.firebaseio.com/v0/item/{i}.json')
    kids = (item.get('kids') or [])[:8]
    comments = []
    for k in kids:
        try:
            c = getj(f'https://hacker-news.firebaseio.com/v0/item/{k}.json')
            if c and c.get('text'):
                txt = c['text'].replace('<p>','\n').replace('&#x27;',"'").replace('&gt;','>').replace('&amp;','&')
                txt = re.sub('<[^>]+>','',txt)
                comments.append((c.get('by'), txt[:900]))
            time.sleep(0.1)
        except Exception as e:
            pass
    out[name] = comments
json.dump(out, open('hn_comments_2026-11-28.json','w'), ensure_ascii=False, indent=1)
for name, cs in out.items():
    print('=====', name, '=====')
    for by, txt in cs[:4]:
        print('--', by, ':', txt[:400])
        print()
