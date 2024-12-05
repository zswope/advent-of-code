from itertools import cycle
from time import time
import math

star1 = 0
star2 = 1

class node():
    def __init__(self, left, right):
        self.left = left
        self.right = right

with open('day8.txt','r') as file:
    data = file.read().split('\n')
#     tmpdata = """LR

# 11A = (11B, XXX)
# 11B = (XXX, 11Z)
# 11Z = (11B, XXX)
# 22A = (22B, XXX)
# 22B = (22C, 22C)
# 22C = (22Z, 22Z)
# 22Z = (22B, 22B)
# XXX = (XXX, XXX)"""
#     if tmpdata:
#         data = tmpdata.split('\n')
    data = [line for line in data if line]
    
    # do computation here!
    steps = data[0]
    nodes = {}
    for dat in data[1:]:
        name = dat[:3]
        left = dat[7:10]
        right = dat[12:15]
        nodes[name] = node(left,right)
    
    curNode = 'AAA'
    for instruction in cycle(steps):
        star1 += 1
        if instruction == 'L':
            curNode = nodes[curNode].left
        elif instruction == 'R':
            curNode = nodes[curNode].right
        if curNode == 'ZZZ':
            break

    print('star1: %s'%star1)
        
    startTime = time()
    startNodes = [node for node in nodes if node[-1] == 'A']
    curNodes = [node for node in nodes if node[-1] == 'A']
    findNodes = []
    numSteps = 0
    for instruction in cycle(steps):
        numSteps += 1
        if instruction == 'L':
            curNodes = [nodes[node].left for node in curNodes if node]
        elif instruction == 'R':
            curNodes = [nodes[node].right for node in curNodes if node]
        for i in range(len(curNodes)):
            # print(curNodes[i])
            if curNodes[i][-1] == 'Z':
                # print('took %d steps to find %s end'%(numSteps,startNodes[i]))
                findNodes.append(numSteps)
                curNodes[i] = ''
        if all(not node for node in curNodes):
            break

for i in findNodes:
    star2 = star2*i//math.gcd(star2, i)
print('star2: %s'%star2)