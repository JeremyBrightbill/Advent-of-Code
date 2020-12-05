"""Utility functions for use in all Advent of Code exercises"""

def load_data(year: int, day: int) -> list:
    path: str = f'{str(year)}/data/{str(day)}.txt'
    with open(path) as f:
        data = f.readlines()
    return [element.strip() for element in data] # remove \n characters

