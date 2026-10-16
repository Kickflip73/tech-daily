import json, urllib.request, urllib.parse, re, time
def algolia(url):
    req = urllib.request.Request(url, headers={'User-Agent':'tech-daily-bot/1.0'})
    return json.loads(urllib.request.urlopen(req, timeout=30).read().decode())
queries = ['OpenCode 2.0', 'Jev 1.14.0 dreamers', 'Iosevka', 'banks offload AI data center debt', 'Starlink site Bulgaria sabotage']
for q in queries:
    try:
        d = algolia('https://hn.algolia.com/api/v1/search?query=' + urllib.parse.quote(q) + '&tags=story&hitsPerPage=1')
        h = d['hits'][0]
        print('===', h['title'], '| points', h.get('points'), '| comments', h.get('num_comments'), '|', h.get('url'))
        cd = algolia(f"https://hn.algolia.com/api/v1/items/{h['objectID']}")
        cnt = 0
        def walk(children, depth=0):
            global cnt
            for c in children:
                if cnt >= 5: return
                t = c.get('text','')
                if t:
                    t = re.sub('<[^>]+>',' ',t)
                    print('  '*(depth+1) + '-', c.get('author','?'), ':', t[:250])
                    cnt += 1
                    walk(c.get('children',[])[:2], depth+1)
        walk(cd.get('children',[])[:4])
        time.sleep(1)
    except Exception as e:
        print('ERR', q, e)
