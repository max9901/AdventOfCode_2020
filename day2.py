#!/usr/bin/python3
line_in = ['1-3 a: abcde','1-3 b: cdefg','2-9 c: ccccccccc']
def check_password_one(line):
    temp = ""
    check_against = ""
    upper = 0
    lower = 0
    upper_set = False;
    lower_set = False;
    for char in line:
        if char is ':':
            check_against = ""
            for char2 in temp:
                if char2 is "-" or char2 is " ":
                    if check_against.isdecimal():
                        if(lower):
                            upper = int(check_against)
                            upper_set = True;
                        else:
                            lower = int(check_against)
                            lower_set = True;
                    else:
                        return 2
                    check_against = ""
                else:
                    check_against +=(char2)
            check_against = check_against
            temp = []
        else:
            temp+= (char)

    if(upper_set == 0 or lower_set == 0):
        return 2
    count =  temp.count(check_against)
    if count <= upper and  count >= lower:
        return False
    return 1
    
def check_password_two(line):
    temp = ""
    check_against = ""
    upper = 0
    lower = 0
    upper_set = False;
    lower_set = False;
    for char in line:
        if char is ':':
            check_against = ""
            for char2 in temp:
                if char2 is "-" or char2 is " ":
                    if check_against.isdecimal():
                        if(lower):
                            upper = int(check_against)
                            upper_set = True;
                        else:
                            lower = int(check_against)
                            lower_set = True;
                    else:
                        return 2
                    check_against = ""
                else:
                    check_against +=(char2)
            check_against = check_against
            temp = []
        else:
            temp+= (char)

    if(upper_set == 0 or lower_set == 0):
        return 2
    if(len(check_against) != 1):
        return 2
    
    if ( bool(temp[lower] == check_against)  != bool(temp[upper] == check_against)):
        return False
    return 1
    
        
# Question 1
valid = 0
with open('day2_input') as f:
    for line in f:
        return_code = check_password_one(line)
        if(return_code == 2):
            print("misformed inputline  : " + line)
        elif(return_code == 0):
            valid += 1
print(valid)  

#Question 2
valid = 0
with open('day2_input') as f:
    for line in f:
        return_code = check_password_two(line)
        if(return_code == 2):
            print("misformed inputline  : " + line)
        elif(return_code == 0):
            valid += 1
print(valid)
