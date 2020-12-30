"""--- Day 2: Password Philosophy ---
https://adventofcode.com/2020/day/2"""

DAY: int = 2

from collections import namedtuple
from utilities import *

# Import -------------------------------------

# Sample data

sample1 = '13-15 b: bbbbbbbbbbbbgbb'

# Puzzle input

data: list = load_data(2020, DAY)

# Solve part 1 -------------------------------

# Split each element into 4 parts: 
# 1) min
# 2) max
# 3) letter 
# 4) password

def split_element(x: str) -> namedtuple:
    split_1 = x.split(' ')
    minmax: list = split_1[0].split('-')
    letter: str = split_1[1].replace(':', '')
    
    Output = namedtuple('Output', 'minimum maximum letter password')
    return Output(int(minmax[0]), int(minmax[1]), letter, split_1[2])

x = split_element(sample1)

def validate_pw(pw: namedtuple) -> bool:
    count: int = pw.password.count(pw.letter)
    return count >= pw.minimum and count <= pw.maximum

data2: list = [split_element(x) for x in data]
data3: list = [validate_pw(x) for x in data2]


# Solve Part 2 -------------------------------

def validate_pw2(pw: namedtuple) -> bool:
    position1: str = pw.password[pw.minimum - 1]
    position2: str = pw.password[pw.maximum - 1]
    
    test1: bool = position1 == pw.letter
    test2: bool = position2 == pw.letter
    count: int = sum([test1, test2])

    return count == 1

data4: list = [validate_pw2(x) for x in data2]

# Output ---------------------------------------------------

if __name__ == "__main__": 

    print("Part 1:")
    print(data3.count(True))

    print("Part 2:")
    print(data4.count(True))