import math
line = list(map(float, input().split()))

while(line[0] != 0 and line[1] != 0 and line[2] != 0):
    actual = math.pi * (line[0] ** 2)
    estimate = ((2 * line[0]) ** 2) * (line[2] / line[1])
    print(str(actual) + " " + str(estimate))
    line = list(map(float, input().split()))