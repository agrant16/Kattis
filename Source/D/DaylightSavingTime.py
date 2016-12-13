# Daylight Saving Time

cases = int(input())

for x in range(cases):
    direction, minChange, hours, minutes = input().strip().split()
    
    minChange = int(minChange)
    hourChange = minChange // 60
    hours = int(hours)
    minutes = int(minutes)

    if direction == 'F':
        if (minutes + (minChange % 60)) >= 60:
            hours = (hours + hourChange + 1) % 24
        else:
            hours = (hours + hourChange) % 24
        minutes = (minutes + minChange) % 60

    if direction == 'B':
        if (minutes - (minChange % 60)) < 0:
            hours = (hours - hourChange - 1) % 24
        else:
            hours = (hours - hourChange) % 24
        minutes = (minutes - minChange) % 60
        
    print(' '.join(map(str, [hours, minutes])))

