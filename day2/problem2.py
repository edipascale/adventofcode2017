with open('input.txt') as f:
    checksum = 0
    for line in f:
        array = list(map(int, line.strip().split('\t')))
        # checksum += max(array) - min(array)
        addend = None
        for i in range(len(array)-1):
            for j in array[i+1:]:
                if array[i] % j == 0:
                    addend = int(array[i] / j)
                    break
                elif j % array[i] == 0:
                    addend = int(j / array[i])
                    break
            if addend:
                checksum += addend
                break
        if not addend:
            print("ERROR")
print("Checksum: ", checksum)
