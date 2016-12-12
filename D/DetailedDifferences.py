N = int(input())

for x in range(N):
    str1 = input()
    str2 = input()
    diffs = ['.' if x is y else '*' for x,y in zip(str1, str2)]
    print(str1)
    print(str2)
    print(''.join(diffs))

