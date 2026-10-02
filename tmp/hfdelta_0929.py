#!/usr/bin/env python3
import json
d = "/mnt/openclaw/.openclaw/workspace/tech-daily/data/"
prev = json.load(open(d + "hfpapers_2026-09-28.json"))
cur = json.load(open(d + "hfpapers_2026-09-29.json"))
def norm(lst):
    out = {}
    for p in lst:
        pp = p.get("paper", p)
        t = (pp.get("title") or "").strip()
        out[t] = pp.get("upvotes", p.get("upvotes", 0))
    return out
P, C = norm(prev), norm(cur)
print(f"prev {len(P)} papers, cur {len(C)} papers, overlap {len(set(P)&set(C))}")
print()
print("=== carryover with delta ===")
for t in C:
    if t in P and C[t] != P[t]:
        print(f"{P[t]:>4} -> {C[t]:>4} (+{C[t]-P[t]:>3})  {t[:90]}")
print()
print("=== NEW today (top by upvotes) ===")
for t, u in sorted(((t, u) for t, u in C.items() if t not in P), key=lambda x: -x[1])[:12]:
    print(f"{u:>4}  {t[:100]}")
