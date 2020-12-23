"""Seating System"""
DAY: int = 11

from utilities import *

# Import -------------------------------------

# Puzzle input
data = load_data(2020, DAY)

# Sample data

samp1 = ['L.LL.LL.LL', 'LLLLLLL.LL', 'L.L.L..L..', 'LLLL.LL.LL', 'L.LL.LL.LL' \
, 'L.LLLLL.LL', '..L.L.....', 'LLLLLLLLLL', 'L.LLLLLL.L', 'L.LLLLL.LL']

# Solve part 1 -------------------------------

class Room: 

    def __init__(self, seating: list): 
        """Initialize based on empty seating chart. Determine dimensions"""
        self.arrangement = seating
        self.x_len = len(seating[0])
        self.y_len = len(seating)

    def __repr__(self): 
        return f'{self.x_len} x {self.y_len} seating matrix'

    def find_adjacent(x: int, y: int): 
        """Make list of all 8 spots adjacent to given coordinate position"""

        if x >= self.x_len or y >= self.y_len: 
            raise ValueError ("Invalid coordinate") 
        else: 
            output: list = []
            # STOPPED HERE


    # def apply(x: list = self.arrangement): 

    # def find_equilibrium()

test1 = Room(samp1)

# Solve Part 2 -------------------------------



# Output -------------------------------------

if __name__ == "__main__": 
    
    print(samp1)

    solution_1 = test1
    print(f'Part 1: {solution_1}')

    # solution_2 = 
    # print(f'Part 2: {solution_2}')