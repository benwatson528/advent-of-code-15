import os
from pathlib import Path

from main.day17.no_such_thing_as_too_much import solve


def test_p1_simple():
    assert solve(read_input("data/test_input.txt"), 25, False) == 4


def test_p1_real():
    assert solve(read_input("data/input.txt"), 150, False) == 1304


def test_p2_simple():
    assert solve(read_input("data/test_input.txt"), 25, True) == 3


def test_p2_real():
    assert solve(read_input("data/input.txt"), 150, True) == 18


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        return [int(x) for x in f.read().splitlines()]
