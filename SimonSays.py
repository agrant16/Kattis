num = int(input())

for x in range(0, num):
    sentence = input()
    if sentence[0:10] == 'Simon says':
        print(sentence[11:])
