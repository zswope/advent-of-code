star1 = 0
star2 = 0
import os
data = open(os.path.basename(__file__).split('.')[0]+'.txt','r').readlines()
# data = """
# RRRRIICCFF
# RRRRIICCCF
# VVRRRCCFFF
# VVRCCCJFFF
# VVVVCJJCFE
# VVIVCCJJEE
# VVIIICJJEE
# MIIIIIJJEE
# MIIISIJEEE
# MMMISSJEEE
# """.split('\n')
data = [line.strip() for line in data if line.strip()]

right = []
down = []
# determine fences
for i,row in enumerate(data):
    for j,plot in enumerate(row):
        if j+1 < len(row) and plot != row[j+1]:
            right.append((i,j))
        if i+1 < len(data) and plot!= data[i+1][j]:
            down.append((i,j))
for ii in range(len(data)):
    right.append((ii,-1))
    right.append((ii,len(data)-1))
for jj in range(len(data[0])):
    down.append((-1,jj))
    down.append((len(data[0])-1,jj))

# iterate through all plots and try to flood fill
accounted = []
for i,row in enumerate(data):
    for j,plot in enumerate(row):
        if (i,j) not in accounted:
            totalFill = [(i,j)]
            prevFill = [(i,j)]
            totalFence = 0
            downFences = []
            rightFences = []
            upFences = []
            leftFences = []
            # flood fill until it stops filling
            while len(prevFill):
                curFill = set()
                for cell in prevFill:
                    if cell not in right:
                        if (cell[0],cell[1]+1) not in totalFill:
                            curFill.add((cell[0],cell[1]+1))
                    else:
                        totalFence += 1
                        rightFences.append(cell)
                    if cell not in down:
                        if (cell[0]+1,cell[1]) not in totalFill:
                            curFill.add((cell[0]+1,cell[1]))
                    else:
                        totalFence += 1
                        downFences.append(cell)
                    if (cell[0],cell[1]-1) not in right:
                        if (cell[0],cell[1]-1) not in totalFill:
                            curFill.add((cell[0],cell[1]-1))
                    else:
                        totalFence += 1
                        leftFences.append(cell)
                    if (cell[0]-1,cell[1]) not in down:
                        if (cell[0]-1,cell[1]) not in totalFill:
                            curFill.add((cell[0]-1,cell[1]))
                    else:
                        totalFence += 1
                        upFences.append(cell)
                totalFill += curFill
                prevFill = curFill
            star1 += len(totalFill) * totalFence
            accounted += totalFill
            
            rightFences.sort(key=lambda x: (x[1],x[0]))
            downFences.sort()
            leftFences.sort(key=lambda x: (x[1],x[0]))
            upFences.sort()

            # if missing one of these items, it is a new side
            # 1) same column
            # 2) only one row apart
            # 3) same plots (only check if all coords are positive)
            rightSides = int(bool(len(rightFences)))
            for u,d in zip(rightFences[:len(rightFences)-1],rightFences[1:]):
                if not (u[1] == d[1] and abs(u[0]-d[0]) == 1):
                    rightSides += 1
            # print('%s has %d right sides'%(plot,rightSides))
            downSides = int(bool(len(downFences)))
            for l,r in zip(downFences[:len(downFences)-1],downFences[1:]):
                if not (l[0] == r[0] and abs(l[1]-r[1]) == 1):
                    downSides += 1
            # print('%s has %d down sides'%(plot,downSides))
            leftSides = int(bool(len(leftFences)))
            for u,d in zip(leftFences[:len(leftFences)-1],leftFences[1:]):
                if not (u[1] == d[1] and abs(u[0]-d[0]) == 1):
                    leftSides += 1
            # print('%s has %d left sides'%(plot,leftSides))
            upSides = int(bool(len(upFences)))
            for l,r in zip(upFences[:len(upFences)-1],upFences[1:]):
                if not (l[0] == r[0] and abs(l[1]-r[1]) == 1):
                    upSides += 1
            # print('%s has %d up sides'%(plot,upSides))
            
            sides = rightSides+downSides+leftSides+upSides
            star2 += len(totalFill) * sides


print('star1: %s'%star1)
print('star2: %s'%star2)