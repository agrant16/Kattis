# Pig Latin

import sys

vowels = 'aeiouy'

def piglatin(word):
    if word[0] in vowels:
        word += 'yay'
    else:
        x = 0
        new = ''
        while word[x] not in vowels:
            new += word[x]
            x += 1
        word = word[x:] + new + 'ay'
    return word

for x in sys.stdin:
    line = x.split()
    for i in range(len(line)):
        line[i] = piglatin(line[i])
    print(' '.join(line))
