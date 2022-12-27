import os
from pathlib import Path

from main.day03.perfectly_spherical_houses_in_a_vacuum import solve


def test_p1_simple():
    assert solve("^>v<", 1) == 4


def test_p1_real():
    assert solve(read_input("data/input.txt"), 1) == 2592


def test_p2_simple():
    assert solve("^>v<", 2) == 3


def test_p2_real():
    assert solve(read_input("data/input.txt"), 2) == 2360


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        return f.read().strip("\n")
