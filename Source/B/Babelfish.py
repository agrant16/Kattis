# Babelfish

import sys
d = {}

for i in sys.stdin:
    s = i.strip()
    if ' ' in s:
        word, key = s.split()
        d[key] = word
    elif s != '':
        print(d[s] if s in d.keys() else 'eh')
