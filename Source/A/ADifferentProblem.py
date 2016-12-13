# A Different Problem

import sys

for x in sys.stdin:
    x, y = map(int, x.split())
    print(abs(x - y))
