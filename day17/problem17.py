def part_one():
    step = 314
    buf = [0]
    pos = 0
    val = 1
    for i in range(1, 2018):
        pos = (pos + (step % i)) % i
        if pos + 1 == i:
            buf.append(val)
        else:
            buf.insert(pos + 1, val)
        pos += 1
        assert buf[pos] == val, buf[pos]
        val += 1
    L = len(buf)
    assert buf[(pos)%L] == 2017, buf[(pos)%L]
    print(buf[(pos+1)%L])

def part_two():
    step = 314
    zeroPos = 0
    afterZero = 1
    pos = 1
    for i in range(2, 50000001):
        pos = (pos + (step % i)) % i
        if pos < zeroPos:
            zeroPos += 1
        elif pos == zeroPos:
            afterZero = i
        pos += 1
    print(afterZero)


part_one()
