
def func(f):
    start = 1
    ret = f(start)
    while True:
        start += 1
        yield ret
        ret = f(start)


def tr_f(x):
    return x * (x + 1) / 2


def pe_f(x):
    return x * (3 * x - 1) / 2


def he_f(x):
    return x * (2 * x - 1)


def solution():

    t = func(tr_f)
    p = func(pe_f)
    h = func(he_f)

    s = [t.next(), p.next(), h.next()]
    op = [t, p, h]

    while True:
        if all([s[0] == s[1], s[0] == s[2]]):
            if s[0] > 40755:
                return s
            s[0] = t.next()
        else:
            m = min(s)
            index = s.index(m)
            s[index] = op[index].next()


print solution()
