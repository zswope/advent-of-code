import heapq
from copy import deepcopy
from collections import defaultdict

# ANSI color codes
RESET = "\033[0m"
RED = "\033[91m"

def findPaths(maze):
    rows = len(maze)
    cols = len(maze[0])

    # Find start (S) and end (E) positions
    start, end = None, None
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == 'S':
                start = (r, c)
            elif maze[r][c] == 'E':
                end = (r, c)

    if not start or not end:
        raise ValueError("Maze must contain both a start ('S') and an end ('E') point")

    # Priority queue for Dijkstra's search
    pq = []
    heapq.heappush(pq, (0, start, 'R', []))  # (cost, current_position, previous_direction, path)

    # Store the best cost to each position
    best_costs = defaultdict(lambda: float('inf'))
    best_costs[(start[0],start[1],'R')] = 0

    # Store all optimal paths
    optimal_paths = []

    # Directions: (row_change, col_change, direction_label)
    directions = [(-1, 0, 'U'), (1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R')]

    while pq:
        cost, (r, c), prev_dir, path = heapq.heappop(pq)

        # If we reach the end, store the path if it has the optimal cost
        if (r, c) == end:
            if not optimal_paths or cost == optimal_paths[0][0]:  # Matches the optimal cost
                optimal_paths.append((cost, path + [(r, c)]))
            elif cost > optimal_paths[0][0]:  # Stop if the cost exceeds the optimal cost
                break
            continue

        # Explore neighbors
        for dr, dc, dir_label in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] != '#':  # Valid move
                # Calculate turn cost
                turn_cost = 0 if prev_dir is None or prev_dir == dir_label else 1000
                new_cost = cost + 1 + turn_cost

                # Only process this node if it's the first time or a better (or equal) cost
                if new_cost <= best_costs[(nr, nc, dir_label)]:
                    best_costs[(nr, nc, dir_label)] = new_cost
                    heapq.heappush(pq, (new_cost, (nr, nc), dir_label, path + [(r, c)]))

    return optimal_paths[0][0], optimal_paths

def printPaths(maze, paths):
    for i, path in enumerate(paths):
        # create a deep copy of the maze to mark the path
        mazeCopy = deepcopy(maze)

        # mark the path in the maze
        for r, c in path:
            if mazeCopy[r][c] not in 'SE':  # Don't overwrite Start/End markers
                mazeCopy[r][c] = '*'

        # Print the maze with the path highlighted
        print(f"\nPath {i + 1}:")
        for row in mazeCopy:
            coloredRow = ''.join(
                f"{RED}{cell}{RESET}" if cell == '*' else cell for cell in row
            )
            print(coloredRow)

star1 = 0
star2 = 0
import os
data = open(os.path.basename(__file__).split('.')[0]+'.txt', 'r').read()
# data = """
# #################
# #...#...#...#..E#
# #.#.#.#.#.#.#.#.#
# #.#.#.#...#...#.#
# #.#.#.#.###.#.#.#
# #...#.#.#.....#.#
# #.#.#.#.#.#####.#
# #.#...#.#.#.....#
# #.#.#####.#.###.#
# #.#.#.......#...#
# #.#.###.#####.###
# #.#.#...#.....#.#
# #.#.#.#####.###.#
# #.#.#.........#.#
# #.#.#.#########.#
# #S#.............#
# #################
# """
data = [list(line.strip()) for line in data.split('\n') if line.strip()]

star1, paths = findPaths(data)
print('found',len(paths),'optimal paths')
# printPaths(data,[path[1] for path in paths])
nodes = set()
for path in paths:
    nodes.update(path[1])
star2 = len(nodes)

print('star1: %s'%star1)
print('star2: %s'%star2)
