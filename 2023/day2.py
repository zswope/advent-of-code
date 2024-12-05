star1 = 0
star2 = 0

def getMaxCubes(rounds):
    green = 0
    blue = 0
    red = 0
    for round in rounds:
        marbles = [m.strip() for m in round.split(',')]
        for color in marbles:
            numColor = int(color.split(' ')[0])
            if 'green' in color:
                green = max(green, numColor)
            elif 'blue' in color:
                blue = max(blue, numColor)
            elif 'red' in color:
                red = max(red, numColor)
            else:
                raise ValueError('invalid color: %s'%color)
    return (green,blue,red)
        
with open('day2.txt','r') as file:
    data = file.read().split('\n')
    data = [line for line in data if line]
    
    # do computation here!
    for dat in data:
        id = int(dat.split(' ')[1][:-1])
        rounds = ''.join(dat.split(':')[1]).strip().split(';')
        green, blue, red = getMaxCubes(rounds)

        if red <= 12 and green <= 13 and blue <= 14:
            star1 += id
        
        star2 += green * blue * red
        
print('star1: %s'%star1)
print('star2: %s'%star2)