class Generator:
    divisor = 2147483647

    def __init__(self, factor, starting):
        self.factor = factor
        self.previous = starting

    def next(self):
        value = (self.previous * self.factor) % self.divisor
        self.previous = value
        return value

def judge(a, b):
    a_bin = format(a, '031b')
    b_bin = format(b, '031b')
    if a_bin[-16:] == b_bin[-16:]:
        return True
    else:
        return False

def part_one():
    A = Generator(16807, 722)
    B = Generator(48271, 354)
    count = 0
    for i in range(40000000):
        if judge(A.next(), B.next()):
            count += 1
    print(count)

def part_two():
    A = Generator(16807, 722)
    B = Generator(48271, 354)
    count = 0
    for i in range(5000000):
        a = 1
        while a % 4 != 0:
            a = A.next()
        b = 1
        while b % 8 != 0:
            b = B.next()
        if judge(a, b):
            count += 1
    print(count)

part_two()
