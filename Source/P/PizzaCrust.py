# Pizza Crust

import math

nums = [int(n) for n in input().strip().split()]
cheese = '{0:.6f}'.format(((math.pi * ((nums[0] - nums[1]) ** 2)) / (math.pi * (nums[0] ** 2))) * 100)
print(cheese)
