def dance(array, moves):
    L = len(array)
    for m in moves:
        if m.startswith('s'):
            #spin
            n = int(m[1:])
            array = array[-n:] + array[:L-n]
            assert len(array)==L, "Length mismatch after spin: {}".format(array)
        elif m.startswith('x'):
            a, _, b = m[1:].partition('/')
            a, b = int(a), int(b)
            array[a], array[b] = array[b], array[a]
        elif m.startswith('p'):
            a_name, _, b_name = m[1:].partition('/')
            a, b = array.index(a_name), array.index(b_name)
            array[a], array[b] = array[b], array[a]
        else:
            raise(ValueError)
    return array


def part_one():
    with open("input.txt", 'r') as f:
        moves = list(f.read().strip().split(','))
    array = list("abcdefghijklmnop")
    print(*dance(array, moves), sep='')

def part_two():
    with open("input.txt", 'r') as f:
        moves = list(f.read().strip().split(','))
    array = list("abcdefghijklmnop")
    L = len(array)
    visited = []
    for i in range(1000000000):
        s = ''.join(array)
        if s in visited:
            print("cycle after {} iterations ({})".format(i, s))
            print(visited[1000000000 % i])
            break
        visited.append(s)
        array = dance(array, moves)

part_one()
part_two()
