#!/usr/bin/env python3
"""Fetch data for 2026-10-21 tech-daily report: GitHub trending (search API), HN top, HF papers."""
import json, ssl, urllib.request, time, os, sys

DATE = "2026-10-21"
DATA_DIR = "/root/.openclaw/workspace/tech-daily/data"
os.makedirs(DATA_DIR, exist_ok=True)

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def fj(url, timeout=25):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "tech-daily-bot/1.0"})
        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as r:
            return json.loads(r.read().decode())
    except Exception as e:
        print("ERR", url, e)
        return None

def ft(url, timeout=30):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "tech-daily-bot/1.0"})
        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as r:
            return r.read().decode()
    except Exception as e:
        print("ERR", url, e)
        return None

# 1. GitHub: recent repos sorted by stars
print("=== GitHub search (created:>2026-10-11) ===")
d = fj("https://api.github.com/search/repositories?q=created:%3E2026-10-11&sort=stars&order=desc&per_page=40")
gh = []
if d:
    for it in d.get("items", []):
        gh.append({
            "full_name": it["full_name"], "stars": it["stargazers_count"],
            "lang": it.get("language"), "desc": it.get("description"),
            "url": it["html_url"], "created": it["created_at"],
            "topics": it.get("topics", []),
        })
    print(f"{len(gh)} repos")
    for r in gh[:40]:
        print(f'{r["full_name"]} | +{r["stars"]} | {r["lang"]} | {(r["desc"] or "")[:100]}')
json.dump(gh, open(f"{DATA_DIR}/github_{DATE}.json", "w"), indent=1, ensure_ascii=False)

# 2. Hacker News top stories
print("\n=== Hacker News ===")
ids = fj("https://hacker-news.firebaseio.com/v0/topstories.json")
hn = []
if ids:
    for sid in ids[:40]:
        s = fj(f"https://hacker-news.firebaseio.com/v0/item/{sid}.json")
        if s:
            hn.append({"id": s.get("id"), "title": s.get("title"), "score": s.get("score"),
                       "descendants": s.get("descendants", 0), "url": s.get("url"),
                       "by": s.get("by")})
        time.sleep(0.04)
    hn.sort(key=lambda x: -(x["score"] or 0))
    print(f"{len(hn)} stories")
    for s in hn:
        print(f'{s["score"]}pt {s["descendants"]}c | {s["title"][:90]} | {s.get("url")}')
json.dump(hn, open(f"{DATA_DIR}/hackernews_{DATE}.json", "w"), indent=1, ensure_ascii=False)

# 3. HuggingFace daily papers
print("\n=== HuggingFace Papers ===")
hfp = fj("https://huggingface.co/api/daily_papers")
if hfp:
    out = []
    for p in hfp[:30]:
        out.append({"title": p.get("title"), "paperId": p.get("paperId"),
                    "upvotes": p.get("paper", {}).get("upvotes") or p.get("upvotes"),
                    "url": f'https://huggingface.co/papers/{p.get("paperId")}'})
    out.sort(key=lambda x: -(x["upvotes"] or 0))
    for p in out:
        print(f'{p["upvotes"]} | {p["title"][:95]} | {p["paperId"]}')
    json.dump(out, open(f"{DATA_DIR}/hf_papers_{DATE}.json", "w"), indent=1, ensure_ascii=False)

print("\nDONE")
