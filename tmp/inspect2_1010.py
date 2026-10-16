import json

repos = json.load(open('data/github_repos_2026-10-10.json'))
prev = {}
import glob
cands = [c for c in glob.glob('data/github_repos_*.json') if '2026-10-10' not in c]
if cands:
    for r in json.load(open(sorted(cands)[-1])):
        prev[r.get('full_name','')] = r

print("=== storytold matrix + selected repos ===")
watch = ['storytold/', 'openai/math', 'mhtsec/ARTEX', 'jiwoochris/artex-ko', 'cskwork/scopeweaver',
         'zhongerxin/iPhone-use', 'nullmoth/', 'openqodex', 'vibe', 'AIHOT', 'aihot', 'universal-modder',
         'aurelio', 'ProxyNodeHub', 'x_gift_bot', 'answer-me-with-html', 'huashu', 'AlIHOT']
seen = set()
for r in repos:
    fn = r['full_name']
    if any(w in fn for w in watch) and fn not in seen:
        seen.add(fn)
        d = ''
        if r.get('prev_stars') is not None:
            d = f" (+{r['stargazers_count']-r['prev_stars']})"
        print(f"{r['stargazers_count']}{d} | {fn}")
print()
print("total storytold stars:")
tot = sum(r['stargazers_count'] or 0 for r in repos if 'storytold/' in r['full_name'])
print(tot, [f"{r['full_name'].split('/')[1]}:{r['stargazers_count']}" for r in repos if 'storytold/' in r['full_name']])
