#!/usr/bin/python3
# list = [1721,979,366,299,675,1456]

import time as time
import sys

#lennard
# do stuff

# # Day 1, Challenge 1 O(n)
# seen = set()
# with open('day1_input') as f:
#     for line in f:
#         x = int(line)
#         if 2020 - x in seen:
#             print(x * (2020 - x))
#         seen.add(x)

t = time.time()
# Day 1, Challenge 2 O(n^2)
seen = set()
with open('day1_input') as f:
    for line in f:
        x = int(line)
        for i in range(2020-x):
            if i in seen and (2020-x)-i in seen:
                print(x * i * (2020 - x - i))
        seen.add(x)

print("lennard time:")
print(time.time() - t)
print("")

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
        # if one + two == 2020:
        #     if(one * two > save_one):
        #         save_one = one*two
        for three in list:
            if one + two + three == 2020:
                if one * two * three > save_two:
                    save_two = one*two*three
print("max time")
print(time.time() - t)
print("")


t = time.time()
num = []
with open('day1_input') as f:
    lines = f.readlines()
    for line in lines:
        line.strip()
        num.append(int(line))

for i in num:
    for j in num: 
        for k in num:
            if i+j+k == 2020:
                print(f"{i}+{j}+{k} == 2020")
                print(f"Answer: {i*j*k}")


print("bram time")
print(time.time() - t)
print("")


# print(save_one)
# print(save_two)
