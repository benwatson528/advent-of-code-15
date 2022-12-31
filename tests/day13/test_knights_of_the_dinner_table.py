import os
import re
from pathlib import Path

from main.day13.knights_of_the_dinner_table import solve


def test_p1_simple():
    assert solve(read_input("data/test_input.txt")) == 330


def test_p1_real():
    assert solve(read_input("data/input.txt")) == 709


def test_p2_real():
    preferences = read_input("data/input.txt")
    for attendee in {p[0] for p in preferences}:
        preferences.append(("Ben", "gain", 0, attendee))
        preferences.append((attendee, "gain", 0, "Ben"))
    assert solve(preferences) == 668


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        return [re.findall(r"(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+).", line)[0] for line in
                f.read().splitlines()]
