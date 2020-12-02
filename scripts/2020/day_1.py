
"""Rough draft of Day 1 part 1
This is terrible, clean up everything! In particular, set up module correctly for utilities"""

# Sample data

samp = [1721, 979, 366, 299, 675, 1456]

def compare_two(n1: int, n2: int, target: int) -> bool:
    added: int = n1 + n2
    test: bool = added == target
    return test

# print(compare_two(samp[0], samp[1], 2700))

#x = find_match(samp, 2020)
#print(x)

def load_data(year: int, day: int) -> str:
    path: str = f'data/{str(year)}/{str(day)}.txt'
    with open(path) as f:
        program = f.read()
    return program

data_raw = load_data(2020, 1)
data_split = data_raw.split('\n')
data = [int(number) for number in data_split]
#print(y)

def find_match(data: list, target: int) -> list:
    for n1 in data:
        for n2 in data: 
            match: bool = compare_two(n1, n2, target)
            if match:
                output = [n1, n2]
                return output

def compare_three(n1: int, n2: int, n3: int, target: int) -> bool:
    added: int = n1 + n2 + n3
    test: bool = added == target
    return test

def find_match3(data: list, target: int) -> list:
    for n1 in data:
        for n2 in data: 
            for n3 in data:
                match: bool = compare_three(n1, n2, n3, target)
                if match:
                    output = [n1, n2, n3]
                    return output



#solution = find_match(data, 2020)
#print(solution)
#print(solution[0] * solution[1])

solution3 = find_match3(data, 2020)
print(solution3)
print(solution3[0] * solution3[1] * solution3[2])