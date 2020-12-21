"""Title"""
DAY: int = 10

from utilities import load_data
from copy import deepcopy

# Import -------------------------------------

# Puzzle input
data_raw = [int(item) for item in load_data(2020, DAY)]
data = [0] + sorted(data_raw) + [max(data_raw) + 3]

# Sample data
samp1_raw: list = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
samp1: list = [0] + sorted(samp1_raw) + [max(samp1_raw) + 3]

# Solve part 1 -------------------------------

def list_differences(x: list) -> list:
    """List the differences between all items in a list"""

    output = []

    for i, item in enumerate(x[:-1]): 
        diff = x[i + 1] - item
        output.append(diff)

    return output

pt1: list = list_differences(data)
    
# Solve Part 2 -------------------------------

def choose_next(current: int, full: list) -> list:
    """Given current position in list of adapters, list all possible options
    for the next step. Original list must be sorted first. NOT RECURSIVE"""

    index: int = full.index(current)
    remaining: list = full[index + 1:]
    possible: list = []
    diff: int = 0
    #counter: int = 0

    while diff < 4: 
        for item in remaining: 
            diff = item - current
            if diff < 4: 
                possible.append(item)
                #counter += 1
        # for adapter in possible: 
        #     choose_next(adapter, full)

    return possible

def count_solutions(current: int, full: list) -> int:
    """Given current position in (sorted) full list of adapters, counts all possible 
    options for the next step. Then runs recursively to count all options for every step 
    after that."""

    target: int = full[-1]
    index: int = full.index(current)
    remaining: list = full[index + 1:]
    counter: int = 0

    # base case
    if current == target: 
        return counter

    # recursive case
    possible: list = []
    for item in remaining: 
        diff = item - current
        if diff > 3: 
            break
        else: 
            possible.append(item)
            counter += 1
            # possible2: list = []
    for adapter in possible: 
        print(adapter)
        counter += count_solutions(adapter, full)

    return counter

    # THIS IS ON THE RIGHT TRACK, it finds all solutions, but not in a countable way
    # Somehow keep track of the decisions all the way along, return not a count but 
    # all combinations


# Output -------------------------------------

if __name__ == "__main__": 
    
    solution_1: int = pt1.count(1) * pt1.count(3)
    print(f'Part 1: {solution_1}')

    test1: list = count_solutions(0, samp1)

    print(samp1)
    solution_2: list = test1
    print(f'Part 2: {solution_2}')