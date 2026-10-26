#!/usr/bin/env python3
"""Fetch tech data sources for 2026-10-26."""
import json, os, re, time, urllib.request, xml.etree.ElementTree as ET

DATE = "2026-10-26"
DATA_DIR = "/root/.openclaw/workspace/tech-daily/data"
os.makedirs(DATA_DIR, exist_ok=True)

def fetch_json(url, timeout=30):
    for attempt in range(2):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "tech-daily-bot/1.0"})
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return json.loads(resp.read().decode())
        except Exception as e:
            print(f"Error fetching {url} (attempt {attempt+1}): {e}")
            time.sleep(2)
    return None

def fetch_text(url, timeout=90):
    for attempt in range(2):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "tech-daily-bot/1.0"})
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read().decode()
        except Exception as e:
            print(f"Error fetching {url} (attempt {attempt+1}): {e}")
            time.sleep(2)
    return None

# 1. Hacker News
print("=== Hacker News ===")
hn_ids = fetch_json("https://hacker-news.firebaseio.com/v0/topstories.json")
hn_stories = []
if hn_ids:
    for story_id in hn_ids[:40]:
        story = fetch_json(f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json")
        if story:
            hn_stories.append(story)
        time.sleep(0.05)
    print(f"Fetched {len(hn_stories)} HN stories")
    with open(f"{DATA_DIR}/hackernews_{DATE}.json", "w") as f:
        json.dump(hn_stories, f, indent=2, ensure_ascii=False)
else:
    print("HN fetch FAILED - skipped")

# 2. arXiv
print("=== arXiv ===")
arxiv_xml = fetch_text("https://export.arxiv.org/api/query?search_query=cat:cs.*&sortBy=submittedDate&sortOrder=descending&max_results=60", timeout=90)
if arxiv_xml:
    ns = {"atom": "http://www.w3.org/2005/Atom"}
    arxiv_papers = []
    try:
        root = ET.fromstring(arxiv_xml.encode())
        for entry in root.findall("atom:entry", ns):
            paper = {}
            t = entry.find("atom:title", ns)
            paper["title"] = re.sub(r"\s+", " ", t.text).strip() if t is not None and t.text else ""
            s = entry.find("atom:summary", ns)
            paper["summary"] = re.sub(r"\s+", " ", s.text).strip() if s is not None and s.text else ""
            i = entry.find("atom:id", ns)
            paper["id"] = i.text if i is not None else ""
            p = entry.find("atom:published", ns)
            paper["published"] = p.text if p is not None else ""
            authors = [a.find("atom:name", ns).text for a in entry.findall("atom:author", ns) if a.find("atom:name", ns) is not None]
            paper["authors"] = authors
            link = entry.find("atom:link[@rel='alternate']", ns)
            paper["link"] = link.get("href", "") if link is not None else ""
            cats = [c.get("term") for c in entry.findall("atom:category", ns)]
            paper["categories"] = cats
            arxiv_papers.append(paper)
    except Exception as e:
        print(f"Error parsing arxiv: {e}")
    with open(f"{DATA_DIR}/arxiv_{DATE}.json", "w") as f:
        json.dump(arxiv_papers, f, indent=2, ensure_ascii=False)
    print(f"Fetched {len(arxiv_papers)} arxiv papers")
else:
    print("arXiv fetch FAILED - skipped")

# 3. GitHub Trending (Search API - repos created in last 10 days, sorted by stars)
print("=== GitHub Trending ===")
gh_repos = []
seen = set()
for page in range(1, 4):
    url = ("https://api.github.com/search/repositories?q=created:%3E2026-10-16&sort=stars&order=desc&per_page=100&page=" + str(page))
    data = fetch_json(url)
    if data and "items" in data:
        for r in data["items"]:
            if r["full_name"] not in seen:
                seen.add(r["full_name"])
                gh_repos.append(r)
    else:
        print(f"Page {page} returned no items")
    time.sleep(1.5)
print(f"Fetched {len(gh_repos)} unique GitHub repos")

# delta vs yesterday snapshot
prev = {}
for prev_file in [f"{DATA_DIR}/github_repos_2026-10-25.json", f"{DATA_DIR}/github_2026-10-25.json"]:
    if os.path.exists(prev_file):
        try:
            for r in json.load(open(prev_file)):
                fn = r.get("full_name", "")
                if fn and fn not in prev:
                    prev[fn] = {"stargazers_count": r.get("stargazers_count", r.get("stars"))}
            print(f"Loaded prev snapshot: {prev_file}")
        except Exception as e:
            print(f"Error loading prev {prev_file}: {e}")

repos_out = []
for r in gh_repos:
    fn = r.get("full_name", "")
    prev_star = prev.get(fn, {}).get("stargazers_count")
    repos_out.append({
        "full_name": fn,
        "stargazers_count": r.get("stargazers_count"),
        "prev_stars": prev_star,
        "language": r.get("language"),
        "description": r.get("description"),
        "created_at": r.get("created_at"),
        "url": r.get("html_url"),
        "topics": r.get("topics", []),
    })

with open(f"{DATA_DIR}/github_repos_{DATE}.json", "w") as f:
    json.dump(repos_out, f, indent=2, ensure_ascii=False)
matched = sum(1 for r in repos_out if r["prev_stars"] is not None)
print(f"Saved {len(repos_out)} repos (delta computed for {matched})")

# 4. HuggingFace Daily Papers
print("=== HuggingFace Papers ===")
hf = fetch_json("https://huggingface.co/api/daily_papers?limit=30")
if hf:
    with open(f"{DATA_DIR}/hfpapers_{DATE}.json", "w") as f:
        json.dump(hf, f, indent=2, ensure_ascii=False)
    print(f"Fetched {len(hf)} HF papers")
else:
    print("HF papers fetch FAILED - skipped")

print("ALL DONE")
