star1 = 0
star2 = 0
import os
data = open(os.path.basename(__file__).split('.')[0]+'.txt','r').read()
# data = """
# """
data = [line.strip() for line in data.split('\n') if line.strip()]

# do computation here!
for dat in data:
    print(dat)

print('star1: %s'%star1)
print('star2: %s'%star2)