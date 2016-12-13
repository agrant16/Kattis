# The Calculus of Ada


def findDiff(l):
    same = False
    diffs = []
    for x in range(0, len(l) - 1):
        diffs.append(l[x + 1] - l[x])

    if len(set(diffs)) is 1:
        same = True

    return diffs, same

nums = [int(n) for n in input().split()][1:]

diffs = []
done = False

diffs.append(nums)

while not done:
    nums, done = findDiff(nums)
    diffs.append(nums)

next = 0
for x in diffs:
    next += x[len(x) - 1]

print(str(len(diffs) - 1) + ' ' + str(next))
