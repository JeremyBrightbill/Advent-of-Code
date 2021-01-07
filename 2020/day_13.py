"""--- Day 13: Shuttle Search ---
https://adventofcode.com/2020/day/13"""

DAY: int = 13

from utilities import *

# Import -------------------------------------

# Puzzle input
data_raw = load_data(2020, DAY)
data_timestamp: int = int(data_raw[0])
data1: list = [int(i) for i in data_raw[1].split(',') if i != 'x']

# Sample data
samp1_raw: list = ['939', '7,13,x,x,59,x,31,19']
samp1_timestamp: int = int(samp1_raw[0])
samp1: list = [int(i) for i in samp1_raw[1].split(',') if i != 'x']

# Solve part 1 -------------------------------

def find_next(timestamp: int, id: int) -> int:
    """Find the next time after given timestamp when bus with given id will pass"""

    pass_time: int = 0

    while True:

        if pass_time >= timestamp:
            return pass_time
        else: 
            pass_time += id

test1: list = [find_next(samp1_timestamp, bus) for bus in samp1]

pt1: list = [find_next(data_timestamp, bus) for bus in data1]
first: int = min(pt1)
first_index = pt1.index(first)
pt1_bus: int = data1[first_index]
wait1: int = first - data_timestamp

# Solve Part 2 -------------------------------



# Output -------------------------------------

if __name__ == "__main__": 
    
    #print(data_id)

    solution_1 = pt1_bus * wait1
    print(f'Part 1: {solution_1}')

    # solution_2 = 
    # print(f'Part 2: {solution_2}')