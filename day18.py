#!/usr/bin/python3

#TODO range(1000) fixen met while loop om het fool proof t maken --> KNOWN BUG maar geen tijd meer. 

def split(word): 
    return [char for char in word]  

resultpart1 = 0
with open('day18.dat') as f:
    for i in f:
        result = []
        i = split(i.strip().replace(" ",""))
        count = 0
        len_check = len(i)
        while 1:
            if len(i) == 1:
                break
            lent = 0
            for jj in range(1000):
                j = jj - lent
                if j >= len(i):
                    break
                if i[j] == "+":
                    if i[j-1].isnumeric() and i[j+1].isnumeric():
                        i[j] = str(int(i[j-1]) + int(i[j+1]))
                        del i[j-1]
                        del i[j]
                        lent += 2
                        j = jj - lent
                if j >= len(i):
                    break
                if i[j] == "*":
                    if i[j-1].isnumeric() and i[j+1].isnumeric():
                        i[j] = str(int(i[j-1]) * int(i[j+1]))
                        del i[j-1]
                        del i[j]
                        lent += 2
                        j = jj - lent
                if j >= len(i):
                    break
                if i[j] == "(":
                    if i[j+2] == ")":
                        del i[j]
                        del i[j+1]
                        lent += 2
                        j = jj - lent
        resultpart1 += int(i[0])
print(f"part1: {resultpart1}")

resultpart2 = 0
with open('day18.dat') as f:
    for i in f:
        result = []
        i = split(i.strip().replace(" ",""))
        count = 0
        len_check = len(i)
        plutormultiply = True
        while 1:
            if len(i) == 1:
                break
            lent = 0
            for jj in range(1000):
                oldplotmultiply = plutormultiply
                j = jj - lent
                if j >= len(i):
                    break
                if(plutormultiply):
                    if i[j] == "+":
                        flag = True
                        for c in i[j:]:
                            if c == ")":
                                flag = True
                                break    
                            if c == "(":
                                flag = False
                                break
                        if flag:
                            if i[j-1].isnumeric() and i[j+1].isnumeric():
                                i[j] = str(int(i[j-1]) + int(i[j+1]))
                                del i[j-1]
                                del i[j]
                                lent += 2
                                j = jj - lent
                    if j >= len(i):
                        break
                else:
                    if i[j] == "*":
                        flag = True
                        for c in i[j:]:
                            if c == ")":
                                flag = True
                                break    
                            if c == "(":
                                flag = False
                                break
                        if flag:
                            if i[j-1].isnumeric() and i[j+1].isnumeric():
                                i[j] = str(int(i[j-1]) * int(i[j+1]))
                                del i[j-1]
                                del i[j]
                                lent += 2
                                j = jj - lent
                    if j >= len(i):
                        break
                if i[j] == "(":
                    if i[j+2] == ")":
                        del i[j]
                        del i[j+1]
                        lent += 2
                        plutormultiply = False
                        break
            plutormultiply = not plutormultiply


        resultpart2 += int(i[0])
print(f"part2: {resultpart2}")
