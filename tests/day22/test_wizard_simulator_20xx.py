from main.day22.Boss import Boss
from main.day22.Hero import Hero
from main.day22.wizard_simulator_20xx import solve


def test_p1_real():
    hero = Hero(50, 500, 0)
    boss = Boss(51, 9)
    assert solve(hero, boss, hero_drain=False) == 900


def test_p2_real():
    hero = Hero(50, 500, 0)
    boss = Boss(51, 9)
    assert solve(hero, boss, hero_drain=True) == 1216
