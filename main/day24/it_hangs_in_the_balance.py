import math
from itertools import combinations


def solve(packages) -> int:
    weight_per_compartment = sum(packages) // 3
    return arrange_packages(packages, weight_per_compartment)


def arrange_packages(packages, weight_per_compartment):
    min_qe = None
    for i in range(len(packages)):
        combs = set(combinations(packages, i + 1))
        for c in [x for x in combs if
                  sum(x) == weight_per_compartment and rest_are_equal(x, weight_per_compartment, packages.copy())]:
            min_qe = math.prod(c) if not min_qe else min(min_qe, math.prod(c))
        if min_qe:
            return min_qe


def rest_are_equal(group_1_packages, weight_per_compartment, packages):
    for group_1 in group_1_packages:
        packages.remove(group_1)
    for i in range(len(packages)):
        for comb in combinations(packages, i + 1):
            if sum(comb) == weight_per_compartment:
                return True
    return False
