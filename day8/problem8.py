from collections import defaultdict
import operator


if __name__ == "__main__":
    registers = defaultdict(int)
    ops = {"inc": operator.add, "dec": operator.sub, '>': operator.gt,
           '<': operator.lt, '>=': operator.ge, '<=': operator.le,
           '==': operator.eq, '!=': operator.ne}
    maxEver = 0
    with open("input.txt", 'r') as f:
        for line in f:
            [target, op, amount, _, cond] = line.strip().split(' ', maxsplit=4)
            [a, opCond, b] = cond.split(' ')
            if ops[opCond](registers[a], int(b)):
                registers[target] = ops[op](registers[target], int(amount))
                if registers[target] > maxEver:
                    maxEver = registers[target]
    print(max(registers.values()))
    print(maxEver)
