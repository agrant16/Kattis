# The Easiest Problem is This One


def digitSum(n):
    return sum([int(x) for x in n])


def findSameDigitSum(sum1, x):
    s = 11
    while digitSum(str(s * x)) != sum1:
        s += 1
    return s

num = input()

while num != '0':
    print(findSameDigitSum(digitSum(num), int(num)))
    num = input()
