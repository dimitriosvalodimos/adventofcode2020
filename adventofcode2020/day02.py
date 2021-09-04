"""
--- Day 2: Password Philosophy ---
Your flight departs in a few days from the coastal airport; the easiest way down to the coast from here is via toboggan.

The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day. "Something's wrong with our computers; we can't log in!" You ask if you can take a look.

Their password database seems to be a little corrupted: some of the passwords wouldn't have been allowed by the Official Toboggan Corporate Policy that was in effect when they were chosen.

To try to debug the problem, they have created a list (your puzzle input) of passwords (according to the corrupted database) and the corporate policy when that password was set.

For example, suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b, but needs at least 1. The first and third passwords are valid: they contain one a or nine c, both within the limits of their respective policies.

How many passwords are valid according to their policies?
"""
from __future__ import annotations
from pprint import PrettyPrinter
from helper import *
import re
from collections import Counter
from operator import xor

p = PrettyPrinter()


def parse_restriction(restriction: str) -> tuple[int, int, str]:
    matches = re.match(r"(\d+)-(\d+) (\w)", restriction)
    start, end, letter = matches.groups()
    return int(start), int(end), letter


def part1(data: list[str]) -> int:
    valid_passwords = 0
    for entry in data:
        restriction, password = [item.strip() for item in entry.split(":")]
        mininum, maximum, letter = parse_restriction(restriction)
        letter_count = Counter(password)
        if mininum <= letter_count.get(letter, -1) <= maximum:
            valid_passwords += 1
    return valid_passwords


def part2(data: list[str]) -> int:
    valid_passwords = 0
    for entry in data:
        restriction, password = [item.strip() for item in entry.split(":")]
        first, second, letter = parse_restriction(restriction)
        if len(password) <= first or len(password) <= second:
            continue
        occurences = set(
            [idx + 1 for idx, char in enumerate(password) if char == letter]
        )
        first_in_set = first in occurences
        second_in_set = second in occurences
        if xor(first_in_set, second_in_set):
            valid_passwords += 1
    return valid_passwords


if __name__ == "__main__":
    data = read_as_string_list(
        "/home/dimitrios/dev/adventofcode2020/adventofcode2020/day02_input.txt"
    )
    result1 = part1(data)
    p.pprint(result1)

    result2 = part2(data)
    p.pprint(result2)
