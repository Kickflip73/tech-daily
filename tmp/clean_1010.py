import re

p = 'reports/2026-10-10.md'
lines = open(p, encoding='utf-8').read().split('\n')
cleaned = [re.sub(r"^M_SPANID='[^']*' ", '', l) for l in lines]
cleaned = [l for l in cleaned if l.strip() != 'MDEOF' and not l.startswith('wc -c ')]
open(p, 'w', encoding='utf-8').write('\n'.join(cleaned))
print('lines:', len(cleaned))
print('spanid remains:', sum('M_SPANID' in l for l in cleaned))
