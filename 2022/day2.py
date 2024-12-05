with open('day2.txt','r') as file:
    data = file.read().split('\n')
    scoring1 = {
        'A X': 4,
        'A Y': 8,
        'A Z': 3,
        'B X': 1,
        'B Y': 5,
        'B Z': 9,
        'C X': 7,
        'C Y': 2,
        'C Z': 6
    }
    scoring2 = {
        'A X': 3,
        'A Y': 4,
        'A Z': 8,
        'B X': 1,
        'B Y': 5,
        'B Z': 9,
        'C X': 2,
        'C Y': 6,
        'C Z': 7
    }
    score1 = 0
    score2 = 0
    for round in data:
        if round != '':
            score1 += scoring1[round]
            score2 += scoring2[round]
    print('star 1: %d'%score1)
    print('star 2: %d'%score2)