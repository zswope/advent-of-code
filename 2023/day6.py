star1 = 1
star2 = 1

with open('day6.txt', 'r') as file:
    data = file.readlines()
    data = [line.split('\n')[0] for line in data if line.split('\n')[0]]
#     data = """Time:      7  15   30
# Distance:  9  40  200""".split('\n')

    for dat in data:
        # load variables
        match dat.split(':')[0]:
            case 'Time':
                times = [int(t) for t in dat.split(':')[1].split(' ') if t]
            case 'Distance':
                distances = [int(d) for d in dat.split(':')[1].split(' ') if d]
    
    for t,d in zip(times,distances):
        curTime = t//2
        numOver = 0
        while abs(curTime-t)*curTime > d:
            numOver += 1
            curTime -= 1
        star1 *= (numOver*2-int(t%2==0))

    t = int(''.join(str(t) for t in times))
    d = int(''.join(str(d) for d in distances))
    curTime = t//2
    numOver = 0
    while abs(curTime-t)*curTime > d:
        numOver += 1
        curTime -= 1
    star2 *= (numOver*2-int(t%2==0))


print('star1: %s'%star1)
print('star2: %s'%star2)