def solve(instructions, registers) -> int:
    i = 0
    while i < len(instructions):
        instruction = instructions[i]
        args = instruction.split(" ")
        match args[0]:
            case "hlf":
                registers[args[1]] //= 2
                i += 1
            case "tpl":
                registers[args[1]] *= 3
                i += 1
            case "inc":
                registers[args[1]] += 1
                i += 1
            case "jmp":
                i += int(args[1])
            case "jie":
                i += int(args[2]) if registers[args[1][0]] % 2 == 0 else 1
            case "jio":
                i += int(args[2]) if registers[args[1][0]] == 1 else 1
    return registers["b"]
