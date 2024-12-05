def moveCrates(count,fromS,toS,i):
    # print(stacks)
    # print('moving %d crates from %d to %d'%(count,fromS,toS))
    if i == 0: # one crate at a time
        stacks[toS-1] = stacks[toS-1] + list(reversed(stacks[fromS-1][-count:]))
    elif i == 1: # all crates at once
        stacks[toS-1] = stacks[toS-1] + stacks[fromS-1][-count:]
    for _ in range(count):
        stacks[fromS-1].pop()

with open('day5.txt','r') as file:
    data = file.read().split('\n\n')
    data = data[1].split('\n')
    data = [line for line in data if line]
    instructions = []
    for instruction in data:
        splitup = instruction.split(' ')
        instructions.append([int(i) for i in splitup if i.isnumeric()])
    for i in range(2):
        stacks = []
        stacks.append(['B','V','S','N','T','C','H','Q'])
        stacks.append(['W','D','B','G'])
        stacks.append(['F','W','R','T','S','Q','B'])
        stacks.append(['L','G','W','S','Z','J','D','N'])
        stacks.append(['M','P','D','V','F'])
        stacks.append(['F','W','J'])
        stacks.append(['L','N','Q','B','J','V'])
        stacks.append(['G','T','R','C','J','Q','S','N'])
        stacks.append(['J','S','Q','C','W','D','M'])
        star = []
        for ins in instructions:
            moveCrates(ins[0],ins[1],ins[2],i)
        for stack in stacks:
            star.append(stack[-1])
    
        print('star%d: '%(i+1)+ str(star))