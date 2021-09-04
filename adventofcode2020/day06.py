"""
--- Day 6: Custom Customs ---
As your flight approaches the regional airport where you'll switch to a much larger plane, customs declaration forms are distributed to the passengers.

The form asks a series of 26 yes-or-no questions marked a through z. All you need to do is identify the questions for which anyone in your group answers "yes". Since your group is just you, this doesn't take very long.

However, the person sitting next to you seems to be experiencing a language barrier and asks if you can help. For each of the people in their group, you write down the questions for which they answer "yes", one per line. For example:

abcx
abcy
abcz
In this group, there are 6 questions to which anyone answered "yes": a, b, c, x, y, and z. (Duplicate answers to the same question don't count extra; each question counts at most once.)

Another group asks for your help, then another, and eventually you've collected answers from every group on the plane (your puzzle input). Each group's answers are separated by a blank line, and within each group, each person's answers are on a single line. For example:

abc

a
b
c

ab
ac

a
a
a
a

b
This list represents answers from five groups:

The first group contains one person who answered "yes" to 3 questions: a, b, and c.
The second group contains three people; combined, they answered "yes" to 3 questions: a, b, and c.
The third group contains two people; combined, they answered "yes" to 3 questions: a, b, and c.
The fourth group contains four people; combined, they answered "yes" to only 1 question, a.
The last group contains one person who answered "yes" to only 1 question, b.
In this example, the sum of these counts is 3 + 3 + 3 + 1 + 1 = 11.

For each group, count the number of questions to which anyone answered "yes". What is the sum of those counts?
"""
from __future__ import annotations
from functools import reduce
from pprint import PrettyPrinter
from helper import *

p = PrettyPrinter()


def part1(data: list[list[str]]) -> int:
    summed_answers = 0
    for group in data:
        single_answers = set([])
        for person_answer in group:
            single_letters = set(person_answer)
            single_answers.update(single_letters)
        summed_answers += len(single_answers)
    return summed_answers


def part2(data: list[list[str]]) -> int:
    summed_shared_answers = 0
    for group in data:
        common_answers = []
        for individual_answers in group:
            single_letters = set(individual_answers)
            common_answers.append(single_letters)
        reduced_set = reduce(lambda x, y: x.intersection(y), common_answers)
        summed_shared_answers += len(reduced_set)
    return summed_shared_answers


if __name__ == "__main__":
    data = read_as_string_list_blanklines(
        "/home/dimitrios/dev/adventofcode2020/adventofcode2020/day06_input.txt"
    )
    result1 = part1(data)
    p.pprint(result1)

    result2 = part2(data)
    p.pprint(result2)
