def printCave(cave):
    for line in cave:
        print(''.join(line))
        
def dropSand():
    sandx = 500
    sandy = 0
    while '.' in cave[sandy+1][sandx-1:sandx+2]:
        # print(cave[sandy+1][sandx-1:sandx+2])
        if cave[sandy+1][sandx] == '.':
            sandy += 1
        elif cave[sandy+1][sandx-1] == '.':
            sandy += 1
            sandx -= 1
        else:
            sandy += 1
            sandx += 1
    cave[sandy][sandx] = 'o'
    if sandy == 0:
        return False
    return True

with open('day14.txt','r') as file:
    data = file.read().split('\n')
    data = [line for line in data if line]
    # data = [
    #     '498,4 -> 498,6 -> 496,6',
    #     '503,4 -> 502,4 -> 502,9 -> 494,9',
    #     '0,11 -> 520,11'
    # ]
    
    data = [line.split(' -> ') for line in data]
    cave = []
    for _ in range(176):
        cave.append(['.']*700)
    for path in data:
        oldx = None
        oldy = None
        for point in path:
            x = int(point.split(',')[0])
            y = int(point.split(',')[1])
            if oldy: # not first point
                # vertical
                if x == oldx:
                    for i in range(min(y,oldy),max(y,oldy)):
                        cave[i][x] = '#'
                # horizontal
                if y == oldy:
                    cave[y][min(x,oldx):max(x,oldx)+1] = ['#'] * (abs(x-oldx)+1)
            oldx = x
            oldy = y
    # printCave(cave)
    star1 = 1
    # import pdb
    while dropSand():
        # pdb.set_trace()
        star1 += 1
        # print(star1)
        # printCave(cave)
    
    # cave[500][8] = '+'
    # printCave(cave)
    
    star2 = 0
    
    print('star1: %d'%star1)
    print('star2: %d'%star2)