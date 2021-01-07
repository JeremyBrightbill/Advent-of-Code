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

def navigate1(commands: list) -> tuple: 
    """Navigate list of commands (each a dictionary of 'action' and 'value') and 
    return coordinates of final position"""

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
        
    return tuple(position)

test1: list = navigate1(samp1)
pt1: tuple = navigate1(data)

# Solve Part 2 -------------------------------

def cartesian_to_polar(position: list) -> list:
    """For use inside navigate_waypoint function: Convert the cartesian (x, y) 
    position of the waypoint to polar (bearing, distance, offset) so the waypoint 
    can be rotated."""

    x: int = position[0]
    y: int = position[1]

    # Treating the start of each quadrant as inclusive

    # 1st quadrant
    if x >= 0 and y > 0: 
        return [0, y, x]

    # 2nd quadrant
    elif y <= 0 and x > 0:
        return [90, x, -1*y]
    
    # 3rd quadrant
    elif x <= 0 and y < 0:
        return [180, -1*y, -1*x]
    
    # 4th quadrant
    elif y >= 0 and x < 0:
        return [270, -1*x, y]

    # origin
    else:
        return [0, 0, 0]


def polar_to_cartesian(polar: list) -> list:
    """For use inside navigate_waypoint function: Convert the polar (bearing, distance, 
    offset) position of the waypoint back to cartesian (x, y) after it is rotated."""

    bearing: int = polar[0]
    distance: int = polar[1]
    offset: int = polar[2]

    # 1st quadrant
    if bearing == 0: 
        return [offset, distance]

    # 2nd quadrant
    elif bearing == 90: 
        return [distance, -1*offset]

    # 3rd quadrant
    elif bearing == 180: 
        return [-1*offset, -1*distance]

    # 4th quadrant
    elif bearing == 270:
        return [-1*distance, offset]

    else:
        raise ValueError("Invalid bearing")


def navigate_waypoint(commands: list, verbose=False) -> tuple: 
    """Navigate list of commands (each a dictionary of 'action' and 'value') and 
    return coordinates of final position"""

    position: list = [0, 0] # x, y
    waypoint_cartesian: list = [10, 1] # x, y (relative to ship)
    waypoint_polar: list = [0, 1, 10] # bearing, distance, and offset in clockwise direction

    conversion: dict = {'N': 1, 'S': -1, 'E': 1, 'W': -1, 'L': -1, 'R': 1, 'F': 1}
    
    if verbose: 
        print(f'position: {position}, waypoint_cartesian: {waypoint_cartesian}, waypoint_polar: {waypoint_polar}')

    for command in commands: 
        
        if verbose: 
            print(f'command: {command}')
        
        change: int = command['value'] * conversion[command['action']]

        if command['action'] in ['N', 'S']: 
            waypoint_cartesian[1] += change # in y
            waypoint_polar = cartesian_to_polar(waypoint_cartesian)
        elif command['action'] in ['E', 'W']: 
            waypoint_cartesian[0] += change # in x
            waypoint_polar = cartesian_to_polar(waypoint_cartesian)
        elif command['action'] in ['L', 'R']: 
            
            bearing_old = waypoint_polar[0]
            bearing_new = bearing_old + change

            if bearing_new > 270:
                bearing_new -= 360
            if bearing_new < 0: 
                bearing_new += 360
            
            waypoint_polar[0] = bearing_new
            waypoint_cartesian = polar_to_cartesian(waypoint_polar)

        elif command['action'] == 'F': 
            
            position[0] += waypoint_cartesian[0] * change
            position[1] += waypoint_cartesian[1] * change

        else: 
            raise ValueError("Invalid action")
        
        if verbose: 
            print(f'position: {position}, waypoint_cartesian: {waypoint_cartesian}, waypoint_polar: {waypoint_polar}')

    return tuple(position)

test2 = navigate_waypoint(samp1)
pt2 = navigate_waypoint(data)

# Output -------------------------------------

if __name__ == "__main__": 
    
    solution_1 = abs(pt1[0]) + abs(pt1[1])
    print(f'Part 1: {solution_1}')

    solution_2 = abs(pt2[0]) + abs(pt2[1])
    print(f'Part 2: {solution_2}')