#!/usr/bin/python

import sys
import re
import numpy as np

if len(sys.argv) != 2:
    print("Please pass in a single .tex file")

filename = str(sys.argv[1])

commentRE = re.compile('%.*')
citeRE = re.compile('\\\\cite.?\{([^\}]*)\}')

with open(filename, 'r') as file:
    data = file.readlines()

allCites = []

for line in data:
    comments = commentRE.match(line)
    if (comments is not None):
        text = line[:comments.start()]
        if (len(text) == 0):
            continue
    else:
        if (len(line) == 0):
            continue
        text = line

    for c in citeRE.findall(text):
        allCites.extend([s.strip() for s in c.split(',')])

allCites = np.array(allCites)

uniqueCites = np.unique(allCites)
citeCounts = {}
maxLength = 0
for c in uniqueCites:
    citeCounts[c] = len(allCites[allCites == c])
    maxLength = max(maxLength,len(c))

print("Total Citations: {}".format(len(uniqueCites)))

sortedCites = {k: v for k, v in sorted(citeCounts.items(), key=lambda item: item[1], reverse=True)}
for s in sortedCites.keys():
    print("{s:{maxLength}} : {count:}".format(s=s,maxLength=maxLength,count=sortedCites[s]))
