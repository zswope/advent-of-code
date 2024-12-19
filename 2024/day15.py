import numpy as np
from copy import deepcopy

def getMove(moveRow):
    # can't move if there's no empty space
    if '.' not in moveRow:
        return None

    emptyIdx = moveRow.index('.')
    # can't move if there's a wall before the empty space
    if moveRow.index('#') < emptyIdx:
        return None

    res = ['.']
    res += moveRow[:emptyIdx]
    res += moveRow[emptyIdx+1:]
    return res

def propagateMove(warehouse, robot):
    bottoms = []
    bottoms.append((robot[0],robot[1]))
    tops = []
    curRow = robot[0]
    nextCols = [robot[1]]
    while curRow:
        cols = deepcopy(nextCols)
        for col in cols:
            match warehouse[curRow-1,col]:
                case '[':
                    if col+1 not in nextCols:
                        bottoms.append((curRow-1,col+1))
                        nextCols.append(col+1)
                case ']':
                    if col-1 not in nextCols:
                        bottoms.append((curRow-1,col-1))
                        nextCols.append(col-1)
                case '.':
                    tops.append((curRow-1,col))
                    nextCols.remove(col)
                case '#':
                    return warehouse
        if len(nextCols):
            curRow -= 1
        else:
            break
    else:
        # didn't break early, there is no solution
        return warehouse
    
    bottoms.sort(key=lambda x: (x[1],x[0]))
    tops.sort(key=lambda x: (x[1],x[0]))
    
    for b,t in zip(bottoms,tops):
        col = b[1]
        warehouse[t[0]:b[0],col] = warehouse[t[0]+1:b[0]+1,col]
        warehouse[b[0],col] = '.'
    
    return warehouse

star1 = 0
star2 = 0 # > 1461549
import os
data = open(os.path.basename(__file__).split('.')[0]+'.txt','r').read()
# big example for part 2
# data = """
# ##########
# #..O..O.O#
# #......O.#
# #.OO..O.O#
# #..O@..O.#
# #O#..O...#
# #O..O..O.#
# #.OO.O.OO#
# #....O...#
# ##########

# <vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
# vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
# ><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
# <<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
# ^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
# ^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
# >^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
# <><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
# ^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
# v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
# """
# small example for part 2
# data = """
# #######
# #...#.#
# #.....#
# #..OO@#
# #..O..#
# #.....#
# #######

# <vv<<^^<<^^
# """
# custom example to test gap in push
# data = """
# #####
# #...#
# #.O.#
# #.O@#
# #.O.#
# #...#
# #####

# <>vv<^
# """
# custom example to test overhanging boxes
# data = """
# ######
# #....#
# #@O..#
# #.O..#
# #.OO.#
# #.O..#
# #.O..#
# #.OO.#
# #.O..#
# #....#
# ######

# >><vvvvvv>v>^
# """
data = data.split('\n\n')
# extract data
warehouse = np.array([list(line) for line in data[0].split('\n') if line])
moves = ''.join(data[1].split('\n'))

# Find the robot coords
robotCoords = np.where(warehouse == '@')
robot = (robotCoords[0][0],robotCoords[1][0])

# do all moves
for move in moves:
    if move == '^':
        update = getMove(np.flip(warehouse[:robot[0]+1,robot[1]]).tolist())
        if update is not None:
            update.reverse()
            warehouse[:robot[0]+1,robot[1]] = update
            robot = (robot[0]-1,robot[1])
    elif move == 'v':
        update = getMove(warehouse[robot[0]:,robot[1]].tolist())
        if update is not None:
            warehouse[robot[0]:,robot[1]] = update
            robot = (robot[0]+1,robot[1])
    elif move == '<':
        update = getMove(np.flip(warehouse[robot[0],:robot[1]+1]).tolist())
        if update is not None:
            update.reverse()
            warehouse[robot[0],:robot[1]+1] = update
            robot = (robot[0],robot[1]-1)
    elif move == '>':
        update = getMove(warehouse[robot[0],robot[1]:].tolist())
        if update is not None:
            warehouse[robot[0],robot[1]:] = update
            robot = (robot[0],robot[1]+1)
    # print('after moving %s, warehouse is:'%move)
    # [print(''.join(line)) for line in warehouse]

# calculate GPS
boxCoords = np.where(warehouse == 'O')
for row,col in zip(boxCoords[0],boxCoords[1]):
    star1 += row*100 + col
print('star1: %s'%star1)

# expand the warehouse for part 2
warehouse2 = []
for row in [line for line in data[0].split('\n') if line]:
    newRow = ''
    for ele in row:
        if ele == '#':
            newRow += '##'
        elif ele == '.':
            newRow += '..'
        elif ele == 'O':
            newRow += '[]'
        elif ele == '@':
            newRow += '@.'
    warehouse2.append(list(newRow))
warehouse = np.array(warehouse2)

# Find the robot coords
robotCoords = np.where(warehouse == '@')
robot = (robotCoords[0][0],robotCoords[1][0])

# do all moves
for moveNum,move in enumerate(moves):
    # more complicated handling for vertical moves
    if move == '^':
        # check if we can perform trivial move
        trivialCol = np.flip(warehouse[:robot[0]+1,robot[1]]).tolist()
        if trivialCol[1] in '.#':
            update = getMove(trivialCol)
            if update is not None:
                update.reverse()
                warehouse[:robot[0]+1,robot[1]] = update
                robot = (robot[0]-1,robot[1])
        # must handle big boxes...
        else:
            update = propagateMove(deepcopy(warehouse),robot)
            if not (update == warehouse).all():
                warehouse = update
                robot = (robot[0]-1,robot[1])
    elif move == 'v':
        # check if we can perform trivial move
        trivialCol = warehouse[robot[0]:,robot[1]].tolist()
        if trivialCol[1] in '.#':
            update = getMove(trivialCol)
            if update is not None:
                warehouse[robot[0]:,robot[1]] = update
                robot = (robot[0]+1,robot[1])
        # must handle big boxes...
        else:
            update = np.flipud(propagateMove(np.flipud(deepcopy(warehouse)),((len(warehouse)-1)-robot[0],robot[1])))
            if not (update == warehouse).all():
                warehouse = update
                robot = (robot[0]+1,robot[1])
    # left and right moves are always trivial
    elif move == '<':
        update = getMove(np.flip(warehouse[robot[0],:robot[1]+1]).tolist())
        if update is not None:
            update.reverse()
            warehouse[robot[0],:robot[1]+1] = update
            robot = (robot[0],robot[1]-1)
    elif move == '>':
        update = getMove(warehouse[robot[0],robot[1]:].tolist())
        if update is not None:
            warehouse[robot[0],robot[1]:] = update
            robot = (robot[0],robot[1]+1)
    # print('move %d: after moving %s, warehouse is:'%(moveNum,move))
    # [print(''.join(line)) for line in warehouse]


# calculate GPS
boxCoords = np.where(warehouse == '[')
for row,col in zip(boxCoords[0],boxCoords[1]):
    star2 += row*100 + col

print('star2: %s'%star2)
