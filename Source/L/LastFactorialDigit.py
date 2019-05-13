# Last Factorial Digit

def factorial(n):
    t = 1
    for x in range(n+1):
        if x == 0:
            t = t*1
        else:
            t = t*x
    return t

N = int(input())

for i in range(N):
    print(str(factorial(int(input())))[-1])