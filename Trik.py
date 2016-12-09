moves = input()

cup = 1

for char in moves:
    if char == 'A':
        if cup == 1:
            cup = 2
        elif cup == 2:
            cup = 1
    elif char == 'B':
        if cup == 2:
            cup = 3
        elif cup == 3:
            cup = 2
    else:
        if cup == 1:
            cup = 3
        elif cup == 3:
            cup = 1

print(cup)
