# Alphabet Spam

line = input().strip()
counts = [0.0 for x in range(4)]

for char in line:
    if ord(char) >= 97 and ord(char) <= 122:
        counts[1] += 1
    elif ord(char) >= 65 and ord(char) <= 90:
        counts[2] += 1
    elif char is '_':
        counts[0] += 1
    else:
        counts[3] += 1

ratios = ['{0:.15f}'.format(x / len(line)) for x in counts]

for ratio in ratios:
    print(ratio)
