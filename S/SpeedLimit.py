num = int(input())

while num != -1:
    miles = 0
    items = {}
    for x in range(0, num):
        nums = list(map(int, input().split()))
        items[x] = (nums[0], nums[1])

    for x in range(num - 1, -1, -1):
        if x == 0:
            miles += items[x][0] * items[x][1]
        else:
            miles += (items[x][1] - items[x-1][1]) * items[x][0]

    print(str(miles) + ' miles')
    num = int(input())