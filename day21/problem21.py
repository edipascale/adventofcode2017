import numpy as np
import sys

def str_to_np(template):
    return np.array([list(w) for w in template.split('/')])

def np_to_str(array):
    return '/'.join(["".join(array[i]) for i in range(array.shape[0])])

def expand_ruleset(rules):
    for entry in list(rules.keys()):
        a = str_to_np(entry)
        for i in range(4):
            temp = np.rot90(a, k=i)
            rules[np_to_str(temp)] = rules[entry]
            rules[np_to_str(np.fliplr(temp))] = rules[entry]
            rules[np_to_str(np.flipud(temp))] = rules[entry]


def part_one(filename, iterations=5):
    rules = {}
    with open(filename, 'r') as f:
        for line in f:
            template, _, new = line.partition(' => ')
            rules[template] = str_to_np(new.strip())
    expand_ruleset(rules)
    m = str_to_np('.#./..#/###')
    for i in range(iterations):
        # print("matrix at iter {}:\n {}\n".format(i, m))
        size = m.shape[0] # square matrix
        if size % 2 == 0:
            newm = np.array([' ' for i in range(int((size/2*3)**2))]).reshape(
                            int(size/2*3), int(size/2*3))
            for j in range(int(size/2)):
                for k in range(int(size/2)):
                    subm = m[j*2:j*2 + 2, k*2:k*2 + 2]
                    out = rules[np_to_str(subm)]
                    newm[j*3:j*3 + 3, k*3:k*3 + 3] = out
        else: #size % 3 == 0
            newm = np.array([' ' for i in range(int((size/3*4)**2))]).reshape(
                            int(size/3*4), int(size/3*4))
            for j in range(int(size/3)):
                for k in range(int(size/3)):
                    subm = m[j*3:j*3 + 3, k*3:k*3 + 3]
                    out = rules[np_to_str(subm)]
                    newm[j*4:j*4 + 4, k*4:k*4 + 4] = out
        m = newm
    count = dict(zip(*np.unique(m, return_counts=True)))
    # print(m.size)
    print(count)

def test():
    s = "#./.."
    a = str_to_np(s)
    a_constr = np.array([['#', '.'],['.','.']])
    print("a is what expected? ", np.all(a == a_constr))
    news = np_to_str(a)
    print("{} => {} => {}".format(s, a, news))

part_one("input.txt")
