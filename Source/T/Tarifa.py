# Tarifa.py

x = int(input())
N = int(input())
t = x
for i in range(N):
    t += x - int(input())
print(t)