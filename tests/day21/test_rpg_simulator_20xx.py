from main.day21.rpg_simulator_20xx import solve_win, solve_lose

WEAPONS = {"Dagger": (8, 4, 0),
           "Shortsword": (10, 5, 0),
           "Warhammer": (25, 6, 0),
           "Longsword": (40, 7, 0),
           "Greataxe": (74, 8, 0)
           }
ARMOR = {"Leather": (13, 0, 1),
         "Chainmail": (31, 0, 2),
         "Splintmail": (53, 0, 3),
         "Bandedmail": (75, 0, 4),
         "Platemail": (102, 0, 5),
         "None": (0, 0, 0)
         }
RINGS = {"Damage +1": (25, 1, 0),
         "Damage +2": (50, 2, 0),
         "Damage +3": (100, 3, 0),
         "Defense +1": (20, 0, 1),
         "Defense +2": (40, 0, 2),
         "Defense +3": (80, 0, 3),
         "NoneLeftHand": (0, 0, 0),
         "NoneRightHand": (0, 0, 0)
         }


def test_p1_real():
    you_hp = 100
    them = (109, 8, 2)
    shop = (WEAPONS, ARMOR, RINGS)
    assert solve_win(you_hp, them, shop) == 111


def test_p2_real():
    you_hp = 100
    them = (109, 8, 2)
    shop = (WEAPONS, ARMOR, RINGS)
    assert solve_lose(you_hp, them, shop) == 188
