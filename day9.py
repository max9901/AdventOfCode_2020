#!/usr/bin/python3
import collections

#READ
numbers = []
with open('day9.dat') as f:
    for line in f.read().splitlines():
        numbers.append(int(line))

#A
numbersDq = collections.deque()
result = 0
for num in numbers:
    check = int(num)
    flag = False
    if len(numbersDq) == 25:
        for i in numbersDq:
            for j in numbersDq:
                if i + j == check:
                    flag = True
        if flag == False:
            break
        numbersDq.popleft()
    numbersDq.append(check)
print(f"A: {check}")
#B
listdq = collections.deque()
for num in reversed(numbers):
    listdq.append(num)
    if check - sum(listdq) == 0 and len(listdq) > 1:
        break
    while check - sum(listdq) < 0:
        if(len(listdq) == 0):
            break
        listdq.popleft()
print(f"B: {max(listdq) + min(listdq)}")


