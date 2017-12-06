def load_balance(banks):
    n = len(banks)
    maxIndex, maxVal = max(enumerate(banks), key = lambda x: x[1])
    banks[maxIndex] = 0
    for i in range(n):
        banks[(maxIndex + 1 + i) % n] += int(maxVal / n)
        if  i < maxVal % n:
            banks[(maxIndex + 1 + i) % n] += 1


# banks = [0, 2, 7, 0]
with open("input.txt", 'r') as f:
    banks = list(map(int, f.read().strip().split('\t')))
n = len(banks)
seen = set()
count = 0
# checksum = sum(banks)
while tuple(banks) not in seen:
    seen.add(tuple(banks))
    load_balance(banks)
    # assert(sum(banks) == checksum)
    count += 1
print(count)
firstSeen = tuple(banks)
load_balance(banks)
count = 1
while tuple(banks) != firstSeen:
    load_balance(banks)
    count += 1
print(count)
