from utilities import *

DAY: int = 6

# Import ------------------------------------------------------

data: str = load_raw(2020, DAY)

parsed: list = [item.replace('\n', ' ') for item in data.split('\n\n')]

# Solve parts 1 and 2 (together) ------------------------------

def count_group(group: str, method: str) -> int: 

    people: list = [set(person) for person in group.split(' ')]

    if method == "any":
        return len(set.union(*people))
    elif method == "every":
        return len(set.intersection(*people))
    else:
        return "Invalid method"


# Output -------------------------------------

if __name__ == "__main__": 
    
    solution_1: int = sum(count_group(group, "any") for group in parsed)
    print(f'Part 1: {solution_1}')

    solution_2: int = sum(count_group(group, "every") for group in parsed)
    print(f'Part 2: {solution_2}')