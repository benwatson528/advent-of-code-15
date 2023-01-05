from main.day20.infinite_elves_and_infinite_houses import solve_p1, solve_p2


def test_p1_simple():
    assert solve_p1(70) == 4


def test_p1_real():
    assert solve_p1(33100000) == 776160


def test_p2_real():
    assert solve_p2(33100000) == 786240
