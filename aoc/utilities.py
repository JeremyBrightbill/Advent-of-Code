"""Utility functions for use in all Advent of Code exercises"""

def load_data(year: int, day: int) -> str:
    path: str = f'data/{str(year)}/{str(day)}.txt'
    with open(path) as f:
        program = f.read()
    return program

x = 3