#!/usr/bin/env python3
"""Complete tech-daily pipeline for 2026-09-18."""
import json
import xml.etree.ElementTree as ET
from datetime import datetime
import urllib.request
import urllib.error
import ssl
import time
import os
import subprocess

DATE = "2026-09-18"
WEEKDAY = "周五"
DATA_DIR = "/root/.openclaw/workspace/tech-daily/data"
REPORTS_DIR = "/root/.openclaw/workspace/tech-daily/reports"
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(REPORTS_DIR, exist_ok=True)

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

# ============================================================
# STEP 1: FETCH DATA
# ============================================================
print("=" * 60)
print("STEP 1: Fetching data sources...")
print("=" * 60)

# 1. Hacker News Top Stories
print("\n=== Fetching Hacker News ===")
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
    print("Failed to fetch HN topstories")

# 2. arXiv Papers
print("\n=== Fetching arXiv ===")
arxiv_xml = fetch_text(
    "http://export.arxiv.org/api/query?search_query=cat:cs.*&sortBy=submittedDate&sortOrder=descending&max_results=50",
    timeout=60
)
arxiv_papers = []
if arxiv_xml:
    with open(f"{DATA_DIR}/arxiv_{DATE}.xml", "w") as f:
        f.write(arxiv_xml)
    ns = {
        "atom": "http://www.w3.org/2005/Atom",
        "arxiv": "http://arxiv.org/schemas/atom"
    }
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
            arxiv_papers.append(paper)
        with open(f"{DATA_DIR}/arxiv_{DATE}.json", "w") as f:
            json.dump(arxiv_papers, f, indent=2, ensure_ascii=False)
        print(f"Fetched {len(arxiv_papers)} arXiv papers")
    except Exception as e:
        print(f"Error parsing arXiv XML: {e}")
else:
    print("Failed to fetch arXiv")

# 3. HuggingFace Papers
print("\n=== Fetching HuggingFace Papers ===")
hf_data = fetch_json("https://huggingface.co/api/papers", timeout=30)
hf_papers = []
if hf_data and isinstance(hf_data, list):
    with open(f"{DATA_DIR}/huggingface_papers_{DATE}.json", "w") as f:
        json.dump(hf_data, f, indent=2, ensure_ascii=False)
    hf_papers = hf_data
    print(f"Fetched HF papers: {len(hf_data)}")
else:
    print(f"Failed to fetch HF papers (type={type(hf_data).__name__})")

# 4. GitHub Trending via API
print("\n=== Fetching GitHub Trending (via search API) ===")
import urllib.parse

github_items = []
queries = [
    ("stars:>100 created:>2026-09-04", "all"),
    ("language:python stars:>50 created:>2026-09-04", "python"),
    ("language:typescript stars:>50 created:>2026-09-04", "typescript"),
    ("language:go stars:>50 created:>2026-09-04", "go"),
    ("language:rust stars:>50 created:>2026-09-04", "rust"),
    ("language:java stars:>50 created:>2026-09-04", "java"),
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
                    "stars_today": None,
                    "description": item.get("description"),
                    "url": item.get("html_url"),
                    "created_at": item.get("created_at"),
                    "updated_at": item.get("updated_at"),
                    "category": lang
                })
        time.sleep(1)
    except Exception as e:
        print(f"  Error fetching GitHub {lang}: {e}")

with open(f"{DATA_DIR}/github_trending_{DATE}.json", "w") as f:
    json.dump({"repositories": github_items}, f, indent=2, ensure_ascii=False)
print(f"Saved {len(github_items)} GitHub repos")

# ============================================================
# STEP 2: GENERATE REPORT
# ============================================================
print("\n" + "=" * 60)
print("STEP 2: Generating report...")
print("=" * 60)

# Load data
with open(f"{DATA_DIR}/github_trending_{DATE}.json") as f:
    gh = json.load(f)
with open(f"{DATA_DIR}/hackernews_{DATE}.json") as f:
    hn = json.load(f)
with open(f"{DATA_DIR}/arxiv_{DATE}.json") as f:
    arxiv = json.load(f)
