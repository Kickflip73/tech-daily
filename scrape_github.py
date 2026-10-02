#!/usr/bin/env python3
"""Scrape GitHub Trending pages using agent-browser and save structured data."""
import json
import subprocess
import time
import re

LANGUAGES = [
    ("", "all"),
    ("/python", "python"),
    ("/typescript", "typescript"),
    ("/go", "go"),
    ("/rust", "rust"),
    ("/java", "java"),
]

JS_EXTRACT = r"""
JSON.stringify(
  Array.from(document.querySelectorAll('article.Box-row')).map(el => {
    const h1 = el.querySelector('h2 a');
    const name = h1 ? h1.textContent.trim().replace(/\\s+/g, '') : null;
    const url = h1 ? 'https://github.com' + h1.getAttribute('href') : null;
    const desc = el.querySelector('p');
    const description = desc ? desc.textContent.trim() : null;
    const lang = el.querySelector('[itemprop="programmingLanguage"]');
    const language = lang ? lang.textContent.trim() : null;
    const starsMatch = el.textContent.match(/(\d[\\d,]*)\s*stars today/);
    const starsToday = starsMatch ? parseInt(starsMatch[1].replace(/,/g, '')) : null;
    // Get total stars from links
    const links = Array.from(el.querySelectorAll('a'));
    let totalStars = null;
    links.forEach(a => {
      const text = a.textContent.trim();
      if (/^\\d/.test(text) && !text.includes('today')) {
        const m = text.match(/([\\d,]+)\s*stars?/);
        if (m) totalStars = parseInt(m[1].replace(/,/g, ''));
      }
    });
    return { name, url, description, language, stars_today: starsToday, total_stars: totalStars };
  })
)
"""

all_repos = []
seen = set()

for path, lang in LANGUAGES:
    print(f"Scraping trending{path or ' (all)'}...")
    url = f"https://github.com/trending{path}"
    
    # Open page
    subprocess.run(["agent-browser", "open", url], capture_output=True, timeout=30)
    time.sleep(3)
    
    # Extract data
    result = subprocess.run(["agent-browser", "eval", "--stdin"], input=JS_EXTRACT, capture_output=True, text=True, timeout=30)
    
    if result.returncode == 0:
        raw = result.stdout.strip()
        # agent-browser returns quoted JSON string, need to unescape
        if raw.startswith('"') and raw.endswith('"'):
            raw = json.loads(raw)  # unescape
        try:
            repos = json.loads(raw)
            for repo in repos:
                if repo["name"] and repo["name"] not in seen:
                    seen.add(repo["name"])
                    repo["category"] = lang
                    all_repos.append(repo)
            print(f"  Found {len(repos)} repos, {len(repos) - len(all_repos) + sum(1 for r in repos if r['name'] not in seen)} new")
        except json.JSONDecodeError as e:
            print(f"  Parse error: {e}")
            print(f"  Raw output: {raw[:200]}")
    else:
        print(f"  Error: {result.stderr[:200]}")

data = {
    "date": "2026-08-23",
    "count": len(all_repos),
    "repositories": all_repos
}

with open("/root/.openclaw/workspace/tech-daily/data/github_trending_2026-08-23.json", "w") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"\nSaved {len(all_repos)} repositories to github_trending_2026-08-23.json")

# Print top 10
print("\nTop 10 by stars today:")
for r in sorted(all_repos, key=lambda x: x.get("stars_today") or 0, reverse=True)[:10]:
    print(f"  {r['stars_today'] or 0:>6}  [{r['category']:12}] {r['name']:40}  {r.get('language', 'N/A')}")
