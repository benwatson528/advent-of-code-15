import os
import re
from collections import defaultdict
from pathlib import Path

from main.day09.all_in_a_single_night import solve


def test_p1_simple():
    assert solve(read_input("data/test_input.txt")) == 605


def test_p1_real():
    assert solve(read_input("data/input.txt")) == 117


def test_2_simple():
    assert solve(read_input("data/test_input.txt"), find_max=True) == 982


def test_p2_real():
    assert solve(read_input("data/input.txt"), find_max=True) == 909


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        places = defaultdict(list)
        lines = f.read().splitlines()
        for line in lines:
            words = re.findall(r"\w+", line)
            places[words[0]].append((words[2], int(words[3])))
            places[words[2]].append((words[0], int(words[3])))
        return places
