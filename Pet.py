max = -1000000
for x in range(5):
    ints = map(int, input().split())
    s = sum(ints)
    if s > max:
        max = s
        row = x + 1

print(str(row) + " " + str(max))
