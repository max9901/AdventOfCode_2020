#!/usr/bin/python3
import collections

#part one 
degree = 90
pos = {"N": 0,"E": 0,"S": 0,"W": 0}
with open('day12.dat') as f:
    for i in f:
        OP    = i[0]
        value = int(i[1:].strip())
        if OP in ["N","S","E","W"]:
            pos[OP] += value
        if OP == "L":
            degree -= value
            while degree < 0:
                degree = 360 + degree
        if OP == "R":
            degree += value
            while degree >= 360:
                degree = degree - 360
        if OP in ["F"]:
            if(degree == 0):
                pos['N'] += value
            elif(degree == 90):
                pos['E'] += value
            elif(degree == 180):
                pos['S'] += value
            elif(degree == 270):
                pos['W'] += value
            else:
                print(degree)
                print("ERROR NOT 90 degree corner, never happends so easier coding :D")
                quit()
print(f"part1 =  {abs(pos['E']-pos['W']) + abs(pos['N']-pos['S'])}")


#part two
degree = 90
waypoint = collections.deque((1,10,0,0))
dict = {"N": 0,"E": 90,"S": 180,"W": 270}
pos  = {"N": 0,"E": 0,"S": 0,"W": 0}
with open('day12.dat') as f:
    for i in f:
        OP    = i[0]
        value = int(i[1:].strip())
        if OP in ["N","S","E","W"]:
            waypoint[int(dict[OP]/90)] += value
        if OP == "L":
            for i in range(int(value/90)):
                waypoint.append(waypoint.popleft())
        if OP == "R":
            for i in range(int(value/90)):
                waypoint.insert(0,waypoint.pop())
        if OP in ["F"]:
            pos['N'] += value * waypoint[0]
            pos['E'] += value  * waypoint[1]
            pos['S'] += value  * waypoint[2]
            pos['W'] += value  * waypoint[3]
print(f"part2 =  {abs(pos['E']-pos['W']) + abs(pos['N']-pos['S'])}")

