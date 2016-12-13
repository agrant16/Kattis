# Bela

values = {'A': (11, 11),
          'K': (4, 4),
          'Q': (3, 3),
          'J': (20, 2),
          'T': (10, 10),
          '9': (14, 0),
          '8': (0, 0),
          '7': (0, 0)}

given = input().split()
hands = int(given[0])
dom = given[1]
score = 0

for x in range(4 * hands):
    card = input()
    score += values[card[0]][0] if card[1] is dom else values[card[0]][1]

print(score)
