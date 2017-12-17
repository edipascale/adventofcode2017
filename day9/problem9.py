def skip_garbage(stream, index):
    current = index + 1
    garbage = 0
    while stream[current] and stream[current] != '>':
        if stream[current] == '!':
            current += 2
        else:
            current += 1
            garbage += 1
    newIndex = current + 1 if stream[current] else  None
    return newIndex, garbage


with open('input.txt', 'r') as f:
    stream = f.read().strip()
depth = 0
parentScore = 0
totalScore = 0
index = 0
totalGarbage = 0
while index < len(stream):
    if stream[index] == '{':
        depth += 1
        parentScore += 1
        totalScore += parentScore
        index += 1
    elif stream[index] == '}':
        depth -= 1
        parentScore -=1
        index += 1
    elif stream[index] == '<':
        index, garbage = skip_garbage(stream, index)
        totalGarbage += garbage
    else:
        index += 1

print(totalScore)
print(totalGarbage)
