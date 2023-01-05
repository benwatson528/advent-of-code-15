import math


def solve_p1(x) -> int:
    for i in range(1, x):
        if sum([d * 10 for d in get_divisors(i)]) >= x:
            return i


def solve_p2(x) -> int:
    for i in range(1, x):
        if sum([d * 11 for d in get_divisors(i) if d * 50 >= i]) >= x:
            return i


def get_divisors(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i * i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor
