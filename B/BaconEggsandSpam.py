food = {}


num = int(input())

while num > 0:

    people = num

    while people > 0:

        line = input().split()

        name = line[0]

        for x in range(1, len(line)):

            yummy = line[x]

            if yummy not in food.keys():
                food[line[x]] = []
                food[line[x]].append(line[0])
            else:
                food[yummy].append(name)

        people -= 1

    keys = sorted(food.keys())
    for key in keys:
        names = sorted(food[key])
        printout = key + ' '
        for name in names:
            printout += name + ' '

        printout = printout.strip()
        print(printout)

    food.clear()
    
    num = int(input())