#!/usr/bin/python3

import string
# byr - four digits; at least 1920 and at most 2002.
# iyr - four digits; at least 2010 and at most 2020.
# eyr - four digits; at least 2020 and at most 2030.
# hgt - a number followed by either cm or in:
#     If cm, the number must be at least 150 and at most 193.
#     If in, the number must be at least 59 and at most 76.
# hcl - a # followed by exactly six characters 0-9 or a-f.
# ecl - exactly one of: amb blu brn gry grn hzl oth.
# pid - a nine-digit number, including leading zeroes.


def checkpassp(dat):
    valids = 0
    checks = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
    for dat1 in dat.split():
        id,value = dat1.split(':')
        if id in checks:
            valids += 1
    if valids == 7:
        return True
    return False

def checkpassp_2(dat):
    valids = 0
    for dat1 in dat.split():
        id,value = dat1.split(':')
        if id == 'byr':
            valids += value.isdigit() and int(value) >= 1920 and int(value) <= 2002
        if id == 'iyr':
            valids += value.isdigit() and int(value) >= 2010 and int(value) <= 2020
        if id == 'eyr':
            valids += value.isdigit() and int(value) >= 2020 and int(value) <= 2030
        if id == 'hgt':
            if value.endswith('cm'):
                valids += 150 <= int(value[:-2]) <= 193
            elif value.endswith('in'):
                valids += 59 <= int(value[:-2]) <= 76
        if id == 'hcl':
            valids += value[0] == '#' and len(value) == 7
            try:
                int(value[1:],16)
            except:
                valids -= 1            
        if id == 'ecl':
            valids += value in ['amb','blu','brn','gry','grn','hzl','oth']
        if id == 'pid':
            valids += value.isdigit() and len(value) == 9
    if valids == 7:
        return True
    return False

#ONE
valid = 0
with open('day4_input') as f:
    for dat in f.read().split("\n\n"):
        if checkpassp(dat):
            valid += 1
print(valid)

#TWO
valid = 0
with open('day4_input') as f:
    for dat in f.read().split("\n\n"):
        if checkpassp_2(dat):
            valid += 1
print(valid)
