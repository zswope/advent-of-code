from collections import defaultdict, deque

def topologicalSort(elements, rules):
    # Filter rules to only include those where both elements are present in the list
    valid = [(a, b) for a, b in rules if a in elements and b in elements]

    # Create a graph and in-degree dictionary
    graph = defaultdict(list)
    inDegree = {element: 0 for element in elements}
    
    # Build the graph and in-degree map using valid rules
    for a, b in valid:
        graph[a].append(b)
        inDegree[b] += 1

    # Initialize a queue with nodes that have no incoming edges
    queue = deque([node for node in elements if inDegree[node] == 0])

    # Perform topological sort
    sortedList = []
    while queue:
        node = queue.popleft()
        sortedList.append(node)
        
        for neighbor in graph[node]:
            inDegree[neighbor] -= 1
            if inDegree[neighbor] == 0:
                queue.append(neighbor)

    # Check if we were able to sort all elements
    if len(sortedList) != len(elements):
        raise ValueError("Partial cycle detected with the provided elements!")

    return sortedList

def checkOrder(elements, rules):
    # Create a mapping from element to its index in the list
    indexMap = {element: i for i, element in enumerate(elements)}

    # Check if each rule (A, B) is satisfied
    for a, b in rules:
        if a in indexMap and b in indexMap:
            if indexMap[a] > indexMap[b]:
                return False  # A appears after B, rule is violated

    return True  # All rules are satisfied

star1 = 0
star2 = 0
import os
with open(os.path.basename(__file__).split('.')[0]+'.txt','r') as file:
    data = file.readlines()
#     data = """47|53
# 97|13
# 97|61
# 97|47
# 75|29
# 61|13
# 75|53
# 29|13
# 97|29
# 53|29
# 61|53
# 97|53
# 61|29
# 47|13
# 75|47
# 97|75
# 47|61
# 75|61
# 47|29
# 75|13
# 53|13

# 75,47,61,53,29
# 97,61,53,29,13
# 75,29,13
# 75,97,47,61,53
# 61,13,29
# 97,13,75,29,47
# """.split('\n')
    data = [line.strip() for line in data if line.strip()]

# sort data to rules and updates
rules = []
updates = []
for dat in data:
    if '|' in dat:
        rules.append(tuple(map(int, dat.split('|'))))
    elif ',' in dat:
        updates.append(list(map(int, dat.split(','))))

# process updates
for update in updates:
    if checkOrder(update, rules):
        star1 += update[len(update)//2]
    else:
        star2 += topologicalSort(update, rules)[len(update)//2]

print('star1: %s'%star1)
print('star2: %s'%star2)