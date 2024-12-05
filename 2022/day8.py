def split(word):
    l = []
    for c in word:
        l.append(int(c))
    return l

with open('day8.txt','r') as file:
    data = file.read().split('\n')
    data = [line for line in data if line]
    # data = ['30373',
    #         '25512',
    #         '65332',
    #         '33549',
    #         '35390']
    trees = []
    for row in data:
        trees.append(split(row))
    star1 = 0
    for row in range(len(trees)):
        for col in range(len(trees[row])):
            h = trees[row][col]
            # print('checking tree of height %d in position (%d,%d)'%(h,row,col))
            visible = 4
            # up
            for i in range(row):
                if trees[i][col] >= h:
                    visible -= 1
                    break
            # down
            for i in range(row+1,len(trees)):
                if trees[i][col] >= h:
                    visible -= 1
                    break
            # left
            for j in range(col):
                if trees[row][j] >= h:
                    visible -= 1
                    break
            # right
            # print(col)
            for j in range(col+1,len(trees)):
                # print('RIGHT: checking tree %d in (%d,%d)'%(trees[row][j],row,j))
                if trees[row][j] >= h:
                    visible -= 1
                    break
            if visible > 0:
                # print('visible from %d sides'%visible)
                star1 += 1
    
    star2 = 0
    for row in range(len(trees)):
        for col in range(len(trees[row])):
            h = trees[row][col]
            # print('checking tree of height %d in position (%d,%d)'%(h,row,col))
            visible1 = 0
            visible2 = 0
            visible3 = 0
            visible4 = 0
            # up
            for i in range(row-1,-1,-1):
                # print('\tUP: looking at %d'%trees[i][col])
                if trees[i][col] < h:
                    visible1 += 1
                elif trees[i][col] >= h:
                    visible1 += 1
                    break
            # print('\tUP: saw %d trees'%visible1)
            # down
            for i in range(row+1,len(trees)):
                if trees[i][col] < h:
                    visible2 += 1
                elif trees[i][col] >= h:
                    visible2 += 1
                    break
            # left
            for j in range(col-1,-1,-1):
                # print('\tLEFT: looking at %d'%trees[row][j])
                if trees[row][j] < h:
                    visible3 += 1
                elif trees[row][j] >= h:
                    visible3 += 1
                    break
            # print('\tLEFT: saw %d trees'%visible3)
            # right
            for j in range(col+1,len(trees)):
                # print('\tRIGHT: looking at %d'%trees[row][j])
                if trees[row][j] < h:
                    visible4 += 1
                elif trees[row][j] >= h:
                    visible4 += 1
                    break
            # print('\tRIGHT: saw %d trees'%visible4)
            # print('tree %d at (%d,%d) has score %d=%d*%d*%d*%d'%(h,row,col,visible1*visible2*visible3*visible4,visible1,visible2,visible3,visible4))
            star2 = max(star2,(visible1*visible2*visible3*visible4))
    
    
    print('star1: '+str(star1))
    print('star2: '+str(star2))