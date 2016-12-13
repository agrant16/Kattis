# Seven Wonders

from collections import Counter

cards = Counter([n for n in input()])
total = sum([x * x for x in cards.values()]) + 7 * min(cards.values()
            ) if len(cards) is 3 else sum([x * x for x in cards.values()])

print(total)
