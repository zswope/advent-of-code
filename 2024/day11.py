from collections import Counter

star1 = 0
star2 = 0
blinks = 75
import os
data = open(os.path.basename(__file__).split('.')[0]+'.txt', 'r').readlines()
# data = """125 17
# """.split('\n')
data = list(map(int,data[0].strip().split(' ')))
counter = Counter()
counter.update(data)
for blink in range(1,blinks+1):
    print('processing blink %d'%blink)
    nextBlink = Counter()
    for num,instances in counter.items():
        intLength = len(str(num))
        # If 0, replaced by 1.
        if num == 0:
            nextBlink[1] += instances
        # If even number of digits, it is split into two stones.
        elif intLength % 2 == 0:
            halfLen = intLength // 2
            nextBlink[num // (10 ** halfLen)] += instances
            nextBlink[num % (10 ** halfLen)] += instances
        # If none of the other rules apply, multiplied by 2024.
        else:
            nextBlink[num * 2024] += instances
    counter = nextBlink

    if blink == 25:
        star1 = sum(counter.values())
        print('star1: %s'%star1)

star2 = sum(counter.values())
print('star2: %s'%star2)
