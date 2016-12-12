# I've Been Everywhere Man

cases = int(input())

for x in range(0, cases):
    cities = int(input())
    visited = list()
    for y in range(0, cities):
        currentCity = input()
        if currentCity not in visited:
            visited.append(currentCity)

    print(len(visited))
