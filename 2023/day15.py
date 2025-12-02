def hash(myString):
    curVal = 0
    for c in myString:
        curVal += ord(c)
        curVal *= 17
        curVal %= 256
    return curVal

def printBoxes(boxes):
    for idx, box in enumerate(boxes):
        if len(box) > 0:
            lenses = ''
            for label in box:
                lenses += ' [%s %d]'%(label, box[label])
            print('Box %d:%s'%(idx, lenses))

star1 = 0
star2 = 0
boxes = [dict() for _ in range(256)]

with open('day15.txt', 'r') as file:
    data = file.readlines()
    data = [line.split('\n')[0] for line in data if line]
    data = ''.join(data)
    # data = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"

data = data.split(',')

for step in data:
    star1 += hash(step)

    label = ''.join([o for o in list(step) if not o in '-=' and o.isalpha()])

    if '-' in step:
        boxes[hash(label)].pop(label, None)
    elif '=' in step:
        boxes[hash(label)][label] = int(step[-1])
    else:
        assert(False)
    # printBoxes(boxes)
    # print('=====================')

for idx, box in enumerate(boxes):
    for jdx, lensVal in enumerate(box.values()):
        star2 += (idx + 1) * (jdx + 1) * lensVal

print('star1: %s'%star1)
print('star2: %s'%star2)
