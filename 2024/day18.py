import numpy as np
from collections import deque

def solve_maze_bfs(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
    queue = deque([(start[0], start[1], 0)])  # (row, col, distance)
    visited = set()
    visited.add(start)

    while queue:
        r, c, dist = queue.popleft()

        # If we reached the end, return the distance
        if (r, c) == end:
            return dist

        # Explore all neighbors
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and maze[nr][nc] == 0:
                visited.add((nr, nc))
                queue.append((nr, nc, dist + 1))

    return -1  # Return -1 if no path exists

star1 = 0
star2 = 0
import os
data = open(os.path.basename(__file__).split('.')[0]+'.txt','r').read()
# data = """
# 5,4
# 4,2
# 4,5
# 3,0
# 2,1
# 6,3
# 2,4
# 1,5
# 0,6
# 3,3
# 2,6
# 5,1
# 1,2
# 5,5
# 2,5
# 6,5
# 1,4
# 0,4
# 6,4
# 1,1
# 6,1
# 1,0
# 0,5
# 1,6
# 2,0
# """
data = [line.strip() for line in data.split('\n') if line.strip()]

# extract coords and create grid
bytes = [tuple(reversed(list(map(int,byte.split(','))))) for byte in data]
gridSize = max(map(max,bytes))+1
grid = np.zeros(shape=(gridSize,gridSize))

numBytes = 1024
grid[tuple(zip(*bytes[:numBytes]))] = 1

star1 = solve_maze_bfs(grid,(0,0),(gridSize-1,gridSize-1))

maxGood = 0
minBad = len(bytes)
while True:
    if maxGood+1 == minBad:
        star2 = ','.join(reversed(list(map(str,bytes[maxGood]))))
        break
    
    midpoint = int(np.mean([minBad,maxGood]))
    # fill in N bytes
    grid = np.zeros(shape=(gridSize,gridSize))
    grid[tuple(zip(*bytes[:midpoint]))] = 1
    
    if solve_maze_bfs(grid,(0,0),(gridSize-1,gridSize-1)) > 0:
        maxGood = midpoint
    else:
        minBad = midpoint
    


print('star1:',star1)
print('star2:',star2)
