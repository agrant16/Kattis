# Apaxiaaaaaaaaaaaans!

name = input()
newName = name[0]
namelist = list(name)
y = 0
for x in namelist:
    if x is not newName[y]:
        newName += x
        y += 1


print(newName)
