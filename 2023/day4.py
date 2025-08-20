star1 = 0
star2 = 0

with open('day4.txt', 'r') as file:
    data = file.readlines()
    data = [line.split('\n')[0] for line in data if line]
#     data = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11""".split('\n')
    

    numCards = {}
    for i in range(1,len(data)+1):
        numCards[i]=1
    for i in range(1,len(data)+1):
        nums = data[i-1].split(':')[1]
        winningNums = set(int(n) for n in (nums.split('|')[0].strip()).split(' ') if n)
        myNums = set(int(n) for n in (nums.split('|')[1].strip()).split(' ') if n)

        matches = winningNums.intersection(myNums)
        
        #star1
        points = 2**(len(matches)-1)
        # sets 0.5 back to 0
        if points < 1: points = 0
        star1 += points
        
        #star2
        for j in range(1,len(matches)+1):
            numCards[i+j] += numCards[i]

star2 = sum(numCards.values())
print('star1: %s'%star1)
print('star2: %s'%star2)