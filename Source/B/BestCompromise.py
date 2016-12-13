# Best Comporomise
t = int(input())

for x in range(t):
    nm = [int(n) for n in input().split()]
    values = {}
    for m in range(nm[1]):
        values[m] = [0, 0]

    for n in range(nm[0]):
        s = input()
        for m in range(nm[1]):
            if s[m] is '0':
                values[m][0] += 1
            else:
                values[m][1] += 1

    s1 = ''

    for m in range(nm[1]):
        s1 += str(values[m].index(max(values[m])))

    print(s1)
