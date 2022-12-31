def solve(s, turns) -> int:
    for _ in range(turns):
        s = play_game(s)
    return len(s)


def play_game(s):
    result = ""
    last = s[0]
    ctr = 1
    for i in range(1, len(s)):
        if s[i] == last:
            ctr += 1
        elif s[i] != last:
            result += f"{ctr}{last}"
            ctr = 1
        last = s[i]
    result += f"{ctr}{last}"
    return result
