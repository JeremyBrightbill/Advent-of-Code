"""Handheld Halting"""
DAY: int = 8

from collections import namedtuple
from copy import deepcopy
from utilities import *

# Import -------------------------------------

# Puzzle input
data: list = load_data(2020, DAY)

def parse_day8(data: list) -> list:
    output: list = []
    for item in data: 
        item1: list = item.split(' ')
        item2: dict = {"op": item1[0], "arg": int(item1[1])}
        output.append(item2)
    return output

program: list = parse_day8(data)

# Sample data

samp_raw: list = ['nop +0', 'acc +1', 'jmp +4', 'acc +3', 'jmp -3', \
    'acc -99', 'acc +1', 'jmp -4', 'acc +6']
samp: list = parse_day8(samp_raw)

samp_raw2: list = ['nop +0', 'acc +1', 'jmp +4', 'acc +3', 'jmp -3', \
    'acc -99', 'acc +1', 'nop -4', 'acc +6']
samp2: list = parse_day8(samp_raw2)


# Solve part 1 -------------------------------

def run_program(program: list, verbose: bool = False) -> tuple: 
    """Run program, terminate with status 0=infinite loop starting, 1=completed. 
    Report status, accumulator value, and (if verbose) log of positions visited"""

    status: int = 0 
    accumulator: int = 0
    position: int = 0
    positions_visited: list = []
    Output = namedtuple('Output', 'status accumulator position_log')

    while True: 

        # infinite loop starting
        if position in positions_visited:
            break 

        # successful termination
        if position >= len(program): 
            status: int = 1 
            break 
        
        positions_visited.append(position)
        op: str = program[position]["op"]
        arg: int = program[position]["arg"]
        
        if op == "acc":
            accumulator += arg
            position += 1
        elif op == "jmp":
            position += arg
        elif op == "nop":
            position += 1
        else: 
            print("Error: invalid code")
            break

    if verbose: 
        return Output(status, accumulator, positions_visited)
    else: 
        return Output(status, accumulator, position_log=None)


# Solve Part 2 -------------------------------

def identify_to_change(program: list) -> tuple: 
    """Identify the single 'nop' or 'jmp' command which, if changed to the 
    other, will cause the program to terminate with status 1 (successful)"""

    output: tuple = None
    lines_to_change: list = []

    for i in enumerate(program): 
            if i[1]["op"] in ['jmp', 'nop']:
                lines_to_change.append(i[0]) # get index

    for i in lines_to_change: 
        
        copy: list = deepcopy(program)
            
        if program[i]['op'] =='jmp': 
            copy[i]['op'] = 'nop'
        elif program[i]['op'] == 'nop':
            copy[i]['op'] = 'jmp'
        else: 
            print("Error")
            break

        outcome: tuple = run_program(copy)
        
        if outcome.status == 1:
            output = outcome

    return output

# Output -------------------------------------

if __name__ == "__main__": 
    
    ex_solution = run_program(samp2, verbose=False)
    print(f'Example: {ex_solution}')

    solution_1 = run_program(program, verbose=False)
    print(f'Part 1: {solution_1}')
    
    solution_2 = identify_to_change(program)
    print(f'Part 2: {solution_2}')