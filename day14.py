#!/usr/bin/python3


# Het kan niet veel lelijker.
# Het kan niet veel lelijker.
# Het kan niet veel lelijker.
# Het kan niet veel lelijker.

#Part1
addressess = [0]
values     = [0]
mask        = 0
def apply_mask(mask,value):
    Xmask = mask.replace("1","0")
    Ymask = int(mask.replace("X","0"),2)
    Xmask = int(Xmask.replace("X","1"),2)
    return ((value & Xmask) | Ymask) &  68719476735
with open('day14.dat') as f:
    for i in f:
        flag = False
        i = i.strip()
        if "mask = " in i:
            mask = i.replace("mask = ","")
        elif "mem[" in i:
            address = (int(i[4:].partition("]")[0]))
            value   = int(i.partition("= ")[2])
            for k, j in enumerate(addressess):
                if j == address:
                    flag = True
                    break;
            if flag:
                values[k] = apply_mask(mask,value)
            else:
                addressess.append(address)
                values.append(apply_mask(mask,value))
print(f"part1 {sum(values)}")

# Part2 Het kan niet veel lelijker.
memory = {}
mask = ""
base_mask                 = 0
addition_mask             = 0
Xs_mask_collection        = 0

import itertools
with open('day14.dat') as ft:
    for i in ft:
        flag = False
        i = i.strip()
        if "mask = " in i:
            mask = i.replace("mask = ","")
            addition_mask = int(mask.replace("X","0"),2)
            base_mask = mask.replace("1","X")
            base_mask = base_mask.replace("0","1")
            base_mask = int(base_mask.replace("X","0"),2)
            Xs_mask = mask.replace("1","0")        
            Xs_mask_collection = []
            for k in range(2**Xs_mask.count('X')):
                Xss = format(k, '036b')
                mout = []
                count = 1
                for XS in Xs_mask:
                    if XS == 'X':
                        mout.append(Xss[-count])
                        count+=1
                    else:
                        mout.append(XS)        
                mout = ''.join(mout)
                Xs_mask_collection.append(int(mout,2))

        elif "mem[" in i:
            address =  int(i[4:].partition("]")[0])
            address =  (( address & base_mask) | addition_mask) &  68719476735
            value   = int(i.partition("= ")[2])
            for Xmas in Xs_mask_collection:
                Newnew_address = address | Xmas
                memory[Newnew_address] = value
e
print(f"part2 {sum(memory.values())}")
