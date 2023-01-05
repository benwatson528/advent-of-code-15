def solve(grid, steps, stuck_corners) -> int:
    grid_size = max(x for x, y in list(grid.keys()))
    for _ in range(steps):
        if stuck_corners:
            turn_on_corners(grid, grid_size)
        grid = move(grid)
    if stuck_corners:
        turn_on_corners(grid, grid_size)
    return count_on_lights(grid)


def turn_on_corners(grid, grid_size):
    grid[(0, 0)] = '#'
    grid[(0, grid_size)] = '#'
    grid[(grid_size, grid_size)] = '#'
    grid[(grid_size, 0)] = '#'


def move(grid):
    new_grid = grid.copy()
    for i, j in grid.keys():
        current_state = grid.get((i, j), '.')
        on_neighbours = count_on_neighbours(grid, i, j)
        if current_state == "#" and on_neighbours not in (2, 3):
            new_grid[(i, j)] = "."
        if current_state == "." and on_neighbours == 3:
            new_grid[(i, j)] = "#"
    return new_grid


def count_on_neighbours(grid, i, j):
    return [grid.get((i + 1, j), '.'),
            grid.get((i + 1, j + 1), '.'),
            grid.get((i - 1, j + 1), '.'),
            grid.get((i - 1, j - 1), '.'),
            grid.get((i + 1, j - 1), '.'),
            grid.get((i, j + 1), '.'),
            grid.get((i, j - 1), '.'),
            grid.get((i - 1, j), '.')].count("#")


def count_on_lights(grid):
    return list(grid.values()).count("#")
