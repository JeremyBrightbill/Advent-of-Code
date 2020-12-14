"""Binary Boarding"""
DAY: int = 5

from utilities import *

# Import -------------------------------------

# Puzzle input
data: list = load_data(2020, DAY)

# Sample data
ex1: str = 'BFFFBBFRRR'
ex2: str = 'FFFBBBFRRR'
ex3: str = 'BBFFBBFRLL'

# Solve part 1 -------------------------------

def binary_search(code: str, lowsym: str, highsym: str) -> int:
    """Given an input code, symbol for lower ('lowsym') and upper ('highsym')
    half, conduct binary search to find result."""

    min: int = 0
    max: int = 2**len(code)

    for char in code:
        if char == lowsym:
            max = ((max - min) / 2) + min
            # print([min, max])
        else: 
            min = ((max - min) / 2) + min
            # print([min, max])
    
    return int(min)

def find_seat(code: str) -> int: 
    """Given input code, find both row number and column number and 
    from there, seat id"""
    rowcode: str = code[:7]
    colcode: str = code[7:]

    rownum: int = binary_search(rowcode, 'F', 'B')
    colnum: int = binary_search(colcode, 'L', 'R')

    return (rownum * 8) + colnum

ids_all: list = [find_seat(code) for code in data]

# Solve Part 2 -------------------------------

missing = []
for i in range(max(ids_all)):
    if i not in ids_all: 
        missing.append(i)

# Output -------------------------------------

if __name__ == "__main__": 

    solution_1 = max(ids_all)
    print(f'Part 1: {solution_1}')

    solution_2 = missing
    print(f'Part 2: {solution_2}')