import os
from pathlib import Path

from main.day16.aunt_sue import solve_p1, solve_p2


def test_p1_real():
    ticker_tape = read_ticker_tape("data/ticker_tape_input.txt")
    sues = read_sues("data/sue_input.txt")
    assert solve_p1(ticker_tape, sues) == '40'


def test_p2_real():
    ticker_tape = read_ticker_tape("data/ticker_tape_input.txt")
    sues = read_sues("data/sue_input.txt")
    assert solve_p2(ticker_tape, sues) == '241'


def read_ticker_tape(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        return {x.split(": ")[0]: int(x.split(": ")[1]) for x in f.read().splitlines()}


def read_sues(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        sues = {}
        lines = f.read().splitlines()
        for line in lines:
            sue_possessions = {x.split(": ")[0]: int(x.split(": ")[1]) for x in
                               ": ".join(line.split(": ")[1:]).split(", ")}
            sues["".join(line.split(": ")[0][4:])] = sue_possessions
        return sues
