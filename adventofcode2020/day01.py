"""
--- Day 1: Report Repair ---
After saving Christmas five years in a row, you've decided to take a vacation at a nice resort on a tropical island. Surely, Christmas will go on without you.

The tropical island has its own currency and is entirely cash-only. The gold coins used there have a little picture of a starfish; the locals just call them stars. None of the currency exchanges seem to have heard of them, but somehow, you'll need to find fifty of these coins by the time you arrive so you can pay the deposit on your room.

To save your vacation, you need to get all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.

Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

For example, suppose your expense report contained the following:

1721
979
366
299
675
1456
In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?
"""
from __future__ import annotations
from pprint import PrettyPrinter
from helper import *

p = PrettyPrinter()


def part1(data: list[int], target: int) -> int:
    # nearly O(1) lookup
    set_repr = set(data)

    for number in data:
        difference = target - number
        if difference in set_repr:
            return difference * number
    return 0


def part2(data: list[int]) -> int:
    for number in data:
        difference = 2020 - number
        sub_result = part1(data, difference)
        if sub_result == 0:
            continue
        else:
            return number * sub_result
    return 0


if __name__ == "__main__":
    data = read_as_int_list(
        "/home/dimitrios/dev/adventofcode2020/adventofcode2020/day01_input.txt"
    )
    result1 = part1(data, 2020)
    p.pprint(result1)

    result2 = part2(data)
    p.pprint(result2)
