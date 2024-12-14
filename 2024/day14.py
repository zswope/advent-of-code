from collections import Counter
import png

def add(x,y):
    return (x[0]+y[0],x[1]+y[1])

def printMap(width,height,positions):
    for j in range(height):
        for i in range(width):
            if (i,j) in positions:
                print(positions[(i,j)],end='')
            else:
                print('.',end='')
        print('')

def mapPng(width,height,positions,filename):
    img = []
    for y in range(height):
        row = []
        for x in range(width):
            if (x,y) in positions:
                row.append(255)
            else:
                row.append(0)
        img.append(row)
    
    writer = png.Writer(width=width,height=height,bitdepth=8,greyscale=True)
    with open(filename, 'wb') as f:
        writer.write(f, img)

class Robot:
    def __init__(self,pX,pY,vX,vY,dims):
        self.pos = (pX,pY)
        self.vel = (vX,vY)
        self.dims = dims
    
    def move(self):
        self.pos = add(self.pos,self.vel)
        if self.pos[0] < 0:
            self.pos = (self.dims[0]+self.pos[0],self.pos[1])
        if self.pos[0] >= self.dims[0]:
            self.pos = (self.pos[0]-self.dims[0],self.pos[1])
        if self.pos[1] < 0:
            self.pos = (self.pos[0],self.dims[1]+self.pos[1])
        if self.pos[1] >= self.dims[1]:
            self.pos = (self.pos[0],self.pos[1]-self.dims[1])
    
    def getQuadrant(self):
        if self.pos[0] < self.dims[0]//2:
            if self.pos[1] < self.dims[1]//2:
                return 1
            if self.pos[1] > self.dims[1]//2:
                return 4
        if self.pos[0] > self.dims[0]//2:
            if self.pos[1] < self.dims[1]//2:
                return 2
            if self.pos[1] > self.dims[1]//2:
                return 3
        return None

star1 = 1
star2 = 6398
time = 6397
import os
data = open(os.path.basename(__file__).split('.')[0]+'.txt','r').read()
# data = """
# p=0,4 v=3,-3
# p=6,3 v=-1,-3
# p=10,3 v=-1,2
# p=2,0 v=2,-1
# p=0,0 v=1,3
# p=3,0 v=-2,-2
# p=7,6 v=-1,-3
# p=3,0 v=-1,-2
# p=9,3 v=2,3
# p=7,3 v=-1,2
# p=2,4 v=2,-3
# p=9,5 v=-3,-3
# """
data = [line.strip() for line in data.split('\n') if line.strip()]

width = 101
height = 103
robots = []
# create all robot objects
for dat in data:
    posX = int(dat.split(' ')[0].split(',')[0].split('=')[-1])
    posY = int(dat.split(' ')[0].split(',')[-1])
    velX = int(dat.split(' ')[1].split(',')[0].split('=')[-1])
    velY = int(dat.split(' ')[1].split(',')[-1])
    robots.append(Robot(posX,posY,velX,velY,(width,height)))
# print('Initial state:')
# printMap(width,height,Counter([r.pos for r in robots]))
for s in range(1,time+1):
    for r in robots:
        r.move()
    if s == 100:
        # count robots in each quadrant
        quads = Counter([r.getQuadrant() for r in robots])
        for k,v in quads.items():
            if k is not None:
                star1 *= v
    
    # create picture
    mapPng(width,height,[r.pos for r in robots],'images/frame%d.png'%s)
    # print('After %d seconds:'%(s))
    # printMap(width,height,Counter([r.pos for r in robots]))
    # input()


print('star1: %s'%star1)
print('star2: %s'%star2)
