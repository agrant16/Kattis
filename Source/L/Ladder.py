# Ladder

import math as m
h, v = map(int, input().split())
print(m.ceil(h / m.sin((v * m.pi) / 180)))
