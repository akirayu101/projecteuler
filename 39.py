def is_right_triangle(a, b, c):
    if a * a + b * b == c * c:
        return True
    return False


def gen_rectangle(s):
    gen = ((x, y, s - x - y) for x in xrange(1, s) for y in xrange(1, s - x))
    for (x, y, z) in gen:
        if all([x < y, y < z, x + y > z]):
            yield (x, y, z)


def solution(x):
    ret = 0
    for (a, b, c) in gen_rectangle(x):
        if is_right_triangle(a, b, c):
            ret += 1
    return ret
max_solutions = 0
max_i = 0
for i in xrange(1000):
    s = solution(i)
    if s > max_solutions:
        max_solutions = s
        max_i = i

print max_i
print max_solutions
