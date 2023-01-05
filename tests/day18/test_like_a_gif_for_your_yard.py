import os
from pathlib import Path

from main.day18.like_a_gif_for_your_yard import solve


def test_p1_simple():
    assert solve(read_input("data/test_input.txt"), 4, False) == 4


def test_p1_real():
    assert solve(read_input("data/input.txt"), 100, False) == 814


def test_p2_simple():
    assert solve(read_input("data/test_input.txt"), 5, True) == 17


def test_p2_real():
    assert solve(read_input("data/input.txt"), 100, True) == 924


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        grid = {}
        for i, line in enumerate(f.read().splitlines()):
            for j, light in enumerate(line):
                grid[(i, j)] = light
        return grid
