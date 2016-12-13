# Eligibility

cases = int(input())

for x in range(0, cases):
    line = input().split()
    hours = int(line[3])
    name = line[0]
    startDate = list(map(int, line[1].split("/")))
    birthDate = list(map(int, line[2].split("/")))

    if startDate[0] > 2009:
        print(name + " eligible")
    elif birthDate[0] > 1990:
        print(name + " eligible")
    elif hours < 41:
        print(name + " coach petitions")
    else:
        print(name + " ineligible")
