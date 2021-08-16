"""--- Day 13: Shuttle Search ---
https://adventofcode.com/2020/day/13"""

DAY: int = 13

from utilities import *
from numpy import lcm

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

data2: list = [i if i == 'x' else int(i) for i in data_raw[1].split(',')]

buses: list = [x for x in data2 if x != 'x']
buses.sort(reverse=True)

def find_relative_times(buses: list, data: list) -> dict: 
    """Find the time lag from each bus to the next in order of shortest
    to longest period"""

    output: dict = {}

    for i, bus in enumerate(buses[:-1]): 
        output[bus] = data.index(buses[i+1]) - data.index(bus)

    return output

relative_times: dict = find_relative_times(buses, data2)

# New plan: start with 643 and 509. 
def find_time2():
    return None

# def find_time_old(buses: list = buses, reqs: list = relative_times) -> bool: 
#     """Docstring"""
    
#     first: int = buses[0]
#     timestamp: int = 0

#     while True: 
        
#         for bus in buses[1:]: 
#             time_next: int = timestamp + reqs[bus]
#             if time_next % bus != 0: 
#                 timestamp += first
#                 break
#             else:
#                 continue
          
#     return timestamp

def find_next_time(increase_by: int, target_bus: int, offset: int, fixed: bool) -> int:
    """increase_by is either 1st bus's period OR period when several 
    previous buses repeat. target_bus is the period of target bus. offset 
    is the time the target bus must differ from the previous. If fixed=True, 
    returns the time of the initial bus, not the target bus"""

    start_time: int = increase_by

    while True: 

        time_next: int = start_time + offset
        if time_next % target_bus == 0: 
            if fixed: 
                return start_time
            else: 
                return time_next
        else: 
            start_time += increase_by


def find_times_all(data: list, buses: list, reqs: list) -> int: 
    """This gets us to the point where the first bus crosses. Now for the remaining 2, 
    with periods shorter than it. """

    increase_by: int = reqs[buses[0]]
    timestamp: int = buses[0]
    
    for i, bus in enumerate(buses): 

        next_bus: int = buses[i+1]
        
        if bus != data[0]: 
            offset: int = data.index(next_bus) - data.index(bus)
            next_time: int = find_next_time(increase_by, next_bus, offset, False)
            timestamp = next_time
            increase_by = timestamp
            print(f'bus: {next_bus}, timestamp: {timestamp}')
            
            
        else: 
            start_time = timestamp
            while True: 
                next_time = start_time + timestamp
                print(next_time)
                bus17 = next_time + data.index(17)
                bus13 = next_time + data.index(13)
                if bus17 % 17 == 0 and bus13 % 13 == 0: 
                    return next_time
                else: 
                    start_time += timestamp 
            # target: int = find_next_time(increase_by, next_bus, offset, False)
            # print(f'bus: {bus}, timestamp: {target}')
            # target1: int = find_next_time(target, 17, reqs[17], False)
            # print(f'bus: {17}, timestamp: {target1}')
            #break
            # return output
            
            # Find the last two
            #target1: int = find_next_time(target, )




def find_time3(timestamp: int, increase_by: int, buses: list, reqs: dict) -> int: 
    """"""
    # Starts at timestamp=0, buses and reqs
    # This will be the recursive case
    # Increase timestamp by bus[0]
    # Check if bus[1] is in required position
    # If not: increase timestamp by bus[0] and check again, etc.
    # If yes: call find_time() again:
        # with timestamp updated to the new time
        # with the first bus removed from the list
        # Now, increase timestamp by starting timestamp each time
    # TO ADD: once we find a time when the FIRST bus coincides, make that our ref point
        # From there, we only need to find 17 and 13 (36 and 36 ahead, respectively)       
    
    while True:

        if reqs[buses[0]] != 0:
            # recursive case PROBLEM IS HERE: it doesn't stop when it reaches the base case
            time_next: int = timestamp + reqs[buses[0]]
            if time_next % buses[1] == 0: 
                print(f'Bus: {buses[1]}, Timestamp: {time_next}')
                find_time(timestamp=time_next, increase_by=time_next, buses=buses[1:], reqs=reqs)
            else: 
                timestamp += increase_by

        else: 
            print("The end")
            break
        #     # base case
        #     time_next: int = timestamp + reqs[buses[1]]
        #     if time_next % buses[1] == 0 and (time_next+1) % buses[2] == 0: 
        #         return f'Final timestamp: {timestamp}'
        #         break
        #     else: 
        #         #print(timestamp)
        #         timestamp += increase_by 
        # # recursive case
        # else: 
        #     while True:
                
    
# Output -------------------------------------

if __name__ == "__main__": 
    
    solution_1 = pt1_bus * wait1
    print(f'Part 1: {solution_1}')

    print(data2)
    print(buses)
    print(relative_times)
    # solution_2 = find_times_all(data2, buses, relative_times)
    # print(f'Part 2: {solution_2}') # 104611117548 wrong