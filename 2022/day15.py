with open('day15.txt','r') as file:
    data = file.read().split('\n')
    data = [line for line in data if line]
    # data = [
    #     'Sensor at x=2, y=18: closest beacon is at x=-2, y=15',
    #     'Sensor at x=9, y=16: closest beacon is at x=10, y=16',
    #     'Sensor at x=13, y=2: closest beacon is at x=15, y=3',
    #     'Sensor at x=12, y=14: closest beacon is at x=10, y=16',
    #     'Sensor at x=10, y=20: closest beacon is at x=10, y=16',
    #     'Sensor at x=14, y=17: closest beacon is at x=10, y=16',
    #     'Sensor at x=8, y=7: closest beacon is at x=2, y=10',
    #     'Sensor at x=2, y=0: closest beacon is at x=2, y=10',
    #     'Sensor at x=0, y=11: closest beacon is at x=2, y=10',
    #     'Sensor at x=20, y=14: closest beacon is at x=25, y=17',
    #     'Sensor at x=17, y=20: closest beacon is at x=21, y=22',
    #     'Sensor at x=16, y=7: closest beacon is at x=15, y=3',
    #     'Sensor at x=14, y=3: closest beacon is at x=15, y=3',
    #     'Sensor at x=20, y=1: closest beacon is at x=15, y=3',
    # ]
    
    sensors = []
    for sensor in data:
        splitUp = sensor.split('=')
        sensorX = int(splitUp[1].split(',')[0])
        sensorY = int(splitUp[2].split(':')[0])
        beaconX = int(splitUp[3].split(',')[0])
        beaconY = int(splitUp[4])
        sensors.append(([sensorX,sensorY,beaconX,beaconY],abs(sensorX-beaconX)+abs(sensorY-beaconY)))

    for row in range(4000001):
        if row % 1000 == 0:
            print(row)
        row2000000 = set([])
        # row = 2000000
        # row = 10
        for sensor in sensors:
            temp = sensor[1] - abs(sensor[0][1] - row)
            for i in range(max(sensor[0][0]-temp,0),min(sensor[0][0]+temp+1,4000001)):
                row2000000.add(i)
        # for sensor in sensors:
        #     if sensor[0][3] == row and sensor[0][2] in row2000000:
        #         row2000000.remove(sensor[0][2])
        if len(row2000000) < 4000000:
            print(row)
    
    star1 = len(row2000000)
    print('star1: '+str(star1))
    # print('star2: '+str(star2))