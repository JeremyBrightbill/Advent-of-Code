"""Handy Haversacks"""
DAY: int = 7

from utilities import *

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

def find_if_holds(bag: str, target: str = "shiny gold") -> bool:
    """Recursively check if a given bag can hold the target bag"""
    contents: dict = parsed[bag]

    # Base case
    if len(contents) == 0: 
        return False
    elif target in list(contents.keys()):
        return True

    # Recursive case
    else: 
        test: list = [find_if_holds(bag_type) for bag_type in contents]
        return any(test)
        

# Solve Part 2 -------------------------------

def count_contents(bag: str) -> int: 
    """Recusively count all other bags contained in a bag"""
    total: int = 0
    contents: dict = parsed[bag]
    
    # Base case: if no contents, total stays 0
    
    # Recursive case:
    if len(contents) > 0: 
        for bag_type in contents: 
            n: int = contents[bag_type]
            total += n + n * count_contents(bag_type)
    
    return total


# Output -------------------------------------

if __name__ == "__main__": 
    
    solution_1 = [find_if_holds(bag) for bag in bags_all].count(True)
    print(f"Part 1: {solution_1}")

    solution_2 = count_contents("shiny gold")
    print(f'Part 2: {solution_2}')