# Goldbach's Conjecture

import sys
import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i * i <= n:
        if (n % i == 0) or (n % (i + 2) == 0):
            return False
        i = i + 6
    return True


cases = int(input())
for i in range(cases):
    n = int(input())
    sums = [(x, n- x) for x in range((n//2) + 1) if is_prime(x) and is_prime(n - x)]
    print('{0} has {1} representation(s)'.format(n, len(sums)))
    for x,y in sums:
        print('{0}+{1}'.format(x,y))
    print()
