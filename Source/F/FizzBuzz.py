# FizzBuzz

nums = list(map(int, input().split()))
x = nums[0]
y = nums[1]
n = nums[2]

for num in range(1, n + 1):
    if num % x is 0 and num % y is 0:
        print("FizzBuzz")
    elif num % x is 0:
        print("Fizz")
    elif num % y is 0:
        print("Buzz")
    else:
        print(num)
