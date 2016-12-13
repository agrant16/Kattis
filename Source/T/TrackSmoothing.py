# Track Smoothing

import math as m

cases = int(input())

for case in range(cases):
    r, ps = map(int, input().split())
    circ = 2 * r * m.pi
    xs = []
    ys = []
    tracklength = 0

    for p in range(ps):
        x, y = map(int, input().split())
        xs.append(x)
        ys.append(y)

    for i in range(ps - 1):
        dx = xs[i + 1] - xs[i]
        dy = ys[i + 1] - ys[i]
        tracklength += m.sqrt(dx * dx + dy * dy)

    dx = xs[0] - xs[-1]
    dy = ys[0] - ys[-1]
    tracklength += m.sqrt(dx * dx + dy * dy)

    if tracklength < circ:
        print('Not possible')
    elif tracklength is circ:
        print(0)
    else:
        print(round((tracklength - circ) / tracklength, 8))
