# Karte

s = input()
dup = False
cards = {'P': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         'H': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         'T': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         'K': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}

for x in range(0, len(s), 3):
    key = s[x]
    i = int(s[x + 1:x + 3]) - 1
    cards[key][i] += 1
    if cards[key][i] > 1:
        print('GRESKA')
        dup = True
        break

if not dup:
    missing = [str(13 - sum(cards[x])) for x in 'PKHT']
    print(' '.join(missing))
