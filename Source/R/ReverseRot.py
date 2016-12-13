# Reverse Rot

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'

while True:
    items = input().strip()
    if ' ' in items:
        shift, string = items.split()
        shift = int(shift)
        string = string[::-1]
        newString = ''
        for x in range(len(string)):
            newString += alpha[(alpha.index(string[x]) + shift) % 28]
        print(newString)
    else:
        break
    
