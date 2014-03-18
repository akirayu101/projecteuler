from math import sqrt


def is_prime(_val):
    for i in xrange(2, int(sqrt(_val)) + 1):
        if _val % i == 0:
            return False
    return True


def solution():
    primes = [i for i in range(2, 1000000) if is_prime(i)]

    def inner(length):
        if sum(primes[0:length]) > 1000000:
            return False, 0
        for x in xrange(len(primes) - length):
            val = sum(primes[x:x + length])
            prime_i = is_prime(val)
            if all([prime_i, val < 1000000]):
                return True, val
        return None, 0
    # binary search

    def binary_search(low, high, f, b, direct):
        mid = (low + high) / 2
        while low <= high:
            mid = (low + high) / 2
            if low == mid:
                return mid
            elif f(mid)[0] == b:
                if direct:
                    low = mid
                else:
                    high = mid
            else:
                if direct:
                    high = mid - 1
                else:
                    low = mid + 1
    low = binary_search(0, len(primes), inner, True, 1)
    high = binary_search(0, len(primes), inner, False, 0)

    max_sequence = 0
    max_num = low
    for x in range(low, high):
        ok, val = inner(x)
        if ok:
            if val > max_sequence:
                max_sequence = val
                max_num = x
    return max_sequence, max_num


print solution()
