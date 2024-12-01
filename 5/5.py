#!/usr/bin/env python3
from collections import defaultdict
# file1 = '5.in'
file1 = '5.test'

M = defaultdict(dict)
id = 0
input = [x.strip() for x in open(file1, 'r').readlines()]
for v in input:
    if v.startswith('seeds'):
        seeds = [int(x) for x in v.split(':')[1].split()]
        
    elif v.endswith('map:'):
        id += 1
    else:
        if len(v) > 0 and v[0].isdigit():
            v1, v2, v3 = [int(x) for x in v.split()]
            # print(v1, v2, v3)
            M[id][(v2, v2+v3 - 1)] = (v1, v1+v3 - 1)
            # print(id, M)
            # M[id]

minloc = int(1e9)

LOC = {}

for s in seeds:
    cv = s
    for map_id in range(1, max(M)+1):
        for b, e in M[map_id]:
            if b <= cv <= e: 
                cv = cv - b + M[map_id][(b, e)][0] 
                break
        # print(s, cv)
    # print(s, cv)
    LOC[cv] = s

ans1 = min(LOC)
print(ans1)

### Part2
seeds_map = []
for x in range(0, len(seeds)-1, 2):
    seeds_map.append((seeds[x], seeds[x]+seeds[x+1]-1))

print(seeds_map)
print(M)
for map_id in range(1, max(M)+1):
# for map_id in range(1, 2):
        print(map_id)
        for b, e in M[map_id]:
            new_seed_map = []
            for (s1, s2) in seeds_map:
                new_st = s1
                new_ed = s2
                if s1 <= b <= s2 and s1 <= e <= s2: # map contained in range, split in 3
                    new_seed_map.append((s1, b-1))
                    new_seed_map.append((M[map_id][(b, e)]))
                    new_seed_map.append((e+1, s2))
                elif s1 <= b <= s2: # begin of map in range, split in 2
                    new_seed_map.append((s1, b-1))
                    new_seed_map.append((M[map_id][(b, e)][0], s2 - b + M[map_id][(b, e)][0]))
                elif s1 <= e <= s2: # end of map in range, split in 2
                    new_seed_map.apend((s1 - b + M[map_id][(b, e)][0], M[map_id][(b, e)][1]))
                    new_seed_map.append((e+1, s2))
                elif b <= s1 and s2 <= e: # range contained in map, transform range
                    new_seed_map.append((s1 - b + M[map_id][(b, e)][0], s2 - b + M[map_id][(b, e)][0]))
                else:
                    new_seed_map.append((s1, s2))   
            #    print(s1, s2, new_st, new_ed)
            seeds_map = new_seed_map
        print(seeds_map)    


locations = []
for x, y in seeds_map:

    locations.append(x)
    locations.append(y)

ans2 = min(locations)

print(ans2)

    
# print(seeds)