#!/usr/bin/env python3
file1 = '2.in'

maxred = 12
maxgreen = 13
maxblue = 14

invalid = []
allgames = []

input = [x.strip() for x in open(file1, 'r').readlines()]
totalpower = 0
for v in input:
    minred = 0
    minblue = 0
    mingreen = 0
    gn = int(v.split(':')[0].split()[1])
    allgames.append(gn)
    subsets = v.split(':')[1].split(';')
    for ss in subsets:
        ps = ss.split(',')
        for p in ps:
            n = int(p.split()[0])
            c = p.split()[1].strip() 
            if c == 'red':
                minred = max(minred, n)
            if c == 'red' and n > maxred:
                invalid.append(gn)
            if c == 'green':
                mingreen = max(mingreen, n)
            if c == 'green' and n > maxgreen:
                invalid.append(gn)
            if c == 'blue':
                minblue = max(minblue, n)
            if c == 'blue' and n > maxblue:
                invalid.append(gn)
    power = minblue * minred * mingreen
    totalpower += power
result = 0
for gn in allgames:
    if not gn in invalid:
         result += gn  
print(result)
print(totalpower)
