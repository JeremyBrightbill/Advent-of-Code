from utilities import load_data

# Import -------------------------------------

# Sample data

#        NOT AVAILABLE FOR THIS ONE

# Puzzle input

data = load_data(2020, 3)

# Solve part 1 -------------------------------

def tree_or_open(line: str, index: int) -> str:
    return line[index]

# print(tree_or_open(data[0], 2))

def traverse_map(map: list, slope_x: int, slope_y: int) -> list: 

    x: int = 0
    y: int = 0
    output: list = []

    # Find width of input map
    width_list: list = list(set([len(row) for row in map]))
    width: int = int(width_list[0])

    while y < len(map): 

        position = map[y][x]
        output.append(position)
        x += slope_x
        y -= slope_y

        if x >= width: 
            x = x - width

    return output

findings: list = traverse_map(data, slope_x = 3, slope_y = -1)
print(findings.count('#'))

# Solve Part 2 -------------------------------