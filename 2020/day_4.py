from utilities import load_raw

DAY: int = 4

# Import -------------------------------------

# Puzzle input

data = load_raw(2020, DAY)

# Sample data



# Solve part 1 -------------------------------

def parse_day4(data: str) -> list:
    passports1: list = data.split('\n\n') 
    passports2: list = [passport.replace('\n', ' ') for passport in passports1]
    return passports2

passports: list = parse_day4(data)

def validate_pt1(string: str, fields: list) -> bool:
    return all(field in string for field in fields)

# string = 'abc def ghi jkl'
fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

# Solve Part 2 -------------------------------

# Create dictionary of each...


# Output -------------------------------------

if __name__ == "__main__": 
    
    solution_1 = [validate_pt1(passport, fields) for passport in passports]
    print(f'Part 1: {solution_1.count(True)}')

    # solution_2 = 
    # print(f'Part 2: {solution_2}')