import os
from pathlib import Path

from main.day07.some_assembly_required import solve


def test_p1_real():
    assert solve(read_input("data/input.txt")) == 16076


def test_p2_real():
    commands = read_input("data/input.txt")
    updated_commands = []
    for command in commands:
        if command.endswith("-> b"):
            updated_commands.append("16076 -> b")
        else:
            updated_commands.append(command)
    assert solve(updated_commands) == 2797


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        return f.read().splitlines()
