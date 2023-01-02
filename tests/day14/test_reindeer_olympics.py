import os
import re
from pathlib import Path

from main.day14.reindeer_olympics import solve_p1, solve_p2


def test_p1_simple():
    assert solve_p1(read_input("data/test_input.txt"), 1000) == 1120


def test_p1_real():
    assert solve_p1(read_input("data/input.txt"), 2503) == 2655


def test_p2_simple():
    assert solve_p2(read_input("data/test_input.txt"), 1000) == 689


def test_p2_real():
    assert solve_p2(read_input("data/input.txt"), 2503) == 1059


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        return [
            re.findall(r"(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.", line)[0]
            for line in f.read().splitlines()]
