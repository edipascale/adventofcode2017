from functools import reduce

def part_one():
    with open('input.txt', 'r') as f:
        lengths = list(map(int, f.read().strip().split(',')))
    current = 0
    skip = 0
    # circle = cycle(list(range(256)))
    size = 256
    circle = list(range(size))
    for l in lengths:
        if current + l <= size:
            revList = circle[current:current+l]
            circle[current:current+l] = revList[::-1]
        else:
            revList = circle[current:] + circle[:l - (size - current)]
            assert len(revList) == l, "len(revList) = {}, l = {}".format(len(revList), l)
            revList.reverse()
            circle[current:] = revList[:size - current]
            # print("Intermediate step: ", circle)
            circle[:l - (size - current)] = revList[size - current:]
        # print(circle)
        current = (current + l + skip) % size
        skip += 1
    print(circle[0] * circle[1])

def part_two():
    with open('input.txt', 'r') as f:
        lengths = list(map(ord, f.read().strip()))
    lengths.extend([17, 31, 73, 47, 23])
    current = 0
    skip = 0
    size = 256
    circle = list(range(size))
    for r in range(64):
        for l in lengths:
            if current + l <= size:
                revList = circle[current:current+l]
                circle[current:current+l] = revList[::-1]
            else:
                revList = circle[current:] + circle[:l - (size - current)]
                assert len(revList) == l, "len(revList) = {}, l = {}".format(len(revList), l)
                revList.reverse()
                circle[current:] = revList[:size - current]
                # print("Intermediate step: ", circle)
                circle[:l - (size - current)] = revList[size - current:]
            # print(circle)
            current = (current + l + skip) % size
            skip += 1
    dense = [reduce((lambda x,y: x ^ y), circle[i*16:i*16 + 16]) for i in range(16)]
    hexa = '0x' + ''.join(("{0:0{1}x}".format(elem, 2) for elem in dense))
    print(hexa)

part_two()
