# Grass Seed

cost = float(input())
lawns = int(input())


def area(x, y):
    return x * y

totalCost = 0

for lawn in range(lawns):
    nums = [float(n) for n in input().split()]
    totalCost += cost * area(nums[0], nums[1])

print('{0:.8f}'.format(totalCost))
