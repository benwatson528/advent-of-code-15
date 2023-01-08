def solve(end_row, end_col) -> int:
    current_row = 1
    current_col = 1
    max_row = 1
    current_val = 20151125
    mult = 252533
    remainder = 33554393
    while (current_row, current_col) != (end_row, end_col):
        if current_row - 1 == 0:
            current_row = max_row + 1
            max_row += 1
            current_col = 1
        else:
            current_row -= 1
            current_col += 1
        current_val = (current_val * mult) % remainder
    return current_val
