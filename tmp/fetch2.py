import urllib.request, re
def f(url, n=3000):
    req = urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0 (Macintosh)'})
    html = urllib.request.urlopen(req, timeout=30).read().decode('utf-8','ignore')
    text = re.sub(r'<script[\s\S]*?</script>|<style[\s\S]*?</style>','',html)
    text = re.sub(r'<[^>]+>',' ',text)
    text = re.sub(r'\s+',' ',text)
    return text[:n]
for u in ['https://www.liquid.ai/blog/lfm2-5-24b-a2b','https://typesafe.ai/blog/jev-1-14','https://anoma.ly/notes/opencode-2-0/']:
    print('=====', u)
    try: print(f(u))
    except Exception as e: print('ERR', e)
