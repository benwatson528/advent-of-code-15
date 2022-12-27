from collections import Counter


def solve_p1(words) -> int:
    return len([s for s in words if is_nice_p1(s)])


def solve_p2(words) -> int:
    return len([s for s in words if is_nice_p2(s)])


def is_nice_p1(s):
    if sum(v for k, v in Counter(s).items() if k in "aeiou") < 3:
        return False
    if not repeats(s, 1):
        return False
    for bad_substr in ("ab", "cd", "pq", "xy"):
        if bad_substr in s:
            return False
    return True


def is_nice_p2(s):
    if not twice_pair(s):
        return False
    if not repeats(s, 2):
        return False
    return True


def repeats(s, gap):
    for c in zip(s, s[gap:]):
        if c[0] == c[1]:
            return True
    return False


def twice_pair(s):
    for i in range(1, len(s)):
        if f"{s[i-1]}{s[i]}" in s[i+1:]:
            return True
    return False
