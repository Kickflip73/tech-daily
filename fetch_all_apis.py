#!/usr/bin/env python3
"""Fetch all API data for tech-daily report."""
import urllib.request
import urllib.error
import json
import xml.etree.ElementTree as ET
from datetime import datetime
import time
import os

DATE = "2026-09-12"
DATA_DIR = "/root/.openclaw/workspace/tech-daily/data"
os.makedirs(DATA_DIR, exist_ok=True)

def fetch_json(url, timeout=30):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "tech-daily-bot/1.0"})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode())
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def fetch_text(url, timeout=30):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "tech-daily-bot/1.0"})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.read().decode()
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

# 1. Hacker News Top Stories
print("=== Fetching Hacker News ===")
hn_ids = fetch_json("https://hacker-news.firebaseio.com/v0/topstories.json")
hn_stories = []
if hn_ids:
    for story_id in hn_ids[:35]:
        story = fetch_json(f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json")
        if story:
            hn_stories.append(story)
        time.sleep(0.05)
    print(f"Fetched {len(hn_stories)} HN stories")
    with open(f"{DATA_DIR}/hackernews_{DATE}.json", "w") as f:
        json.dump(hn_stories, f, indent=2, ensure_ascii=False)
else:
    print("Failed to fetch HN topstories")

# 2. arXiv Papers
print("\n=== Fetching arXiv ===")
arxiv_xml = fetch_text(
    "http://export.arxiv.org/api/query?search_query=cat:cs.*&sortBy=submittedDate&sortOrder=descending&max_results=50",
    timeout=60
)
if arxiv_xml:
    with open(f"{DATA_DIR}/arxiv_{DATE}.xml", "w") as f:
        f.write(arxiv_xml)
    # Parse to JSON
    ns = {
        "atom": "http://www.w3.org/2005/Atom",
        "arxiv": "http://arxiv.org/schemas/atom"
    }
    try:
        root = ET.fromstring(arxiv_xml.encode())
        papers = []
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
            primary_cat = entry.find("arxiv:primary_category", ns)
            paper["primary_category"] = primary_cat.get("term", "") if primary_cat is not None else ""
            categories = []
            for cat in entry.findall("atom:category", ns):
                term = cat.get("term", "")
                if term:
                    categories.append(term)
            paper["categories"] = categories
            link = entry.find("atom:link[@rel='alternate']", ns)
            paper["link"] = link.get("href", "") if link is not None else ""
            papers.append(paper)
        with open(f"{DATA_DIR}/arxiv_{DATE}.json", "w") as f:
            json.dump(papers, f, indent=2, ensure_ascii=False)
        print(f"Fetched {len(papers)} arXiv papers")
    except Exception as e:
        print(f"Error parsing arXiv XML: {e}")
else:
    print("Failed to fetch arXiv")

# 3. HuggingFace Papers
print("\n=== Fetching HuggingFace Papers ===")
hf_data = fetch_json("https://huggingface.co/api/papers", timeout=30)
if hf_data:
    with open(f"{DATA_DIR}/huggingface_papers_{DATE}.json", "w") as f:
        json.dump(hf_data, f, indent=2, ensure_ascii=False)
    print(f"Fetched HF papers: {len(hf_data) if isinstance(hf_data, list) else 'non-list'}")
else:
    print("Failed to fetch HF papers")

print("\n=== All API fetches complete ===")
