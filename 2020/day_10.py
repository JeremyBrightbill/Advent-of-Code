"""Title"""
DAY: int = 10

# from utilities import load_data
# from os import listdir

# Import -------------------------------------

def load_data(day: int) -> list:
    path: str = f'data/{str(day)}.txt'
    with open(path) as f:
        data = f.readlines()
    return [element.strip() for element in data] # remove \n characters
# Puzzle input
data_raw = [int(item) for item in load_data(DAY)]
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

# def find_omissible(x: list) -> list:

#     # Make sure sorted
#     x = sorted(x)
#     output: list = []

#     for i, item in enumerate(x[:-1]):
#         if i > 0 and x[i+1] - x[i-1] <= 3: 
#             output.append(item)
    
#     return output

# omissible: list = find_omissible(samp1)

# def apply_omissions(x: list, omissible_list: list) -> list:

#     output: list = []

#     for item in omissible_list: 
#         copy: list = x.copy()
#         del copy[item]
#         output.append(copy)

#     return output

# samp2: list = apply_omissions(samp1, omissible)


def omit_where_possible(x: list) -> list:
    """Function that takes an arrangement (x), determines which items are omissible, 
    and returns a list of all possible new arrangements"""

    # Make sure sorted
    x = sorted(x)
    omissible: list = []

    for i, item in enumerate(x[:-1]): # MUST BE A PROBLEM HERE!!!
        if i > 0 and x[i+1] - x[i-1] <= 3: 
            omissible.append(item)
    
    output: list = []

    for item in omissible: 
        copy: list = x.copy()
        copy.remove(item)
        output.append(copy)

    return output

# THIS IS ON THE RIGHT TRACK, just figure out how to keep track of new values. 
# Then simplify

samp2: list = omit_where_possible(samp1)

samp3: list = []

for item in samp2: 
    omitted: list = omit_where_possible(item)
    if len(omitted) > 0: 
        for sublist in omitted: 
            samp3.append(sublist)

#samp4: list = []

for item in samp3: 
    if item not in samp2: 
        samp2.append(item)



# Output -------------------------------------

if __name__ == "__main__": 
    
    solution_1: int = pt1.count(1) * pt1.count(3)
    print(f'Part 1: {solution_1}')

    print(samp2)
    # solution_2: list = test1
    # print(f'Part 2: {solution_2}')