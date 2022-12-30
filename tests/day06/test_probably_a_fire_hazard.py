import os
import re
from pathlib import Path

from main.day06.probably_a_fire_hazard import solve_p1, solve_p2


def test_p1_simple():
    assert solve_p1(read_input("data/test_input.txt")) == 998996


def test_p1_real():
    assert solve_p1(read_input("data/input.txt")) == 569999


def test_p2_simple():
    assert solve_p2(read_input("data/test_input.txt")) == 1001996


def test_p2_real():
    assert solve_p2(read_input("data/input.txt")) == 17836115


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        lines = f.read().splitlines()
        commands = []
        for line in lines:
            if line.startswith("turn on"):
                action = "turn on"
            elif line.startswith("turn off"):
                action = "turn off"
            else:
                action = "toggle"
            commands.append([action] + re.findall(r'\d+', line))
        return commands
