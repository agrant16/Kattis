# Quality-Adjusted Life-Year

from functools import reduce 

N = int(input())

qaly = 0
for i in range(N):
    q, y = map(float, input().split())
    qaly += q*y
print('{:.3f}'.format(qaly))