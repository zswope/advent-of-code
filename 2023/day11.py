import numpy as np
from itertools import combinations

star1 = 0
star2 = 0

with open('day11.txt','r') as file:
    data = file.read().split('\n')
#     tmpdata = """...#......
# .......#..
# #.........
# ..........
# ......#...
# .#........
# .........#
# ..........
# .......#..
# #...#....."""
#     if tmpdata:
#         data = tmpdata.split('\n')
    data = [line for line in data if line]
    data = np.array([list(l) for l in data])

# universe expansion
expansionFactor = 1000000
# expansionFactor = 2
rows = []
cols = []
for row in range(len(data)):
    if '#' in data[row]:
        continue
    rows.append(row)
for col in range(len(data[0])):
    if '#' in data[:,col]:
        continue
    cols.append(col)

rows = np.array(rows)
cols = np.array(cols)
print(rows)
print(cols)

# find galaxies
galaxyCoords = list(zip(*np.where(data == '#')))
expandedCoords = []
# update coords according to expansion
print('expanding...')
for coord in galaxyCoords:
    expandedCoords.append((coord[0]+len(np.where(rows < coord[0])[0])*(expansionFactor-1), coord[1]+len(np.where(cols < coord[1])[0])*(expansionFactor-1)))
print('galaxyCoords:')
print(galaxyCoords)
print('expandedCoords:')
print(expandedCoords)
# create all pairs
print('getting pairs...')
galaxyPairs = combinations(expandedCoords, 2)
print('calculating distance...')
for (galaxy1,galaxy2) in galaxyPairs:
    star1 += abs(galaxy1[0]-galaxy2[0])+abs(galaxy1[1]-galaxy2[1])

print('star1: %s'%star1)
print('star2: %s'%star2)