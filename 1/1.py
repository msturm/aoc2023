#!/usr/bin/env python3
file1 = '1.in'
#file1 = '1.test'

input = [x.strip() for x in open(file1, 'r').readlines()]
sum = 0
LN = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
for v in input:
    n1 = -1
    n2 = -1
    v1 = v
    v2 = v
    for a, b in enumerate(v):
        for n, l in enumerate(LN):
            if v1[a:].startswith(l):
                v1= v1.replace(l, str(n+1))    

    for i, x in enumerate(v1):
        if x.isnumeric() and n1 == -1:
            n1 = x


    for i in range(len(v2), 0, -1):
        for n, l in enumerate(LN):
            if v2[i:].startswith(l):
                v2 = v2.replace(l, str(n+1))    

    for i, x in enumerate(v2[::-1]):
    #    print(v2[::-1],x,n2)
        if x.isnumeric() and n2 == -1:
            n2 = x

    print(v)
    print(v1)
    print(v2)
    if n2 == -1:
        n2 = n1
    print(n1, n2)
    sum += int(n1 + n2)
print(sum)
            	
