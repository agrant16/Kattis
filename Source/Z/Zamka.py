# Zamka

L = int(input())
D = int(input())
X = int(input())
sums = [num for num in range(L, D + 1) if sum(int(digit)
                                              for digit in str(num)) is X]
print(min(sums))
print(max(sums))
