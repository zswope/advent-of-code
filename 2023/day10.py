import math
from contextlib import suppress

star1 = 0
star2 = 0

class pipe():
    def __init__(self, pipeType, lastDir):
        self.last = lastDir
        self.type = pipeType
        if pipeType == '|':
            if lastDir == 'up':
                self.next = 'down'
            elif lastDir == 'down':
                self.next = 'up'
            else:
                raise ValueError('invalid direction %s for pipe type %s'%(lastDir,pipeType))
        elif pipeType == '-':
            if lastDir == 'left':
                self.next = 'right'
            elif lastDir == 'right':
                self.next = 'left'
            else:
                raise ValueError('invalid direction %s for pipe type %s'%(lastDir,pipeType))
        elif pipeType == 'L':
            if lastDir == 'up':
                self.next = 'right'
            elif lastDir == 'right':
                self.next = 'up'
            else:
                raise ValueError('invalid direction %s for pipe type %s'%(lastDir,pipeType))
        elif pipeType == 'F':
            if lastDir == 'down':
                self.next = 'right'
            elif lastDir == 'right':
                self.next = 'down'
            else:
                raise ValueError('invalid direction %s for pipe type %s'%(lastDir,pipeType))
        elif pipeType == '7':
            if lastDir == 'down':
                self.next = 'left'
            elif lastDir == 'left':
                self.next = 'down'
            else:
                raise ValueError('invalid direction %s for pipe type %s'%(lastDir,pipeType))
        elif pipeType == 'J':
            if lastDir == 'up':
                self.next = 'left'
            elif lastDir == 'left':
                self.next = 'up'
            else:
                raise ValueError('invalid direction %s for pipe type %s'%(lastDir,pipeType))
            
    def getNextInChain(self, curCoords):
        if self.next == 'left':
            return ((curCoords[0],curCoords[1]-1),'right')
        elif self.next == 'right':
            return ((curCoords[0],curCoords[1]+1),'left')
        elif self.next == 'up':
            return ((curCoords[0]-1,curCoords[1]),'down')
        elif self.next == 'down':
            return ((curCoords[0]+1,curCoords[1]),'up')
        
    def updateMaze(self, pipeCoords, insideList, outsideList):
        # update inside
        for inside in insideList.split(':'):
            if inside == 'left' and pipeCoords[1]>0 and maze[pipeCoords[0]][pipeCoords[1]-1] == '.':
                maze[pipeCoords[0]][pipeCoords[1]-1] = 'I'
            elif inside == 'right' and pipeCoords[1]<len(maze[0])-1 and maze[pipeCoords[0]][pipeCoords[1]+1] == '.':
                maze[pipeCoords[0]][pipeCoords[1]+1] = 'I'
            elif inside == 'up' and pipeCoords[0]>0 and maze[pipeCoords[0]-1][pipeCoords[1]] == '.':
                maze[pipeCoords[0]-1][pipeCoords[1]] = 'I'
            elif inside == 'down' and pipeCoords[0]<len(maze)-1 and maze[pipeCoords[0]+1][pipeCoords[1]] == '.':
                maze[pipeCoords[0]+1][pipeCoords[1]] = 'I'
        # update outside
        for outside in outsideList.split(':'):
            if outside == 'left' and pipeCoords[1]>0 and maze[pipeCoords[0]][pipeCoords[1]-1] == '.':
                maze[pipeCoords[0]][pipeCoords[1]-1] = 'O'
            elif outside == 'right' and pipeCoords[1]<len(maze[0])-1 and maze[pipeCoords[0]][pipeCoords[1]+1] == '.':
                maze[pipeCoords[0]][pipeCoords[1]+1] = 'O'
            elif outside == 'up' and pipeCoords[0]>0 and maze[pipeCoords[0]-1][pipeCoords[1]] == '.':
                maze[pipeCoords[0]-1][pipeCoords[1]] = 'O'
            elif outside == 'down' and pipeCoords[0]<len(maze)-1 and maze[pipeCoords[0]+1][pipeCoords[1]] == '.':
                maze[pipeCoords[0]+1][pipeCoords[1]] = 'O'
        return self.getNextInChain(pipeCoords)

def printMaze(maze):
    print('=======MAZE=======')
    for row in maze:
        print(''.join(row))

def allEmpty(maze):
    emptyCoordsList = []
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == '.':
                emptyCoordsList.append((i, j))
    return emptyCoordsList

