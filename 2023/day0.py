star1 = 0
star2 = 0

with open('day0.txt','r') as file:
    data = file.read().split('\n')
    tmpdata = """"""
    if tmpdata:
        data = tmpdata.split('\n')
    data = [line.strip() for line in data if line.strip()]
    
# do computation here!
for dat in data:
    print(dat)

print('star1: %s'%star1)
print('star2: %s'%star2)