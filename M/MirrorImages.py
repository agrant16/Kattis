# Mirror Images

cases = int(input())
grid = []

for x in range(1, cases + 1):
    nums = [int(n) for n in input().split()]
    for row in range(nums[0]):
        grid.append(input())

    print('Test ' + str(x))
    for i in range(len(grid) - 1, -1, -1):
        print(grid[i][::-1])

    grid.clear()
