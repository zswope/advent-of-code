from copy import deepcopy
from time import time

def tryRows(rows, prevStar = -1):
    for m in range(len(rows[0])-1):
        for c in range(len(rows)):
            # print('====== COL %d ====='%m)
            # print(''.join(list(reversed(rows[c][max(0,m-(len(rows[c])-m)+2):m+1]))))
            # print(rows[c][m+1:min(len(rows[c]),(m+1)*2)])
            if ''.join(list(reversed(rows[c][max(0,m-(len(rows[c])-m)+2):m+1]))) != rows[c][m+1:min(len(rows[c]),(m+1)*2)]:
                break
        else:
            if m+1 != prevStar:
                # print('found m at col %d!'%m)
                return m+1
    return 0

def tryCols(cols, prevStar = -1):
    for m in range(len(cols[0])-1):
        for c in range(len(cols)):
            # print('====== ROW %d ====='%m)
            # print(''.join(list(reversed(cols[c][max(0,m-(len(cols[c])-m)+2):m+1]))))
            # print(''.join(list(cols[c][m+1:min(len(cols[c]),(m+1)*2)])))
            if ''.join(list(reversed(cols[c][max(0,m-(len(cols[c])-m)+2):m+1]))) != ''.join(list(cols[c][m+1:min(len(cols[c]),(m+1)*2)])):
                break
        else:
            if (m+1)*100 != prevStar:
                # print('found m at row %d!'%m)
                return (m+1)*100
    return 0

def getAttempts(field):
    startTime = time()
    initField = [list(line) for line in field]
    allFields = []
    for i in range(len(field)):
        for j in range(len(field[i])):
            newField = deepcopy(initField)
            newField[i][j] = '.' if field[i][j] == '#' else '#'
            allFields.append([''.join(line) for line in newField])
    # print('getAttempts() took %d seconds'%(time()-startTime))
    return allFields

star1 = 0
star2 = 0

with open('day13.txt', 'r') as file:
    data = file.read().split('\n\n')
    # data = [line.split('\n')[0] for line in data if line]
#     data = """#.##..##.
# ..#.##.#.
# ##......#
# ##......#
# ..#.##.#.
# ..##..##.
# #.#.##.#.

# #...##..#
# #....#..#
# ..##..###
# #####.##.
# #####.##.
# ..##..###
# #....#..#""".split('\n\n')

for field in data:
    # try the mirror between all columns
    rows = field.split('\n')
    s1 = tryRows(rows)
    if not s1:
        # try the mirror between all rows
        cols = list(zip(*rows))
        s1 = tryCols(cols)
    star1 += s1
    
    # star2
    allRows = getAttempts(rows)
    for rows in allRows:
        # try the mirror between all columns
        s = tryRows(rows,s1)
        if not s:
            # try the mirror between all rows
            cols = list(zip(*rows))
            try:
                s = tryCols(cols,s1)
            except:
                import pdb; pdb.set_trace()
        if s:
            star2 += s
            break


print('star1: %s'%star1)
print('star2: %s'%star2)
