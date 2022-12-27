import os
from pathlib import Path

from main.day01.not_quite_lisp import solve_p1, solve_p2


def test_p1_simple():
    assert solve_p1(")())())") == -3


def test_p1_real():
    assert solve_p1(read_input("data/input.txt")) == 280


def test_p2_simple():
    assert solve_p2("()())") == 5


def test_p2_real():
    assert solve_p2(read_input("data/input.txt")) == 1797


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        return f.read().strip("\n")
