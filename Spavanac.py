nums = list(map(int, input().split()))

hours = nums[0]
minutes = nums[1]

if minutes < 45:
    minutes += 15
    if hours is 0:
        hours = 23
    else:
        hours -= 1
else:
    minutes = minutes - 45


print(str(hours) + " " + str(minutes))