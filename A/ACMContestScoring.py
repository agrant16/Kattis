# ACM Scoring Contest
line = input()

problems = {}
while line != "-1":
    line = line.split()
    key = line[1]
    minutes = int(line[0])
    if key not in problems.keys():
        problems[key] = []
        problems[key].append(line[2])
        problems[key].append(0)

    if problems[key][0] != 'right':
        problems[key][0] = line[2]

        if problems[key][0] == 'wrong':
            problems[key][1] += 20
        elif problems[key][0] == 'right':
            problems[key][1] += minutes
    elif problems[key][1] == 0:
        problems[key][1] += minutes

    line = input()


count = 0
score = 0
for key in problems.keys():
    if problems[key][0] == 'right':
        count += 1
        score += problems[key][1]

print(str(count) + " " + str(score))
