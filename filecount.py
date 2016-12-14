"""
Program: filecount.py
Description: This script walks through Source/ obtaining counts of all 
             the solutions held within as well as their location and the 
             associated problem title (listed on the first line of each 
             program) for each solution.

             After gathering all required data it then creates and formats 
             the README.md file for this repository. 
"""

import os
import os.path

# Dictionary to hold language counts.
langs = {'cc': ['C++', 0],
         'py': ['Python 3', 0],
         'java': ['Java', 0]}

paths = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ' # string of paths within Source/
problems = {} # dictionary to store file paths and the problem titles
total = 0 # the number of files. 

for letter in paths:
    problems['Source/' + letter] = []

# Walk through each of the directories included in paths.
for d, subd, files in os.walk('Source'):
    for i in files: # iterate through the files in Source/d
        langs[i[i.index('.') + 1:]][1] += 1  # update each lang's count
        # Open each file, get the title of the problem, and store the
        # file path and the title in problems
        f = open(d + '/' + i, 'r')
        problems[d].append((d + '/' + i, f.readline().strip()[2:]))
        f.close()

f = open('README.md', 'w')  # Open README.md for writing.

# Print various information including link to open.kattis.com and the number
# of solutions in my repository.
f.write('# Kattis\n\n')
f.write('This repository contains my solutions to problems found on '
        '[open.kattis.com](http://open.kattis.com). My profile can be found '
        '[here](http://open.kattis.com/users/alan-grant-1058).\n\n')
f.write('There are currently ' + str(sum([len(item) 
        for item in problems.values()]))  + ' problem solutions contained '
        'here. The problems are listed below in Alphabetical order. Each '
        'listing of a problem is also a link to the source code for my '
        'solution of that problem. For Java solutions Kattis requires that '
        'the class and file name be "Main". I have changed any Java '
        'solutions so that the class and file names are the associated '
        'problem title.\n\n')

# Print chart displaying languages used and the number of solutions using
# that language
f.write('| Language | Solutions Using |\n|---|---|\n')
for key, item in langs.items():
    f.write('| ' + item[0] + ' | ' + str(item[1]) + ' |\n')
f.write('\n')

# Print a table of contents with links to the proper sections.
f.write('Click the appropriate character to jump to the section containing '
        'problems whose titles begin with that character. To return to the '
        'top click the link titled "-Top-" at the bottom of the section.'
        '\n\n')

for x in paths:
    f.write('[**' + x + '**]' + '(#' + x.lower() + ')\t')
f.write('\n\n')

# Print the solutions in alphabetical order with each letter/number having
# its own section. Each listing of a problem is also a link to that problem's
# solution.
for char in paths:
    d = 'Source/' + char
    problems[d] = sorted(problems[d], key=lambda s: s[1].lower())
    f.write('# ' + char + '\n\n')
    for (fp, name) in problems[d]:
        f.write('[' + name + '](' + fp + ')\n\n')
    f.write('\n')
    f.write('[-Top-](#kattis)\n\n')

f.close()  # Close README.md
