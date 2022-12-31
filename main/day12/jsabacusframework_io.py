import re


def solve_p1(x) -> int:
    return sum(int(x) for x in re.findall(r"-?\d+", x))


def solve_p2(x) -> int:
    to_remove = []
    for red in re.finditer(r':"red"', x):
        to_remove.append(range(find_start_of_obj(x, red.start()), find_end_of_obj(x, red.end()) + 1))
    return solve_p1(remove_reds(to_remove, x))


def find_start_of_obj(x, start_of_red):
    ctr = 0
    for i in range(start_of_red, 0, -1):
        if x[i] == "}":
            ctr += 1
        elif x[i] == "{" and ctr == 0:
            return i
        elif x[i] == "{":
            ctr -= 1


def find_end_of_obj(x, end_of_red):
    ctr = 0
    for i in range(end_of_red, len(x) - 1):
        if x[i] == "{":
            ctr += 1
        elif x[i] == "}" and ctr == 0:
            return i
        elif x[i] == "}":
            ctr -= 1


def remove_reds(to_remove, x):
    reds_removed = ""
    for i in range(len(x)):
        remove = False
        for r in to_remove:
            if i in r:
                remove = True
        if not remove:
            reds_removed += x[i]
    return reds_removed
