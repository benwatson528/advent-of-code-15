import os
from pathlib import Path

from main.day08.matchsticks import solve_p1, solve_p2


def test_p1_simple():
    assert solve_p1(read_input("data/test_input.txt")) == 12


def test_p1_real():
    assert solve_p1(read_input("data/input.txt")) == 1333


def test_p2_simple():
    assert solve_p2(read_input("data/test_input.txt")) == 19


def test_p2_real():
    assert solve_p2(read_input("data/input.txt")) == 0


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        lines = f.read().splitlines()
        return lines
