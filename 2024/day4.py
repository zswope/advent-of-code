import numpy as np

star1 = 0
star2 = 0
import os
with open(os.path.basename(__file__).split('.')[0]+'.txt', 'r') as file:
    data = file.readlines()
#     data = """MMMSXXMASM
# MSAMXMSMSA
# AMXSXMAAMM
# MSAMASMSMX
# XMASAMXAMM
# XXAMMXXAMA
# SMSMSASXSS
# SAXAMASAAA
# MAMMMXMMMM
# MXMXAXMASX
# """.split('\n')
    data = np.array([list(line.split('\n')[0]) for line in data if line])

for row in range(len(data)):
    for col in range(len(data[0])):
        # for star2, data[row][col] must be A
        if data[row,col] == 'A':
            if row == 0 or col == 0 or row == len(data)-1 or col == len(data[0])-1:
                pass
            else:
                cross = 0
                if data[row-1,col-1] == 'M' and data[row+1,col+1] == 'S':
                    cross += 1
                elif data[row-1,col-1] == 'S' and data[row+1,col+1] == 'M':
                    cross += 1
                if data[row-1,col+1] == 'M' and data[row+1,col-1] == 'S':
                    cross += 1
                elif data[row-1,col+1] == 'S' and data[row+1,col-1] == 'M':
                    cross += 1
                if cross == 2:
                    star2 += 1

        # for star1, data[row][col] must be X
        if data[row,col] != 'X':
            continue
    
        # ....
        # XMAS
        # ....
        # ....
        try:
            if ''.join(data[row,col:col+4]) == 'XMAS': star1 += 1
        except IndexError: pass
        # ....
        # SAMX
        # ....
        # ....
        try:
            if ''.join(data[row,col-3:col+1]) == 'SAMX': star1 += 1
        except IndexError: pass
        # .X..
        # .M..
        # .A..
        # .S..
        try:
            if ''.join(data[row:row+4,col]) == 'XMAS': star1 += 1
        except IndexError: pass
        # .S..
        # .A..
        # .M..
        # .X..
        try:
            if ''.join(data[row-3:row+1,col]) == 'SAMX': star1 += 1
        except IndexError: pass
        # X...
        # .M..
        # ..A.
        # ...S
        try:
            if ''.join([data[row+t,col+t] for t in range(4)]) == 'XMAS': star1 += 1
        except IndexError: pass
        # S...
        # .A..
        # ..M.
        # ...X
        try:
            if row - 3 < 0 or col - 3 < 0:
                raise IndexError
            if ''.join([data[row-t,col-t] for t in range(4)]) == 'XMAS': star1 += 1
        except IndexError: pass
        # ...X
        # ..M.
        # .A..
        # S...
        try:
            if col - 3 < 0:
                raise IndexError
            if ''.join([data[row+t,col-t] for t in range(4)]) == 'XMAS': star1 += 1
        except IndexError: pass
        # ...S
        # ..A.
        # .M..
        # X...
        try:
            if row - 3 < 0:
                raise IndexError
            if ''.join([data[row-t,col+t] for t in range(4)]) == 'XMAS': star1 += 1
        except IndexError: pass

print('star1: %d'%star1)
print('star2: %d'%star2)