import dataclasses
import random

EFFECT_SPELLS = {2: 6, 3: 6, 4: 5}
SPELL_COSTS = {0: 53, 1: 73, 2: 113, 3: 173, 4: 229}
SPELL_NAMES = {0: "Magic Missile", 1: "Drain", 2: "Shield", 3: "Poison", 4: "Recharge"}


def solve(hero, boss) -> int:
    minimum_mana_spend = 9999
    for _ in range(10000):
        hero_win, mana_spend = fight(dataclasses.replace(hero), dataclasses.replace(boss))
        if hero_win:
            minimum_mana_spend = min(minimum_mana_spend, mana_spend)
    return minimum_mana_spend


def fight(hero, boss):
    active_effects = []
    hero_turn = True
    while hero.hp > 0:
        active_effects = action_effects(active_effects, hero, boss)
        if boss.hp <= 0:
            return True, hero.get_mana_spent()
        if hero_turn:
            if (spell := choose_spell(active_effects, hero)) is None:
                return False, hero.get_mana_spent()
            if spell_effect := cast_spell(hero, boss, spell):
                active_effects.append(spell_effect)
            if boss.hp <= 0:
                return True, hero.get_mana_spent()
        else:
            hero.hp -= max(1, boss.damage - hero.armor)
        hero_turn = not hero_turn
    return hero.hp > 0, hero.get_mana_spent()


def cast_spell(hero, boss, spell):
    if spell == 0:
        boss.hp -= 4
    elif spell == 1:
        boss.hp -= 2
        hero.hp += 2
    elif spell == 2:
        hero.armor += 7

    hero.spend_mana(SPELL_COSTS[spell])
    if spell in EFFECT_SPELLS:
        return spell, EFFECT_SPELLS[spell] - 1


def action_effects(active_effects, hero, boss):
    for active_spell, turns_left in active_effects:
        if active_spell == 3:
            boss.hp -= 3
        elif active_spell == 4:
            hero.mana += 101
    return decrement_effect_turns(active_effects, hero)


def decrement_effect_turns(active_effects, hero):
    updated_active_effects = []
    for active_spell, turns in active_effects:
        if turns - 1 >= 0:
            updated_active_effects.append((active_spell, turns - 1))
        elif active_spell == 2:
            hero.armor -= 7
    return updated_active_effects


def choose_spell(active_effects, hero):
    possible_spells = list(set(range(5)) - set(a[0] for a in active_effects))
    possible_spells = [x for x in possible_spells if hero.mana >= SPELL_COSTS[x]]
    return random.choice(possible_spells) if len(possible_spells) > 0 else None
