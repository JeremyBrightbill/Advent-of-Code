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

fields_pt1 = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

# Solve Part 2 -------------------------------

def validate_field(fname: str, fval: str) -> bool:

    test: bool = False

    if fname == 'byr':
        if fval.isdecimal(): 
            test = int(fval) >= 1920 and int(fval) <= 2002
    elif fname == 'iyr':
        if fval.isdecimal():
            test: bool = int(fval) >= 2010 and int(fval) <= 2020
    elif fname == 'eyr':
        if fval.isdecimal():
            test: bool = int(fval) >= 2020 and int(fval) <= 2030
    elif fname == 'hgt':
        if len(fval) >= 4: 
            units: str = fval[-2:]
            if units == 'cm':
                value: str = fval[:-2]
                try:
                    value = float(value)
                    test = value >= 150 and value <= 193
                except:
                    test = False
            if units == 'in':
                value: str = fval[:-2]
                try:
                    value = float(value)
                    test = value >= 59 and value <= 76
                except:
                    test = False
    elif fname == 'hcl':
        if len(fval) == 7:
            test = fval[0] == '#' and fval[1:].isalnum() and not any(x.isupper() for x in fval)
    elif fname == 'ecl':
        test = fval in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    elif fname == 'pid':
        test = len(fval) == 9 and fval.isnumeric()

    return test

fields_all: dict = {
    'byr': False, 
    'iyr': False, 
    'eyr': False, 
    'hgt': False, 
    'hcl': False, 
    'ecl': False, 
    'pid': False
}

def validate_pt2(passport: str, fields_all = fields_all, diagnostic = False) -> bool:

    fields: list = passport.split(' ')
    tests: dict = fields_all.copy()

    for field in fields:
        pair: list = field.split(':')
        if pair[0] in tests.keys():
            tests[pair[0]] = validate_field(pair[0], pair[1])
    
    if diagnostic:
        print(f'tests: {tests}\npassport: {passport}\n')
    else: 
        return all(list(tests.values()))

# Output -------------------------------------

if __name__ == "__main__": 
    
    solution_1 = [validate_pt1(passport, fields_pt1) for passport in passports]
    print(f'Part 1: {solution_1.count(True)}')

    solution_2 = [validate_pt2(passport) for passport in passports].count(True)
    print(f'Part 2: {solution_2}')