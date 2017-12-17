from collections import Counter

def simplify_opposites(dic, a, b):
    if dic[a] > dic[b]:
        dic[a] -= dic[b]
        dic[b] = 0
    else:
        dic[b] -= dic[a]
        dic[a] = 0

def simplify_complementary(dic, a, b, c):
    m = min(dic[a], dic[b])
    dic[a] -= m
    dic[b] -= m
    dic[c] += m

def brute_distance(movesList):
    c = Counter(movesList)
    # print(c)
    simplify_opposites(c, 'n', 's')
    simplify_opposites(c, 'nw', 'se')
    simplify_opposites(c, 'sw', 'ne')
    # print(c)
    simplify_complementary(c, 'sw', 'se', 's')
    simplify_complementary(c, 's', 'ne', 'se')
    simplify_complementary(c, 'se', 'n', 'ne')
    simplify_complementary(c, 'ne', 'nw', 'n')
    simplify_complementary(c, 'n', 'sw', 'nw')
    simplify_complementary(c, 'nw', 's', 'sw')
    # print(c)
    return sum(c.values())

def part_one():
    with open("input.txt", 'r') as f:
        moves = list(f.read().strip().split(','))
    print(brute_distance(moves))

def part_two():
    with open("input.txt", 'r') as f:
        moves = list(f.read().strip().split(','))
    maxDistance = 0
    for i in range(1, len(moves)):
        current = brute_distance(moves[:i])
        if current > maxDistance:
            maxDistance = current
    print(maxDistance)

part_two()
