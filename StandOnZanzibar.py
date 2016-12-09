T = int(input())

while T > 0:
    T -= 1
    nums = [int(n) for n in input().split() if int(n) is not 0]
    imports = 0
    for x in range(0, len(nums) - 1):
        if nums[x + 1] > (2 * nums[x]):
            imports += nums[x + 1] - (2 * nums[x])

    print(imports)
