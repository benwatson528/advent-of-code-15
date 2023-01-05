import os
from pathlib import Path

from main.day19.medicine_for_rudolph import solve_p1, solve_p2


def test_p1_simple():
    replacements, molecule = read_input("data/test_input.txt")
    assert solve_p1(replacements, molecule) == 4


def test_p1_real():
    replacements, molecule = read_input("data/input.txt")
    assert solve_p1(replacements, molecule) == 518


def test_p2_real():
    replacements, molecule = read_input("data/input.txt")
    assert solve_p2(replacements, molecule) == 200


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        raw_lines = f.read().splitlines()
        replacements = [line.split(" => ") for line in raw_lines[:-2]]
        molecule = raw_lines[-1]
        return replacements, molecule
