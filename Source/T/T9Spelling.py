# T9 Spelling

keypad = {'a': 2,
          'b': 22,
          'c': 222,
          'd': 3,
          'e': 33,
          'f': 333,
          'g': 4,
          'h': 44,
          'i': 444,
          'j': 5,
          'k': 55,
          'l': 555,
          'm': 6,
          'n': 66,
          'o': 666,
          'p': 7,
          'q': 77,
          'r': 777,
          's': 7777,
          't': 8,
          'u': 88,
          'v': 888,
          'w': 9,
          'x': 99,
          'y': 999,
          'z': 9999,
          ' ': 0
          }

n = int(input())

for x in range(1, n + 1):
    message = input()
    converted_message = ' '
    for c in message:
        if converted_message[len(converted_message) - 1] == str(keypad[c])[0]:
            converted_message += ' '
        converted_message += str(keypad[c])
        converted_message.strip()

    print('Case #' + str(x) + ': ' + converted_message)
