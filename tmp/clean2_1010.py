import re

p = 'reports/2026-10-10.md'
text = open(p, encoding='utf-8').read()
text = re.sub(r"M_SPANID='[^']*' ?", '', text)
open(p, 'w', encoding='utf-8').write(text)
print('spanid remains:', text.count('M_SPANID'))
print('mdEOF remains:', text.count('MDEOF'))
