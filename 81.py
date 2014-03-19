def process_input():
    matrix = []
    with open("matrix.txt") as f:
        for line in f:
            line = line.strip().split(",")
            matrix.append([int(i) for i in line])
    return matrix


def min_solution(sets, min_s, x, y):
    if min_s[x][y] != None:
        return min_s[x][y]

    if all([x > 0, y > 0]):
        min_s[x][y] = min(
            [min_solution(sets, min_s, x - 1, y), min_solution(sets, min_s, x, y - 1)]) + sets[x][y]
    elif x == 0:
        min_s[x][y] = sum(sets[0][i] for i in xrange(y + 1))
    elif y == 0:
        min_s[x][y] = sum(sets[i][0] for i in xrange(x + 1))
    return min_s[x][y]


def solution():
    min_s = [[None for i in xrange(80)] for i in range(80)]
    sets = process_input()
    min_s[0][0] = sets[0][0]
    return min_solution(sets, min_s, 79, 79)

print solution()
