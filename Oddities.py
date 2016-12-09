cases = int(input())
for x in range(0, cases):
	num = int(input())
	print(str(num) + " is even" if num % 2 == 0 else str(num) + " is odd")
