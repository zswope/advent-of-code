star1FindList = {
    '1':1,
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
    '0':0,
}
star2FindList={
    '1':1,
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
    '0':0,
    'one':1,
    'two':2,
    'three':3,
    'four':4,
    'five':5,
    'six':6,
    'seven':7,
    'eight':8,
    'nine':9,
    'zero':0,
}

with open('day1.txt','r') as file:
    data = file.read().split('\n')
    data = [line for line in data if line]
    
    star1Sum = 0
    for string in data:
        first = 'na'
        firstIndex = len(string)*2
        last = 'na'
        lastIndex = -1
        for f in star1FindList:
            idx = string.find(f)
            if idx != -1 and idx < firstIndex:
                firstIndex = idx
                first = f
            idx = string.rfind(f)
            if idx > lastIndex:
                lastIndex = idx
                last = f
        star1Sum += int(str(star1FindList[first]) + str(star1FindList[last]))
    star2Sum = 0
    for string in data:
        first = 'na'
        firstIndex = len(string)*2
        last = 'na'
        lastIndex = -1
        for f in star2FindList:
            idx = string.find(f)
            if idx != -1 and idx < firstIndex:
                firstIndex = idx
                first = f
            idx = string.rfind(f)
            if idx > lastIndex:
                lastIndex = idx
                last = f
        star2Sum += int(str(star2FindList[first]) + str(star2FindList[last]))
    
print('star1: %s'%(star1Sum))
print('star2: %s'%(star2Sum))