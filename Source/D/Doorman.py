# Doorman

maxDiff = int(input())
line = input()
people, w, m, diff = 0, 0, 0, 0
good = True

while good:
    if len(line) is 1:
        if line[0] is 'W':
            w += 1
        else:
            m += 1
        diff =  abs(w - m)
        if diff > maxDiff:
            good = False
            continue
        else:
            people += 1
            good = False
            continue
    if line[0] is 'W':
        w += 1
    else:
        m += 1
    diff = abs(w - m)
    if diff > maxDiff:
        if line[0] is 'W':
            w -= 1
        else:
            m -= 1
        if line[1] is 'W':
            w += 1
        else:
            m += 1
        diff = abs(w - m)
        if diff > maxDiff:
            good = False
        else:
            people += 1
            line = line[0] + line[2:]
    else:
        people += 1
        line = line[1:]
        

print(people)
