star1 = 0
star2 = 0

with open('day9.txt','r') as file:
    data = file.read().split('\n')
#     tmpdata = """0 3 6 9 12 15
# 1 3 6 10 15 21
# 10 13 16 21 30 45"""
#     if tmpdata:
#         data = tmpdata.split('\n')
    data = [line for line in data if line]
    
# do computation here!
for dat in data:
    sequences = []
    sequences.append([int(x) for x in dat.split(' ')])
    while not all(num == 0 for num in sequences[-1]):
        sequences.append([])
        for i in range(len(sequences[-2])-1):
            sequences[-1].append(sequences[-2][i+1]-sequences[-2][i])

    sequences.reverse()
    for i in range(1,len(sequences)):
        sequences[i].append(sequences[i][-1]+sequences[i-1][-1])
        sequences[i].insert(0,sequences[i][0]-sequences[i-1][0])
    star1 += sequences[-1][-1]
    star2 += sequences[-1][0]

print('star1: %s'%star1)
print('star2: %s'%star2)
