def is_anagram_of(a, b):
    if len(a) != len(b):
        return False
    temp = list(b)
    for letter in (l for l in a):
        try:
            temp.remove(letter)
        except:
            return False
    return True


with open('input.txt') as f:
    correct = 0
    checked = 0
    for line in f:
        checked += 1
        passphrase = list(line.strip().split(' '))
        # if len(passphrase) < 2 or len(set(passphrase)) < len(passphrase):
        #     continue
        # correct += 1
        found = False
        for i in range(len(passphrase) - 1):
            for word in passphrase[i+1:]:
                if is_anagram_of(passphrase[i], word):
                    found = True
                    break
            if found:
                break
        if not found:
            correct += 1
print(correct, '/', checked)

print(is_anagram_of("topo", "poot"))
