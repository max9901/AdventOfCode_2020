#!/usr/bin/python3
# list = [1721,979,366,299,675,1456]

import time as time
import sys


#max
t = time.time()
list = []
with open("day1_input") as f:
    temp = f.readlines()
    for x in temp:
        list.append(int(x))
save_one = 0
save_two = 0
for one in list:
    for two in list:
	#part 1
        # if one + two == 2020:
        #     if(one * two > save_one):
        #         save_one = one*two
	#part2
        for three in list:
            if one + two + three == 2020:
                if one * two * three > save_two:
                    save_two = one*two*three
print(time.time() - t)
print("")
