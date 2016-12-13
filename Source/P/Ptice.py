# Ptice

Adrian = ('ABC' * 33) + 'A'
Bruno = 'BABC' * 25
Goran = ('CCAABB' * 16) + 'CCAA'

correct = { 'Adrian' : 0,
            'Bruno' : 0,
            'Goran' : 0 }

questions = int(input().strip())
answers = input().strip()

for x in range(questions):
    if answers[x] is Adrian[x]:
        correct['Adrian'] += 1
    if answers[x] is Bruno[x]:
        correct['Bruno'] += 1
    if answers[x] is Goran[x]:
        correct['Goran'] += 1

m = max(correct.values())

print(m)

for key in sorted(correct.keys()):
    if correct[key] is m:
        print(key)
