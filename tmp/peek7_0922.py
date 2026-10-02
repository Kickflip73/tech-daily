import json
D = "2026-09-22"
ax = json.load(open(f"/root/.openclaw/workspace/tech-daily/data/arxiv_{D}.json"))
kw_groups = {
    "AI/LLM/Agent": ["agent", "llm", "language model", "reasoning", "rl", "reinforcement", "distillation", "moe", "mixture"],
    "Security": ["security", "attack", "vulnerab", "privacy", "adversar"],
    "Robotics": ["robot", "manipulation", "locomotion", "quadruped", "embodied"],
    "CV/Generation": ["video", "image", "diffusion", "generation", "3d", "visual"],
    "Systems": ["database", "distributed", "system", "compiler", "network"],
    "Bio/Health": ["medical", "clinical", "biolog", "genome", "health", "cell"],
}
for gname, kws in kw_groups.items():
    print(f"=== {gname} ===")
    n = 0
    for p in ax:
        t = p.get("title", "").lower()
        s = p.get("summary", "").lower()
        if any(k in t or k in s for k in kws):
            n += 1
            if n <= 6:
                print(f'  [{p.get("id","").split("/")[-1]}] {p.get("title","")[:105]}')
                print(f'      {(p.get("summary","")[:230])}')
    print(f"  ({n} matched)")
    print()
