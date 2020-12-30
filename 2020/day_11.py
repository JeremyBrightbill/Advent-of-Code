"""Seating System"""
DAY: int = 11

from utilities import *

# Import -------------------------------------

# Puzzle input
data = load_data(2020, DAY)

# Sample data

samp1 = ['L.LL.LL.LL', 'LLLLLLL.LL', 'L.L.L..L..', 'LLLL.LL.LL', 'L.LL.LL.LL' \
, 'L.LLLLL.LL', '..L.L.....', 'LLLLLLLLLL', 'L.LLLLLL.L', 'L.LLLLL.LL']

# Solve part 1 -------------------------------

class Room: 

    def __init__(self, seating: list, max_occupied: int): 
        """Initialize based on empty seating chart. Determine dimensions"""
        self.chart = seating
        self.max_occupied = max_occupied
        self.x_len = len(seating[0])
        self.y_len = len(seating)

    def find_adjacent(self, x: int, y: int) -> list: 
        """Find contents of all spots adjacent to given coordinate position."""

        if x < 0 or x >= self.x_len: 
            raise ValueError("Invalid x-coordinate")
        elif y < 0 or y >= self.y_len: 
            raise ValueError("Invalid y-coordinate")

        top: int = y-1
        bottom: int = y+1
        left: int = x-1
        right: int = x+1

        spots: list = [ \
            self.chart[top][left] if y > 0 and x > 0 else None, \
            self.chart[top][x] if y > 0 else None, \
            self.chart[top][right] if y > 0 and x < self.x_len-1 else None, \
            self.chart[y][left] if x > 0 else None, \
            self.chart[y][right] if x < self.x_len-1 else None, \
            self.chart[bottom][left] if y < self.y_len-1 and x > 0 else None, \
            self.chart[bottom][x] if y < self.y_len-1 else None, \
            self.chart[bottom][right] if y < self.y_len-1 and x < self.x_len-1 else None]

        return [_ for _ in spots if _]

    def find_first_visible(self, x: int, y: int, change_x: int, change_y: int) -> str:
        """Find the contents of the first visible chair in a given direction. For use
        inside find_visible method"""

        output: str = None
        
        while True: 

            x += change_x
            y += change_y
            
            if x > self.x_len-1 or x < 0 or y > self.y_len-1 or y < 0: 
                break
            elif self.chart[y][x] in ['L', '#']:
                output = self.chart[y][x]
                break
            else: 
                continue

        return output

    def find_visible(self, x: int, y: int) -> list:
        """Find contents of first seat visible in each direction from given 
        coordinate position."""

        if x < 0 or x >= self.x_len: 
            raise ValueError("Invalid x-coordinate")
        elif y < 0 or y >= self.y_len: 
            raise ValueError("Invalid y-coordinate")

        output: list = []

        for change_x in [-1, 0, 1]:
            for change_y in [-1, 0, 1]: 

                if not (change_x == 0 and change_y == 0): 
                    output.append(self.find_first_visible(x, y, change_x, change_y))

        return output

    def apply(self, method: str): 
        """Apply a single round of the seating rules to all seats simultaneously"""

        if method not in ['adjacent', 'sight']: 
            raise ValueError("Method must be 'adjacent' or 'sight'")

        occupied: int = 0
        output: list = []

        for y, y_content in enumerate(self.chart): 

            new_y: list = []
            
            for x, x_content in enumerate(y_content): 
                
                if method == 'adjacent':
                    test: list = self.find_adjacent(x, y)
                else: # method == 'sight'
                    test: list = self.find_visible(x, y)
                
                if x_content == 'L' and test.count('#') == 0:
                    new_y.append('#')
                elif x_content == '#' and test.count('#') >= self.max_occupied:
                    new_y.append('L')
                else: 
                    new_y.append(x_content)

            occupied += new_y.count('#')
            output.append(new_y)
            
        self.chart = output
        return occupied

    def find_equilibrium(self, method: str):
        """Apply repeated rounds of the seating rules until equilibrium is reached"""

        if method not in ['adjacent', 'sight']: 
            raise ValueError("Method must be 'adjacent' or 'sight'")

        first_round: int = self.apply(method=method)
        
        while True: 

            next_round: int = self.apply(method=method)
            if next_round == first_round: 
                return next_round
            else: 
                first_round = next_round

test1 = Room(samp1, max_occupied=4)
pt1 = Room(data, max_occupied=4)

# Solve Part 2 -------------------------------

test2 = Room(samp1, max_occupied=5)
pt2 = Room(data, max_occupied=5)

# Output -------------------------------------

if __name__ == "__main__": 
    
    solution_1 = pt1.find_equilibrium(method='adjacent')
    print(f'Part 1: {solution_1}')

    solution_2 = pt2.find_equilibrium(method='sight')
    print(f'Part 2: {solution_2}')