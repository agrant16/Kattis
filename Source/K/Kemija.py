# Kemija

vowels = 'aeiou'
sentence = input()
for c in vowels:
    sentence = sentence.replace(c + 'p' + c, c)
print(sentence)
