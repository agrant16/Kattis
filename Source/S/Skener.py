# Skener

nums = [int(n) for n in input().split()]
lines = []
for x in range(nums[0]):
    lines.append(input())

lines = [''.join([nums[3] * char for char in line]) for line in lines for x in range(nums[2])]

for line in lines:
    print(line)
