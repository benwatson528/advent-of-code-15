import re


def solve_p1(replacements, molecule) -> int:
    mutations = set()
    for replacement_key, replacement_value in replacements:
        for idx in re.finditer(replacement_key, molecule):
            mutations.add(molecule[:idx.start()] + replacement_value + molecule[idx.end():])
    return len(mutations)


def solve_p2(replacements, molecule) -> int:
    return reduce_molecule([(v, k) for k, v in replacements], molecule)


def reduce_molecule(replacements, starting_molecule) -> int:
    mutations = [(starting_molecule, 0)]
    while mutations:
        mutation, num_turns = mutations.pop()
        if mutation == "e":
            return num_turns
        next_move = mutation
        for replacement_key, replacement_value in replacements:
            if replacement_key in mutation:
                for idx in re.finditer(replacement_key, mutation):
                    reduced = mutation[:idx.start()] + replacement_value + mutation[idx.end():]
                    if len(reduced) <= len(next_move):
                        next_move = reduced

        mutations.append((next_move, num_turns + 1))
