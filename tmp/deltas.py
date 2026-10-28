import json

D = "/root/.openclaw/workspace/tech-daily/data"
repos = json.load(open(f"{D}/github_repos_2026-10-28.json"))
prev = json.load(open(f"{D}/github_repos_2026-10-27.json"))
prevmap = {r["full_name"]: r["stargazers_count"] for r in prev}

# Show trending repos from trending ecosystem that I want deltas for
names = ["Zagitta/gpu-unlock","JustAResearcher/gpu-unlock-ada","impacifist/Windows-GPU-UNLOCK","KohakuBlueleaf/KohakUnlock",
"pengchujin/aerial-tv","rddmwmddr/android-ad-cleaner","simbasjungles/free-my-tv","udhaykumarbala/cleanyourtv-app",
"lesnolie/Tigris","lasharor/cleanyourtv-WebOS","jss8649/quiet-tizen","wangrongding/tv-fresh","humblemuzzu/dumbtv",
"man15h/tellyscope","piermark/omarchytv","mihirgupta0900/tv-home","mirkobrombin/raven",
"designfuchen/word-atlas","xiaoyang111222/cn-math-taxonomy","DenisSergeevitch/ex-ussr-kinship-research","huaxialucaicaizi/ai-startup-skills",
"t3dotgg/tstack","morganlinton/BeautifulRust","Jakeschincariol/day-trader-skill","lyramakesmusic/neuron-explorer",
"indexable-inc/blaze","stencil-hq/dquickts","mizorewww/gdirect","enesozturk/dimensional-drawing","JoasASantos/REA-Prompts",
"oosexgang/hackios-xnu-kernel","EthanArbuckle/fairplay-decrypt","DrWhax/unfairplay","misshexa66/OunceCake","UniXNU/UniXNU","Snapintosh/Snapintosh",
"zengshuangzi/mcd-money-saver","alchaincyf/huashu-motion","andyhuo520/digital-human-koubo","Tencent-Hunyuan/Hy-Nomas",
"eagle-hq/EAGLE-4","colinhacks/reylo","wevm/ondine","MemTensor/MemT-1.0","JMS1717/ming-voice","inclusionAI/Ming-3.0-tts",
"ikow/php2shell-poc","assetnote/php2shell-scanner","NCSC-NL/php2shell","KillaBoi/StealMyBitcoin-PoC",
"LNPANDY/NX2Apple","kuraeow/ultratears","opentrap/opentrap","songjianyang/xss-audit","ZiChuanLan/pi-purge","ZiChuanLan/agent-purge",
"xevrion/hatchzip","wesbos/3d-model-anything","aicodeking/pandacode","armanlife/firefox-vpn-client","egoist/mygo-cloudmusic",
"stackedlol/ascii-sharks","interplains/zero-breach","quantum9/na","daveebbelaar/bama","NyxFoundation/nyxis","mxhm11cr/LinuxRunner"]

seen = set()
for n in names:
    r = [x for x in repos if x["full_name"] == n]
    if r:
        r = r[0]
        pv = r.get("prev_stars")
        seen.add(n)
        print(f"{n:<48} total={r['stargazers_count']:>6} prev={pv} delta={(r['stargazers_count']-pv) if pv is not None else 'NEW'}")
    elif n in prevmap:
        print(f"{n:<48} NOT in today's 300 (prev total={prevmap[n]})")
    else:
        print(f"{n:<48} not in either snapshot")
