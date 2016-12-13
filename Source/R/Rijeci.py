# Rijeci

presses = int(input())
A = 0
B = 1

while presses > 1:
    temp = A
    A = B
    B += temp
    presses -= 1

print(str(A) + ' ' + str(B))
