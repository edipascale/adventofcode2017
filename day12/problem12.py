from collections import defaultdict

def group(pipes, node):
    connected = set([node])
    stack = list(pipes[node])
    while stack:
        current = stack.pop()
        if current not in connected:
            connected.add(current)
            stack.extend((elem for elem in pipes[current] if elem not in stack and elem not in connected))
    return connected

def part_one_and_two():
    pipes = defaultdict(set)
    allNodes = set()
    with open('input.txt', 'r') as f:
        for line in f:
            node, _, connections = line.partition(' <-> ')
            node = int(node)
            allNodes.add(node)
            connections = set(map(int, connections.strip().split(', ')))
            pipes[node] = connections
            # should I add node to the sets in pipe[connections] too?
    g = group(pipes, 0)
    print(len(g))
    totalGroups = 0
    while len(allNodes) > 0:
        elem = allNodes.pop()
        connected = group(pipes, elem)
        allNodes -= connected
        totalGroups += 1
    print(totalGroups)

part_one_and_two()
