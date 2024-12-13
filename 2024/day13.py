import numpy as np

star1 = 0
star2 = 0
import os
data = open(os.path.basename(__file__).split('.')[0]+'.txt','r').read()
# data = """
# Button A: X+94, Y+34
# Button B: X+22, Y+67
# Prize: X=8400, Y=5400

# Button A: X+26, Y+66
# Button B: X+67, Y+21
# Prize: X=12748, Y=12176

# Button A: X+17, Y+86
# Button B: X+84, Y+37
# Prize: X=7870, Y=6450

# Button A: X+69, Y+23
# Button B: X+27, Y+71
# Prize: X=18641, Y=10279
# """
data = [line.strip().split('\n') for line in data.split('\n\n') if line.strip()]

# do computation here!
for dat in data:
    # extract vars
    aX = int(dat[0].split(',')[0].split('+')[-1])
    aY = int(dat[0].split('+')[-1])
    bX = int(dat[1].split(',')[0].split('+')[-1])
    bY = int(dat[1].split('+')[-1])
    pX = int(dat[2].split(',')[0].split('=')[-1])
    pY = int(dat[2].split('=')[-1])

    # create system of equations
    A = np.array([[aX,bX],[aY,bY]])
    b = np.array([pX,pY])
    solution = np.linalg.solve(A, b)
    a = round(solution[0])
    b = round(solution[1])
    # make sure this is a solution
    if aX*a+bX*b==pX and aY*a+bY*b==pY:
        star1 += a*3+b

    # update prize values and run again
    pX += 10000000000000
    pY += 10000000000000
    b = np.array([pX,pY])
    solution = np.linalg.solve(A, b)
    a = round(solution[0])
    b = round(solution[1])
    # make sure this is a solution
    if aX*a+bX*b==pX and aY*a+bY*b==pY:
        star2 += a*3+b

print('star1: %s'%star1)
print('star2: %s'%star2)
