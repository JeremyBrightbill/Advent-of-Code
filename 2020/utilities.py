"""Utility functions for use in all Advent of Code exercises"""

def load_data(year: int, day: int) -> list:
    path: str = f'{str(year)}/data/{str(day)}.txt'
    with open(path) as f:
        data = f.readlines()
    return [element.strip() for element in data] # remove \n characters

def load_raw(year: int, day: int) -> str:
    path: str = f'{str(year)}/data/{str(day)}.txt'
    with open(path) as f:
        data = f.read()
    return data

def compare_two(n1: int, n2: int, target: int) -> bool:
    return n1 + n2 == target

def find_match(data: list, target: int) -> list: 

    output: list = []
    
    for n1 in data:
        for n2 in data: 
            match: bool = compare_two(n1, n2, target)
            if match:
                output = [n1, n2]
                return output

