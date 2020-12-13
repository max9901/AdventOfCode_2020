#!/usr/bin/python3
import math
with open('day13.dat') as f:
    lines= f.read().splitlines()

#part one 
lines[0] = int(lines[0])
results = [0,0]
for bus in [int(i) for i in  list(filter(lambda a: a != 'x',lines[1].split(',')))]:
    check =  math.floor(lines[0]/bus) * bus   + bool(lines[0]%bus) * bus
    if not results[1]:
        results = [bus,check]
    if check < results[1]:
        results = [bus,check]
print(f"Part1 {results[0]*(results[1] - lines[0])}")

# part 2
current_bus = [] 
for  i, bus in enumerate([bus for bus in lines[1].split(",")]):
    if not i:
        current_bus = [0, int(bus), i]
        continue
    if bus == "x":
        continue
    next_bus = [0, int(bus), i]
    offset = 0
    nbm = current_bus[0]
    while 1:
        if not (nbm + (next_bus[2] - current_bus[2])) % next_bus[1]:
            if not offset :
                offset = nbm
            else:
                current_bus =  (offset, nbm - offset, 0)
                break
        nbm += current_bus[1]
print(f"part2 {current_bus[0]}")