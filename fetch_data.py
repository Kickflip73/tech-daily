#!/usr/bin/env python3
"""Fetch tech daily data from multiple sources."""
import json
import xml.etree.ElementTree as ET
from datetime import datetime
import urllib.request
import urllib.error
import ssl

# Disable SSL verification for some hosts
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def fetch_json(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, context=ctx, timeout=30) as resp:
        return json.loads(resp.read().decode('utf-8'))

def fetch_text(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, context=ctx, timeout=30) as resp:
        return resp.read().decode('utf-8')

# ============= Hacker News =============
print("Fetching Hacker News...")
top_ids = fetch_json("https://hacker-news.firebaseio.com/v0/topstories.json")[:30]
hn_stories = []
for sid in top_ids:
    try:
        story = fetch_json(f"https://hacker-news.firebaseio.com/v0/item/{sid}.json")
        if story:
            hn_stories.append({
                "id": story.get("id"),
                "title": story.get("title"),
                "url": story.get("url"),
                "score": story.get("score"),
                "by": story.get("by"),
                "time": story.get("time"),
                "descendants": story.get("descendants", 0),
                "type": story.get("type")
            })
    except Exception as e:
        print(f"  Error fetching story {sid}: {e}")

with open("/root/.openclaw/workspace/tech-daily/data/hackernews_2026-08-23.json", "w") as f:
    json.dump({"date": "2026-08-23", "count": len(hn_stories), "stories": hn_stories}, f, indent=2)
print(f"  Saved {len(hn_stories)} HN stories")

# ============= arXiv =============
print("Fetching arXiv...")
arxiv_xml = fetch_text("http://export.arxiv.org/api/query?search_query=cat:cs.*&sortBy=submittedDate&sortOrder=descending&max_results=50")

ns = {
    'atom': 'http://www.w3.org/2005/Atom',
    'arxiv': 'http://arxiv.org/schemas/atom'
}
root = ET.fromstring(arxiv_xml)
arxiv_papers = []
for entry in root.findall('atom:entry', ns):
    paper = {
        "id": entry.find('atom:id', ns).text if entry.find('atom:id', ns) is not None else None,
        "title": entry.find('atom:title', ns).text.strip() if entry.find('atom:title', ns) is not None else None,
        "summary": entry.find('atom:summary', ns).text.strip() if entry.find('atom:summary', ns) is not None else None,
        "published": entry.find('atom:published', ns).text if entry.find('atom:published', ns) is not None else None,
        "updated": entry.find('atom:updated', ns).text if entry.find('atom:updated', ns) is not None else None,
        "primary_category": entry.find('arxiv:primary_category', ns).get('term') if entry.find('arxiv:primary_category', ns) is not None else None,
        "categories": [cat.get('term') for cat in entry.findall('atom:category', ns)],
        "authors": [author.find('atom:name', ns).text for author in entry.findall('atom:author', ns) if author.find('atom:name', ns) is not None],
        "links": [{"href": link.get('href'), "type": link.get('type', ''), "title": link.get('title', '')} for link in entry.findall('atom:link', ns)],
        "comment": entry.find('arxiv:comment', ns).text if entry.find('arxiv:comment', ns) is not None else None
    }
    arxiv_papers.append(paper)

with open("/root/.openclaw/workspace/tech-daily/data/arxiv_2026-08-23.json", "w") as f:
    json.dump({"date": "2026-08-23", "count": len(arxiv_papers), "papers": arxiv_papers}, f, indent=2)
print(f"  Saved {len(arxiv_papers)} arXiv papers")

# ============= HuggingFace Papers =============
print("Fetching HuggingFace Papers...")
try:
    hf_data = fetch_json("https://huggingface.co/api/papers?date=2026-08-23")
    hf_papers = []
    for p in hf_data:
        hf_papers.append({
            "id": p.get("id"),
            "title": p.get("title"),
            "upvotes": p.get("upvotes"),
            "publishedAt": p.get("publishedAt"),
            "authors": [a.get("name") for a in p.get("authors", [])],
            "summary": p.get("summary"),
            "ai_summary": p.get("ai_summary"),
            "projectPage": p.get("projectPage"),
            "githubRepo": p.get("githubRepo"),
            "thumbnailUrl": p.get("thumbnailUrl")
        })
    with open("/root/.openclaw/workspace/tech-daily/data/huggingface_papers_2026-08-23.json", "w") as f:
        json.dump({"date": "2026-08-23", "count": len(hf_papers), "papers": hf_papers}, f, indent=2)
    print(f"  Saved {len(hf_papers)} HF papers")
except Exception as e:
    print(f"  Error fetching HF papers: {e}")
    # Save empty placeholder
    with open("/root/.openclaw/workspace/tech-daily/data/huggingface_papers_2026-08-23.json", "w") as f:
        json.dump({"date": "2026-08-23", "count": 0, "papers": [], "error": str(e)}, f, indent=2)

# ============= GitHub Trending (alternative approach via GitHub API) =============
print("Fetching GitHub Trending (via search API)...")
# GitHub trending doesn't have a direct API, but we can use search for recently created repos with stars
github_items = []

# Try using GitHub's search API for repos created recently with high stars
# We use a simple approach: search for repos with stars > 50 created in last week
queries = [
    ("stars:>100 created:>2026-08-11", "all"),
    ("language:python stars:>50 created:>2026-08-11", "python"),
    ("language:typescript stars:>50 created:>2026-08-11", "typescript"),
    ("language:go stars:>50 created:>2026-08-11", "go"),
    ("language:rust stars:>50 created:>2026-08-11", "rust"),
    ("language:java stars:>50 created:>2026-08-11", "java"),
]

for q, lang in queries:
    try:
        url = f"https://api.github.com/search/repositories?q={urllib.parse.quote(q)}&sort=stars&order=desc&per_page=25"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, context=ctx, timeout=30) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            for item in data.get("items", []):
                github_items.append({
                    "name": item.get("full_name"),
                    "language": item.get("language") or lang,
                    "stars": item.get("stargazers_count"),
                    "stars_today": None,  # Not available via API
                    "description": item.get("description"),
                    "url": item.get("html_url"),
                    "created_at": item.get("created_at"),
                    "updated_at": item.get("updated_at"),
                    "category": lang
                })
    except Exception as e:
        print(f"  Error fetching GitHub {lang}: {e}")

with open("/root/.openclaw/workspace/tech-daily/data/github_trending_2026-08-23.json", "w") as f:
    json.dump({"date": "2026-08-23", "count": len(github_items), "repositories": github_items}, f, indent=2)
print(f"  Saved {len(github_items)} GitHub repos")

print("\nDone!")
