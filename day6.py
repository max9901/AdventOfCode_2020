#!/usr/bin/python3

import time as time

#max
t = time.time()
#question one
result = 0
seen = []
with open('day6_input') as f:
    for line in f:
        if line == "\n":
            result += len(seen)
            seen = []
        else:
            for i in line[0:len(line)-1]:
                seen.append(i) if i not in seen else seen
result += len(seen)
print(result)

#question two
result = 0
seen = []
new = True
with open('day6_input') as f:
    for line in f:
        if line == "\n":
            result += len(seen)
            seen = []
            new = True
        else:
            seen_new = []
            if new == True:
                new = False
                for i in line[0:len(line)-1]:                
                    seen_new.append(i)
            for i in line[0:len(line)-1]:
                 if i in seen:
                     seen_new.append(i)
            seen = seen_new
result += len(seen)
print(result)
print("max")
print(time.time() - t)
print("")


#lennard
import functools
t = time.time()
print(sum(
    len(set(group.replace('\n','')))
    for group in open('day6_input').read().split('\n\n')
    ))
print(sum(
    len(functools.reduce(lambda a, b: set(a) & set(b), group))
    for group in map(str.splitlines, open('day6_input').read().split('\n\n'))
    ))

print("lennard")
print(time.time() - t)
print("")