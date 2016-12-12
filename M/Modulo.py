nums = []

for x in range(10):
    nums.append(int(input()))

print(len(set([x % 42 for x in nums])))
