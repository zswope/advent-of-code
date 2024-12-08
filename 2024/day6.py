from collections import defaultdict
from copy import deepcopy

def printMap(data):
    print('=================')
    for dat in data:
        print(''.join(dat))
    print('=================')

def loopCheck(dataCopy, prevPositionsCopy,guardCharCopy):
    while True:
        row = None
        col = None
        for i, r in enumerate(dataCopy):
            if guardCharCopy in r:
                row = i
                col = r.index(guardCharCopy)
        if row is None or col is None:
            print('Could not find guardCharCopy: %s in dataCopy:'%guardCharCopy)
            printMap(dataCopy)
            raise ValueError('Failed to locate guard')

        # check for loop
        if guardCharCopy in prevPositionsCopy[(row,col)]:
            return True

        # save position for infinite loop checking
        prevPositionsCopy[(row,col)] += guardCharCopy

        # check if guard is exiting
        if ((guardCharCopy == '^' and row == 0) or
            (guardCharCopy == 'v' and row == len(dataCopy)-1) or
            (guardCharCopy == '<' and col == 0) or
            (guardCharCopy == '>' and col == len(dataCopy[0])-1)):
            dataCopy[row][col] = 'X'
            return False

        # step forward
        if guardCharCopy == '^' and dataCopy[row-1][col] in '.X':
            dataCopy[row][col] = 'X'
            dataCopy[row-1][col] = '^'
        if guardCharCopy == 'v' and dataCopy[row+1][col] in '.X':
            dataCopy[row][col] = 'X'
            dataCopy[row+1][col] = 'v'
        if guardCharCopy == '<' and dataCopy[row][col-1] in '.X':
            dataCopy[row][col] = 'X'
            dataCopy[row][col-1] = '<'
        if guardCharCopy == '>' and dataCopy[row][col+1] in '.X':
            dataCopy[row][col] = 'X'
            dataCopy[row][col+1] = '>'
        
        # rotate
        if guardCharCopy == '^' and dataCopy[row-1][col] == '#':
            dataCopy[row][col] = '>'
            guardCharCopy = '>'
        if guardCharCopy == 'v' and dataCopy[row+1][col] == '#':
            dataCopy[row][col] = '<'
            guardCharCopy = '<'
        if guardCharCopy == '<' and dataCopy[row][col-1] == '#':
            dataCopy[row][col] = '^'
            guardCharCopy = '^'
        if guardCharCopy == '>' and dataCopy[row][col+1] == '#':
            dataCopy[row][col] = 'v'
            guardCharCopy = 'v'
    

star1 = 0
star2 = 0
import os
with open(os.path.basename(__file__).split('.')[0]+'.txt','r') as file:
    data = file.readlines()
#     data = """....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#..^.....
# ........#.
# #.........
# ......#...
# """.split('\n')
    data = [list(line.strip()) for line in data if line.strip()]

guardChar = '^'
prevPositions = defaultdict(lambda: '')
blocks = set()
while True:
    row = None
    col = None
    for i, r in enumerate(data):
        if guardChar in r:
            row = i
            col = r.index(guardChar)
    if row is None or col is None:
        print('Could not find guardChar: %s in data:'%guardChar)
        printMap(data)
        raise ValueError('Failed to locate guard')

    # check if guard is exiting
    if ((guardChar == '^' and row == 0) or
        (guardChar == 'v' and row == len(data)-1) or
        (guardChar == '<' and col == 0) or
        (guardChar == '>' and col == len(data[0])-1)):
        data[row][col] = 'X'
        break

    # try placing an object in front of the guard and check for an infinite loop
    newData = deepcopy(data)
    if guardChar == '^':
        block = (row-1,col)
        newData[row-1][col] = '#'
    elif guardChar == 'v':
        block = (row+1,col)
        newData[row+1][col] = '#'
    elif guardChar == '<':
        block = (row,col-1)
        newData[row][col-1] = '#'
    elif guardChar == '>':
        block = (row,col+1)
        newData[row][col+1] = '#'
    if loopCheck(newData, deepcopy(prevPositions), deepcopy(guardChar)):
        blocks.add(block)

    # save position for infinite loop checking
    prevPositions[(row,col)] += guardChar

    # step forward
    if guardChar == '^' and data[row-1][col] in '.X':
        data[row][col] = 'X'
        data[row-1][col] = '^'
    if guardChar == 'v' and data[row+1][col] in '.X':
        data[row][col] = 'X'
        data[row+1][col] = 'v'
    if guardChar == '<' and data[row][col-1] in '.X':
        data[row][col] = 'X'
        data[row][col-1] = '<'
    if guardChar == '>' and data[row][col+1] in '.X':
        data[row][col] = 'X'
        data[row][col+1] = '>'
    
    # rotate
    if guardChar == '^' and data[row-1][col] == '#':
        data[row][col] = '>'
        guardChar = '>'
    if guardChar == 'v' and data[row+1][col] == '#':
        data[row][col] = '<'
        guardChar = '<'
    if guardChar == '<' and data[row][col-1] == '#':
        data[row][col] = '^'
        guardChar = '^'
    if guardChar == '>' and data[row][col+1] == '#':
        data[row][col] = 'v'
        guardChar = 'v'
    
star1 = [el for sublist in data for el in sublist].count('X')
star2 = len(blocks)

print('star1: %s'%star1)
print('star2: %s'%star2)
