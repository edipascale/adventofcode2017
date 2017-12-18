from functools import reduce

def knot_hash(data, size=256, suffix=[17, 31, 73, 47, 23], rounds=64):
    lengths = list(map(ord, data.strip()))
    lengths.extend(suffix)
    current = 0
    skip = 0
    circle = list(range(size))
    for r in range(rounds):
        for l in lengths:
            if current + l <= size:
                revList = circle[current:current+l]
                circle[current:current+l] = revList[::-1]
            else:
                revList = circle[current:] + circle[:l - (size - current)]
                assert len(revList) == l, "len(revList) = {}, l = {}".format(len(revList), l)
                revList.reverse()
                circle[current:] = revList[:size - current]
                circle[:l - (size - current)] = revList[size - current:]
            current = (current + l + skip) % size
            skip += 1
    dense = [reduce((lambda x,y: x ^ y), circle[i*16:i*16 + 16]) for i in range(16)]
    return '0x' + ''.join(("{0:0{1}x}".format(elem, 2) for elem in dense))

def getRegions(grid, rows, cols):
    regions = []
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                regions.append(regionSize(grid, rows, cols, i, j))
    return regions

def regionSize(grid, rows, cols, i, j):
    if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == 0:
        return 0
    count = 1 # because grid[i][j] == 1
    grid[i][j] = 0 # visisted
    count += regionSize(grid, rows, cols, i-1, j)
    count += regionSize(grid, rows, cols, i, j-1)
    count += regionSize(grid, rows, cols, i, j+1)
    count += regionSize(grid, rows, cols, i+1, j)
    return count

def part_one_and_two():
    prefix = "oundnydw-"
    count = 0
    grid = []
    for i in range(128):
        hexa = knot_hash(prefix+str(i))
        binary = list(map(int, format(int(hexa, 16), '0128b')))
        grid.append(binary)
        # count += sum((1 for x in binary if x == '1'))
        count += sum(binary)
    print(count)

    regions = getRegions(grid, 128, 128)
    print(len(regions))

part_one_and_two()
