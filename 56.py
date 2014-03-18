def one_count(x):
    ret = 0
    while x != 0:
        x = x & (x - 1)
        ret += 1
    return ret


def num_count(x):
    return sum([int(i) for i in str(x)])


def solution():
    max_c = 0
    for (x, y) in [(x, y) for x in xrange(100) for y in xrange(100)]:
        c = num_count(pow(x, y))
        if c > max_c:
            max_c = c
    return max_c

print solution()
