cypher = input()

chunks = [cypher[0 + i:3 + i] for i in range(0, len(cypher), 3)]

days = 0

for x in chunks:
    if x is not 'PER':
        if x[0] is not 'P':
            days += 1
        if x[1] is not 'E':
            days += 1
        if x[2] is not 'R':
            days += 1

print(days)
