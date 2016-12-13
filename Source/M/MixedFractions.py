# Mixed Fractions

nums = list(map(int, input().split()))

while nums[0] is not 0:
    mixedfraction = []
    mixedfraction.append(nums[0] // nums[1])
    mixedfraction.append(nums[0] % nums[1])

    print(str(mixedfraction[0]) + " " + str(mixedfraction[1]) + 
            " / " + str(nums[1]))
    nums = list(map(int, input().split()))