with open(f"{DATA_DIR}/huggingface_papers_{DATE}.json") as f:
    hf = json.load(f)

# Deduplicate and sort GitHub repos
seen = set()
repos = []
for r in gh['repositories']:
    if r['name'] and r['name'] not in seen:
        seen.add(r['name'])
        repos.append(r)
repos.sort(key=lambda r: r.get('stars', 0), reverse=True)

# Sort HN stories
stories = sorted(hn, key=lambda s: s.get('score', 0), reverse=True)

# Sort HF papers
hf_papers = sorted(hf, key=lambda p: p.get('upvotes', 0), reverse=True) if isinstance(hf, list) else []

# ============================================================
# BUILD REPORT
# ============================================================
parts = []

# Header
parts.append(f"""# 🔥 每日技术热点报告 — {DATE}（{WEEKDAY}）

---
""")

# Section 1: GitHub Trending - Deep dive top repos
top_repos = repos[:12]
parts.append("## 一、🏆 GitHub Trending 重点项目深度解读\n")

# Generate deep dives for top repos
counter = 1
for repo in top_repos:
    name = repo.get('name', 'Unknown')
    url = repo.get('url', f"https://github.com/{name}")
    lang = repo.get('language', 'Unknown')
    stars = repo.get('stars', 0)
    desc = repo.get('description') or '暂无描述'

    parts.append(f"""### {counter}. {name}（{stars:,} ⭐）

> **仓库**：{url}
> **语言**：{lang}

**简介：** {desc}

""")
    counter += 1

# More repos table
other_repos = repos[12:28]
if other_repos:
    parts.append("### 其他值得一看的项目\n\n| 项目 | ⭐总计 | 链接 | 一句话 |\n|------|--------|------|--------|\n")
    for repo in other_repos:
        name = repo.get('name', '')
        url = repo.get('url', '')
        stars = repo.get('stars', 0)
        desc = (repo.get('description') or '暂无描述')[:50]
        parts.append(f"| {name} | {stars:,} | [GitHub]({url}) | {desc} |\n")
    parts.append("\n")

# Section 2: Hacker News
parts.append("""---

## 二、📰 Hacker News 热门技术新闻\n
""")

for i, story in enumerate(stories[:15]):
    title = story.get('title', 'No title')
    score = story.get('score', 0)
    url = story.get('url', '')
    hn_url = f"https://news.ycombinator.com/item?id={story.get('id', '')}"
    descendants = story.get('descendants', 0)

    # Determine priority based on score
    if score >= 400:
        icon = "🔴"
    elif score >= 150:
        icon = "🟡"
    else:
        icon = "🟢"

    parts.append(f"""### {icon} {title}（{score} 分，{descendants} 评论）
> **原文**：{url or hn_url}
> **HN 讨论**：{hn_url}

""")

# More HN
if len(stories) > 15:
    parts.append("### 🟢 其他值得关注\n\n| 热度 | 标题 | 链接 |\n|------|------|------|\n")
    for story in stories[15:25]:
        title = story.get('title', '')[:60]
        score = story.get('score', 0)
        url = story.get('url', '') or f"https://news.ycombinator.com/item?id={story.get('id', '')}"
        parts.append(f"| {score}pt | {title} | [{url[:40]}...]({url}) |\n")
    parts.append("\n")

# Section 3: arXiv
parts.append("""---

## 三、📄 arXiv 精选论文\n
""")

# Categorize papers
categories = {
    'AI / 大模型': [],
    '🤖 机器人 / 具身智能': [],
    '🧠 机器学习 / 深度学习': [],
    '🔒 软件工程 / 工具': [],
    '🔐 安全 / 隐私': [],
    '📡 系统 / 网络': [],
    '🖼️ 计算机视觉': [],
    '其他': []
}

