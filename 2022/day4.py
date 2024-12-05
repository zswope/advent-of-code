with open('day4.txt','r') as file:
    data = file.read().split('\n')
    data = [line for line in data if line]
    count1 = 0
    count2 = 0
    for pair in data:
        elves = pair.split(',')
        elf1 = elves[0].split('-')
        elf2 = elves[1].split('-')
        elf11 = int(elf1[0])
        elf12 = int(elf1[1])
        elf21 = int(elf2[0])
        elf22 = int(elf2[1])
        if elf11 >= elf21 and elf12 <= elf22:
            count1 += 1
        elif elf21 >= elf11 and elf22 <= elf12:
            count1 += 1
        if elf11 <= elf21 and elf12 >= elf21:
            count2 += 1
        elif elf21 <= elf11 and elf22 >= elf11:
            count2 += 1
    print(count1)
    print(count2)