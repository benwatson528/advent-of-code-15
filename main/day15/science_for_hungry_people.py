import math


def solve(ingredients, calorie_limit=None) -> int:
    max_score = 0
    ingredient_values = list(ingredients.values())
    for amount in find_combinations(1, 100, [[0] * len(ingredients)], len(ingredients)):
        calories = sum(amount[i] * ingredient_values[i][4] for i in range(len(ingredient_values)))
        if calorie_limit and calories != calorie_limit:
            continue
        scores = []
        for properties in range(4):
            scores.append(
                max(0, sum(amount[i] * ingredient_values[i][properties] for i in range(len(ingredient_values)))))
        max_score = max(max_score, math.prod(scores))
    return max_score


def find_combinations(current, total, subtotals, num_elems):
    if current > total:
        return subtotals
    new_subtotals = []

    for subtotal in subtotals:
        for i in range(num_elems):
            new_subtotal = subtotal.copy()
            new_subtotal[i] += 1
            new_subtotals.append(new_subtotal)
    return find_combinations(current + 1, total, [list(x) for x in set(tuple(x) for x in new_subtotals)], num_elems)
