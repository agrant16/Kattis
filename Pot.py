n = int(input())
strings = []
for x in range(n):
    strings.append(input())

total = sum([int(x[:len(x) - 1]) ** int(x[len(x) - 1:]) for x in strings])

print(total)
