"""--- Day 9: Encoding Error ---
https://adventofcode.com/2020/day/9"""

DAY: int = 9

from utilities import *

# Import -------------------------------------

# Puzzle input
data_raw: list = load_data(2020, DAY)
data: list = [int(item) for item in data_raw]

# Sample data
samp1: list = [35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, \
    182, 127, 219, 299, 277, 309, 576]


# Solve part 1 -------------------------------

def find_first_invalid(program: list, n: int) -> int: 
    """A valid number in the program must be a sum of two of the preceding n digits. 
    Function to find the first invalid number in the program."""
    lines: list = []
        
    for i in enumerate(program): 
        index: int = i[0]
        if index >= n: 
            current_digit: int = i[1]
            preceding: list = program[index-n:index]
            test: bool = find_match(preceding, current_digit) is not None
            lines.append((i, test))

    return [x[0] for x in lines if not x[1]][0]
        
pt1_target = find_first_invalid(data, 25)[1]


# Solve Part 2 -------------------------------

def find_contiguous(program: list, target: int, max_search: int) -> list: 
    """Find group of at least 2 contiguous numbers in the program that sum to the target. 
    Start with n = 2 and increment. Includes a max_search to limit the size of n."""

    n: int = 2

    while n < max_search: 

        start: int = 0
        stop: int = start + n

        while stop <= len(program): 
            
            group: list = program[start:stop]
            if sum(group) == target: 
                return group 
            else: 
                start += 1
                stop += 1

        n += 1

matching_group: list = find_contiguous(data, pt1_target, 1000)

# Output -------------------------------------

if __name__ == "__main__": 
    
    solution_1 = pt1_target
    print(f'Part 1: {solution_1}')
    
    solution_2 = min(matching_group) + max(matching_group)
    print(f'Part 2: {solution_2}')