with open('day10.txt','r') as file:
    data = file.read().split('\n')
    # tmpdata = """
    #     7-F7-
    #     .FJ|7
    #     SJLL7
    #     |F--J
    #     LJ.LJ
    # """
    # tmpdata = """
    #     ..........
    #     .S------7.
    #     .|F----7|.
    #     .||....||.
    #     .||....||.
    #     .|L-7F-J|.
    #     .|..||..|.
    #     .L--JL--J.
    #     ..........
    # """
    # tmpdata = """
    #     .F----7F7F7F7F-7....
    #     .|F--7||||||||FJ....
    #     .||.FJ||||||||L7....
    #     FJL7L7LJLJ||LJ.L-7..
    #     L--J.L7...LJS7F-7L7.
    #     ....F-J..F7FJ|L7L7L7
    #     ....L7.F7||L7|.L7L7|
    #     .....|FJLJ|FJ|F7|.LJ
    #     ....FJL-7.||.||||...
    #     ....L---J.LJ.LJLJ...
    # """
    # if tmpdata:
    #     data = tmpdata.split('\n')
    data = [line.strip() for line in data if line.strip()]
    
# do computation here!
maze = []
start = ()
# create maze 2d list
for i,dat in enumerate(data):
    if 'S' in dat:
        start = (i,dat.find('S'))
    maze.append(list(dat))
# pprint(maze)

# handle start pipe (we need to provide its initial connections)
pipes = {
    start: pipe('F','down')
}
nextPipe, lastDir = pipes[start].getNextInChain(start)
# print(nextPipe)
while maze[nextPipe[0]][nextPipe[1]] != 'S':
    star1 += 1
    pipes[nextPipe] = pipe(maze[nextPipe[0]][nextPipe[1]], lastDir)
    nextPipe, lastDir = pipes[nextPipe].getNextInChain(nextPipe)
    # print(nextPipe)

# row, col
ioStart = (4, 88)
outsideList = 'up'
insideList = 'down'

# clear maze of excess pipes
for row in range(len(data)):
    for col in range(len(data[row])):
        if not ((row, col) in pipes.keys()):
            maze[row][col] = '.'

# handle start pipe
# printMaze(maze)
# print('start iterations with pipe %s (%s). %s is inside. %s is outside'%(ioStart,pipes[ioStart].type,insideList,outsideList))
nextPipe, lastDir = pipes[ioStart].updateMaze(ioStart,insideList,outsideList)
# printMaze(maze)
# print('next pipe = %s (%s). %s in inside. %s is outside'%(nextPipe,pipes[nextPipe].type,insideList,outsideList))
# recurse through pipes
while nextPipe != ioStart:
    nextPipe, lastDir = pipes[nextPipe].updateMaze(nextPipe,insideList,outsideList)
    match pipes[nextPipe].type:
        case '|':
            if 'left' in insideList or 'right' in outsideList:
                insideList='left'
                outsideList='right'
            elif 'right' in insideList or 'left' in outsideList:
                insideList='right'
                outsideList='left'
            else:
                printMaze(maze)
                raise ValueError('invalid inside/outside lists for case %s: insideList = %s, outsideList = %s'%(pipes[nextPipe].type,insideList,outsideList))
        case '-':
            if 'up' in insideList or 'down' in outsideList:
                insideList='up'
                outsideList='down'
            elif 'down' in insideList or 'up' in outsideList:
                insideList='down'
                outsideList='up'
            else:
                printMaze(maze)
                raise ValueError('invalid inside/outside lists for case %s: insideList = %s, outsideList = %s'%(pipes[nextPipe].type,insideList,outsideList))
        case 'L':
            if lastDir == 'up':
                if 'right' in insideList or 'left' in outsideList:
                    insideList=''
                    outsideList='left:down'
                elif 'left' in insideList or 'right' in outsideList:
                    insideList='left:down'
                    outsideList=''
                else:
                    printMaze(maze)
                    raise ValueError('invalid inside/outside lists for case %s: insideList = %s, outsideList = %s'%(pipes[nextPipe].type,insideList,outsideList))
            elif lastDir == 'right':
                if 'up' in insideList or 'down' in outsideList:
                    insideList=''
                    outsideList='left:down'
                elif 'down' in insideList or 'up' in outsideList:
                    insideList='left:down'
                    outsideList=''
                else:
                    printMaze(maze)
                    raise ValueError('invalid inside/outside lists for case %s: insideList = %s, outsideList = %s'%(pipes[nextPipe].type,insideList,outsideList))
            else:
                printMaze(maze)
                raise ValueError('invalid last direction for case %s: %s'%(pipes[nextPipe].type,lastDir))
        case 'F':
            if lastDir == 'right':
                if 'up' in insideList or 'down' in outsideList:
                    insideList='up:left'
                    outsideList=''
                elif 'down' in insideList or 'up' in outsideList:
                    insideList=''
                    outsideList='up:left'
                else:
                    printMaze(maze)
                    raise ValueError('invalid inside/outside lists for case %s: insideList = %s, outsideList = %s'%(pipes[nextPipe].type,insideList,outsideList))
            elif lastDir == 'down':
                if 'left' in insideList or 'right' in outsideList:
                    insideList='up:left'
                    outsideList=''
                elif 'right' in insideList or 'left' in outsideList:
                    insideList=''
                    outsideList='up:left'
                else:
                    printMaze(maze)
                    raise ValueError('invalid inside/outside lists for case %s: insideList = %s, outsideList = %s'%(pipes[nextPipe].type,insideList,outsideList))
            else:
                printMaze(maze)
                raise ValueError('invalid last direction for case %s: %s'%(pipes[nextPipe].type,lastDir))
        case '7':
            if lastDir == 'down':
                if 'left' in insideList or 'right' in outsideList:
                    insideList=''
                    outsideList='up:right'
                elif 'right' in insideList or 'left' in outsideList:
                    insideList='up:right'
                    outsideList=''
                else:
                    printMaze(maze)
                    raise ValueError('invalid inside/outside lists for case %s: insideList = %s, outsideList = %s'%(pipes[nextPipe].type,insideList,outsideList))
            elif lastDir == 'left':
                if 'up' in insideList or 'down' in outsideList:
                    insideList='up:right'
                    outsideList=''
                elif 'down' in insideList or 'up' in outsideList:
                    insideList=''
                    outsideList='up:right'
                else:
                    printMaze(maze)
                    raise ValueError('invalid inside/outside lists for case %s: insideList = %s, outsideList = %s'%(pipes[nextPipe].type,insideList,outsideList))
            else:
                printMaze(maze)
                raise ValueError('invalid last direction for case %s: %s'%(pipes[nextPipe].type,lastDir))
        case 'J':
            if lastDir == 'left':
                if 'up' in insideList or 'down' in outsideList:
                    insideList=''
                    outsideList='down:right'
                elif 'down' in insideList or 'up' in outsideList:
                    insideList='down:right'
                    outsideList=''
                else:
                    printMaze(maze)
                    raise ValueError('invalid inside/outside lists for case %s: insideList = %s, outsideList = %s'%(pipes[nextPipe].type,insideList,outsideList))
            elif lastDir == 'up':
                if 'left' in insideList or 'right' in outsideList:
                    insideList=''
                    outsideList='down:right'
                elif 'right' in insideList or 'left' in outsideList:
                    insideList='down:right'
                    outsideList=''
                else:
                    printMaze(maze)
                    raise ValueError('invalid inside/outside lists for case %s: insideList = %s, outsideList = %s'%(pipes[nextPipe].type,insideList,outsideList))
            else:
                printMaze(maze)
                raise ValueError('invalid last direction for case %s: %s'%(pipes[nextPipe].type,lastDir))
            
