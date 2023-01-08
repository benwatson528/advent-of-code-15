import os
from pathlib import Path

from main.day24.it_hangs_in_the_balance import solve


def test_p1_simple():
    assert solve(read_input("data/test_input.txt")) == 99


def test_p1_real():
    assert solve(read_input("data/input.txt")) == 11846773891


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        return [int(x) for x in f.read().splitlines()]
