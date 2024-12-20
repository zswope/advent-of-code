from copy import deepcopy
from itertools import groupby

def checksum(blocks):
    star = 0
    for i,b in enumerate(blocks):
        if b != -1:
            star += (i*b)
    return star

def part1(blocks):
    return checksum(blocks)

def part2(blocks):
    return checksum(blocks)

star1 = 0
star2 = 0
import os
with open(os.path.basename(__file__).split('.')[0]+'.txt', 'r') as file:
    data = file.readlines()
#     data = """2333133121414131402
# """.split('\n')
    data = [line.split('\n')[0] for line in data if line]
    data = list(map(int, data[0]))

ID = 0
isFile = True
blocks = []
# construct pre-compression blocks
for n in data:
    if isFile:
        blocks += [ID] * n
        ID += 1
    else:
        blocks += [-1] * n
    isFile = not isFile

# copy blocks
blocks1 = deepcopy(blocks)
blocks2 = deepcopy(blocks)

# fragmented compress
while True:
    # find first empty block
    try:
        emptyIdx = blocks1.index(-1)
    except: # no more empty blocks, compression done
        break

    # move last element
    blocks1[emptyIdx] = blocks1[-1]
    del blocks1[-1]
    
    # remove trailing empty space
    while blocks1[-1] == -1:
        del blocks1[-1]

# calculate checksum
star1 = checksum(blocks1)
print('star1: %s'%star1)

# whole file compress
for id in range(ID-1,0,-1):
    # get size of last file
    fileSize = blocks2.count(id)
    fileIndex = blocks2.index(id)

    # find first gap >= fileSize
    emptys = []
    i = 0
    emptyIdx = None
    for key, group in groupby(blocks2):
        elems = len(list(group))
        if key == -1 and elems > 0:
            emptys.append((elems, i))
        i += elems
    for empty in emptys:
        if empty[0] >= fileSize:
            emptyIdx = empty[1]
            break

    # move file to gap
    if emptyIdx is not None and emptyIdx < fileIndex:
        blocks2[emptyIdx:emptyIdx+fileSize] = blocks2[fileIndex:fileIndex+fileSize]
        blocks2[fileIndex:fileIndex+fileSize] = [-1] * fileSize

star2 = checksum(blocks2)
print('star2: %s'%star2)
