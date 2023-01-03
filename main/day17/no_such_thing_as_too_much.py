def solve(containers, litres, minimal_containers) -> int:
    if minimal_containers:
        minimal = find_minimal(litres, containers, [], [])
        fewest = min(len(x) for x in minimal)
        return len([x for x in minimal if len(x) == fewest])
    else:
        return combine(litres, containers)


def combine(litres, containers):
    if litres < 0:
        return 0
    elif not containers:
        return 1 if litres == 0 else 0
    else:
        return combine(litres - containers[0], containers[1:]) + combine(litres, containers[1:])


def find_minimal(litres, containers, current, used):
    if litres < 0:
        return []
    elif not containers:
        return [current] if litres == 0 else []
    else:
        return find_minimal(litres - containers[0], containers[1:], current + [containers[0]], used)\
            + find_minimal(litres, containers[1:], current, used)
