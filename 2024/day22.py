from collections import defaultdict

# @cache - do not need to cache mixPrune because mixPrune is only called on misses in nextSecret
def mixPrune(secret, res):
    return (secret ^ res) % 16777216

# @cache - turns out it was slower with this lol - too many misses
def nextSecret(secret):
    secret = mixPrune(secret, secret * 64)
    secret = mixPrune(secret, secret // 32)
    secret = mixPrune(secret, secret * 2048)
    return secret

star1 = 0
star2 = 0
import os
data = open(os.path.basename(__file__).split('.')[0]+'.txt','r').read()
# data = """
# 1
# 10
# 100
# 2024
# """
# data = '123'
# data = """
# 1
# 2
# 3
# 2024
# """
data = [line.strip() for line in data.split('\n') if line.strip()]
data = list(map(int,data))

# generate all valid change lists
changes = defaultdict(int)

for num in data:
    prices = [(num%10,None)]
    for i in range(2000):
        num = nextSecret(num)
        price = num%10
        prices.append((price,price-prices[-1][0]))
    star1 += num

    deltaPrice = [p[1] for p in prices[1:]]
    seen = set()
    for i,change in enumerate(zip(deltaPrice[:-3],deltaPrice[1:-2],deltaPrice[2:-1],deltaPrice[3:])):
        if change not in seen:
            changes[change] += prices[i+4][0]
            seen.add(change)
    
star2 = changes[max(changes, key=changes.get)]

print('star1:',star1)
print('star2:',star2)
