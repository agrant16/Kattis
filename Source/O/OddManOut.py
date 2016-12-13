# Odd Man Out

from collections import Counter

cases = int(input())

for x in range(1, cases + 1):
    guests = int(input())
    codes = Counter([n for n in input().split()])
    alone = [key for key, value in codes.items() if value is 1][0]
    print('Case #' + str(x) + ': ' + alone)
