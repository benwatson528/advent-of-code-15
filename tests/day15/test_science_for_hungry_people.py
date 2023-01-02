import os
import re
from pathlib import Path

from main.day15.science_for_hungry_people import solve


def test_p1_simple():
    assert solve(read_input("data/test_input.txt")) == 62842880


def test_p1_real():
    assert solve(read_input("data/input.txt")) == 13882464


def test_p2_simple():
    assert solve(read_input("data/test_input.txt"), 500) == 57600000


def test_p2_real():
    assert solve(read_input("data/input.txt"), 500) == 11171160


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        raw_ingredients = [re.findall(
            r"(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)", line)[0]
                           for line in f.read().splitlines()]
        return {ingredient[0]: (int(ingredient[1]), int(ingredient[2]), int(ingredient[3]), int(ingredient[4]),
                                int(ingredient[5])) for ingredient in raw_ingredients}
