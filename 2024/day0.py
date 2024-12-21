star1 = 0
star2 = 0
import os
data = open(os.path.basename(__file__).split('.')[0]+'.txt','r').read()
# data = """
# """
data = [line.strip() for line in data.split('\n') if line.strip()]



print('star1:',star1)
print('star2:',star2)
