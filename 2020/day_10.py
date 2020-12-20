"""Title"""
DAY: int = 10

from utilities import load_data

# Import -------------------------------------

# Puzzle input
# data_raw = [int(item) for item in load_data(2020, DAY)]
# data = [0] + sorted(data_raw) + [max(data_raw) + 3]

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

#pt1: list = list_differences(data)
    
# Solve Part 2 -------------------------------

def find_omissible(x: list) -> list:

    # Make sure sorted
    x = sorted(x)
    output: list = []

    for i, item in enumerate(x[:-1]):
        if i > 0 and x[i+1] - x[i-1] <= 3: 
            output.append(item)
    
    return output

test1: list = find_omissible(samp1)

# Output -------------------------------------

if __name__ == "__main__": 
    
    # solution_1: int = pt1.count(1) * pt1.count(3)
    # print(f'Part 1: {solution_1}')

    solution_2: list = test1
    print(f'Part 2: {solution_2}')