star1 = 0
star2 = float('inf')

def getSeedLocation(seed):
    soil = getTranslation(seed,seed2soil)
    fertilizer = getTranslation(soil,soil2fertilizer)
    water = getTranslation(fertilizer,fertilizer2water)
    light = getTranslation(water,water2light)
    temperature = getTranslation(light,light2temperature)
    humidity = getTranslation(temperature,temperature2humidity)
    location = getTranslation(humidity,humidity2location)
    return location

def getTranslation(input,maps):
    for map in maps:
        sourceStart = map[1]
        outStart = map[0]
        interval = map[2]
        if input >= sourceStart and input < sourceStart+interval:
            return outStart + input - sourceStart
    return input

with open('day5.txt', 'r') as file:
    data = file.readlines()
    data = [line.split('\n')[0] for line in data if line]
    data = [line for line in data if line]
#     data = """seeds: 79 14 55 13

# seed-to-soil map:
# 50 98 2
# 52 50 48

# soil-to-fertilizer map:
# 0 15 37
# 37 52 2
# 39 0 15

# fertilizer-to-water map:
# 49 53 8
# 0 11 42
# 42 0 7
# 57 7 4

# water-to-light map:
# 88 18 7
# 18 25 70

# light-to-temperature map:
# 45 77 23
# 81 45 19
# 68 64 13

# temperature-to-humidity map:
# 0 69 1
# 1 0 69

# humidity-to-location map:
# 60 56 37
# 56 93 4""".split('\n')
#     data = [line for line in data if line]

    mode = 'seeds'
    seed2soil = []
    soil2fertilizer = []
    fertilizer2water = []
    water2light = []
    light2temperature = []
    temperature2humidity = []
    humidity2location = []
    for dat in data:
        # mode setter
        match dat:
            case 'seed-to-soil map:':
                mode = 'seed-to-soil'
                continue
            case 'soil-to-fertilizer map:':
                mode = 'soil-to-fertilizer'
                continue
            case 'fertilizer-to-water map:':
                mode = 'fertilizer-to-water'
                continue
            case 'water-to-light map:':
                mode = 'water-to-light'
                continue
            case 'light-to-temperature map:':
                mode = 'light-to-temperature'
                continue
            case 'temperature-to-humidity map:':
                mode = 'temperature-to-humidity'
                continue
            case 'humidity-to-location map:':
                mode = 'humidity-to-location'
                continue
        
        match mode:
            case 'seeds':
                star1Seeds = [int(seed) for seed in dat.split(':')[1].strip().split(' ')]

            case 'seed-to-soil':
                vals = tuple(int(v) for v in dat.split(' '))
                seed2soil.append(vals)
            case 'soil-to-fertilizer':
                vals = tuple(int(v) for v in dat.split(' '))
                soil2fertilizer.append(vals)
            case 'fertilizer-to-water':
                vals = tuple(int(v) for v in dat.split(' '))
                fertilizer2water.append(vals)
            case 'water-to-light':
                vals = tuple(int(v) for v in dat.split(' '))
                water2light.append(vals)
            case 'light-to-temperature':
                vals = tuple(int(v) for v in dat.split(' '))
                light2temperature.append(vals)
            case 'temperature-to-humidity':
                vals = tuple(int(v) for v in dat.split(' '))
                temperature2humidity.append(vals)
            case 'humidity-to-location':
                vals = tuple(int(v) for v in dat.split(' '))
                humidity2location.append(vals)

# star1 = min([humidity2location[temperature2humidity[light2temperature[water2light[fertilizer2water[soil2fertilizer[seed2soil[seed]]]]]]] for seed in seeds])
star1 = min(getSeedLocation(seed) for seed in star1Seeds)
for i in range(0,len(star1Seeds),2):
    print('looking at group: %d'%star1Seeds[i])
    for seed in range(star1Seeds[i],star1Seeds[i]+star1Seeds[i+1]):
        star2 = min(star2, getSeedLocation(seed))
print('star1: %s'%star1)
print('star2: %s'%star2)