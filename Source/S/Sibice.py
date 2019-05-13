# Sibice

import math

N, w, h = map(int, input().split())
hyp = math.sqrt(w*w + h*h)
for x in range(N):
    if int(input()) > hyp:
        print('NE')
    else:
        print('DA')
