def compare(left,right):
    # return 0 if left is smaller
    # return 1 if equal
    # return 2 if right is smaller
    if type(left) == int and type(right) == int:
        if left < right:
            return 0
        elif left == right:
            return 1
        else:
            return 2
    elif type(left) == list and type(right) == list:
        smaller = compare(len(left),len(right))
        for l,r in zip(left,right):
            c = compare(l,r)
            if c != 1:
                return c
        return smaller
    elif type(left) == list and type(right) == int:
        return compare(left,[right])
    elif type(left) == int and type(right) == list:
        return compare([left],right)

with open('day13.txt','r') as file:
    data = file.read().split('\n\n')
    data = [line for line in data if line]
    # data = ['[1,1,3,1,1]\n[1,1,5,1,1]','[[1],[2,3,4]]\n[[1],4]','[9]\n[[8,7,6]]','[[4,4],4,4]\n[[4,4],4,4,4]','[7,7,7,7]\n[7,7,7]','[]\n[3]','[[[]]]\n[[]]','[1,[2,[3,[4,[5,6,7]]]],8,9]\n[1,[2,[3,[4,[5,6,0]]]],8,9]']
    
    star1 = 0
    for i,packets in enumerate(data):
        left = eval(packets.split('\n')[0])
        # print(left)
        right = eval(packets.split('\n')[1])
        # print(right)
        if compare(left,right) in [0,1]:
            star1 += i+1
    
    print('star1: %d'%star1)
    
with open('day13.txt','r') as file:
    data = file.read().split('\n')
    data = [eval(line) for line in data if line]
    # data = [[1,1,3,1,1],[1,1,5,1,1],[[1],[2,3,4]],[[1],4],[9],[[8,7,6]],[[4,4],4,4],[[4,4],4,4,4],[7,7,7,7],[7,7,7],[],[3],[[[]]],[[]],[1,[2,[3,[4,[5,6,7]]]],8,9],[1,[2,[3,[4,[5,6,0]]]],8,9]]
    
    data.append([[2]])
    data.append([[6]])
    
    # print(data)
    n = len(data)
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
    swapped = False
    # Traverse through all array elements
    for i in range(n-1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            # print(compare(data[j],data[j+1]))
            if compare(data[j],data[j + 1]) == 2:
                swapped = True
                data[j], data[j + 1] = data[j + 1], data[j]
         
        if not swapped:
            # if we haven't needed to make a single swap, we
            # can just exit the main loop.
            break
    
    # print(data)
    star2 = (data.index([[2]])+1) * (data.index([[6]])+1)
    print('star2: %d'%star2)