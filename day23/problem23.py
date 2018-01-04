from collections import defaultdict
import math

def count_mul(commands):
    registers = defaultdict(int)
    mulCount = 0
    row = 0
    valid = list("abcdefgh")
    def value(e):
        return registers[e] if e in valid else int(e)
    while row >=0 and row < len(commands):
        command, x, y = commands[row].strip().split(' ')
        if command == "set":
            registers[x] = value(y)
        elif command == "sub":
            registers[x] -= value(y)
        elif command == "mul":
            mulCount += 1
            registers[x] *= value(y)
        elif command == "jnz":
            row = row + value(y) if value(x) != 0 else row + 1
            continue
        else:
            raise(ValueError)
        row += 1
    print(mulCount)

def part_one(filename):
    with open(filename, 'r') as f:
        commands = f.readlines()
    count_mul(commands)

def part_two():
    h = 0
    for x in range(109900, 126900 + 1, 17):
        if any(x % i == 0 for i in range(2, int(math.sqrt(x) + 1))):
            h += 1
    print(h)

part_one("input.txt")
part_two()
