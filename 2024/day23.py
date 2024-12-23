import networkx as nx
import matplotlib.pyplot as plt

star1 = 0
star2 = 0
import os
data = open(os.path.basename(__file__).split('.')[0]+'.txt','r').read()
data = [line.strip() for line in data.split('\n') if line.strip()]
data = [tuple(dat.split('-')) for dat in data]

# create graph of all connected computers
G = nx.Graph()
G.add_edges_from(data)

# find all cycles with a computer that starts with t
cycles = []
for cycle in nx.simple_cycles(G, length_bound=3):
    for comp in cycle:
        if comp[0] == 't':
            cycles.append(cycle)
            break

star1 = len(cycles)
star2 = ','.join(sorted(max(nx.find_cliques_recursive(G), key=len)))

print('star1:',star1)
print('star2:',star2)
