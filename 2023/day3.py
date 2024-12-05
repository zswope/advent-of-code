import re

star1 = 0
star2 = 0

def adjacentToSymbol(index, length, symbols):
    return any(symbol in range(index-1,index+length+1) for symbol in symbols)

def adjacentToTwo(index,nums):
    totalAdjacent = 0
    product = 1
    for num in nums:
        if adjacentToSymbol(num[1],len(num[0]),[index]):
            totalAdjacent += 1
            # print('num %s is adjacent to * at index %d'%(num,index))
            product *= int(num[0])
    return (totalAdjacent == 2, product)
            


with open('day3.txt','r') as file:
    data = file.read().split('\n')
#     data = """
# 467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..""".split('\n')
    data = [line for line in data if line]
    
    # do computation here!
    # data = data[:4]
    # print(data)
    for i in range(len(data)):
        result = [(match.group(), match.start()) for match in re.finditer(r'\d+|\d+\.\d+', data[i])]
        symbols = []
        if i > 0:
            symbols += [match.start() for match in re.finditer(r'[^0-9.]', data[i-1])]
        symbols += [match.start() for match in re.finditer(r'[^0-9.]', data[i])]
        if i < len(data)-1:
            symbols += [match.start() for match in re.finditer(r'[^0-9.]', data[i+1])]
        # print(result)
        # print(symbols)
        for res in result:
            if adjacentToSymbol(res[1],len(res[0]),symbols):
                # print('%s is adjacent to a symbol'%res[0])
                star1+=int(res[0])
        
        gears = [match.start() for match in re.finditer(r'\*', data[i])]
        results = []
        if i > 0:
            results += [(match.group(), match.start()) for match in re.finditer(r'\d+|\d+\.\d+', data[i-1])]
        results += [(match.group(), match.start()) for match in re.finditer(r'\d+|\d+\.\d+', data[i])]
        if i < len(data)-1:
            results += [(match.group(), match.start()) for match in re.finditer(r'\d+|\d+\.\d+', data[i+1])]
            
        for gear in gears:
            res,product = adjacentToTwo(gear,results)
            if res:
                star2+= product
        

print('star1: %s'%star1)
print('star2: %s'%star2)