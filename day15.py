#part1
with open("day15.dat") as f:
    num = [int(i) for i in f.readline().strip().split(',')]
seen = {}
for i, j in enumerate(num):
    seen[j] = i
while 1:
    if(num[-2] == num[-1]):
        num.append(1)
    elif (num.count(num[-1]) == 1):
        num.append(0)
    else:
        num.append(len(num) -1 - seen[num[-1]])
    seen[num[-2]] = len(num) -2
    if len(num) -1 >= 2020:
        break
print(f"part1: {num[-2]}")

#part2
with open("day15.dat") as f:
    num2 = [int(i) for i in f.readline().strip().split(',')]
seen2 = {}
for i, j in enumerate(num2):
    seen2[j] = i
count = len(num2)  
count2 = 0
while True:
    check = seen2.get(num2[-1], -1)
    if num2[-1] == num2[-2]:
        num2.append(1)
    elif(check == -1 or check == count-1):  
        num2.append(0)
    else:
        num2.append(count - check - 1)
    seen2[num2[-2]] = count - 1
    if (count + 1) % 3000000 == 0:
        count2 +=10
        print(str(count2) + "%" )
    if count >= 30000000 - 1:
        break
    count += 1
print(f"Part2: {num2[-1]}")