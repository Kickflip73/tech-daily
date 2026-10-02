#!/usr/bin/env python3
"""Fetch Hacker News, arXiv, and HuggingFace data for 2026-08-25."""
import json, urllib.request, urllib.error, time

# 1. Hacker News
print("Fetching Hacker News...")
try:
    with urllib.request.urlopen("https://hacker-news.firebaseio.com/v0/topstories.json", timeout=30) as resp:
        top_ids = json.loads(resp.read())
    stories = []
    for sid in top_ids[:40]:
        try:
            with urllib.request.urlopen(f"https://hacker-news.firebaseio.com/v0/item/{sid}.json", timeout=10) as resp:
                item = json.loads(resp.read())
            if item:
                stories.append(item)
        except Exception as e:
            print(f"  Story {sid} error: {e}")
        time.sleep(0.05)
    with open("/root/.openclaw/workspace/tech-daily/data/hackernews_2026-08-25.json", "w") as f:
        json.dump({"date": "2026-08-25", "count": len(stories), "stories": stories}, f, indent=2, ensure_ascii=False)
    print(f"  Saved {len(stories)} stories")
except Exception as e:
    print(f"  HN error: {e}")

# 2. arXiv
print("Fetching arXiv...")
try:
    url = "http://export.arxiv.org/api/query?search_query=cat:cs.*&sortBy=submittedDate&sortOrder=descending&max_results=50"
    with urllib.request.urlopen(url, timeout=30) as resp:
        data = resp.read()
    with open("/root/.openclaw/workspace/tech-daily/data/arxiv_2026-08-25.xml", "wb") as f:
        f.write(data)
    print(f"  Saved arXiv XML ({len(data)} bytes)")
except Exception as e:
    print(f"  arXiv error: {e}")

# 3. HuggingFace Papers
print("Fetching HuggingFace Papers...")
try:
    url = "https://huggingface.co/api/papers?date=2026-08-25"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        papers = json.loads(resp.read())
    with open("/root/.openclaw/workspace/tech-daily/data/huggingface_papers_2026-08-25.json", "w") as f:
        json.dump({"date": "2026-08-25", "count": len(papers), "papers": papers}, f, indent=2, ensure_ascii=False)
    print(f"  Saved {len(papers)} papers")
except Exception as e:
    print(f"  HF error: {e}")

print("\nAll done!")
