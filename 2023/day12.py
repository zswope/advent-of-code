from itertools import permutations

star1 = 0
star2 = 0
totalLayouts = 0

def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

def bruteForce(springs,numNeeded):
    fillSpots = find(springs,'?')
    intStr = '#'*numNeeded+'.'*(len(fillSpots)-numNeeded)
    # print(springs)
    # print(intStr)
    layouts = []
    for p in set(permutations(intStr)):
        for c,i in zip(p,fillSpots):
            springs = springs[:i]+c+springs[i+1:]
        layouts.append(springs)
    print('trying %d layouts for %s'%(len(layouts),springs))
    global totalLayouts
    totalLayouts += len(layouts)
    return layouts

def isValid(springs,key):
    curSpring = 0
    validLayout = True
    for i in range(len(springs)):
        if springs[i] == '#':
            curSpring += 1
        elif springs[i] == '.' and curSpring >0 :
            validLayout = validLayout and curSpring == key[0]
            key = key[1:]
            curSpring = 0
    if key:
        validLayout = validLayout and curSpring == key[0]
    return validLayout

with open('day12.txt','r') as file:
    data = file.read().split('\n')
    tmpdata = """
        ???.### 1,1,3
        .??..??...?##. 1,1,3
        ?#?#?#?#?#?#?#? 1,3,1,6
        ????.#...#... 4,1,1
        ????.######..#####. 1,6,5
        ?###???????? 3,2,1
    """
    if tmpdata:
        data = tmpdata.split('\n')
    data = [line.strip() for line in data if line.strip()]

# do computation here!
for dat in data:
    springs = dat.split(' ')[0]
    key = [int(x) for x in dat.split(' ')[1].split(',')]
    # print(springs)
    # print(key)
    # do some smart stuff to elminate a ton of options
    # kinda just gonna try shit until something works :shrug:
    print(springs.split('.'))
    
    neededSprings = sum(key) - springs.count('#')
    for layout in bruteForce(springs,neededSprings):
        # print(layout)
        if isValid(layout,key):
            star1 += 1

print('star1: %s'%star1)
print('star2: %s'%star2)
print('totalLayouts: %s'%totalLayouts)