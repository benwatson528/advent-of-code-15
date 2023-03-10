import os
from pathlib import Path

from main.day11.corporate_policy import solve


def test_p1_simple():
    assert solve("abcdefgh") == "abcdffaa"


def test_p1_real():
    assert solve("vzbxkghb") == "vzbxxyzz"


def test_p2_real():
    assert solve("vzbxxzaa") == "vzcaabcc"
