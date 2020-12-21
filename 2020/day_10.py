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
    for the next step. Original list must be sorted first. CURRENTLY NOT RECURSIVE"""

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


# def find_omissible(x: list) -> list:
#     """Test to find omissible items in list (those which would not leave a
#     gap of more than 3 between contiguous items)"""

#     # Make sure sorted
#     x = sorted(x)
#     output: list = []

#     for i, item in enumerate(x[:-1]):
#         if i > 0 and x[i+1] - x[i-1] <= 3: 
#             output.append(item)

#     return output
    

# def omit_where_possible(x: list, omissible: list) -> list:
#     """Find which elements in list (except first and last) can be omitted, 
#     if all remaining items are within 3 units of each other. Then produce list
#     with all these combinations with one item omitted"""
    
#     # Make sure sorted
#     x = sorted(x)
#     omissible_local: list = [item for item in omissible if item in x]
#     output: list = []

#     for item in omissible_local: 
#         copy: list = x.copy()
#         copy.remove(item)
#         output.append(copy)

#     return output
    
# def count_all_combos(x: list) -> list:
#     """Recursive function to find out how many combinations each level down
    
#     TO SPEED UP: Only need to find omissible once. """

#     overall: list = [x.copy()]
#     omissible_all = find_omissible(x)
#     checking_now: list = [x.copy()]
#     checking_next: list = []
#     count: int = 0

#     while len(checking_now) > 0: 
#         for item in checking_now: 
#             combos: list = omit_where_possible(item, omissible_all)
#             for combo in combos: 
#                 if combo not in overall: 
#                     overall.append(combo)
#                     count += 1
#                     print(count)
#                     if len(find_omissible(combo)) > 0:
#                         checking_next.append(combo)
#         print(f'checking_next: {len(checking_next)}')
#         checking_now, checking_next = checking_next, []
#         print(f'overall: {len(overall)}')
#     return overall  


# test1: list = count_all_combos(samp1)
# test2: list = count_all_combos(data)


# Output -------------------------------------

if __name__ == "__main__": 
    
    solution_1: int = pt1.count(1) * pt1.count(3)
    print(f'Part 1: {solution_1}')

    test1: list = choose_next(10, samp1)

    print(samp1)
    solution_2: list = test1
    print(f'Part 2: {solution_2}')