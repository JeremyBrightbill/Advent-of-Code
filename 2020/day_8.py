"""Handheld Halting"""

from utilities import *

DAY: int = 8

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

# Solve part 1 -------------------------------

def run_program1(program: list, verbose: bool = False) -> str: 
    """Run list of commands, stop just before 2nd pass through infinite loop
    and return value of accumulator at that point"""

    accumulator: int = 0
    position: int = 0
    positions_visited: list = []

    while True: 

        if position in positions_visited:
            break
        
        positions_visited.append(position)
        current_op: str = program[position]["op"]
        current_arg: int = program[position]["arg"]
        
        if current_op == "acc":
            accumulator += current_arg
            position += 1
        elif current_op == "jmp":
            position += current_arg
        elif current_op == "nop":
            position += 1
        else: 
            print("Error: invalid code")
            break

    if verbose: 
        return f'\naccumulator: {accumulator}\nposition: {position}\npositions_visited: {positions_visited}'
    else: 
        return f'accumulator: {accumulator}'



# Solve Part 2 -------------------------------



# Output -------------------------------------

if __name__ == "__main__": 
    
    #print(samp)
    #print(samp[0]["op"])
    #print(run_program1(samp))

    solution_1 = run_program1(program, verbose=True)
    print(f'Part 1: {solution_1}')

    # solution_2 = 
    # print(f'Part 2: {solution_2}')