from collections import defaultdict

star1 = 0
star2 = 0
cardVal = {
    '2':'02',
    '3':'03',
    '4':'04',
    '5':'05',
    '6':'06',
    '7':'07',
    '8':'08',
    '9':'09',
    'T':'10',
    'J':'11',
    'Q':'12',
    'K':'13',
    'A':'14',
}

def getHandType(nums):
    if 5 in nums:
        return 7
    elif 4 in nums:
        return 6
    elif 3 in nums and 2 in nums:
        return 5
    elif 3 in nums:
        return 4
    elif nums.count(2) == 2:
        return 3
    elif 2 in nums:
        return 2
    else:
        return 1

with open('day7.txt','r') as file:
    data = file.read().split('\n')
#     tmpdata = """32T3K 765
# T55J5 684
# KK677 28
# KTJJT 220
# QQQJA 483"""
#     if tmpdata:
#         data = tmpdata.split('\n')
    data = [line for line in data if line]
    
    # do computation here!
    star1HandRanks = []
    star2HandRanks = []
    for dat in data:
        cards = defaultdict(lambda: 0)
        handVal = ''
        for card in dat.split(' ')[0]:
            cards[card] += 1
            handVal += cardVal[card]

        handType = str(getHandType(list(cards.values())))            
        star1HandRanks.append((int(handType + handVal),int(dat.split(' ')[1])))
        
        bestHandType = str(max(getHandType()))
        
        # print(dat)
    
    star1HandRanks.sort()
    star2HandRanks.sort()
    for i in range(len(star1HandRanks)):
        star1 += (i+1)*star1HandRanks[i][1]
        star2 += (i+1)*star2HandRanks[i][1]

print('star1: %s'%star1)
print('star2: %s'%star2)