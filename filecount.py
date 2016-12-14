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
import time

# Dictionary to hold language counts.
langs = {'.cc': ['C++', 0],
         '.py': ['Python 3', 0],
         '.java': ['Java', 0]}

paths = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ' # string of paths within Source/
# dictionary to store file paths and the problem titles
problems = {'Source/' + c: [] for c in paths}
toc = ['[**' + c + '**]' + '(#' + c.lower() + ')\t' for c in paths] + ['\n\n']

# Walk through each of the directories included in paths.
for d, subd, files in os.walk('Source'):
    for name in files: # iterate through the files in Source/d
        langs[os.path.splitext(name)[1]][1] += 1  # update each lang's count
        # Open each file, get the title of the problem, and store the
        # file path and the title in problems
        f = open(d + '/' + name, 'r')
        problems[d].append((d + '/' + name, f.readline().strip()[2:]))
        f.close()

f = open('README.md', 'w')  # Open README.md for writing.

# Print header, name, date/time of last update, and various information about 
# the repository
f.write('# Kattis Problem Solutions\n**Alan Grant**\n**Updated:** ' 
        + time.strftime('%A %B %d, %Y') + ' at ' + time.strftime('%I:%M:%S %p')
        + '\n\nThis repository contains my solutions to problems found on '
        '[open.kattis.com](http://open.kattis.com). My profile can be found '
        '[here](http://open.kattis.com/users/alan-grant-1058).\n\nThe problems'
        ' are listed below in Alphabetical order. Each listing of a problem is'
        ' also a link to the source code for my solution of that problem. For '
        'Java solutions Kattis requires that the class and file name be '
        '"Main". I have changed any Java solutions so that the class and file '
        'names are the associated problem title.\n\n')

# Print chart displaying languages used and the number of solutions using
# that language
f.writelines(s for lst in [['|Language|Number of Solutions|\n|---| ---:|\n'],
             ['|' + v[0] + '|' + str(v[1]) + '|\n' for v in langs.values()],
             ['|All|' + str(sum(v[1] for v in langs.values())) + '|\n\n']] 
             for s in lst)

# Print a table of contents with links to the proper sections.
f.write('Click the appropriate character to jump to the section containing '
        'problems whose titles begin with that character. To return to the '
        'top click the link titled "-Top-" at the bottom of the section.\n\n')

f.writelines(s for s in toc)

# Print the solutions in alphabetical order with each letter/number having
# its own section. Each listing of a problem is also a link to that problem's
# solution.
for char in paths:
    d = 'Source/' + char
    # sort each array of problem titles ignoring case
    problems[d] = sorted(problems[d], key=lambda s: s[1].lower())
    f.write('### ' + char + '\n\n') # Section header
    for (fp, name) in problems[d]:
        f.write('[' + name + '](' + fp + ')\n\n') # link to solution source
    f.write('\n')
    f.write('[-Top-](#kattis-problem-solutions)\n\n') # link to top of readme

f.close()  # Close README.md
