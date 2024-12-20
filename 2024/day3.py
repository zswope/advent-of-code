import re

star1 = 0
star2 = 0
import os
with open(os.path.basename(__file__).split('.')[0]+'.txt', 'r') as file:
    data = file.readlines()
#     data = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
# """.split('\n')
    data = [line.split('\n')[0] for line in data if line]
    data = ''.join(data)

pattern = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don\'t\(\)')
matches = pattern.finditer(data)

enabled = True
for match in matches:
    if match.group() == 'do()':
        enabled = True
    elif match.group() == 'don\'t()':
        enabled = False
    else:
        n1, n2 = map(int, match.groups())
        star1 += (n1*n2)
        if enabled:
            star2 += (n1*n2)

print('star1: %s'%star1)
print('star2: %s'%star2)