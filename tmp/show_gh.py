import json

D = "/root/.openclaw/workspace/tech-daily/data"

# GitHub repos sorted by daily delta
repos = json.load(open(f"{D}/github_repos_2026-10-28.json"))
known_bad = ["AnyUnlock", "IOBIT", "Canva-Pro", "Photoshop", "AutoCAD", "Office-Tool", "WINZIP", "CCleaner", "Avast", "KMSPico", "Windows-10", "Repack", "Pre-Activat", "preactivat", "Crack", "crack", "Keygen", "keygen", "Activator", "Patch", "Sony-Vegas", "Filmora", "Navicat", "IDM-"]
def is_bad(r):
    fn = r.get("full_name", "").lower()
    desc = (r.get("description") or "").lower()
    for b in known_bad:
        if b.lower() in fn or b.lower() in desc:
            return True
    return False

good = [r for r in repos if not is_bad(r)]
# compute delta
for r in good:
    if r.get("prev_stars") is not None:
        r["delta"] = r["stargazers_count"] - r["prev_stars"]
    else:
        r["delta"] = None

withdelta = sorted([r for r in good if r["delta"]], key=lambda x: -x["delta"])
print("=== GH TOP by daily delta ===")
for r in withdelta[:60]:
    print(f"+{r['delta']:>5} | {r['stargazers_count']:>6} | {r['full_name']:<50} | {(r.get('description') or '')[:80]}")
print()
print("=== GH TOP by total stars (no delta info) ===")
nodelta = sorted([r for r in good if not r["delta"]], key=lambda x: -(x.get("stargazers_count") or 0))
for r in nodelta[:25]:
    print(f"{r['stargazers_count']:>6} | {r['full_name']:<50} | {(r.get('description') or '')[:80]}")
