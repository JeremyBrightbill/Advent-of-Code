"""--- Day 10: Adapter Array ---
https://adventofcode.com/2020/day/10"""

DAY: int = 10

from utilities import load_data
from functools import reduce 
import operator

# Import -------------------------------------

# Puzzle input
data_raw = [int(item) for item in load_data(2020, DAY)]
data = [0] + sorted(data_raw) + [max(data_raw) + 3]

# Sample data
samp1_raw: list = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
samp1: list = [0] + sorted(samp1_raw) + [max(samp1_raw) + 3]

samp2_raw: list = [28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38, \
    39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3]
samp2: list = [0] + sorted(samp2_raw) + [max(samp2_raw) + 3]

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

# Combinations don't multiply past the gaps of 3. Those gaps separate the full list into 
# shorter groups. The number of combinations in the group is determined by its length. 
# Combinations for the whole list are the product of all the group combinations. 

def find_group_lengths(x: list) -> list:
    """Given list of adapters, split into groups every time there is a gap of 3. 
    Return a list of the length of each group"""

    output: list = []
    count: int = 0
    
    for i, item in enumerate(x[:-1]): 
        count += 1
        diff: int = x[i + 1] - item
        if diff >= 3: 
            output.append(count)
            count: int = 0

    return output 

def count_combinations(group_len: int) -> int: 
    """Given a group length, return the number of combinations. After the first 3, 
    it's the sum of the previous 3."""

    sequence: list = [1, 1, 2]

    if group_len < 1: 
        raise ValueError ("Length must be greater than 0")
    if group_len <= 3: 
        return sequence[group_len - 1]
    else: 
        while len(sequence) < group_len: 
            next_item: int = sum(sequence[-3:])
            sequence.append(next_item)
        return sequence[-1]

group_lengths: list = find_group_lengths(data)
combos: list = [count_combinations(group) for group in group_lengths]


# Output -------------------------------------

if __name__ == "__main__": 
    
    solution_1: int = pt1.count(1) * pt1.count(3)
    print(f'Part 1: {solution_1}')

    solution_2: int = reduce(operator.mul, combos)
    print(f'Part 2: {solution_2}')