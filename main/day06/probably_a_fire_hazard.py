def solve_p1(commands) -> int:
    illuminated = set()
    for c in commands:
        action, x1, y1, x2, y2 = c[0], int(c[1]), int(c[2]), int(c[3]), int(c[4])
        for row in range(x1, x2 + 1):
            for col in range(y1, y2 + 1):
                change_state(action, row, col, illuminated)
    return len(illuminated)


def solve_p2(commands) -> int:
    illuminated = {}
    for row in range(0, 1000):
        for col in range(0, 1000):
            illuminated[(row, col)] = 0
    for c in commands:
        action, x1, y1, x2, y2 = c[0], int(c[1]), int(c[2]), int(c[3]), int(c[4])
        for row in range(x1, x2 + 1):
            for col in range(y1, y2 + 1):
                change_brightness(action, row, col, illuminated)
    return sum(illuminated.values())


def change_state(action, row, col, illuminated):
    light = row, col
    match action:
        case "turn on":
            illuminated.add(light)
        case "turn off":
            if light in illuminated:
                illuminated.remove(light)
        case "toggle":
            if light in illuminated:
                illuminated.remove(light)
            else:
                illuminated.add(light)


def change_brightness(action, row, col, illuminated):
    light = row, col
    match action:
        case "turn on":
            illuminated[light] += 1
        case "turn off":
            illuminated[light] = max(illuminated[light] - 1, 0)
        case "toggle":
            illuminated[light] += 2
