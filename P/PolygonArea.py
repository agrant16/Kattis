# Polygon Area

def cworccw(list):
	value = 0
	for x in range(len(list) - 1):
	    value += ((list[x + 1][0] - list[x][0]) * 
            (list[x][1] + list[x + 1][1]))

	return value + (list[0][0] - list[-1][0]) * (list[0][1] + list[-1][1])
	
 
points = int(input())

while points != 0:
	shape = []

	for x in range(points):
		(x, y) = map(int, input().split())
		shape.append((x,y))

	value = cworccw(shape)

	s = 'CCW ' if value < 0 else 'CW '

	s += '{0:.1f}'.format(abs(value) / 2.0)
	print(s)
	
	points = int(input())
