def part_one(filename):
    pos, vel, acc = {}, {}, {}
    with open(filename, 'r') as f:
        for i, line in enumerate(f):
            start = line.index('<') + 1
            end = line.index('>')
            p_list = list(map(int,line[start:end].split(',')))
            pos[i] = sum(list(map(abs, p_list)))
            start = line.index('<', end) + 1
            end = line.index('>', start)
            p_list = list(map(int,line[start:end].split(',')))
            vel[i] = sum(list(map(abs, p_list)))
            start = line.index('<', end) + 1
            end = line.index('>', start)
            p_list = list(map(int,line[start:end].split(',')))
            acc[i] = sum(list(map(abs, p_list)))
    m = min(acc.values())
    candidates = [x for x in acc if acc[x] == m]
    print(candidates)
    if len(candidates) > 1:
        m = min((vel.get(x) for x in candidates))
        newCandidates = [x for x in candidates if vel[x] == m]
        print(newCandidates)
        if len(newCandidates) > 1:
            m = min((vel.get(x) for x in newCandidates))
            candidates = [x for x in newCandidates if pos[x] == m]
            print(candidates)

def distance(a, b):
    return sum(list(map(abs, (b[i] - a[i] for i in range(3)))))

def part_two(filename):
    pos, vel, acc = {}, {}, {}
    remaining = set()
    with open(filename, 'r') as f:
        for i, line in enumerate(f):
            remaining.add(i)
            start = line.index('<') + 1
            end = line.index('>')
            pos[i] = list(map(int,line[start:end].split(',')))
            start = line.index('<', end) + 1
            end = line.index('>', start)
            vel[i] = list(map(int,line[start:end].split(',')))
            start = line.index('<', end) + 1
            end = line.index('>', start)
            acc[i] = list(map(int,line[start:end].split(',')))
    lastCollision = 0
    while lastCollision < 1000:
        # update all positions and velocities
        currentPos = {}
        collided = set()
        for x in remaining:
            for i in range(3):
                vel[x][i] += acc[x][i]
                pos[x][i] += vel[x][i]
            # check for collisions
            if pos[x] in currentPos.values():
                collided.add(x)
                collided = collided | set([elem for elem in currentPos.keys()
                                          if currentPos[elem] == pos[x]])
            else :
                currentPos[x] = pos[x]
        remaining = remaining - collided
        if len(remaining) < 2:
            break
        if len(collided) > 0:
            lastCollision = -1
        lastCollision += 1
    print(len(remaining))


part_one("input.txt")
part_two("input.txt")
