from aocInput import dataInput
import math
data = dataInput()
# data =\
# """L68
# L30
# R48
# L5
# R60
# L55
# L1
# L99
# R14
# L82""".split('\n')

star1 = 0
star2 = 0

data = [int(s[1:])*(1 if s[0] == 'R' else -1) for s in data]

curPos = 50
for turn in data:
    curPos += turn
    curPos %= 100
    
    if curPos == 0:
        star1 += 1
        star2 += 1
    
    # handle multiple turns
    star2 += abs(turn)//100

    # already handled the case of landing at 0 above
    if curPos != 0:
        # if the turn was to the right and the turn was further than where we're at, we obviously passed 0
        star2 += turn > 0 and turn%100 > curPos
        # if the turn was to the left and the turn was further than the "negativeness (100-cur)" we're at, we obviously passed 0
        star2 += turn < 0 and abs(turn)%100 > 100-curPos

print('star1:',star1)
print('star2:',star2)
