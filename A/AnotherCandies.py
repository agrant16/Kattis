# Another Candies

testcases = int(input())

for x in range(0, testcases):
    input()
    candies = 0
    children = int(input())

    for x in range(0, children):
        candy = int(input())
        candies += candy

    remainder = candies % children

    if remainder == 0:
        print("YES")
    else:
        print("NO")
