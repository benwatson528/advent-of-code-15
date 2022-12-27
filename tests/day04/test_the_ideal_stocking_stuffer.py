from main.day04.the_ideal_stocking_stuffer import solve


def test_p1_simple():
    assert solve("abcdef", 5) == 609043


def test_p1_real():
    assert solve("ckczppom", 5) == 117946


def test_p2_real():
    assert solve("ckczppom", 6) == 3938038
