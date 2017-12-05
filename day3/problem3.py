from itertools import islice, chain

def spiral_coords(linearIndex):
    elems = 1
    n = 0
    while linearIndex > elems:
        n += 1
        prevElems = elems
        elems += 8 * n
    offset = x - prevElems - 1
    return n, offset


def linear_index(n, offset):
    return 1 + 8*n + offset


def part_one():
    x = 277678
    n, offset = spiral_coords(x)
    offset = offset % (2 * n)
    arrayGen = chain((i for i in range(2*n - 1, n, -1)), (j for j in range(n, 2*n + 1)))
    dist = next(islice(arrayGen, offset, None))
    print(dist)


def add_to_spiral(lastInserted, spiral):
    x, y = lastInserted[0], lastInserted[1]
    # move right if there is space there and something up
    if (x+1, y) not in spiral and (x, y+1) in spiral:
        # possible adjacents: up+right, up, up+left, left.
        spiral[(x+1, y)] = spiral.get((x+2, y+1), 0) + \
                           spiral.get((x+1, y+1), 0) + \
                           spiral.get((x, y+1), 0) + \
                           spiral.get((x, y), 0)
        return (x+1, y)
    # move up if there is space and there is something left
    if (x, y+1) not in spiral and (x-1, y) in spiral:
        # possible adjacents: down, down+left, left, up+left.
        spiral[(x, y+1)] = spiral.get((x, y), 0) + \
                           spiral.get((x-1, y), 0) + \
                           spiral.get((x-1, y+1), 0) + \
                           spiral.get((x-1, y+2), 0)
        return (x, y+1)
    # move left if there is space and there is something down
    if (x-1, y) not in spiral and (x, y-1) in spiral:
        # possible adjacents: right, down+right, down, down+left.
        spiral[(x-1, y)] = spiral.get((x, y), 0) + \
                           spiral.get((x, y-1), 0) + \
                           spiral.get((x-1, y-1), 0) + \
                           spiral.get((x-2, y-1), 0)
        return (x-1, y)
    # move down if there is space and there is something right
    if (x, y-1) not in spiral and (x+1, y) in spiral:
        # possible adjacents: up, up+right, right, down+right.
        spiral[(x, y-1)] = spiral.get((x, y), 0) + \
                           spiral.get((x+1, y), 0) + \
                           spiral.get((x+1, y-1), 0) + \
                           spiral.get((x+1, y-2), 0)
        return (x, y-1)
    # we should never get here
    print("ERROR add_to_spiral")
    return (0, 0)


def part_two():
    gt = 277678
    spiral = {}
    spiral[(0,0)] = 1
    spiral[(1,0)] = 1
    lastInserted = (1,0)
    i = 2
    while spiral[lastInserted] < gt:
        lastInserted = add_to_spiral(lastInserted, spiral)
        i += 1
    print(spiral[lastInserted])

if __name__ == '__main__':
    part_two()
