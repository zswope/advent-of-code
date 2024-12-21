import numpy as np
from collections import deque, defaultdict

def manhattan(l,r):
    rowDiff = abs(l[0] - r[0])
    colDiff = abs(l[1] - r[1])
    return rowDiff + colDiff

def shortcuts(maze, start, end, cheatDist):
    timeSave = defaultdict(int)
    
    rows, cols = len(maze), len(maze[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
    queue = deque([(start[0], start[1], [start])])  # (row, col, distance)
    visited = set()
    visited.add(start)

    while queue:
        r, c, path = queue.popleft()
        for prevCell in path[:(0-cheatDist)-1]:
            dist = manhattan((r,c),prevCell)
            if 2 <= dist <= cheatDist:
                timeSaved = ((len(path))-(path.index(prevCell)+1))-dist
                timeSave[timeSaved] += 1

        # If we reached the end, return the distance
        if (r, c) == end:
            return timeSave

        # Explore all neighbors
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and maze[nr][nc] == 0:                    
                visited.add((nr, nc))
                queue.append((nr, nc, path + [(nr,nc)]))

star1 = 0
star2 = 0
import os
data = open(os.path.basename(__file__).split('.')[0]+'.txt','r').read()
# data = """
# ###############
# #...#...#.....#
# #.#.#.#.#.###.#
# #S#...#.#.#...#
# #######.#.#.###
# #######.#.#...#
# #######.#.###.#
# ###..E#...#...#
# ###.#######.###
# #...###...#...#
# #.#####.#.###.#
# #.#...#.#.#...#
# #.#.#.#.#.#.###
# #...#...#...###
# ###############
# """
data = np.array([list(line.strip()) for line in data.split('\n') if line.strip()])

# extract data
grid = np.zeros(shape=(len(data),len(data[0])))
grid[np.where(data == '#')] = 1
start = list(zip(*np.where(data == 'S')))[0]
end = list(zip(*np.where(data == 'E')))[0]

timeSave = shortcuts(grid, start, end, 2)
# get number of cheats that save 100+ ps
for k,v in timeSave.items():
    if k >= 100:
        star1 += v
print('star1:',star1)

timeSave2 = shortcuts(grid, start, end, 20)
# get number of cheats that save 100+ ps
for k,v in timeSave2.items():
    if k >= 100:
        star2 += v
print('star2:',star2)
