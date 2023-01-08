import os
from pathlib import Path

from main.day23.opening_the_turing_lock import solve


def test_p1_real():
    assert solve(read_input("data/input.txt"), {"a": 0, "b": 0}) == 307


def test_p2_real():
    assert solve(read_input("data/input.txt"), {"a": 1, "b": 0}) == 307


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        return f.read().splitlines()
