def part_one(filename):
    maze = []
    with open(filename, 'r') as f:
        for line in f:
            maze.append(line.rstrip())
    # print(*maze, sep='\n')
    path, steps = explore(maze)
    print(*path, sep='')
    print(steps)

class Dir:
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

def is_path(maze, row, col):
    try:
        return row >= 0 and col >= 0 and maze[row][col] not in [' ', '\n']
    except IndexError:
        return False

def explore(maze):
    row = 0
    col = maze[0].index('|')
    stuck = False
    path = []
    d = Dir.DOWN
    steps = 0
    while not stuck:
        steps += 1
        if maze[row][col].isalpha():
            if maze[row][col] in path:
                print("Warning - passing again through", maze[row][col])
            path.append(maze[row][col])
        n_row, n_col = Dir.straight(row, col, d)
        if is_path(maze, n_row, n_col):
            row, col = n_row, n_col
        else: # we need to turn
            if d == Dir.DOWN or d == Dir.UP:
                if is_path(maze, row, col+1):
                    col += 1
                    d = Dir.RIGHT
                elif is_path(maze, row, col-1):
                    col -= 1
                    d = Dir.LEFT
                else:
                    stuck = True
                    break
            elif d == Dir.LEFT or d == Dir.RIGHT:
                if is_path(maze, row+1, col):
                    row += 1
                    d = Dir.DOWN
                elif is_path(maze, row-1, col):
                    row -= 1
                    d = Dir.UP
                else:
                    stuck = True
                    break
    return path, steps

part_one("input.txt")
