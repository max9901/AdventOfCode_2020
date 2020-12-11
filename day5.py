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