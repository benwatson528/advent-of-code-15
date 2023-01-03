def solve_p1(ticker_tape, sues) -> int:
    for compound_name, compound_quantity in ticker_tape.items():
        filtered_sues = {}
        for sue_id, sue_compounds in sues.items():
            if compound_name in sue_compounds and sue_compounds[compound_name] != compound_quantity:
                continue
            else:
                filtered_sues[sue_id] = sue_compounds
        sues = filtered_sues.copy()
    return list(sues.keys())[0]


def solve_p2(ticker_tape, sues) -> int:
    for compound_name, compound_quantity in ticker_tape.items():
        filtered_sues = {}
        for sue_id, sue_compounds in sues.items():
            if compound_name in ("cats", "trees") and compound_name in sue_compounds:
                if sue_compounds[compound_name] <= compound_quantity:
                    continue
            if compound_name in ("pomeranians", "goldfish") and compound_name in sue_compounds:
                if sue_compounds[compound_name] >= compound_quantity:
                    continue
            elif compound_name in sue_compounds and sue_compounds[compound_name] != compound_quantity:
                continue
            filtered_sues[sue_id] = sue_compounds
        sues = filtered_sues.copy()
    return list(sues.keys())[0]
