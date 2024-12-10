def safeInt(x):
    if x == '.':
        return -1
    else:
        return (int(x))

def findSummits(data, start):
    for key in range(1,10):
        if key == 1:
            starts = [start]
        else:
            starts = nextStep
        nextStep = set()
        for start in starts:
            if start[0] > 0:
                if data[start[0]-1][start[1]] == key:
                    nextStep.add((start[0]-1,start[1]))
            if start[0]+1 < len(data):
                if data[start[0]+1][start[1]] == key:
                    nextStep.add((start[0]+1,start[1]))
            if start[1] > 0:
                if data[start[0]][start[1]-1] == key:
                    nextStep.add((start[0],start[1]-1))
            if start[1]+1 < len(data[0]):
                if data[start[0]][start[1]+1] == key:
                    nextStep.add((start[0],start[1]+1))
    summits = nextStep
    return summits
    
def findConnected(data, starts, key):
    hits = []
    for start in starts:
        if start[0] > 0:
            if data[start[0]-1][start[1]] == key:
                hits.append((start[0]-1,start[1]))
        if start[0]+1 < len(data):
            if data[start[0]+1][start[1]] == key:
                hits.append((start[0]+1,start[1]))
        if start[1] > 0:
            if data[start[0]][start[1]-1] == key:
                hits.append((start[0],start[1]-1))
        if start[1]+1 < len(data[0]):
            if data[start[0]][start[1]+1] == key:
                hits.append((start[0],start[1]+1))
    return hits


star1 = 0
star2 = 0
import os
data = open(os.path.basename(__file__).split('.')[0]+'.txt','r').readlines()
# data = """89010123
# 78121874
# 87430965
# 96549874
# 45678903
# 32019012
# 01329801
# 10456732
# """.split('\n')
data = [list(map(safeInt, line.strip())) for line in data if line.strip()]

# Find all instances of an element and save the coordinates
zeros = []
# Iterate through each row
for i, row in enumerate(data):
    # Iterate through each element in the row
    for j, element in enumerate(row):
        # Check if the element matches the target
        if element == 0:
            zeros.append((i, j))

# Find all summits connected to each trailhead
for zero in zeros:
    summits = findSummits(data,zero)
    star1 += len(summits)

# Find all ones connected to a trailhead
ones = findConnected(data,zeros,1)
twos = findConnected(data,ones,2)
threes = findConnected(data,twos,3)
fours = findConnected(data,threes,4)
fives = findConnected(data,fours,5)
sixes = findConnected(data,fives,6)
sevens = findConnected(data,sixes,7)
eights = findConnected(data,sevens,8)
nines = findConnected(data,eights,9)

star2 = len(nines)

print('star1: %s'%star1)
print('star2: %s'%star2)