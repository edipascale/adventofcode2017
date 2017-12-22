from collections import defaultdict
from threading import Thread
from queue import Queue
from sys import exit

def soundcard(commands):
    registers = defaultdict(int)
    lastPlayed = None
    row = 0
    while row >=0 and row < len(commands):
        command, x, *y = commands[row].strip().split(' ')
        if y:
            y = registers[y[0]] if y[0].isalpha() else int(y[0])
        if command == "snd":
            x = registers[x] if x.isalpha() else int(x)
            lastPlayed = x
        elif command == "set":
            registers[x] = y
        elif command == "add":
            registers[x] += y
        elif command == "mul":
            registers[x] = registers[x] * y
        elif command == "mod":
            registers[x] = registers[x] % y
        elif command == "rcv":
            x = registers[x] if x.isalpha() else int(x)
            if x != 0:
                print("recover applies:", lastPlayed)
                break
        elif command == "jgz":
            row = row + y if registers[x] > 0 else row + 1
        else:
            raise(ValueError)
        if command != "jgz":
            row += 1

def run(commands, p, sendQueue, rcvQueue):
    registers = defaultdict(int)
    registers['p'] = p
    row = 0
    global count
    while row >=0 and row < len(commands):
        command, x, *y = commands[row].strip().split(' ')
        if y:
            y = registers[y[0]] if y[0].isalpha() else int(y[0])
        if command == "snd":
            x = registers[x] if x.isalpha() else int(x)
            sendQueue.put(x)
            if p == 1:
                count += 1
        elif command == "set":
            registers[x] = y
        elif command == "add":
            registers[x] += y
        elif command == "mul":
            registers[x] = registers[x] * y
        elif command == "mod":
            registers[x] = registers[x] % y
        elif command == "rcv":
            registers[x] = rcvQueue.get()
        elif command == "jgz":
            x = registers[x] if x.isalpha() else int(x)
            row = row + y if x > 0 else row + 1
        else:
            raise(ValueError)
        if command != "jgz":
            row += 1


count = 0

def part_two(filename):
    with open(filename, 'r') as f:
        commands = f.readlines()
    toA = Queue()
    toB = Queue()
    A = Thread(target=run, args=(commands, 0, toB, toA))
    B = Thread(target=run, args=(commands, 1, toA, toB))

    A.start()
    B.start()

    B.join(timeout=1)
    if B.is_alive():
        print(count)
    exit()


def part_one(filename):
    with open(filename, 'r') as f:
        commands = f.readlines()
    soundcard(commands)

part_one("input.txt")
part_two("input.txt")
