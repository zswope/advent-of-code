from copy import deepcopy
import numpy as np

def printBoard(rope):
    minRow = 0
    minCol = 0
    maxRow = 0
    maxCol = 0
    for knot in rope:
        minRow = min(knot[0],minRow)
        maxRow = max(knot[0],maxRow)
        minCol = min(knot[1],minCol)
        maxCol = max(knot[1],maxCol)
    # print('(%d,%d)-(%d,%d)'%(minRow,minCol,maxRow,maxCol))
    board = []
    for _ in range(maxRow-minRow+1):
        board.append('%s'%('.'*(maxCol-minCol+1)))
    knotNum = 0
    for knot in rope:
        # print(len(board))
        # print(len(board[0]))
        # print(knot)
        # print('placing %d, '%(knotNum)+str(knot)+' at '+str([maxRow-knot[0],minCol+knot[1]]))
        l = list(board[maxRow-knot[0]])
        # print('len(l)=%d,knot[1]-maxCol-1=%d,maxCol=%d,knot[1]=%d'%(len(l),knot[1]-maxCol-1,maxCol,knot[1]))
        l[knot[1]-maxCol-1] = str(knotNum)
        board[maxRow-knot[0]] = ''.join(l)
        # print(str(knot[0])+ ': ' +str(board[knot[0]]))
        knotNum += 1
    print('========')
    # print(rope)
    print('   '+''.join([str(abs(x)) for x in list(range(minCol,maxCol+1))]))
    for i,line in enumerate(board):
        print('%d: '%(list(range(maxRow,minRow-1,-1))[i])+str(line))
    print('========')
    
def isFar(knot1,knot2):
    return knot1[0] == knot2[0]+2 or knot1[0] == knot2[0]-2 or knot1[1] == knot2[1]+2 or knot1[1] == knot2[1]-2

def initRope(length):
    rope = []
    for _ in range(length):
        rope.append([0,0])
    return rope

def moveRope(data,length):
    rope = initRope(length)
    visited = []
    for ins in data:
        (idx,c) = dir[ins.split(' ')[0]]
        for _ in range(int(ins.split(' ')[1])):
            oldrope = deepcopy(rope)
            rope[0][idx] += c
            # print('moving head from '+str(oldrope[0])+' to '+str(rope[0]))
            for i in range(len(rope)-1):
                # print('considering %d at '%(i)+str(rope[i]))
                if isFar(rope[i],rope[i+1]):
                    # print('moving %d from '%(i+1)+str(rope[i+1])+' to '+str(oldrope[i]))
                    # if i == 6:
                    #     print('current instruction: '+str(ins))
                    #     print('end of rope has moved from '+str(oldrope[-1])+' to '+str(rope[-1]))
                    move = list(np.subtract(oldrope[i],rope[i+1]))
                    # print('move: sub('+str(rope[i+1])+','+str(oldrope[i])+'= '+str(move))
                    rope[i+1] = oldrope[i]
                    if all(move):
                        j = i+1
                        while j+1 < len(rope) and isFar(rope[j],rope[j+1]):
                            # print('special moving %d from '%(j+1)+str(rope[j+1])+' to '+str(list(np.add(rope[j+1],move))))
                            move = [0 if not x else int(x/abs(x)) for x in list(np.subtract(rope[j],rope[j+1]))]
                            rope[j+1] = list(np.add(rope[j+1],move))
                            j += 1
                        # print(rope)
            if rope[-1] not in visited:
                visited.append(rope[-1])
    return len(visited)

with open('day9.txt','r') as file:
    data = file.read().split('\n')
    data = [line for line in data if line]
    dir = {
        'R': (1, 1),
        'L': (1, -1),
        'U': (0, 1),
        'D': (0, -1)
    }
    
    star1 = moveRope(data, 2)

    star2 = moveRope(data, 10)
    
    print('star1: '+str(star1))
    print('star2: '+str(star2))