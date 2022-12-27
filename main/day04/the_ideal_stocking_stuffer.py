import hashlib


def solve(x, num_zeroes) -> int:
    i = 1
    prefix = "0" * num_zeroes
    while True:
        hashed = hashlib.md5(f"{x}{i}".encode('utf-8')).hexdigest()
        if hashed[:num_zeroes] == prefix:
            return i
        i += 1
