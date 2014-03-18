from math import sqrt


def is_prime(_val):
    for i in xrange(2, int(sqrt(_val)) + 1):
        if _val % i == 0:
            return False
    return True


def rotate_str(x, n):
    return x[n:] + x[:n]


def is_clr_prime(x, primes):
    x_str = str(x)
    x_len = len(x_str)
    numbers = [int(rotate_str(x_str, i)) for i in range(x_len)]
    if all([number in primes for number in numbers]):
        return True, numbers
    else:
        return False, numbers


primes = [i for i in range(2, 1000000) if is_prime(i)]

primes_dict = {}
for i in primes:
    primes_dict[i] = 1


result = {}
for i in primes:
    ok, ret = is_clr_prime(i, primes_dict)
    if ok:
        result[ret[0]] = ret
    else:
        for j in ret:
            if j in primes_dict:
                del primes_dict[j]


print len(result)
