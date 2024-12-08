def mul(curVal, nums):
    global testValue
    if len(nums) == 0:
        return curVal == testValue
    
    curVal *= nums[0]
    return mul(curVal, nums[1:]) or add(curVal, nums[1:]) or concat(curVal, nums[1:])

def add(curVal, nums):
    global testValue
    if len(nums) == 0:
        return curVal == testValue
    
    curVal += nums[0]
    return mul(curVal, nums[1:]) or add(curVal, nums[1:]) or concat(curVal, nums[1:])

def concat(curVal, nums):
    global testValue
    if len(nums) == 0:
        return curVal == testValue
    
    curVal = int(str(curVal) + str(nums[0]))
    return mul(curVal, nums[1:]) or add(curVal, nums[1:]) or concat(curVal, nums[1:])

star1 = 0
star2 = 0
import os
with open(os.path.basename(__file__).split('.')[0]+'.txt','r') as file:
    data = file.readlines()
#     data = """190: 10 19
# 3267: 81 40 27
# 83: 17 5
# 156: 15 6
# 7290: 6 8 6 15
# 161011: 16 10 13
# 192: 17 8 14
# 21037: 9 7 18 13
# 292: 11 6 16 20
# """.split('\n')
    data = [line.strip() for line in data if line.strip()]

# do computation here!
for dat in data:
    global testValue
    testValue = int(dat.split(':')[0])
    nums = list(map(int, dat.split(': ')[1].split(' ')))

    if mul(nums[0],nums[1:]) or add(nums[0],nums[1:]) or concat(nums[0], nums[1:]):
        star1 += testValue

print('star1: %s'%star1)
print('star2: %s'%star2)