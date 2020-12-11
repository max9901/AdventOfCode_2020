#!/usr/bin/python3
numbers = []
with open('day10.dat') as f:
    for line in f.read().splitlines():
        numbers.append(int(line))

numbers.append(max(numbers)+3)
numbers.sort()

#PART 1
counts = [0,0,0,0]
currentJOLT = 0
for num in numbers:
    tmp = num - currentJOLT
    if tmp < 4:
        counts[tmp] += 1
        currentJOLT = num
    else:
        print("error out of bounds")
        quit()
print(counts[1]*counts[3])

#PART2
options = [0] * (max(numbers)+1)
options[0] = 1
for num in numbers:
    if(num > 2):
        options[num] = options[num - 1] + options[num - 2] + options[num - 3]
    elif num > 1:
        options[num] = options[num - 1] + options[num - 2]
    elif num > 0:
        options[num] = options[num - 1] 
    else:
        print("error out of bounds")
        quit()  
print(options[-1])
