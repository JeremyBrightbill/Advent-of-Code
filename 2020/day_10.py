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

# def choose_next(current: int, full: list) -> list:
#     """Given current position in list of adapters, list all possible options
#     for the next step. Original list must be sorted first. NOT RECURSIVE"""

#     index: int = full.index(current)
#     remaining: list = full[index + 1:]
#     possible: list = []
#     diff: int = 0
#     #counter: int = 0

#     while diff < 4: 
#         for item in remaining: 
#             diff = item - current
#             if diff < 4: 
#                 possible.append(item)
#                 #counter += 1
#         # for adapter in possible: 
#         #     choose_next(adapter, full)

#     return possible

# def count_solutions(current: int, full: list) -> int:
#     """Given current value in (sorted) full list of adapters, counts all possible 
#     options for the next step. Then runs recursively to count all options for every step 
#     after that."""

#     target: int = full[-1]
#     index: int = full.index(current)
#     remaining: list = full[index + 1:]
#     counter: int = 0

#     # base case
#     if current == target: 
#         return counter

#     # recursive case
#     possible: list = []
#     for item in remaining: 
#         diff = item - current
#         if diff > 3: 
#             break
#         else: 
#             possible.append(item)
#             counter += 1
#             # possible2: list = []
#     for adapter in possible: 
#         print(adapter)
#         counter += count_solutions(adapter, full)

#     return counter

#     # THIS IS ON THE RIGHT TRACK, it finds all solutions, but not in a countable way
#     # Somehow keep track of the decisions all the way along, return not a count but 
#     # all combinations


# def find_all_solutions_old(already: list, full: list) -> list: 
#     """Given values already selected in full (sorted) list of adapters, finds all 
#     possible options for the next step. Then runs recursively to find all options 
#     for every step after that, all the way to finding all possible arrangements."""

#     current: int = already[-1]
#     index: int = full.index(current)
#     remaining: list = full[index + 1:]
#     output: list = []

#     # base case  
#     if already[-1] == full[-1]: 
#         return already

#     # recursive case
#     possible_next: list = []
#     for item in remaining: 
#         if item - current <= 3: 
#             possible_next.append(item)
#         else:
#             break       

#     for adapter in possible_next: 
#         new_arrange: list = already.copy()
#         new_arrange.append(adapter)
#         output.append(find_all_solutions(new_arrange, full))
#         # solutions: list = find_all_solutions(new_arrange, full)
#         # print(solutions)
#         # for solution in solutions: 
#         #     print(solution)
#         #     #output.append(solution)

#     return output

#     # This almost works


def count_all_solutions_old(already: list, full: list) -> int: 
    """Given values already selected in full (sorted) list of adapters, finds all 
    possible options for the next step. Then runs recursively to find all options 
    for every step after that, all the way to finding all possible arrangements."""

    current: int = already[-1]
    index: int = full.index(current)
    remaining: list = full[index + 1:] # sorted(list(set(full).difference(set(already)))) #
    count: int = 0

    # base case  
    if already[-1] == full[-1]: 
        count += 1
        return count

    # recursive case
    possible_next: list = []
    for item in remaining: 
        if item - current <= 3: 
            possible_next.append(item)
        else:
            break       

    for adapter in possible_next: 
        new_arrange: list = already.copy()
        new_arrange.append(adapter)
        count += count_all_solutions(new_arrange, full)

    return count

# STILL TOO SLOW. See if it's better to only pass current, not already

def count_all_solutions(current: int, full: list) -> int: 
    """Given values already selected in full (sorted) list of adapters, finds all 
    possible options for the next step. Then runs recursively to find all options 
    for every step after that, all the way to finding all possible arrangements."""

    index: int = full.index(current)
    remaining: list = full[index + 1:] 
    
    # base case  
    if current == full[-1]: 
        return 1

    # recursive case
    count: int = 0
    possible_next: list = []

    for item in remaining: 
        if item - current <= 3: 
            possible_next.append(item)
        else:
            break       

    for choice in possible_next: 
        count += count_all_solutions(choice, full)

    return count

# I got it! First identify the points at which there is a choice. 
# Count the options at each choice point. 
# Multiply all options from all choice points. 


# Output -------------------------------------

if __name__ == "__main__": 
    
    solution_1: int = pt1.count(1) * pt1.count(3)
    print(f'Part 1: {solution_1}')

    test1 = count_all_solutions(current=0, full=samp1)

    #print(samp1)
    solution_2: list = count_all_solutions(current=data[0], full=data) 
    print(f'Part 2: {solution_2}')