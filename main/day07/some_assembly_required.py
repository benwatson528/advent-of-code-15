import operator
import re


def solve(commands) -> int:
    wires = {}
    while "a" not in wires:
        commands = run_commands(commands, wires)
        if "a" in wires:
            return wires["a"]


def run_commands(commands, wires):
    unsolved = []
    for command in commands:
        if "AND" in command:
            if not try_command(command, wires, "AND", operator.and_):
                unsolved.append(command)
        elif "OR" in command:
            if not try_command(command, wires, "OR", operator.or_):
                unsolved.append(command)
        elif "RSHIFT" in command:
            if not try_command(command, wires, "RSHIFT", operator.rshift):
                unsolved.append(command)
        elif "LSHIFT" in command:
            if not try_command(command, wires, "LSHIFT", operator.lshift):
                unsolved.append(command)
        elif "NOT" in command:
            matches = re.findall(r"NOT (\w+) -> (\w+)", command)[0]
            if matches[0].isnumeric():
                wires[matches[1]] = ~int(matches[0])
            elif matches[0] in wires:
                wires[matches[1]] = ~int(wires[matches[0]])
            else:
                unsolved.append(command)
        else:
            matches = re.findall(r"(\w+) -> (\w+)", command)[0]
            if matches[0].isnumeric():
                wires[matches[1]] = int(matches[0])
            elif matches[0] in wires:
                wires[matches[1]] = int(wires[matches[0]])
            else:
                unsolved.append(command)
    return unsolved


def try_command(command, wires, action, op):
    matches = re.findall(rf"(\w+) {action} (\w+) -> (\w+)", command)[0]
    if matches[0].isnumeric() and matches[1].isnumeric():
        wires[matches[2]] = op(int(matches[0]), int(matches[1]))
        return True
    elif matches[0].isnumeric() and matches[1] in wires:
        wires[matches[2]] = op(int(matches[0]), wires[matches[1]])
        return True
    elif matches[1].isnumeric() and matches[0] in wires:
        wires[matches[2]] = op(wires[matches[0]], int(matches[1]))
        return True
    elif matches[0] in wires and matches[1] in wires:
        wires[matches[2]] = op(wires[matches[0]], wires[matches[1]])
        return True
    return False
