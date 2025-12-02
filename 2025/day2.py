from aocInput import dataInput
data = dataInput()
# data =\
# """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,\
# 1698522-1698528,446443-446449,38593856-38593862,565653-565659,\
# 824824821-824824827,2121212118-2121212124""".split('\n')
data = data[0].split(',')

star1 = 0
star2 = 0
invalidSet = set()

for r in data:
    rStart = int(r.split('-')[0])
    rEnd = int(r.split('-')[1])
    for i in range(rStart,rEnd+1):
        iStr = str(i)
        iLen = len(iStr) # could use log to get num digits instead
        if iLen%2 == 0 and iStr[:iLen//2] == iStr[iLen//2:]:
            # print(f'Found that {i} in range {r} is invalid!')
            star1 += i
        
        for j in range(1,iLen):
            if i not in invalidSet and iStr == iStr[:j]*(iLen//j):
                # print(f'Found that {i} in range {r} is invalid due to cycle of {iStr[:j]}*{iLen//j}!')
                invalidSet.add(i)
                star2 += i

# import pdb; pdb.set_trace()

print('star1:',star1)
print('star2:',star2)
