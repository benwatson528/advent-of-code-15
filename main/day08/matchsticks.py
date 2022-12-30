def solve_p1(strs) -> int:
    return sum(len(s) - len(eval(s)) for s in strs)


def solve_p2(strs) -> int:
    return sum(len("\"" + s.replace("\\", "\\\\").replace('"', r"\"") + "\"") - len(s) for s in strs)
