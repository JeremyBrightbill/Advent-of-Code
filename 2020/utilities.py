"""Utility functions for use in all Advent of Code exercises"""

def load_data(day: int) -> str:
    path: str = f'2020/data/{str(day)}.txt'
    with open(path) as f:
        program = f.read()
    return program

x = 3