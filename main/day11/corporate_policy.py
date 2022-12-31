def solve(password) -> str:
    while not is_valid(password):
        password = increment_password(password)
    return password


def increment_password(password):
    for i in range(len(password) - 1, 0, -1):
        if password[i] != "z":
            return password[:i] + chr(ord(password[i]) + 1) + ("a" * (len(password) - i - 1))


def is_valid(password):
    return contains_increasing_straight(password) and does_not_contain_invalid_character(
        password) and contains_two_pairs(password)


def contains_increasing_straight(password):
    for i in range(2, len(password)):
        if ord(password[i - 1]) - ord(password[i - 2]) == 1 and ord(password[i]) - ord(password[i - 1]) == 1:
            return True
    return False


def does_not_contain_invalid_character(password):
    return not any(x in password for x in ("i", "o", "l"))


def contains_two_pairs(password):
    seen = None
    for i in range(1, len(password)):
        if password[i - 1] == password[i]:
            if seen and password[i] != seen:
                return True
            else:
                seen = password[i]
    return False
