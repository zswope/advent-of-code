with open('day11.txt','r') as file:
    data = file.read().split('\n\n')
    data = [line for line in data if line]
#     data = [
# '''Monkey 0:
#   Starting items: 79, 98
#   Operation: new = old * 19
#   Test: divisible by 23
#     If true: throw to monkey 2
#     If false: throw to monkey 3''',

# '''Monkey 1:
#   Starting items: 54, 65, 75, 74
#   Operation: new = old + 6
#   Test: divisible by 19
#     If true: throw to monkey 2
#     If false: throw to monkey 0''',

# '''Monkey 2:
#   Starting items: 79, 60, 97
#   Operation: new = old * old
#   Test: divisible by 13
#     If true: throw to monkey 1
#     If false: throw to monkey 3''',

# '''Monkey 3:
#   Starting items: 74
#   Operation: new = old + 3
#   Test: divisible by 17
#     If true: throw to monkey 0
#     If false: throw to monkey 1'''
#     ]
    
    monkeys = []
    for l in data:
        d = l.split('\n')
        monkey = [
            [int(x) for x in (d[1].split(': ')[1]).split(', ')], # items
            ''.join((d[2].split('= ')[1]).split(' ')[:2])+'='+(d[2].split('= ')[1]).split(' ')[2], # operation
            int(d[3].split(' ')[-1]), # test
            int(d[4].split(' ')[-1]), # true
            int(d[5].split(' ')[-1]), # false
            0
            ]
        monkeys.append(monkey)
    # print(monkeys)
    
    #begin round
    for i in range(10000):
        # print('ROUND %d'%i)
        # print([item for sublist in [x[0] for x in monkeys] for item in sublist])
        for monkey in monkeys:
            # print(monkeys.index(monkey))
            for old in monkey[0]:
                monkey[5] += 1
                # print('  Monkey inspects an item with a worry level of %d'%old)
                exec(monkey[1])
                # print('    Worry level is %d'%old)
                # old = old // 3
                if old > 9699690: # product of all divisible checks
                    old %= 9699690
                # print('    Worry level divided by 3 to %d'%old)
                if old % monkey[2] == 0:
                    # print('    is divisible, throwing to monkey %d'%monkey[3])
                    monkeys[monkey[3]][0].append(old)
                else:
                    # print('    is not divisible, throwing to monkey %d'%monkey[4])
                    monkeys[monkey[4]][0].append(old)
            monkey[0] = []
        # print(monkeys)
    activity = [x[5] for x in monkeys]
    # print(activity)
    most = max(activity)
    activity.remove(most)
    star1 = most*max(activity)
    print('star1: %d'%star1)