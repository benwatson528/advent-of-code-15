from collections import Counter


def solve(movements, num_santas) -> int:
    houses = Counter()
    current_locations = [(0, 0)] * num_santas
    houses[current_locations[0]] += 1
    for i, m in enumerate(movements):
        idx = i % num_santas
        current_locations[idx] = move(current_locations[idx], m)
        houses[current_locations[idx]] += 1
    return len([v for v in houses.values() if v >= 1])


def move(current_location, m):
    match m:
        case "^":
            current_location = (current_location[0], current_location[1] - 1)
        case "v":
            current_location = (current_location[0], current_location[1] + 1)
        case "<":
            current_location = (current_location[0] - 1, current_location[1])
        case ">":
            current_location = (current_location[0] + 1, current_location[1])
    return current_location
