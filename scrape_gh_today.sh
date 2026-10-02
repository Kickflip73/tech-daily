#!/bin/bash
# Scrape GitHub Trending pages
PAGES="https://github.com/trending https://github.com/trending/python https://github.com/trending/typescript https://github.com/trending/go https://github.com/trending/rust https://github.com/trending/java"
OUTDIR="/root/.openclaw/workspace/tech-daily/data"
DATE="2026-08-27"

for page in $PAGES; do
  name=$(echo "$page" | sed 's|https://github.com/trending||;s|^/||')
  [ -z "$name" ] && name="all"
  echo "Fetching $name..."
  agent-browser open "$page" && agent-browser wait --load networkidle
  agent-browser eval --stdin < /tmp/gh_extract.js > "$OUTDIR/gh_trending_${name}_${DATE}.json" 2>&1
  echo "Done $name"
done
agent-browser close
echo "All done"
