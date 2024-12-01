#!/usr/bin/env python3
from collections import defaultdict
file1 = '4.in'
# file1 = '4.test'

input = [x.strip() for x in open(file1, 'r').readlines()]
W = {}
CC = defaultdict(int)
ans1 = 0
for i, v in enumerate(input):
    score = 0
    cn = int(v.split(':')[0].split()[1])
    winning = [int(x) for x in v.split(':')[1].split('|')[0].split()]
    yn = [int(x) for x in v.split(':')[1].split('|')[1].split()]
    W[i] = 0
    for n in yn: 
        if n in winning and score == 0:
            W[i] += 1         
            score = 1
        elif n in winning:
            W[i] += 1
            score *= 2
                

    ans1 += score
    CC[i] += 1
    for v in range(W[i]):
        CC[i + 1 + v] += CC[i]

print(W)

print(CC)
ans2 = sum(CC.values())
print(ans2)
print(ans1)