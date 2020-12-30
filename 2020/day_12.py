"""Rain Risk
https://adventofcode.com/2020/day/12"""

DAY: int = 12

from utilities import *

# Import -------------------------------------

# Puzzle input
data_raw: list = load_data(2020, DAY)
data: list = [{'action': i[0], 'value': int(i[1:])} for i in data_raw]

# Sample data
samp1_raw: list = ['F10', 'N3', 'F7', 'R90', 'F11']
samp1: list = [{'action': i[0], 'value': int(i[1:])} for i in samp1_raw]

# Solve part 1 -------------------------------

def navigate(commands: list) -> tuple: 
    """Navigate list of commands (each a dictionary of 'action' and 'value') and 
    return coordinates of final position (list of 2)"""

    position: list = [0, 0] # x, y
    bearing: int = 90
    conversion: dict = {'N': 1, 'S': -1, 'E': 1, 'W': -1, 'L': -1, 'R': 1, 'F': 1}

    for command in commands: 
        
        change: int = command['value'] * conversion[command['action']]

        if command['action'] in ['N', 'S']: 
            position[1] += change
        elif command['action'] in ['E', 'W']: 
            position[0] += change
        elif command['action'] in ['L', 'R']: 
            bearing += change
        elif command['action'] == 'F': 
            
            if bearing == 0: 
                position[1] += change
            elif bearing == 90: 
                position[0] += change
            elif bearing == 180: 
                position[1] -= change
            elif bearing == 270:
                position[0] -= change 
            else: 
                raise ValueError("Invalid bearing")

        else: 
            raise ValueError("Invalid action")

        if bearing > 270:
            bearing -= 360
        if bearing < 0: 
            bearing += 360
        
    return (position[0], position[1])

test1: list = navigate(samp1)
pt1: tuple = navigate(data)

# Solve Part 2 -------------------------------



# Output -------------------------------------

if __name__ == "__main__": 
    
    solution_1 = abs(pt1[0]) + abs(pt1[1])
    print(f'Part 1: {solution_1}')

    # solution_2 = 
    # print(f'Part 2: {solution_2}')