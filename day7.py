#!/usr/bin/python3
import regex as re
rules = {}
with open('day7_input') as f:
    for line in f.read().splitlines():
        color, rule = re.match(re.compile(r'(\w+ \w+) bags contain (.*)'), line).groups()
        rules[color] = [(int(match.group(1)), match.group(2)) for match in re.finditer(re.compile(r'(\d+) (\w+ \w+) bags?'), rule)]

result = set()
def check(target_color):
    for color, contains in rules.items():
        if any(sub_color == target_color for _, sub_color in contains):
            result.add(color)
            check(color)

def check_count(color):
    return 1 + sum(count * check_count(sub_color) for count, sub_color in rules[color])

check("shiny gold")
print(len(result))
print(check_count("shiny gold") - 1)







