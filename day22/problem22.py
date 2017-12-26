from enum import Enum

stateDict = {'.': 'W', 'W': '#', '#': 'F', 'F': '.'}

class Dir(Enum):
    DOWN = 0
    LEFT = 1
    UP = 2
    RIGHT = 3

    def straight(row, col, d):
        if d == Dir.DOWN:
            return row+1, col
        elif d == Dir.LEFT:
            return row, col-1
        elif d == Dir.UP:
            return row-1, col
        else: # Dir.RIGHT
            return row, col+1

    def turn_right(d):
        return Dir((d.value + 1) % 4)

    def turn_left(d):
        return Dir((d.value - 1) % 4)

    def reverse(d):
        return Dir((d.value + 2) % 4)


def part_one(filename, iterations=10000):
    grid = {}
    with open(filename, 'r') as f:
        for row, line in enumerate(f.readlines()):
            middle = len(line.strip()) // 2
            for col, char in enumerate(line.strip()):
                grid[(row,col)] = char
    row, col = middle, middle
    count = 0
    d = Dir.UP
    for i in range(iterations):
        target = grid[(row, col)] if (row, col) in grid else '.'
        # print("grid[{},{}] = {}".format(x, y, target))
        if target == '#': #infected
            d = Dir.turn_right(d)
            grid[(row, col)] = '.'
            row, col = Dir.straight(row, col, d)
        else: #clean
            d = Dir.turn_left(d)
            grid[(row, col)] = '#'
            count += 1
            row, col = Dir.straight(row, col, d)
    print(count)

def part_two(filename, iterations=10000000):
    grid = {}
    with open(filename, 'r') as f:
        for row, line in enumerate(f.readlines()):
            middle = len(line.strip()) // 2
            for col, char in enumerate(line.strip()):
                grid[(row,col)] = char
    row, col = middle, middle
    count = 0
    d = Dir.UP
    for i in range(iterations):
        target = grid[(row, col)] if (row, col) in grid else '.'
        # print("grid[{},{}] = {}".format(x, y, target))
        if target == '#': #infected
            d = Dir.turn_right(d)
        elif target == 'W': #weakened
            count += 1
        elif target == 'F': #flagged
            d = Dir.reverse(d)
        else: #clean
            d = Dir.turn_left(d)
        grid[(row, col)] = stateDict[target]
        row, col = Dir.straight(row, col, d)
    print(count)


# part_one("input.txt", 10000)
part_two("input.txt")
