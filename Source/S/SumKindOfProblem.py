# Sum Kind of Problem


def oddSum(n):
    return n * n


def evenSum(n):
    return n * n + n


def firstN(n):
    return (n * (n + 1)) // 2

cases = int(input())

for x in range(cases):
    nums = [int(n) for n in input().split()]
    s = str(nums[0]) + " " + str(firstN(nums[1])) + " " + str(oddSum(nums[1]))
    s += " " + str(evenSum(nums[1]))
    print(s)
