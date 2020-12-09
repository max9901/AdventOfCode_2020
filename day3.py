#!/usr/bin/python3
import numpy as np
import time as time
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
data = ['..##.......',
        '#...#...#..',
        '.#....#..#.',
        '..#.#...#.#',
        '.#...##..#.',
        '..#.##.....',
        '.#.#.#....#',
        '.#........#',
        '#.##...#...',
        '#...##....#',
        '.#..#...#.#']
t = time.time()
iterator       = 5
Down           = [1,1,1,1,2]
Shift          = [3,1,5,7,1]
positioncount  = [0,0,0,0,0]
downcount      = [0,0,0,0,0]
threecount     = [0,0,0,0,0]
with open('day3_input') as f:
    next(f)
    # for dat in data[1:len(data)]:
    for dat in f.read().splitlines():
        for i in range(iterator):
            downcount[i] += 1
            if(downcount[i] == Down[i]):
                downcount[i] = 0
            else:
                continue
            positioncount[i] += Shift[i]
            if positioncount[i] >= (len(dat)):
                positioncount[i] = positioncount[i] - len(dat)
            if(dat[positioncount[i]] == "#"):
                threecount[i] += 1
            # print(str(dat[0:positioncount]) + f"{bcolors.WARNING}{bcolors.BOLD}{bcolors.UNDERLINE}" +str(dat[positioncount])+ f"{bcolors.ENDC}" + str(dat[positioncount+1:len(dat)]))
# print(threecount)
result = 1
for i in range(iterator):
    result *= threecount[i]
print(f'product: {result}')
print(time.time() - t)
print("")