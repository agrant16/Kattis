# Dice Cup

values = {}
nums = [int(n) for n in input().split()]

for x in range(1, nums[0] + 1):
    for y in range(1, nums[1] + 1):
        value = x + y
        if value in values.keys():
            values[value] += 1
        else:
            values[value] = 1

highest = max(values.values())

for key, item in values.items():
    if item is highest:
        print(key)
