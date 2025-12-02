from copy import deepcopy

def nextCoords(i,j,dir):
    match dir:
        case 'up':
            return i-1,j
        case 'down':
            return i+1,j
        case 'left':
            return i,j-1
        case 'right':
            return i,j+1

star1 = 0
star2 = 0

with open('day16.txt', 'r') as file:
    data = file.readlines()
    data = [line.split('\n')[0] for line in data if line]
#     data = """.|...\....
# |.-.\.....
# .....|-...
# ........|.
# ..........
# .........\\
# ..../.\\\..
# .-.-/..|..
# .|....-|.\\
# ..//.|....""".split('\n')

startBeams = []
for i in range(len(data)):
    startBeams.append(((i,0),'right'))
for j in range(len(data[0])):
    startBeams.append(((0,j),'down'))
for i in range(len(data)):
    startBeams.append(((i,len(data[-1])-1),'left'))
for j in range(len(data[-1])):
    startBeams.append(((len(data)-1,j),'up'))

for idx, initial in enumerate(startBeams):
    # track coordinates visited as [((i, j), direction), ...]
    visited = []
    beams = [initial]
    nextBeams = []
    while True:
        for (i,j), dir in beams:
            # only process if we haven't already been here
            if ((i,j),dir) in visited:
                continue
            visited.append(((i,j),dir))
            match (data[i][j], dir):
                case ('.', _):
                    # print('going %s through .'%dir)
                    # continue in same direction
                    nextDir = dir
                    nextI, nextJ = nextCoords(i,j,nextDir)
                    # print('going %s from (%d,%d) to (%d,%d)'%(nextDir,i,j,nextI,nextJ))
                    if nextI >= 0 and nextJ >= 0 and nextI < len(data) and nextJ < len(data[0]):
                        nextBeams.append(((nextI,nextJ),nextDir))
                case ('|', 'up') | ('|', 'down'):
                    # print('going vertical through |')
                    # continue in same direction
                    nextDir = dir
                    nextI, nextJ = nextCoords(i,j,nextDir)
                    # print('going %s from (%d,%d) to (%d,%d)'%(nextDir,i,j,nextI,nextJ))
                    if nextI >= 0 and nextJ >= 0 and nextI < len(data) and nextJ < len(data[0]):
                        nextBeams.append(((nextI,nextJ),nextDir))
                case ('|', 'left') | ('|', 'right'):
                    # print('going horizontal into |')
                    # split the beam!
                    nextDir = 'up'
                    nextI, nextJ = nextCoords(i,j,nextDir)
                    # print('going %s from (%d,%d) to (%d,%d)'%(nextDir,i,j,nextI,nextJ))
                    if nextI >= 0 and nextJ >= 0 and nextI < len(data) and nextJ < len(data[0]):
                        nextBeams.append(((nextI,nextJ),nextDir))
                    nextDir = 'down'
                    nextI, nextJ = nextCoords(i,j,nextDir)
                    # print('going %s from (%d,%d) to (%d,%d)'%(nextDir,i,j,nextI,nextJ))
                    if nextI >= 0 and nextJ >= 0 and nextI < len(data) and nextJ < len(data[0]):
                        nextBeams.append(((nextI,nextJ),nextDir))
                case ('-', 'up') | ('-', 'down'):
                    # print('going vertical into -')
                    # split the beam!
                    nextDir = 'left'
                    nextI, nextJ = nextCoords(i,j,nextDir)
                    # print('going %s from (%d,%d) to (%d,%d)'%(nextDir,i,j,nextI,nextJ))
                    if nextI >= 0 and nextJ >= 0 and nextI < len(data) and nextJ < len(data[0]):
                        nextBeams.append(((nextI,nextJ),nextDir))
                    nextDir = 'right'
                    nextI, nextJ = nextCoords(i,j,nextDir)
                    # print('going %s from (%d,%d) to (%d,%d)'%(nextDir,i,j,nextI,nextJ))
                    if nextI >= 0 and nextJ >= 0 and nextI < len(data) and nextJ < len(data[0]):
                        nextBeams.append(((nextI,nextJ),nextDir))
                case ('-', 'left') | ('-', 'right'):
                    # print('going horizontal through -')
                    # continue in the same direction
                    nextDir = dir
                    nextI, nextJ = nextCoords(i,j,nextDir)
                    # print('going %s from (%d,%d) to (%d,%d)'%(nextDir,i,j,nextI,nextJ))
                    if nextI >= 0 and nextJ >= 0 and nextI < len(data) and nextJ < len(data[0]):
                        nextBeams.append(((nextI,nextJ),nextDir))
                case ('\\', 'up') | ('/', 'down'):
                    # print('going up into \\ or down into /')
                    # go left
                    nextDir = 'left'
                    nextI, nextJ = nextCoords(i,j,nextDir)
                    # print('going %s from (%d,%d) to (%d,%d)'%(nextDir,i,j,nextI,nextJ))
                    if nextI >= 0 and nextJ >= 0 and nextI < len(data) and nextJ < len(data[0]):
                        nextBeams.append(((nextI,nextJ),nextDir))
                case ('\\', 'down') | ('/', 'up'):
                    # print('going down into \\ or up into /')
                    # go right
                    nextDir = 'right'
                    nextI, nextJ = nextCoords(i,j,nextDir)
                    # print('going %s from (%d,%d) to (%d,%d)'%(nextDir,i,j,nextI,nextJ))
                    if nextI >= 0 and nextJ >= 0 and nextI < len(data) and nextJ < len(data[0]):
                        nextBeams.append(((nextI,nextJ),nextDir))
                case ('\\', 'left') | ('/', 'right'):
                    # print('going left into \\ or right into /')
                    # go up
                    nextDir = 'up'
                    nextI, nextJ = nextCoords(i,j,nextDir)
                    # print('going %s from (%d,%d) to (%d,%d)'%(nextDir,i,j,nextI,nextJ))
                    if nextI >= 0 and nextJ >= 0 and nextI < len(data) and nextJ < len(data[0]):
                        nextBeams.append(((nextI,nextJ),nextDir))
                case ('\\', 'right') | ('/', 'left'):
                    # print('going right into \\ or left into /')
                    # go down
                    nextDir = 'down'
                    nextI, nextJ = nextCoords(i,j,nextDir)
                    # print('going %s from (%d,%d) to (%d,%d)'%(nextDir,i,j,nextI,nextJ))
                    if nextI >= 0 and nextJ >= 0 and nextI < len(data) and nextJ < len(data[0]):
                        nextBeams.append(((nextI,nextJ),nextDir))
                case (c, d):
                    print('unknown case: passing through %s going %s'%(c,d))
                    exit()
                    # ???
                case _:
                    print('how...')
                    exit()
                    # ??????????????????

            # print('next: ' + str(nextBeams))
            # print('visited: ' + str(visited))
            # import pdb; pdb.set_trace()
        
        if len(nextBeams) == 0:
            break
        else:
            beams = deepcopy(nextBeams)
            nextBeams = []

    if idx == 0:
        star1 = len(list(dict(visited).items()))
    star2 = max(star2,len(list(dict(visited).items())))
    print('after iteration %d, star2 is %d'%(idx,star2))

print('star1: %s'%star1)
print('star2: %s'%star2)