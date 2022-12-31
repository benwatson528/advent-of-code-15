import os
from pathlib import Path

from main.day10.elves_look__elves_say import solve


def test_p1_simple():
    assert solve("111221", 40) == 237746


def test_p1_real():
    assert solve("3113322113", 40) == 329356


def test_p2_real():
    assert solve("3113322113", 50) == 4666278
