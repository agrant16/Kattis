# Dice Game

Gunnar = sum(list(map(int, input().split())))
Emma = sum(list(map(int, input().split())))

if Emma > Gunnar:
    print('Emma')
elif Gunnar > Emma:
    print('Gunnar')
else:
    print('Tie')
