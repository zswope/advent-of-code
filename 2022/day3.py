def getPriority(letter):
    priority = 0
    if letter.isupper():
        priority = ord(letter)-38
    elif letter.islower():
        priority = ord(letter)-96
    return priority

with open('day3.txt','r') as file:
    data = file.read().split('\n')
    data = [line for line in data if line]
    common = []
    for sack in data:
        firstpart, secondpart = sack[:len(sack)//2], sack[len(sack)//2:]
        common.append(''.join(set(firstpart).intersection(secondpart)))
    priority = 0
    for letter in common:
        priority += getPriority(letter)
    print('star 1: %d'%(priority))
    
    common2 = []
    for i in range(0,len(data),3):
        common2.append(''.join(set(''.join(set(data[i]).intersection(data[i+1]))).intersection(data[i+2])))
    priority2 = 0
    for letter in common2:
        priority2 += getPriority(letter)
    print('star 2: %d'%(priority2))