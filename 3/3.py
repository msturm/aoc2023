#!/usr/bin/env python3
file1 = '3.in'
# file1 = '3.test'

input = [x.strip() for x in open(file1, 'r').readlines()]

G = {}
S = []
NUM = {}
for r, v in enumerate(input):
    for c in range(0, len(v)):
        G[(r, c)] = v[c]

for r in range(0, len(input)):
    for c in range(0, len(v)):
        if G[(r, c)] != '.' and not str(G[(r, c)]).isdigit():
            S.append((r, c))

sum = 0
for r in range(0, len(input)):
    N = []
    curnum = ''
    for c in range(0, len(v)):
        if G[(r, c)].isdigit():
            if curnum == '':
                N.append((r-1, c-1))
                N.append((r, c-1))
                N.append((r+1, c-1))
            N.append((r-1, c))
            N.append((r+1, c))
            curnum += G[(r, c)]
            if c == len(v) -1:
                for x in range(c-len(curnum), c):
                    NUM[(r, x)] = int(curnum)
                for n in N:
                    if n in S:
                        sum += int(curnum)
                        curnum = ''
                        N = []
        else:
            if curnum != '': # end of number
                N.append((r-1, c))
                N.append((r, c))
                N.append((r+1, c))
                for x in range(c-len(curnum), c):
                    NUM[(r, x)] = int(curnum)
                for n in N:
                    if n in S:
                        # print(curnum)
                        sum += int(curnum)
                        curnum = ''
                        N = []
                curnum = ''
                N = []

prod = 0
for r, c in S:
    if G[(r, c)] == '*':
        n1 = -1
        n2 = -1
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if (r+dr, c+dc) in NUM:
                    if n1 == -1:
                        n1 = NUM[(r+dr, c+dc)]
                    elif n1 != NUM[(r+dr, c+dc)]:
                        prod += n1 * NUM[(r+dr, c+dc)]
                        n1 = -1

print(sum)
print(prod)
        