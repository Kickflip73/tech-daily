import urllib.request, re, html, json, sys

def ft(url):
    try:
        req = urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0'})
        return urllib.request.urlopen(req, timeout=25).read().decode('utf-8','ignore')
    except Exception as e:
        return ''

def clean(t):
    t = re.sub(r'<script.*?</script>|<style.*?</style>','',t,flags=re.S)
    t = re.sub(r'<[^>]+>',' ',t)
    return html.unescape(re.sub(r'\s+',' ',t)).strip()

if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else 'hn'
    if mode == 'hn':
        t = ft('https://hn.algolia.com/api/v1/search?tags=front_page&hitsPerPage=45')
        data = json.loads(t)
        for h in data['hits'][:45]:
            print(h.get('points'), 'pt |', h.get('num_comments'), 'c |', h.get('title'), '|', h.get('url') or ('https://news.ycombinator.com/item?id=' + str(h.get('objectID'))))
    else:
        u = sys.argv[2]
        t = ft(u)
        if t:
            c = clean(t)
            i = c.lower().find(sys.argv[3].lower()) if len(sys.argv) > 3 else 0
            print(c[max(0,i-200):i+3500])
        else:
            print('FETCH FAILED')
