import json
gh = json.load(open('data/github_trending_2026-09-24.json'))['repositories']
seen = {}
for r in gh:
    n = r['name']
    if n not in seen or r['stars'] > seen[n]['stars']:
        seen[n] = r
top = sorted(seen.values(), key=lambda x: -x['stars'])
print(f"Unique repos: {len(top)}")
for r in top[:50]:
    print(f"{r['stars']:>7}  {r['name']:<45} {str(r['language']):<12} {str(r['description'])[:95]}")
