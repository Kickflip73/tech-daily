#!/usr/bin/env python3
"""Fetch tech data sources for 2026-09-23."""
import json
import xml.etree.ElementTree as ET
import urllib.request
import urllib.parse
import ssl
import time
import os

DATE = "2026-09-23"
DATA_DIR = "/root/.openclaw/workspace/tech-daily/data"
os.makedirs(DATA_DIR, exist_ok=True)

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def fetch_json(url, timeout=30):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "tech-daily-bot/1.0"})
        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
            return json.loads(resp.read().decode())
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def fetch_text(url, timeout=30):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "tech-daily-bot/1.0"})
        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
            return resp.read().decode()
    except Exception as e:
        print(f"Error fetching {url}: {e}")
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

# 2. arXiv
print("=== arXiv ===")
arxiv_xml = fetch_text(
    "http://export.arxiv.org/api/query?search_query=cat:cs.*&sortBy=submittedDate&sortOrder=descending&max_results=50",
    timeout=60)
if arxiv_xml:
    with open(f"{DATA_DIR}/arxiv_{DATE}.xml", "w") as f:
        f.write(arxiv_xml)
    ns = {"atom": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}
    arxiv_papers = []
    try:
        root = ET.fromstring(arxiv_xml.encode())
        for entry in root.findall("atom:entry", ns):
            paper = {}
            title = entry.find("atom:title", ns)
            paper["title"] = title.text.strip() if title is not None and title.text else ""
            summary = entry.find("atom:summary", ns)
            paper["summary"] = summary.text.strip() if summary is not None and summary.text else ""
            id_elem = entry.find("atom:id", ns)
            paper["id"] = id_elem.text if id_elem is not None else ""
            published = entry.find("atom:published", ns)
            paper["published"] = published.text if published is not None else ""
            authors = []
            for author in entry.findall("atom:author", ns):
                name = author.find("atom:name", ns)
                if name is not None and name.text:
                    authors.append(name.text)
            paper["authors"] = authors
            link = entry.find("atom:link[@rel='alternate']", ns)
            paper["link"] = link.get("href", "") if link is not None else ""
            arxiv_papers.append(paper)
        with open(f"{DATA_DIR}/arxiv_{DATE}.json", "w") as f:
            json.dump(arxiv_papers, f, indent=2, ensure_ascii=False)
        print(f"Fetched {len(arxiv_papers)} arXiv papers")
    except Exception as e:
        print(f"Error parsing arXiv XML: {e}")

# 3. HuggingFace Papers
print("=== HuggingFace Papers ===")
hf_data = fetch_json("https://huggingface.co/api/papers", timeout=30)
if hf_data and isinstance(hf_data, list):
    with open(f"{DATA_DIR}/huggingface_papers_{DATE}.json", "w") as f:
        json.dump(hf_data, f, indent=2, ensure_ascii=False)
    print(f"Fetched HF papers: {len(hf_data)}")

# 4. GitHub Trending via search API
print("=== GitHub Trending ===")
github_items = []
queries = [
    ("stars:>100 created:>2026-09-14", "all"),
    ("language:python stars:>50 created:>2026-09-14", "python"),
    ("language:typescript stars:>50 created:>2026-09-14", "typescript"),
    ("language:go stars:>50 created:>2026-09-14", "go"),
    ("language:rust stars:>50 created:>2026-09-14", "rust"),
    ("language:java stars:>50 created:>2026-09-14", "java"),
]
for q, lang in queries:
    try:
        url = f"https://api.github.com/search/repositories?q={urllib.parse.quote(q)}&sort=stars&order=desc&per_page=25"
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, context=ctx, timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            for item in data.get("items", []):
                github_items.append({
                    "name": item.get("full_name"),
                    "language": item.get("language") or lang,
                    "stars": item.get("stargazers_count"),
                    "description": item.get("description"),
                    "url": item.get("html_url"),
                    "created_at": item.get("created_at"),
                    "category": lang
                })
        time.sleep(1)
    except Exception as e:
        print(f"  Error fetching GitHub {lang}: {e}")

with open(f"{DATA_DIR}/github_trending_{DATE}.json", "w") as f:
    json.dump({"repositories": github_items}, f, indent=2, ensure_ascii=False)
print(f"Saved {len(github_items)} GitHub repos")
print("DONE")
