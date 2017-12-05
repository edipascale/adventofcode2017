with open('input.txt') as f:
    seq = list(map(int, list(f.readline().strip())))
    n = len(seq)
    offset = int(n/2)
    value = sum([seq[i] for i in range(n) if seq[i] == seq[(i+offset)%n]])
    print(value)
