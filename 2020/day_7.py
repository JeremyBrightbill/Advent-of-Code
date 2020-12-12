import re
from utilities import *

DAY: int = 7

# Import -------------------------------------

# Puzzle input
data = load_data(2020, DAY)

parsed: dict = {}

for rule in data: 
    str2: list = rule.split(' contain ')
    container: str = str2[0][:-5] # chop off " bags"
    contents_raw: list = str2[1].split(', ')
    contents: dict = {}
    for item in contents_raw: 
        if item != "no other bags.":
            item2: list = item.split(' ')
            bag: str = item2[1] + ' ' + item2[2]
            number: int = int(item2[0])
            contents[bag] = number
    parsed[container] = contents

bags_all: list = list(parsed.keys())

# Solve part 1 -------------------------------

target: str = "shiny gold"
can_hold: list = []
cannot_hold: list = []
unknown: list = bags_all.copy()

def find_if_holds(container: str) -> str:

    output: str = "other"

    contents: dict = parsed[container]
    contents_keys: list = list(contents.keys())

    if len(contents_keys) == 0: 
        output = "no more" 
    else: 
        contains_target: bool = target in contents_keys
        contains_can_hold: bool = any([item in can_hold for item in contents_keys])
        if contains_target or contains_can_hold:
            output = "target" 
    
    return output


for i in range(100):
    for container in unknown: 
        contents: str = find_if_holds(container)
        if contents == "target": 
            can_hold.append(container)
            unknown.remove(container)
        elif contents == "no more": 
            cannot_hold.append(container)
            unknown.remove(container)
        else: 
            continue    

# Solve Part 2 -------------------------------

contents

def count_contents(bag: str) -> int: 
    """Find how many other bags the given bag contains"""
    output: int = 0
    contents: dict = parsed[bag]
    global examine_next
    examine_next = list(contents.keys())
    for bag in contents: 
        output += contents[bag]
        
    return output

examine_next: list = ["vibrant orange"]
running_total: int = 0

for item in examine_next:
    running_total += count_contents(item)

# target: str = "shiny gold"
# target_total_contents: int = 0

# #while True: 
# target_contents: dict = parsed[target]
# if len(target_contents) == 0: 
#     #break
#     print("done")
# else: 
#     for bag in target_contents: 
#         target_total_contents += target_contents[bag]

# Output -------------------------------------

if __name__ == "__main__": 
    
    solution_1 = len(can_hold)
    print(f"Part 1: {solution_1}")

    print(parsed["shiny gold"])
    print(running_total)
    print(examine_next)
    # solution_2 = parsed["shiny gold"]
    # print(f'Part 2: {solution_2}')