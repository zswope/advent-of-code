def getDirSize(startIndex,dirName):
    start = data.index('$ cd '+dirName,startIndex)+2
    while (start-2) in claimed:
        startIndex = start-1
        start = data.index('$ cd '+dirName,startIndex)+2
    claimed.append(start-2)
    end = [idx for idx, s in enumerate(data[start:]) if '$ cd' in s][0]+start
    size = 0
    for item in data[start:end]:
        if item[:3] == 'dir':
            size += getDirSize(start,item.split(' ')[1])
        else:
            size += int(item.split(' ')[0])
    allDirs.append((dirName,size))
    return size

with open('day7.txt','r') as file:
    claimed = []
    data = file.read().split('\n')
    data = [line for line in data if line]
    allDirs = []
    size = getDirSize(0,'/')
    allDirs = sorted(allDirs, key = lambda x: x[1])
    neededSize = allDirs[-1][1]-40000000
    star1 = 0
    for tup in allDirs:
        if tup[1] <= 100000:
            star1 += tup[1]
    star2 = 0
    for tup in allDirs:
        if tup[1] >= neededSize:
            star2 = tup[1]
            break
    print(allDirs)
    print('star1: '+str(star1))
    print('star2: '+str(star2))