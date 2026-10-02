#!/usr/bin/env python3
import json
import xml.etree.ElementTree as ET
from datetime import datetime

DATE = '2026-09-13'
DATA_DIR = '/root/.openclaw/workspace/tech-daily/data'

# Check arxiv - if we got rate limited, use most recent
arxiv_papers = []
try:
    with open(f'{DATA_DIR}/arxiv_{DATE}.xml') as f:
        content = f.read()
    if 'Rate exceeded' not in content:
        ns = {'atom': 'http://www.w3.org/2005/Atom', 'arxiv': 'http://arxiv.org/schemas/atom'}
        root = ET.fromstring(content.encode())
        for entry in root.findall('atom:entry', ns):
            paper = {}
            title = entry.find('atom:title', ns)
            paper['title'] = title.text.strip() if title is not None and title.text else ''
            summary = entry.find('atom:summary', ns)
            paper['summary'] = summary.text.strip() if summary is not None and summary.text else ''
            id_elem = entry.find('atom:id', ns)
            paper['id'] = id_elem.text if id_elem is not None else ''
            authors = []
            for author in entry.findall('atom:author', ns):
                name = author.find('atom:name', ns)
                if name is not None and name.text:
                    authors.append(name.text)
            paper['authors'] = authors
            primary_cat = entry.find('arxiv:primary_category', ns)
            paper['primary_category'] = primary_cat.get('term', '') if primary_cat is not None else ''
            link = entry.find("atom:link[@rel='alternate']", ns)
            paper['link'] = link.get('href', '') if link is not None else ''
            arxiv_papers.append(paper)
        print(f'Parsed {len(arxiv_papers)} arXiv papers from {DATE}')
    else:
        print(f'arXiv rate limited for {DATE}')
except Exception as e:
    print(f'Error parsing arXiv {DATE}: {e}')

# If empty, try previous days
if not arxiv_papers:
    for fallback in ['2026-09-12', '2026-09-11', '2026-09-10', '2026-09-09', '2026-09-07', '2026-09-05']:
        try:
            with open(f'{DATA_DIR}/arxiv_{fallback}.xml') as f:
                content = f.read()
            if 'Rate exceeded' not in content:
                ns = {'atom': 'http://www.w3.org/2005/Atom', 'arxiv': 'http://arxiv.org/schemas/atom'}
                root = ET.fromstring(content.encode())
                for entry in root.findall('atom:entry', ns):
                    paper = {}
                    title = entry.find('atom:title', ns)
                    paper['title'] = title.text.strip() if title is not None and title.text else ''
                    summary = entry.find('atom:summary', ns)
                    paper['summary'] = summary.text.strip() if summary is not None and summary.text else ''
                    id_elem = entry.find('atom:id', ns)
                    paper['id'] = id_elem.text if id_elem is not None else ''
                    authors = []
                    for author in entry.findall('atom:author', ns):
                        name = author.find('atom:name', ns)
                        if name is not None and name.text:
                            authors.append(name.text)
                    paper['authors'] = authors
                    primary_cat = entry.find('arxiv:primary_category', ns)
                    paper['primary_category'] = primary_cat.get('term', '') if primary_cat is not None else ''
                    link = entry.find("atom:link[@rel='alternate']", ns)
                    paper['link'] = link.get('href', '') if link is not None else ''
                    arxiv_papers.append(paper)
                print(f'Fallback to arXiv {fallback}: {len(arxiv_papers)} papers')
                break
        except Exception as e:
            continue

# Save parsed arxiv
if arxiv_papers:
    with open(f'{DATA_DIR}/arxiv_{DATE}.json', 'w') as f:
        json.dump(arxiv_papers, f, indent=2, ensure_ascii=False)

# Print summaries of HN
with open(f'{DATA_DIR}/hackernews_{DATE}.json') as f:
    hn = json.load(f)
print(f'\n=== HN Top Stories ({len(hn)}) ===')
for s in hn[:15]:
    score = s.get('score', 0)
    title = s.get('title', 'N/A')
    url = s.get('url', '')
    comments = s.get('descendants', 0)
    print(f'{score:>4}pt | {title[:80]} | {comments}c')

# Print GitHub repos
with open(f'{DATA_DIR}/github_trending_{DATE}.json') as f:
    gh = json.load(f)
repos = gh.get('repositories', [])
print(f'\n=== GitHub Repos ({len(repos)}) ===')
repos_sorted = sorted(repos, key=lambda x: x.get('stars', 0), reverse=True)
for r in repos_sorted[:20]:
    name = r.get('name', '')
    stars = r.get('stars', 0)
    lang = r.get('language', '')
    desc = (r.get('description') or '')[:60]
    print(f'{stars:>6} | {name:<40} | {lang:<12} | {desc}')

# Print HF papers
with open(f'{DATA_DIR}/huggingface_papers_{DATE}.json') as f:
    hf = json.load(f)
print(f'\n=== HF Papers ({len(hf)}) ===')
for p in hf[:15]:
    title = p.get('title', 'N/A')
    up = p.get('upvotes', 0)
    print(f'{up:>4} | {title[:70]}')

# Print arXiv papers
print(f'\n=== arXiv Papers ({len(arxiv_papers)}) ===')
for p in arxiv_papers[:15]:
    title = p.get('title', 'N/A')
    cat = p.get('primary_category', '')
    print(f'[{cat}] {title[:70]}')
