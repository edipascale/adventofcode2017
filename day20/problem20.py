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


part_one("input.txt")
