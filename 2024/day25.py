import numpy as np

star1 = 0
star2 = 0
import os
data = open(os.path.basename(__file__).split('.')[0]+'.txt','r').read()
# data = """
# #####
# .####
# .####
# .####
# .#.#.
# .#...
# .....

# #####
# ##.##
# .#.##
# ...##
# ...#.
# ...#.
# .....

# .....
# #....
# #....
# #...#
# #.#.#
# #.###
# #####

# .....
# .....
# #.#..
# ###..
# ###.#
# ###.#
# #####

# .....
# .....
# .....
# #....
# #.#..
# #.#.#
# #####
# """
data = [line.strip() for line in data.split('\n\n') if line.strip()]
data = [np.array([list(line.strip()) for line in dat.split('\n') if line.strip()]) for dat in data]

# split out locks and keys
locks = []
keys = []
for dat in data:
    if (dat[0] == '#').all(): # lock
        locks.append([np.count_nonzero(dat[:,i] == '#')-1 for i in range(len(dat[0]))])
    if (dat[-1] == '#').all(): # key
        keys.append([np.count_nonzero(dat[:,i] == '#')-1 for i in range(len(dat[0]))])

for lock in locks:
    for key in keys:
        for l,k in zip(lock,key):
            if l+k > 5:
                break
        else:
            star1 += 1

print('star1:',star1)
print('star2:',star2)
