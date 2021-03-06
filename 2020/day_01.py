"""--- Day 1: Report Repair ---
https://adventofcode.com/2020/day/1"""

DAY: int = 1

import sys
from utilities import compare_two, find_match, load_data

# Import -------------------------------------

# Puzzle input 
data_raw = load_data(2020, DAY)
data = [int(number) for number in data_raw]

# Sample data
samp = [1721, 979, 366, 299, 675, 1456]

# Solve part 1 ------------------------------------

# Functions are from utilities

solution = find_match(data, 2020)


# Solve part 2 -------------------------------

def compare_three(n1: int, n2: int, n3: int, target: int) -> bool:
    added: int = n1 + n2 + n3
    test: bool = added == target
    return test

def find_match3(data: list, target: int) -> list:
    for n1 in data:
        for n2 in data: 
            for n3 in data:
                match: bool = compare_three(n1, n2, n3, target)
                if match:
                    output = [n1, n2, n3]
                    return output


solution3 = find_match3(data, 2020)


if __name__ == "__main__":

    print("Part 1:")
    print(solution)
    print(solution[0] * solution[1])

    print("Part 2:")
    print(solution3)
    print(solution3[0] * solution3[1] * solution3[2])