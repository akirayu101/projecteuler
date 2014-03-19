
from math import sqrt


def gen_square():
    start = 1
    while True:
        yield start ** 2 * 2
        start += 1


def is_prime(_val):
    for i in xrange(2, int(sqrt(_val)) + 1):
        if _val % i == 0:
            return False
    return True


def gen_prime():
    i = 2
    while True:
        if is_prime(i):
            yield i
        i += 1


def solution():
    primes = []
    prime_gen = gen_prime()

    squares = []
    square_gen = gen_square()

    start = 9

    while True:
        start += 2
        while is_prime(start):
            start += 2

        next_p = prime_gen.next()
        next_square = square_gen.next()

        primes.append(next_p)
        squares.append(next_square)
        ok = False
        while any([next_p < start, next_square < start]):
            next_p = prime_gen.next()
            next_square = square_gen.next()
            primes.append(next_p)
            squares.append(next_square)
        else:
            for square in squares:
                if start - square in primes:
                    ok = True
                    break
            if not ok:
                return start

print solution()
