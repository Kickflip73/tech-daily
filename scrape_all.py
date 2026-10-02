#!/usr/bin/env python3
"""Scrape all 6 GitHub Trending pages via agent-browser."""
import json, subprocess, time

JS_EXTRACT = r"""
JSON.stringify(
  Array.from(document.querySelectorAll('article.Box-row')).map(el => {
    const h1 = el.querySelector('h2 a');
    const name = h1 ? h1.textContent.trim().replace(/\s+/g, '') : null;
    const url = h1 ? 'https://github.com' + h1.getAttribute('href') : null;
    const desc = el.querySelector('p');
    const description = desc ? desc.textContent.trim() : null;
    const lang = el.querySelector('[itemprop="programmingLanguage"]');
    const language = lang ? lang.textContent.trim() : null;
    const starsMatch = el.textContent.match(/(\d[\d,]*)\s*stars today/);
    const starsToday = starsMatch ? parseInt(starsMatch[1].replace(/,/g, '')) : null;
    return { name, url, description, language, stars_today: starsToday };
  })
)
"""

pages = [
    ("/trending", "all"),
    ("/trending/python", "python"),
    ("/trending/typescript", "typescript"),
    ("/trending/go", "go"),
    ("/trending/rust", "rust"),
    ("/trending/java", "java"),
]

all_repos = []
seen = set()

for path, cat in pages:
    print(f"Fetching {cat}...")
    subprocess.run(["agent-browser", "open", f"https://github.com{path}"], capture_output=True, timeout=30)
    time.sleep(3)
    result = subprocess.run(["agent-browser", "eval", "--stdin"], input=JS_EXTRACT, capture_output=True, text=True, timeout=30)
    
    if result.returncode == 0:
        raw = result.stdout.strip()
        if raw.startswith('"') and raw.endswith('"'):
            raw = json.loads(raw)
        repos = json.loads(raw)
        for r in repos:
            r["category"] = cat
            if r["name"] not in seen:
                seen.add(r["name"])
                all_repos.append(r)
        print(f"  {len(repos)} repos scraped")
    else:
        print(f"  Error: {result.stderr[:100]}")

# Save
with open("/root/.openclaw/workspace/tech-daily/data/github_trending_2026-09-12.json", "w") as f:
    json.dump({"date": "2026-08-18", "count": len(all_repos), "repositories": all_repos}, f, indent=2, ensure_ascii=False)

print(f"\nTotal unique repos: {len(all_repos)}")
print("Top 10 by stars today:")
for r in sorted(all_repos, key=lambda x: x.get("stars_today") or 0, reverse=True)[:10]:
    print(f"  {r['stars_today'] or 0:>6}  [{r['category']:12}] {r['name']:40}  {r.get('language', 'N/A')}")
