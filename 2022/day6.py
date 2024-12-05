with open('day6.txt','r') as file:
    data = file.read().split('\n')
    data = [line for line in data if line]
    data = data[0]
    for i in range(len(data)-4):
        if len(set(data[i:i+4])) == 4:
            star1 = i+4
            break
    for i in range(len(data)-14):
        if len(set(data[i:i+14])) == 14:
            star2 = i+14
            break
    print('star1: '+str(star1))
    print('star2: '+str(star2))