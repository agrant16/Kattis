# Soylent

T = int(input())
for x in range(T):
    calories = int(input())
    bottles = calories // 400 if calories % 400 is 0 else (calories // 400) + 1
    print(bottles)