for paper in arxiv_papers:
    cats = paper.get('categories', [])
    title = paper.get('title', '')
    summary = paper.get('summary', '')
    pid = paper.get('id', '').split('/')[-1] if paper.get('id') else ''
    if 'arxiv.org/abs/' in (paper.get('id') or ''):
        pid = paper.get('id', '').split('arxiv.org/abs/')[-1]
    link = paper.get('link', f"https://arxiv.org/abs/{pid}")
    authors = ', '.join(paper.get('authors', [])[:3])
    if len(paper.get('authors', [])) > 3:
        authors += ' 等'

    # Classify
    cat_matched = False
    cat_text = ' '.join(cats).lower()
    if any(k in cat_text for k in ['cs.ai', 'cs.cl', 'cs.lg', 'cs.ne', 'cs.cy', 'cs.hc']):
        if any(k in cat_text for k in ['robot', 'manipul', 'grasp', 'navigation', 'mobile']):
            categories['🤖 机器人 / 具身智能'].append((title, authors, summary, link))
        elif any(k in cat_text for k in ['vision', 'cv', 'image', 'video', 'multimodal']):
            categories['🖼️ 计算机视觉'].append((title, authors, summary, link))
        elif any(k in cat_text for k in ['secur', 'privac', 'crypt']):
            categories['🔐 安全 / 隐私'].append((title, authors, summary, link))
        else:
            categories['AI / 大模型'].append((title, authors, summary, link))
        cat_matched = True
    elif any(k in cat_text for k in ['cs.se', 'cs.pl', 'cs.sd']):
        categories['🔒 软件工程 / 工具'].append((title, authors, summary, link))
        cat_matched = True
    elif any(k in cat_text for k in ['cs.ni', 'cs.os', 'cs.dc', 'cs.ar']):
        categories['📡 系统 / 网络'].append((title, authors, summary, link))
        cat_matched = True

    if not cat_matched:
        categories['其他'].append((title, authors, summary, link))

for cat_name, papers in categories.items():
    if not papers:
        continue
    parts.append(f"### {cat_name}\n\n")
    for title, authors, summary, link in papers[:4]:
        # Extract first sentence for brevity
        first_sentence = summary.split('.')[0] if summary else '暂无摘要'
        if len(first_sentence) > 200:
            first_sentence = first_sentence[:200] + '...'
        parts.append(f"**{title}**\n")
        parts.append(f"> 作者：{authors}\n")
        parts.append(f"> 链接：{link}\n\n")
        parts.append(f"{first_sentence}\n\n")
    parts.append("---\n\n")

# Section 4: HuggingFace
parts.append("## 四、🤗 HuggingFace 热门论文\n\n")
parts.append("| 论文 | 作者 | 👍 | 一句话 |\n|------|------|----|--------|\n")
for paper in hf_papers[:15]:
    title = paper.get('title', '')[:50]
    authors = paper.get('authors', '')[:30] if paper.get('authors') else '未知'
    upvotes = paper.get('upvotes', 0)
    # Try to get a one-liner
    summary = paper.get('summary', '') or paper.get('abstract', '')
    oneliner = (summary[:80] + '...') if summary else '暂无摘要'
    parts.append(f"| {title} | {authors} | {upvotes} | {oneliner} |\n")
parts.append("\n")

# Section 5: Stats
parts.append("""---

## 五、📊 今日热点统计\n
""")

parts.append(f"""| 指标 | 数值 |
|------|------|
| 📦 GitHub Trending 项目总数 | {len(repos)} 个 |
| 🔥 最热仓库 | {repos[0]['name'] if repos else 'N/A'}（{repos[0]['stars'] if repos else 0:,} ⭐）|
| 💬 最热闹 HN 讨论 | {stories[0]['title'] if stories else 'N/A'}（{stories[0]['score'] if stories else 0} 分）|
| 📄 arXiv 论文总数 | {len(arxiv_papers)} 篇 |
| 🤗 HuggingFace 论文 | {len(hf_papers)} 篇 |

""")

# Section 6: Trend Analysis
parts.append("""---

## 六、🔍 趋势洞察与深度分析\n
""")

# Analyze top languages
from collections import Counter
lang_counter = Counter([r.get('language', 'Unknown') for r in repos if r.get('language')])
top_langs = lang_counter.most_common(5)

# Analyze HN topics
hn_titles = ' '.join([s.get('title', '').lower() for s in stories[:20]])

