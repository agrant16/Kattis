# Cetvrta

xcoords = []
ycoords = []

for x in range(3):
    nums = [int(n) for n in input().split()]
    xcoords.append(nums[0])
    ycoords.append(nums[1])

xcoords = sorted(xcoords)
ycoords = sorted(ycoords)

x = xcoords[2] if xcoords[0] == xcoords[1] else xcoords[0]
y = ycoords[2] if ycoords[0] == ycoords[1] else ycoords[0]

print(str(x) + ' ' + str(y))
