import math as m
s = input()
prod = len(s)
limit = int(m.sqrt(len(s)))

r = max([num for num in range(1, limit + 1) if prod % num is 0])

c = prod // r

chars = list(map(list, zip(*[[s[r * x + y] for y in range(r)] for x in range(c)])))
print(''.join([''.join(x) for x in chars]))

