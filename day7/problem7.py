from collections import deque, Counter

class Node:
    def __init__(self, name, weight=0):
        self.name = name
        self.parent = None
        self.children = []
        self.weight = weight
        self.totalWeight = weight
        self.balanced = True

    def addChild(self, child):
        self.children.append(child)
        child.parent = self
        self.totalWeight += child.weight
        self.checkBalance()
        if self.parent:
            self.parent.notifyNewWeight(child.weight)

    def addChildren(self, children):
        for c in children:
            self.addChild(c)

    def changeWeight(self, newWeight):
        # print(self.weight, self.totalWeight, newWeight)
        weightDiff = newWeight - self.weight
        self.totalWeight += weightDiff
        self.weight = newWeight
        # print(self.weight, self.totalWeight, weightDiff)
        if self.parent:
            self.parent.notifyNewWeight(weightDiff)

    def notifyNewWeight(self, weightDiff):
        self.totalWeight += weightDiff
        self.checkBalance()
        if self.parent:
            self.parent.notifyNewWeight(weightDiff)

    def checkBalance(self):
        if len(set((c.totalWeight for c in self.children))) > 1:
            self.balanced = False
        else:
            self.balanced = True

    def __repr__(self):
        return "<Node name:{} weight:{} total:{}>".format(
            self.name, self.weight, self.totalWeight
        )


def loadBalance(root):
    current = root
    workToDo = False
    while not current.balanced:
        workToDo = True
        print (current.name, "is unbalanced -> ", [
               c.totalWeight for c in current.children])
        # there is only one so we only need to find it
        try:
            child = next(c for c in current.children if not c.balanced)
        except:
            break
        current = child
    if not workToDo:
        return True
    weights = [c.totalWeight for c in current.children]
    count = Counter(weights)
    problem = next(c for c in count if count[c] == 1)
    weights.remove(problem)
    newWeight = weights.pop()
    problemChild = next(c for c in current.children if c.totalWeight == problem)
    print("Balancing {} from {} to {}".format(problemChild.name, problem, newWeight))
    difference = newWeight - problem
    problemChild.changeWeight(problemChild.weight + difference)
    return False



nodes = {}
rootCandidates = set()
nonRoots = set()
with open('input.txt', 'r') as f:
    for line in f:
        name = line.split(' ')[0]
        weight = int(line.split(' ')[1].lstrip('(').rstrip(')\n '))
        if name in nodes:
            nodes[name].changeWeight(weight)
        else:
            nodes[name] = Node(name, weight)
        (_, _, children) = line.partition('-> ')
        if children != '':
            children = [c.rstrip(',\n') for c in children.split(' ')]
            rootCandidates.add(name)
            nonRoots = nonRoots | set(children)
            for c in children:
                if c not in nodes:
                    nodes[c] = Node(c)
                nodes[name].addChild(nodes[c])
root = (rootCandidates - nonRoots).pop()
print(root)
#print(*(c.name for c in nodes[root].children), sep=' ')
print(nodes[root])
loadBalance(nodes[root])
print(nodes[root])
loadBalance(nodes[root])
