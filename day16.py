#!/usr/bin/python3
#Part1
count = 0
checks = {}
your_Ticket   = []
Valid_Tickets = []
error = 0

def check_number(num,check_dic):
    flag = False
    for i in check_dic.values():
        for j in i:
            if j[0] <= num <= j[1]:
                return 0
    if num == 0:
        num = 1
    return num

with open('day16.dat') as f:
    for i in f:
        i = i.strip()
        if i == "":
            next(f)
            count += 1
            continue
        if count == 0:
            dit = i.partition(":")
            dat = dit[2].split(" or ")
            checks[dit[0]] = [[int(k) for k in dat[0].split('-')], [int(k) for k in dat[1].split('-')]]
        if count == 1:
            your_Ticket = [int(k) for k in i.split(',')]
        if count == 2:
            dit = 0 
            for c in [int(k) for k in i.split(',')]:
                dit += check_number(c,checks)
            error += dit
            if not dit:
                Valid_Tickets.append([int(k) for k in i.split(',')])
            continue
        if count > 2:
            print("error")

print(f"Part 1: {error}")

def part2(value, VT,count,key):
    for tick in VT:
        if (value[0][0] <= tick[count] <= value[0][1] or value[1][0] <= tick[count] <= value[1][1]):
            dd = 0
        else:
            return 0
    return 1

full_options = []
for key,values in checks.items():
    options = []
    for i in range(len(your_Ticket)):
        if(part2(values,Valid_Tickets,i,key)):
            options.append(i)  
    full_options.append(options)

Solution = [len(your_Ticket)+2] * (len(your_Ticket)+1)
for i in range(len(your_Ticket)+1):
    count = 0
    for ot in full_options: 
        if i == len(ot):
            for tt in ot:
                if tt not in Solution:
                    Solution[count] = tt
                    break
        count += 1
        
result = 1
for i in range(6):
    result *= your_Ticket[Solution[i]]
print(f"Part 2: {result}")