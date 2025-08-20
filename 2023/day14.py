from day14_helper import *

star1 = 0
star2 = 0
cycles = 0
loads = [0]

def printPlatform(p):
    for i,row in enumerate(p):
        print('%d: %s'%(i,row))

with open('day14.txt', 'r') as file:
    data = file.readlines()
    data = [line.split('\n')[0] for line in data if line]
#     data = """O....#....
# O.OO#....#
# .....##...
# OO.#O....O
# .O.....O#.
# O.#..O.#.#
# ..O..#O..O
# .......O..
# #....###..
# #OO..#....""".split('\n')

# convert strings to list of ints
convertDict = {
    '.' : 0,
    'O' : 1,
    '#' : 2
}
printPlatform(data)
platform = []
for line in data:
    platform.append([convertDict[ele] for ele in line])

# printPlatform(platform)
tiltNorth(platform)
# printPlatform(platform)

printPlatform(platform)

star1 = getLoad(platform)

print('===========================')

# finish first cycle
tiltWest(platform)
tiltSouth(platform)
tiltEast(platform)
cycles += 1

loads.append(getLoad(platform))

printPlatform(platform)

for _ in range(1,1000000000):
    # do the cycle
    cycle(platform)
    loads.append(getLoad(platform))
    loop, idx = detectLoop(loads, 3, 3)
    if idx:
        star2 = getInterpolatedLoad(loads, loop, idx, 1000000000)
        break

print('star1: %s'%star1)
print('star2: %s'%star2)