parts.append(f"""### 趋势 1：语言生态热度

今日 GitHub Trending 语言分布 Top 5：
""")
for lang, count in top_langs:
    parts.append(f"- **{lang}**：{count} 个项目\n")

parts.append(f"""
### 趋势 2：Hacker News 热点主题

Top 20 HN 故事标题高频关键词分析显示，今日讨论集中在：
""")

# Simple keyword extraction
keywords = []
for story in stories[:20]:
    title = story.get('title', '').lower()
    for kw in ['ai', 'agent', 'llm', 'openai', 'google', 'microsoft', 'apple', 'rust', 'python', 'security', 'privacy', 'blockchain', 'crypto', 'database', 'kubernetes', 'docker']:
        if kw in title:
            keywords.append(kw)
kw_counter = Counter(keywords)
if kw_counter:
    for kw, count in kw_counter.most_common(8):
        parts.append(f"- **{kw}**：{count} 次提及\n")
else:
    parts.append("- 今日话题较为分散，无单一集中主题\n")

parts.append("""
### 趋势 3：学术前沿动态

arXiv 今日论文分布反映了当前 AI 研究的核心方向：
""")
for cat_name, papers in categories.items():
    if papers:
        parts.append(f"- **{cat_name}**：{len(papers)} 篇\n")

parts.append(f"""
---

## 七、📋 今日 Action Items

| 优先级 | 行动 | 原因 |
|--------|------|------|
| 🔴 高 | 浏览今日 GitHub 最热项目 | {repos[0]['name'] if repos else 'N/A'} 获得最高关注 |
| 🔴 高 | 阅读 HN 最高分讨论 | 获取技术社区最前沿的洞察 |
| 🟡 中 | 浏览 arXiv 新论文 | 了解学术研究最新进展 |
| 🟡 中 | 关注 HuggingFace 热门论文 | AI 应用层创新风向标 |
| 🟢 低 | 跟踪编程语言生态变化 | Rust/Go/Python/TypeScript 持续演进 |

---

> 📝 *由 J.A.R.V.I.S. 自动生成 | 数据来源：GitHub Trending、Hacker News、arXiv、HuggingFace Papers*
> 📅 *{DATE} | 本期关注：AI Agent 生态、编程语言演进、安全与隐私*
""")

# Write report
report = '\n'.join(parts)
report_path = f"{REPORTS_DIR}/{DATE}.md"
with open(report_path, 'w') as f:
    f.write(report)

print(f"\n✅ Report generated: {report_path}")
print(f"   Length: {len(report)} chars")
print(f"   Repos: {len(repos)}")
print(f"   HN stories: {len(stories)}")
print(f"   arXiv papers: {len(arxiv_papers)}")
print(f"   HF papers: {len(hf_papers)}")

# ============================================================
# STEP 3: GIT COMMIT & PUSH
# ============================================================
print("\n" + "=" * 60)
print("STEP 3: Git commit and push...")
print("=" * 60)

os.chdir("/root/.openclaw/workspace/tech-daily")

subprocess.run(["git", "add", f"data/github_trending_{DATE}.json"], check=False)
subprocess.run(["git", "add", f"data/hackernews_{DATE}.json"], check=False)
subprocess.run(["git", "add", f"data/arxiv_{DATE}.json"], check=False)
subprocess.run(["git", "add", f"data/arxiv_{DATE}.xml"], check=False)
subprocess.run(["git", "add", f"data/huggingface_papers_{DATE}.json"], check=False)
subprocess.run(["git", "add", f"reports/{DATE}.md"], check=False)

result = subprocess.run(
    ["git", "commit", "-m", f"📰 tech-daily report {DATE}"],
    capture_output=True, text=True
)
print(result.stdout)
if result.returncode != 0:
    print(f"Git commit output (may be nothing to commit): {result.stderr}")

push_result = subprocess.run(["git", "push", "origin", "main"], capture_output=True, text=True)
print(push_result.stdout)
if push_result.returncode != 0:
    print(f"Git push error: {push_result.stderr}")
else:
    print("✅ Git push successful")

print("\n" + "=" * 60)
print("PIPELINE COMPLETE")
print("=" * 60)
