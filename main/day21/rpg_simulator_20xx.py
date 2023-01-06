import itertools


def solve(you_hp, them, shop) -> int:
    minimum_spend = 9999
    for damage, armor, spend in get_loadouts(shop):
        you = (you_hp, damage, armor)
        if fight(you, them):
            minimum_spend = min(minimum_spend, spend)
    return minimum_spend


def fight(you, them):
    you_hp, you_damage, you_armor = you
    them_hp, them_damage, them_armor = them

    while you_hp > 0:
        them_hp -= max(1, you_damage - them_armor)
        if them_hp <= 0:
            return True
        you_hp -= max(1, them_damage - you_armor)
    return you_hp > 0


def get_loadouts(shop):
    weapons = shop[0]
    armors = shop[1]
    rings = shop[2]
    ring_pairs = list(itertools.combinations(rings.keys(), 2))
    loadouts = []
    for weapon_values in weapons.values():
        for armor_values in armors.values():
            for ring_pair in ring_pairs:
                left_ring, right_ring = rings[ring_pair[0]], rings[ring_pair[1]]
                damage = weapon_values[1] + left_ring[1] + right_ring[1]
                armor = armor_values[2] + left_ring[2] + right_ring[2]
                spend = weapon_values[0] + armor_values[0] + left_ring[0] + right_ring[0]
                loadouts.append((damage, armor, spend))
    return loadouts
