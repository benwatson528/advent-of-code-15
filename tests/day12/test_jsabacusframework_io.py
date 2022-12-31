import os
from pathlib import Path

from main.day12.jsabacusframework_io import solve_p1, solve_p2


def test_p1_simple():
    assert solve_p1(read_input("data/test_input.txt")) == 6


def test_p1_real():
    assert solve_p1(read_input("data/input.txt")) == 191164


def test_p2_simple():
    assert solve_p2(read_input("data/test_input.txt")) == 4


def test_p2_real():
    assert solve_p2(read_input("data/input.txt")) == 87842


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        return f.read().strip("\n")
