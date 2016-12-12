nums = list(map(int, input().split()))

if (nums[0] + nums[1]) == nums[2]:
    nums = list(map(str, nums))
    print(nums[0] + "+" + nums[1] + "=" + nums[2])
elif (nums[0] // nums[1]) == nums[2]:
    nums = list(map(str, nums))
    print(nums[0] + "/" + nums[1] + "=" + nums[2])
elif (nums[0] - nums[1]) == nums[2]:
    nums = list(map(str, nums))
    print(nums[0] + "-" + nums[1] + "+" + nums[2])
elif (nums[0] * nums[1]) == nums[2]:
    nums = list(map(str, nums))
    print(nums[0] + "*" + nums[1] + "=" + nums[2])
elif nums[0] == (nums[1] + nums[2]):
    nums = list(map(str, nums))
    print(nums[0] + "=" + nums[1] + "+" + nums[2])
elif nums[0] == (nums[1] * nums[2]):
    nums = list(map(str, nums))
    print(nums[0] + "=" + nums[1] + "*" + nums[2])
elif nums[0] == (nums[1] // nums[2]):
    nums = list(map(str, nums))
    print(nums[0] + "=" + nums[1] + "/" + nums[2])
elif nums[0] == (nums[1] - nums[2]):
    nums = list(map(str, nums))
    print(nums[0] + "=" + nums[1] + "-" + nums[2])
