import os
from pathlib import Path

from main.day05.doesn_t_he_have_intern_elves_for_this_ import solve_p1, solve_p2


def test_p1_simple():
    assert solve_p1(read_input("data/p1_test_input.txt")) == 2


def test_p1_real():
    assert solve_p1(read_input("data/input.txt")) == 255


def test_p2_simple():
    assert solve_p2(read_input("data/p2_test_input.txt")) == 2


def test_p2_real():
    assert solve_p2(read_input("data/input.txt")) == 55


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        lines = f.read().splitlines()
        return lines
