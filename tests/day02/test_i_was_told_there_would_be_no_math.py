import os
from pathlib import Path

from main.day02.i_was_told_there_would_be_no_math import solve


def test_p1_simple():
    assert solve(read_input("data/test_input.txt"))[0] == 58


def test_p1_real():
    assert solve(read_input("data/input.txt"))[0] == 1606483


def test_p2_simple():
    assert solve(read_input("data/test_input.txt"))[1] == 34


def test_p2_real():
    assert solve(read_input("data/input.txt"))[1] == 3842356


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        return [line.split("x") for line in f.read().splitlines()]
