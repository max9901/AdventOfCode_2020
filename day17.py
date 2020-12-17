#!/usr/bin/python3

#comment part that isn't used --> same function names

#part1
# import copy
# def print_map(Dimmm):
#     for dim2 in Dimmm:
#         for dim in dim2:
#             print(dim)
#         print("")

# def append_values_for_next_step(Dimmm):
#     for d2 in Dimmm:
#         add = len(d2[0]) + 2
#         for d in d2:
#             d.append('.')   
#             d.insert(0,'.')
#         d2.insert(0,(['.']*add))
#         d2.append((['.']*add))
#     add2 = len(Dimmm[0])
#     Dimmm.insert(0,[['.' for x in y] for y in Dimmm[0]])
#     Dimmm.append([['.' for x in y] for y in Dimmm[0]])
    
# def check_values(dimmm):
#     check_dim = [[[x for x in y] for y in z] for z in dimmm]
#     for i,d2 in enumerate(check_dim):
#         for j,d in enumerate(d2):
#             for k,p in enumerate(d):
#                 # RULES :
#                 if p == '#':
#                     count = 0
#                     for kk in [-1,0,1]:
#                         if( (k + kk) < 0 or (k + kk) >= len(d)):
#                             continue
#                         for jj in [-1,0,1]:
#                             if((j + jj) < 0 or (j + jj) >= len(d2)):
#                                 continue
#                             for ii in [-1,0,1]:
#                                 if((i + ii) < 0 or (i + ii) >= len(check_dim)):
#                                     continue
#                                 if kk == jj == ii == 0:
#                                     continue
#                                 if(check_dim[i+ii][j+jj][k+kk] == '#'):
#                                     count += 1
#                     if count not in [2,3]:
#                         dimmm[i][j][k] = '.'
#                 else:
#                     count = 0
#                     for kk in [-1,0,1]:
#                         if( (k + kk) < 0 or (k + kk) >= len(d)):
#                             continue
#                         for jj in [-1,0,1]:
#                             if((j + jj) < 0 or (j + jj) >= len(d2)):
#                                 continue
#                             for ii in [-1,0,1]:
#                                 if((i + ii) < 0 or (i + ii) >= len(check_dim)):
#                                     continue
#                                 if(check_dim[i+ii][j+jj][k+kk] == '#'):
#                                     count += 1
#                                     # print(i,j,k,count)
#                     if count == 3:
#                         # print('hit',count,i,j,k)
#                         dimmm[i][j][k] = '#'
                
# dim2 = []
# Dim3d = []
# with open('day17.dat') as f:
#     for i in f:
#         i = i.strip()
#         dim2.append([j for j in i.strip()])     
# Dim3d.append(dim2)

# print("step0")
# print_map(Dim3d)

# for i in range(6):
#     print("step: ",i)
#     append_values_for_next_step(Dim3d)
#     check_values(Dim3d)


# result = 0
# for dim2 in Dim3d:
#     for dim in dim2:
#         for d in dim:
#             if d == '#':
#                 result += 1
# print(result)



#part 2
import copy
def print_map(Dimmm):
    for dim3 in Dimmm:
        for dim2 in dim3:
            for dim in dim2:
                print(dim)
            print(" ")
        print(" ")
    print(" ")
    print(" ")

def append_values_for_next_step(Dimmm):
    for d3 in Dimmm:
        for d2 in d3:
            add = len(d2[0]) + 2
            for d in d2:
                d.append('.')   
                d.insert(0,'.')
            d2.insert(0,(['.']*add))
            d2.append((['.']*add))
        d3.append([['.' for x in y] for y in d3[0]])
        d3.insert(0,[['.' for x in y] for y in d3[0]])

    Dimmm.insert(0,[[['.' for x in y] for y in z] for z in Dimmm[0]])
    Dimmm.append([[['.' for x in y] for y in z] for z in Dimmm[0]])

    
def check_values(dimmm):
    check_dim = [[[[x for x in y] for y in z] for z in w] for w in dimmm]
    for l,d3 in enumerate(check_dim):
        for i,d2 in enumerate(d3):
            for j,d in enumerate(d2):
                for k,p in enumerate(d):
                    # RULES :
                    if p == '#':
                        count = 0
                        for kk in [-1,0,1]:
                            if( (k + kk) < 0 or (k + kk) >= len(d)):
                                continue
                            for jj in [-1,0,1]:
                                if((j + jj) < 0 or (j + jj) >= len(d2)):
                                    continue
                                for ii in [-1,0,1]:
                                    if((i + ii) < 0 or (i + ii) >= len(d3)):
                                        continue
                                    for ll in [-1,0,1]:
                                        if((l + ll) < 0 or (l + ll) >= len(check_dim)):
                                            continue
                                        if ll == kk == jj == ii == 0:
                                            continue
                                        if(check_dim[l+ll][i+ii][j+jj][k+kk] == '#'):
                                            count += 1
                        if count not in [2,3]:
                            dimmm[l][i][j][k] = '.'
                    else:
                        count = 0
                        for kk in [-1,0,1]:
                            if( (k + kk) < 0 or (k + kk) >= len(d)):
                                continue
                            for jj in [-1,0,1]:
                                if((j + jj) < 0 or (j + jj) >= len(d2)):
                                    continue
                                for ii in [-1,0,1]:
                                    if((i + ii) < 0 or (i + ii) >= len(check_dim)):
                                        continue
                                    for ll in [-1,0,1]:
                                        if((l + ll) < 0 or (l + ll) >= len(check_dim)):
                                            continue
                                        if(check_dim[l+ll][i+ii][j+jj][k+kk] == '#'):
                                            count += 1
                        if count == 3:
                            dimmm[l][i][j][k] = '#'
                
dim2 = []
Dim3d = []
Dim4d = []
with open('day17.dat') as f:
    for i in f:
        i = i.strip()
        dim2.append([j for j in i.strip()])     

Dim3d.append(dim2)
Dim4d.append(Dim3d)
print_map(Dim4d)

for i in range(6):
    print("step: ",i)
    append_values_for_next_step(Dim4d)
    check_values(Dim4d)


result = 0
for dim3 in Dim4d:
    for dim2 in dim3:
        for dim in dim2:
            for d in dim:
                if d == '#':
                    result += 1
print(result)
