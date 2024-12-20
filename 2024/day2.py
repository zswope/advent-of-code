from itertools import combinations

star1 = 0
star2 = 0
import os
with open(os.path.basename(__file__).split('.')[0]+'.txt', 'r') as file:
    data = file.readlines()
#     data = """7 6 4 2 1
# 1 2 7 8 9
# 9 7 6 2 1
# 1 3 2 4 5
# 8 6 4 4 1
# 1 3 6 7 9
# """.split('\n')
    data = [line.split('\n')[0] for line in data if line]

# The levels are either all increasing or all decreasing.
# Any two adjacent levels differ by at least one and at most three.
for dat in data:
    levels = dat.split()
    levels = [int(l) for l in levels]

    lt = [j-i < 0 for i, j in zip(levels[:-1], levels[1:])]
    gt = [j-i > 0 for i, j in zip(levels[:-1], levels[1:])]
    if not all(lt) and not all(gt):
        # print('unsafe due to some increase and some decrease')
        continue
    
    diffs = [abs(j-i) < 1 or abs(j-i) > 3 for i, j in zip(levels[:-1], levels[1:])]
    if any(diffs):
        # print('unsafe due to invalid difference')
        continue

    star1 += 1

for dat in data:
    levels = dat.split()
    levels = [int(l) for l in levels]

    possibilities = [levels]
    possibilities += list(combinations(levels, len(levels)-1))

    for p in possibilities:
        lt = [j-i < 0 for i, j in zip(p[:-1], p[1:])]
        gt = [j-i > 0 for i, j in zip(p[:-1], p[1:])]
        if not all(lt) and not all(gt):
            # print('unsafe due to some increase and some decrease')
            continue
        
        diffs = [abs(j-i) < 1 or abs(j-i) > 3 for i, j in zip(p[:-1], p[1:])]
        if any(diffs):
            # print('unsafe due to invalid difference')
            continue

        star2 += 1
        break

print('star1: %s'%star1)
print('star2: %s'%star2)