printMaze(maze)
# flood fill
iters = 0
while any('.' in row for row in maze):
    print('looping...')
    for emptyCoords in allEmpty(maze):
        if emptyCoords[0] > 0 and maze[emptyCoords[0]-1][emptyCoords[1]] == 'I':
            maze[emptyCoords[0]][emptyCoords[1]] = 'I'
        elif emptyCoords[0] < len(maze)-1 and maze[emptyCoords[0]+1][emptyCoords[1]] == 'I':
            maze[emptyCoords[0]][emptyCoords[1]] = 'I'
        elif emptyCoords[1] > 0 and maze[emptyCoords[0]][emptyCoords[1]-1] == 'I':
            maze[emptyCoords[0]][emptyCoords[1]] = 'I'
        elif emptyCoords[1] < len(maze[0])-1 and maze[emptyCoords[0]][emptyCoords[1]+1] == 'I':
            maze[emptyCoords[0]][emptyCoords[1]] = 'I'
        if emptyCoords[0] > 0 and maze[emptyCoords[0]-1][emptyCoords[1]] == 'O':
            maze[emptyCoords[0]][emptyCoords[1]] = 'O'
        elif emptyCoords[0] < len(maze)-1 and maze[emptyCoords[0]+1][emptyCoords[1]] == 'O':
            maze[emptyCoords[0]][emptyCoords[1]] = 'O'
        elif emptyCoords[1] > 0 and maze[emptyCoords[0]][emptyCoords[1]-1] == 'O':
            maze[emptyCoords[0]][emptyCoords[1]] = 'O'
        elif emptyCoords[1] < len(maze[0])-1 and maze[emptyCoords[0]][emptyCoords[1]+1] == 'O':
            maze[emptyCoords[0]][emptyCoords[1]] = 'O'
        iters += 1

printMaze(maze)
star2 = sum(row.count('I') for row in maze)

print('star1: %s'%math.ceil(star1/2))
print('star2: %s'%star2)