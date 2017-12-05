# from sys import exit
with open("input.txt", 'r') as f:
    instr = [int(line.rstrip('\n')) for line in f]
#instr = [0, 3, 0, 1, -3]
count = 0
current = 0
while True:
    #print("Step {}: index {}, jump {}".format(count, current, instr[current]))
    count += 1
    n = current + instr[current]
    instr[current] = instr[current] + 1 if instr[current] < 3 else instr[current] - 1
    if n >= len(instr) or n < 0:
        break
    current = n
print(count)
