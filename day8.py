#!/usr/bin/python3
import regex as re
def clean(Instructions):
    for i in range(len(Instructions)):
        Instructions[i][2] = 0

def run_code(Instructions):
    Instruction_counter = 0
    value = 0
    while True:
        Instructions[Instruction_counter][2] += 1
        #dus fout:
        if (Instructions[Instruction_counter][2]) == 2:
            clean(Instructions)
            return False,value
        if Instructions[Instruction_counter][0] == 'acc':
            value += Instructions[Instruction_counter][1]
        if Instructions[Instruction_counter][0] == 'jmp':
            Instruction_counter += Instructions[Instruction_counter][1]
            continue
        Instruction_counter += 1
        if(Instruction_counter >= len(Instructions)-1):
            clean(Instructions)
            return True,value

inst = []
rules = {}
with open('day8.dat') as f:
    for line in f.read().splitlines():
        temp = re.match(re.compile(r'(\w+)+ (.*)'), line).groups()
        inst.append([temp[0],int(temp[1]),0])
#1
print(run_code(inst))
#2
for i in range(len(inst)):
    if inst[i][0] == 'acc':
        continue
    if inst[i][0] == 'nop':
        inst[i][0] = 'jmp'  
    elif inst[i][0] == 'jmp':
        inst[i][0] = 'nop'
    returncode, value = run_code(inst)
    if returncode == True:
        print(value)
        break
    if inst[i][0] == 'nop':
        inst[i][0] = 'jmp'
    elif inst[i][0] == 'jmp':
        inst[i][0] = 'nop'