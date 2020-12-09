#!/usr/bin/python3
import time as time

def function(inn):
    row = 0
    colum = 0
    count = 64
    for i in  range(7):
        if inn[i] == 'B':           
            row = row | count 
        count = count >> 1
    count = 4
    for i in range(3):
        if inn[i+7] == 'R':           
            colum = colum | count 
        count = count >> 1
    return row*8+colum

t = time.time()
big = 0
test =[False] * 1024
with open('day5_input') as f:
    for line in f:
        id = function(line)
        test[id] = True
        if id > big:
            big = id

print(big)
count = 0
for tt in range(1024):
    if test[tt] == False:
        if(test[tt-1] == True):
            print(tt)
            break

print("max")
print(time.time() - t)
print("")


#lennard
t = time.time()

import numpy as np
lines = open('day5_input').read().splitlines()
data = np.array(lines, dtype='c')
row = ((data[:,:7] == b'B') * 2**np.arange(7)[::-1]).sum(axis=1)
col = ((data[:,7:] == b'R') * 2**np.arange(3)[::-1]).sum(axis=1)
seat = np.sort(row*8 + col)
idx = np.where(np.diff(seat) == 2)
print(seat.max(), seat[idx] + 1)

print("lennard")
print(time.time() - t)
print("")