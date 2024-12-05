with open('day1.txt','r') as file:
    data = file.read().split("\n\n")
    elves = []
    for elf in data:
        elves.append(elf.split("\n"))
    cals1 = 0
    cals2 = 0
    cals3 = 0
    for elf in elves:
        elf = [int(i) for i in elf if not i == '']
        curCals = sum(elf)
        if curCals > cals3:
            if cals3 > cals2:
                if cals2 > cals1:
                    cals1 = cals2
                cals2 = cals3
            cals3 = curCals
        elif curCals > cals2:
            if cals2 > cals1:
                cals1 = cals2
            cals2 = curCals
        elif curCals > cals1:
            cals1 = curCals
    print('star 1: %d'%cals3)
    print('star 2: %d'%(cals1 + cals2 + cals3))