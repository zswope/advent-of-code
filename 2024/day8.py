from itertools import combinations

def add(t1, t2):
    return (t1[0]+t2[0],t1[1]+t2[1])
def sub(t1, t2):
    return (t1[0]-t2[0],t1[1]-t2[1])

def rangeCheck(dims, a):
    return 0 <= a[0] < dims[0] and 0 <= a[1] < dims[1]

star1 = 0
star2 = 0
import os
with open(os.path.basename(__file__).split('.')[0]+'.txt','r') as file:
    data = file.readlines()
    data = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
""".split('\n')
    data = [line.strip() for line in data if line.strip()]

dimensions = (len(data),len(data[0]))
antinodes = set()
antinodes2 = set()
antennae = {e:[] for e in set([el for dat in data for el in dat]) if e != '.'}

# get coords for every antenna and store it in the cooresponding dict key
for antenna in antennae:
    # Iterate through each row
    for i, row in enumerate(data):
        # Iterate through each element in the row
        for j, element in enumerate(row):
            # Check if the element matches the target
            if element == antenna:
                antennae[antenna].append((i, j))

# iterate over every matching pair of antennae and add the (row, col, type) to antinodes
for antennaList in antennae.values():
    for comb in combinations(antennaList, 2):
        a1 = add(comb[0],sub(comb[0],comb[1]))
        a2 = add(comb[1],sub(comb[1],comb[0]))
        if rangeCheck(dimensions, a1):
            antinodes.add(a1)
        if rangeCheck(dimensions, a2):
            antinodes.add(a2)

star1 = len(antinodes)
print('star1: %s'%star1)

for antennaList in antennae.values():
    for comb in combinations(antennaList, 2):
        a1 = comb[0]
        a2 = comb[1]
        d1 = sub(comb[0],comb[1])
        d2 = sub(comb[1],comb[0])
        while rangeCheck(dimensions, a1):
            antinodes2.add(a1)
            a1 = add(a1,d1)
        while rangeCheck(dimensions, a2):
            antinodes2.add(a2)
            a2 = add(a2,d2)

star2 = len(antinodes2)
print('star2: %s'%star2)