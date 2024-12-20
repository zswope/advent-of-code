from copy import deepcopy


def runProg(prog,registers):
    # initialize for operation
    output = []
    regA = registers['A']
    regB = registers['B']
    regC = registers['C']

    def getComboOperand(operand):
        match operand:
            case operand if operand < 4:
                return operand
            case 4:
                return regA
            case 5:
                return regB
            case 6:
                return regC
            case 7:
                raise IndexError('Combo operand 7 is reserved!')

    curPtr = 0
    while curPtr < len(prog):
        opcode = prog[curPtr]
        operand = prog[curPtr + 1]

        if opcode == 0:   # adv
            regA = regA // (2 ** getComboOperand(operand))
        elif opcode == 1: # bxl
            regB = regB ^ operand
        elif opcode == 2: # bst
            regB = getComboOperand(operand) % 8
        elif opcode == 3: # jnz
            if regA:
                curPtr = operand
                continue
        elif opcode == 4: # bxc
            regB = regB ^ regC
        elif opcode == 5: # out
            output.append(getComboOperand(operand) % 8)
        elif opcode == 6: # bdv
            regB = int(regA / (2 ** getComboOperand(operand)))
        elif opcode == 7: # cdv
            regC = int(regA / (2 ** getComboOperand(operand)))

        curPtr += 2
    return output

star1 = 0
star2 = 0
import os
data = open(os.path.basename(__file__).split('.')[0]+'.txt', 'r').read()
# data = """
# Register A: 729
# Register B: 0
# Register C: 0

# Program: 0,1,5,4,3,0
# """
data = [line.strip().split('\n') for line in data.split('\n\n') if line.strip()]

# extract data
registers = {k[-1]:int(v) for k,v in [reg.split(': ') for reg in data[0]]}
prog = list(map(int,data[1][0].split(': ')[-1].split(',')))

# run program for standard output
star1 = ','.join(list(map(str,runProg(prog,registers))))

print('star1:',star1)

# recreate CPU instructions specified by program to reverse loop
# (probably) specific to input!
def runIter(regA):
    regB = regA % 8
    regB = regB ^ 2
    regC = regA // (2**regB)
    regB = regB ^ regC
    regB = regB ^ 7
    return regB % 8

nextA = [0] # start with termination condition
for out in reversed(prog):
    curA = deepcopy(nextA)
    nextA = []
    for thisA in curA:
        for i in range(8):
            if runIter(thisA+i) == out:
                # each loop, A reduces by a factor of 8
                nextA.append((thisA+i)*8)

star2 = min(nextA)//8

# verify value for funsies :)
registers['A'] = star2
assert runProg(prog,registers) == prog

print('star2: %s'%star2)
