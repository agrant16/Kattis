# Support Vector Machine

import math as m
import sys

length = int(input())
wb = [float(n) for n in input().split()]
w = wb[:len(wb) - 1]
b = wb[len(wb) - 1]

def transpose(w):
    return [[x] for x in w]

def matrixMult(x, w):
    return sum([(a * b[0]) for a,b, in zip(x, w)])

def magnitude(w):
    return m.sqrt(sum([x * x for x in w]))

def dx(x):
    return (matrixMult(x, transpose(w)) + b) / magnitude(w) 

for i in sys.stdin:
    x = [float(n) for n in i.split()]
    print(dx(x))
