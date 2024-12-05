from collections import Counter

star1 = 0
star2 = 0
import os
with open(os.path.basename(__file__).split('.')[0]+'.txt','r') as file:
    data = file.read().split('\n')
#     tmpdata = """3   4
# 4   3
# 2   5
# 1   3
# 3   9
# 3   3"""
#     if tmpdata:
#         data = tmpdata.split('\n')
    data = [line.strip() for line in data if line.strip()]
    
# do computation here!
left = []
right = []
for dat in data:
    left.append(int(dat.split()[0]))
    right.append(int(dat.split()[1]))

left.sort()
right.sort()
    
star1 = sum([abs(int(l)-int(r)) for l,r in zip(left,right)])

rightFreq = Counter(right)

star2 = sum([l*rightFreq[l] for l in left])

print('star1: %s'%star1)
print('star2: %s'%star2)