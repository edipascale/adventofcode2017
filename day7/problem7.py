from collections import deque, Counter
import networkx as nx

nodes = {}
rootCandidates = set()
nonRoots = set()
graph = nx.DiGraph()
with open('input.txt', 'r') as f:
    for line in f:
        name = line.split(' ')[0]
        weight = int(line.split(' ')[1].lstrip('(').rstrip(')\n '))
        graph.add_node(name, weight=weight)
        (_, _, children) = line.partition('-> ')
        if children != '':
            children = [c.rstrip(',\n') for c in children.split(' ')]
            rootCandidates.add(name)
            nonRoots = nonRoots | set(children)
            for c in children:
                graph.add_edge(name, c)
root = (rootCandidates - nonRoots).pop()
print(root)
#print(*(c.name for c in nodes[root].children), sep=' ')
ordered = list(nx.topological_sort(graph))
weights = {}
for node in reversed(ordered):
    w_attr = nx.get_node_attributes(graph, 'weight')
    total = w_attr[node]
    counts = Counter(weights[child] for child in graph[node])
    unbalanced = None

    for child in graph[node]:
        if len(counts) > 1 and counts[weights[child]] == 1:
            unbalanced = child
            print("Unbalanced child:", child)
            break
        val = weights[child]
        total += weights[child]

    if unbalanced:
        diff = weights[unbalanced] - val
        print(w_attr[unbalanced] - diff)
        break

    # Store the total weight of the node
    weights[node] = total
