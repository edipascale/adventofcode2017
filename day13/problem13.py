def trip(layers, lastLayer, initDelay=0):
    current = 0
    totalCost = 0
    caught = False
    for i in range(lastLayer + 1):
        if i in layers and (i + initDelay) % (2 * (layers[i] - 1)) == 0:
            # print("caught at layer {} with cost {}".format(i, i*layers[i]))
            totalCost += i * layers[i]
            caught = True
    return caught, totalCost

def part_one_and_two():
    layers = {}
    with open("input.txt", 'r') as f:
        for line in f:
            [depth, scan] = list(map(int, line.strip().split(': ')))
            layers[depth] = scan
        lastLayer = depth
    _, cost = trip(layers, lastLayer)
    print(cost)
    caught = True
    i = 0
    while caught:
        i += 1
        caught, cost = trip(layers, lastLayer, initDelay=i)
    print("Not caught after delay ", i)

part_one_and_two()
