from collections import Counter

s = input()

letters = sorted([x[1] for x in Counter(s).items()])

print(sum(letters) - sum(letters[-2:]) if len(letters) > 2 else 0)
