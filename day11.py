#!/usr/bin/python3

#opgave 1
seats_read1    = []
with open('day11.dat') as f:
    seats_read = [list(i.strip()) for i in f]

def check_seats_1(seats):
    newseats = 0
    while newseats != seats:
        newseats = [[i for i in row] for row in seats]
        for i in range(len(newseats)):
            for j in range(len(newseats[0])):
                if newseats[i][j] == '.':
                    seats[i][j] =  '.'
                elif newseats[i][j] == 'L':
                    FLAG_OCU = True
                    for k in range(-1,2):
                        for t in range(-1,2):
                            if (k == 0 and t == 0):
                                continue
                            if(i + k < 0 ): 
                                continue
                            if(i + k >= len(newseats)): 
                                continue
                            if(j + t < 0 ): 
                                continue
                            if(j + t >= len(newseats[0])): 
                                continue
                            if newseats[i+k][j+t] == '#':
                                FLAG_OCU = False
                    if FLAG_OCU:
                        seats[i][j] =  '#'
                    else:
                        seats[i][j] =  'L'
                elif newseats[i][j] == '#':
                    FLAG = 0
                    for k in range(-1,2):
                        for t in range(-1,2):
                            if (k == 0 and t == 0):
                                continue
                            if(i + k < 0 ): 
                                continue
                            if(i + k >= len(newseats)): 
                                continue
                            if(j + t < 0 ): 
                                continue
                            if(j + t >= len(newseats[0])): 
                                continue
                            if newseats[i+k][j+t] == '#':
                                FLAG += 1
                    if FLAG >= 4:
                        seats[i][j] =  'L'
                    else:
                        seats[i][j] =  '#'
    return seats

result = 0
seats_read = check_seats_1(seats_read)
for i in range(len(seats_read)):
    for j in range(len(seats_read[0])):
        if seats_read[i][j] == '#':
            result += 1
print(result)

#opgave 2
seats_read    = []
with open('day11.dat') as f:
    seats_read = [list(i.strip()) for i in f]

def check_seats_2(newseats):
    seats = 0
    while seats != newseats:
        seats = [[i for i in row] for row in newseats]
        for i in range(len(newseats)):
            for j in range(len(newseats[0])):
                if seats[i][j] == '.':
                    newseats[i][j] = '.'
                elif seats[i][j] == '#':
                    count = 0
                    for check in [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]:
                        distance = 0
                        while True:
                            distance += 1
                            y = check[0]*distance + i
                            x = check[1]*distance + j
                            if not (y >= 0 and y < len(seats_read) and x >= 0 and x < len(seats_read[0])): break
                            if seats[y][x] == '#':
                                count += 1
                                break
                            if seats[y][x] == 'L':
                                break
                    if count >= 5:
                        newseats[i][j] = 'L'
                    else:
                        newseats[i][j] = '#'
                else:
                    count = 0
                    for check in [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]:
                        distance = 0
                        while True:
                            distance += 1
                            y = check[0]*distance + i
                            x = check[1]*distance + j
                            if not (y >= 0 and y < len(seats_read) and x >= 0 and x < len(seats_read[0])): break
                            if seats[y][x] == '#':
                                count += 1
                                break
                            if seats[y][x] == 'L':
                                break
                    if count:
                        newseats[i][j] = 'L'
                    else:
                        newseats[i][j] = '#'
    return seats

seats_read = check_seats_2(seats_read)
result = 0
for i in range(len(seats_read)):
    for j in range(len(seats_read[0])):
        if seats_read[i][j] == '#':
            result += 1
print(result)