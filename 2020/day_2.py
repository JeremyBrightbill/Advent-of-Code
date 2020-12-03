import sys
from utilities import *

from collections import namedtuple

# Import -------------------------------------

# Sample data

sample1 = '13-15 b: bbbbbbbbbbbbgbb'

# Puzzle input

data_raw: str = load_data(2)
data: list = data_raw.split('\n')

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

# print(x)
# print(validate_pw(x))

data2: list = [split_element(x) for x in data]
data3: list = [validate_pw(x) for x in data2]

#print("Part 1:")
#print(data3.count(True))


# Solve Part 2 -------------------------------

def validate_pw2(pw: namedtuple) -> bool:
    position1: str = pw.password[pw.minimum - 1]
    position2: str = pw.password[pw.maximum - 1]
    
    test1: bool = position1 == pw.letter
    test2: bool = position2 == pw.letter
    count: int = sum([test1, test2])

    return count == 1
    # return position1

#print(validate_pw2(x))

data4: list = [validate_pw2(x) for x in data2]

print("Part 2:")
print(data4.count(True))