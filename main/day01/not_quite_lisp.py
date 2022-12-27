def solve_p1(s) -> int:
    return s.count("(") - s.count(")")


def solve_p2(s) -> int:
    counter = 0
    for i, c in enumerate(s):
        counter = counter + 1 if c == "(" else counter - 1
        if counter < 0:
            return i + 1