# Line Them Up

n = int(input())
increasing = False
neither = False
s1 = input()
s2 = input()

if s1 < s2:
    increasing = True

for x in range(n - 2):
    s1 = s2
    s2 = input()

    if s1 > s2 and increasing:
        neither = True      
        break
    elif not increasing and s1 < s2:
        neither = True  
        break


if not neither:
    if increasing:
        print("INCREASING")
    else:
        print("DECREASING")
else:
    print("NEITHER")
