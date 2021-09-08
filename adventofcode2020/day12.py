"""
--- Day 12: Rain Risk ---
Your ferry made decent progress toward the island, but the storm came in faster than anyone expected. The ferry needs to take evasive actions!

Unfortunately, the ship's navigation computer seems to be malfunctioning; rather than giving a route directly to safety, it produced extremely circuitous instructions. When the captain uses the PA system to ask if anyone can help, you quickly volunteer.

The navigation instructions (your puzzle input) consists of a sequence of single-character actions paired with integer input values. After staring at them for a few minutes, you work out what they probably mean:

Action N means to move north by the given value.
Action S means to move south by the given value.
Action E means to move east by the given value.
Action W means to move west by the given value.
Action L means to turn left the given number of degrees.
Action R means to turn right the given number of degrees.
Action F means to move forward by the given value in the direction the ship is currently facing.
The ship starts by facing east. Only the L and R actions change the direction the ship is facing. (That is, if the ship is facing east and the next instruction is N10, the ship would move north 10 units, but would still move east if the following action were F.)

For example:

F10
N3
F7
R90
F11
These instructions would be handled as follows:

F10 would move the ship 10 units east (because the ship starts by facing east) to east 10, north 0.
N3 would move the ship 3 units north to east 10, north 3.
F7 would move the ship another 7 units east (because the ship is still facing east) to east 17, north 3.
R90 would cause the ship to turn right by 90 degrees and face south; it remains at east 17, north 3.
F11 would move the ship 11 units south to east 17, south 8.
At the end of these instructions, the ship's Manhattan distance (sum of the absolute values of its east/west position and its north/south position) from its starting position is 17 + 8 = 25.

Figure out where the navigation instructions lead. What is the Manhattan distance between that location and the ship's starting position?
"""
from __future__ import annotations
from pprint import PrettyPrinter
from helper import *
import re

p = PrettyPrinter()


def parse_sequence(s: str) -> tuple[str, int]:
    matches = re.match(r"(N|S|E|W|L|R|F){1}(\d+)", s)
    d, a = matches.groups()
    return d, int(a)


def change_facing(current: str, direction: str, amount: int) -> str:
    amount = amount // 90
    directions = ["N", "E", "S", "W"]
    current_idx = directions.index(current)
    new_direction = ""
    if direction == "L":
        new_direction = directions[(current_idx - amount) % 4]
    elif direction == "R":
        new_direction = directions[(current_idx + amount) % 4]
    return new_direction


def part1(data):
    facing = "E"
    traveled = {"N": 0, "E": 0, "S": 0, "W": 0}
    for entry in data:
        direction, amount = parse_sequence(entry)
        if direction in ["N", "E", "S", "W"]:
            traveled[direction] += amount
        elif direction == "L" or direction == "R":
            facing = change_facing(facing, direction, amount)
        elif direction == "F":
            traveled[facing] += amount
    absolute_east_west = abs(traveled["E"] - traveled["W"])
    absolute_north_south = abs(traveled["N"] - traveled["S"])
    return absolute_east_west + absolute_north_south


def part2(data):
    pass


if __name__ == "__main__":
    data = read_as_string_list(
        "/home/dimitrios/dev/adventofcode2020/adventofcode2020/day12_input.txt"
    )
    result1 = part1(data)
    p.pprint(result1)

    result2 = part2(data)
    p.pprint(result2)
