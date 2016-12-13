# Stacking Cups

def is_int(x):
    try:
        i = int(x)
    except:
        return False
    return True

num = int(input())
stuff = []

for x in range(num):
    line = input().split()
    if is_int(line[0]):
        stuff.append((int(line[0]), line[1]))
    else:
        stuff.append((2 * int(line[1]), line[0]))

stuff = sorted(stuff)

for pair in stuff:
    print(pair[1])

        
