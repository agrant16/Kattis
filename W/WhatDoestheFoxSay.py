# What Does the Fox Say?

sounds = []
num = int(input())

for x in range(0, num):
    recording = input().split()
    animals = input().split()
    while len(animals) <= 3:
        sounds.append(animals[2])
        animals = input().split()
    fox = [x for x in recording if x not in sounds]
    foxString = ""
    for x in range(0, len(fox)):
        if x != (len(fox) - 1):
            foxString = foxString + fox[x] + " "
        else:
            foxString = foxString + fox[x]
    print(foxString)
    

