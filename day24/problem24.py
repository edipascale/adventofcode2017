
def max_bridge(seq, pieces):
    pins = seq[-1][1]
    #print(seq, strength)
    candidates = [p for p in pieces if pins in p]
    maxStrength = sum(list(map(sum, seq)))
    for c in candidates:
        newSeq = seq[:]
        newPieces = pieces[:]
        newPieces.remove(c)
        if pins == c[0]:
            newSeq.append(c)
        else:
            newSeq.append(c[::-1])
        newStrength = max_bridge(newSeq, newPieces)
        if newStrength > maxStrength:
            maxStrength = newStrength
    return maxStrength

def longest_bridge(seq, pieces):
    pins = seq[-1][1]
    #print(seq, strength)
    candidates = [p for p in pieces if pins in p]
    maxStrength = sum(list(map(sum, seq)))
    maxLen = len(seq)
    for c in candidates:
        newSeq = seq[:]
        newPieces = pieces[:]
        newPieces.remove(c)
        if pins == c[0]:
            newSeq.append(c)
        else:
            newSeq.append(c[::-1])
        newLen, newStrength = longest_bridge(newSeq, newPieces)
        if newLen > maxLen or (newLen == maxLen and newStrength > maxStrength):
            maxLen = newLen
            maxStrength = newStrength
    return maxLen, maxStrength

def part_two(filename):
    pieces = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            pieces.append(tuple(map(int, (line.strip().split('/')))))
    startList = [p for p in pieces if 0 in p]
    maxStrength = 0
    maxLength = 0
    for p in startList:
        temp = pieces[:]
        temp.remove(p)
        if (p[0] != 0 and p[1] == 0):
            p = p[::-1]
        length, strength = longest_bridge([p], temp)
        if length > maxLength or (length == maxLength and strength > maxStrength):
            maxLength = length
            maxStrength = strength
    print(maxStrength, maxLength)

part_two("input.txt")
