class Gate():
    def __init__(self, inputs):
        self.type = inputs[1]
        self.I = [inputs[0],inputs[2]]
        self.O = inputs[-1]

    def canRun(self, wires):
        return self.I[0] in wires and self.I[1] in wires

    def run(self, wires):
        if self.type == 'AND':
            return wires[self.I[0]] and wires[self.I[1]]
        if self.type == 'OR':
            return wires[self.I[0]] or wires[self.I[1]]
        if self.type == 'XOR':
            return wires[self.I[0]] ^ wires[self.I[1]]

star1 = 0
star2 = 0
import os
data = open(os.path.basename(__file__).split('.')[0]+'.txt','r').read()
data = [line.strip() for line in data.split('\n\n') if line.strip()]
wires = {dat.split(': ')[0]:int(dat.split(': ')[1]) for dat in data[0].split('\n')}
gates = [Gate(dat.split(' ')) for dat in data[1].split('\n')]
largestZ = int(sorted([dat.split(' ')[-1] for dat in data[1].split('\n') if dat.split(' ')[-1][0] == 'z'])[-1][1:])

# process logic
while any('z%02d'%(i) not in wires for i in range(largestZ+1)):
    for gate in gates:
        if gate.O not in wires and gate.canRun(wires):
            wires[gate.O] = gate.run(wires)

star1 = int(''.join(str(wires['z%02d'%i]) for i in range(largestZ,-1,-1)), 2)

# repeat entire process but with swapped gates to verify hand-found solution

data = open(os.path.basename(__file__).split('.')[0]+'.txt','r').read()
data = [line.strip() for line in data.split('\n\n') if line.strip()]
wires = {dat.split(': ')[0]:int(dat.split(': ')[1]) for dat in data[0].split('\n')}
gates = [Gate(dat.split(' ')) for dat in data[1].split('\n')]
largestX = int(sorted([dat.split(':')[0] for dat in wires if dat.split(':')[0][0] == 'x'])[-1][1:])
largestY = int(sorted([dat.split(':')[0] for dat in wires if dat.split(':')[0][0] == 'y'])[-1][1:])
largestZ = int(sorted([dat.split(' ')[-1] for dat in data[1].split('\n') if dat.split(' ')[-1][0] == 'z'])[-1][1:])

# perform swaps
toSwap = {
    'z07':'kbg',
    'kfm':'z20',
    'hnv':'z28',
    'tqr':'hth',
    'kbg':'z07',
    'z20':'kfm',
    'z28':'hnv',
    'hth':'tqr',
}
for gate in gates:
    if gate.O in toSwap:
        gate.O = toSwap[gate.O]

# process logic
while any('z%02d'%(i) not in wires for i in range(largestZ+1)):
    for gate in gates:
        if gate.O not in wires and gate.canRun(wires):
            wires[gate.O] = gate.run(wires)

a = int(''.join(str(wires['x%02d'%i]) for i in range(largestX,-1,-1)), 2)
b = int(''.join(str(wires['y%02d'%i]) for i in range(largestY,-1,-1)), 2)
c = int(''.join(str(wires['z%02d'%i]) for i in range(largestZ,-1,-1)), 2)
print('%d + %d = %d'%(a,b,c))

star2 = ','.join(sorted(toSwap.keys()))

print('star1:',star1)
print('star2:',star2)
