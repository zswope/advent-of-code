def drawCRT(crt):
    print(''.join(crt[:40]))
    print(''.join(crt[40:80]))
    print(''.join(crt[80:120]))
    print(''.join(crt[120:160]))
    print(''.join(crt[160:200]))
    print(''.join(crt[200:240]))
    
def addCheck(cycle,x,star1):
    if cycle % 20 == 0 and cycle % 40 != 0:
        star1 += x*cycle
    return star1

def crtPixel(cycle,x):
    if (cycle-1)%40 in list(range(x-1,x+2)):
        crt[cycle-1] = '#'
    else:
        # print('crt at %d, sprite at [%d,%d,%d]'%(cycle-1,x-1,x,x+1))
        crt[cycle-1] = '.'

with open('day10.txt','r') as file:
    data = file.read().split('\n')
    data = [line for line in data if line]
    
    star1 = 0
    cycle = 0
    x = 1
    crt = [0]*240
    for ins in data:
        if ins.split(' ')[0] == 'noop':
            cycle += 1
            crtPixel(cycle,x)
            star1 = addCheck(cycle,x,star1)
            continue
        cycle += 1
        crtPixel(cycle,x)
        star1 = addCheck(cycle,x,star1)
        cycle += 1
        crtPixel(cycle,x)
        star1 = addCheck(cycle,x,star1)
        x += int(ins.split(' ')[1])
    drawCRT(crt)
    
    print('star1: %d'%star1)