"""Toboggan Trajectory"""
DAY: int = 3

import math
from utilities import load_data

# Import -------------------------------------

# Puzzle input
data = load_data(2020, DAY)

# Sample data


# Solve part 1 -------------------------------

def traverse_map(map: list, slope_right: int, slope_down: int) -> int: 

    right: int = 0
    down: int = 0
    output: list = []

    # Find width of input map
    width_list: list = list(set([len(row) for row in map]))
    width: int = int(width_list[0])

    while down < len(map): 

        position: str = map[down][right]
        output.append(position)
        right += slope_right
        down += slope_down

        if right >= width: 
            right = right - width

    return output.count('#')

# Solve Part 2 -------------------------------

rights: list = [1, 3, 5, 7, 1]
downs: list = [1, 1, 1, 1, 2]


# Output -------------------------------------

if __name__ == "__main__": 

    solution_1: int = traverse_map(data, 3, 1)
    print(f'Day {DAY} Part 1: {solution_1}')

    solution_2: int = math.prod([traverse_map(data, right, down) for right, down in zip(rights, downs)])
    print(f'Day {DAY} Part 2: {solution_2}')
