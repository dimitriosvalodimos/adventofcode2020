"""
--- Day 11: Seating System ---
Your plane lands with plenty of time to spare. The final leg of your journey is a ferry that goes directly to the tropical island where you can finally start your vacation. As you reach the waiting area to board the ferry, you realize you're so early, nobody else has even arrived yet!

By modeling the process people use to choose (or abandon) their seat in the waiting area, you're pretty sure you can predict the best place to sit. You make a quick map of the seat layout (your puzzle input).

The seat layout fits neatly on a grid. Each position is either floor (.), an empty seat (L), or an occupied seat (#). For example, the initial seat layout might look like this:

L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
Now, you just need to model the people who will be arriving shortly. Fortunately, people are entirely predictable and always follow a simple set of rules. All decisions are based on the number of occupied seats adjacent to a given seat (one of the eight positions immediately up, down, left, right, or diagonal from the seat). The following rules are applied to every seat simultaneously:

If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
Otherwise, the seat's state does not change.
Floor (.) never changes; seats don't move, and nobody sits on the floor.

After one round of these rules, every seat in the example layout becomes occupied:

#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##
After a second round, the seats with four or more occupied adjacent seats become empty again:

#.LL.L#.##
#LLLLLL.L#
L.L.L..L..
#LLL.LL.L#
#.LL.LL.LL
#.LLLL#.##
..L.L.....
#LLLLLLLL#
#.LLLLLL.L
#.#LLLL.##
This process continues for three more rounds:

#.##.L#.##
#L###LL.L#
L.#.#..#..
#L##.##.L#
#.##.LL.LL
#.###L#.##
..#.#.....
#L######L#
#.LL###L.L
#.#L###.##
#.#L.L#.##
#LLL#LL.L#
L.L.L..#..
#LLL.##.L#
#.LL.LL.LL
#.LL#L#.##
..L.L.....
#L#LLLL#L#
#.LLLLLL.L
#.#L#L#.##
#.#L.L#.##
#LLL#LL.L#
L.#.L..#..
#L##.##.L#
#.#L.LL.LL
#.#L#L#.##
..L.L.....
#L#L##L#L#
#.LLLLLL.L
#.#L#L#.##
At this point, something interesting happens: the chaos stabilizes and further applications of these rules cause no seats to change state! Once people stop moving around, you count 37 occupied seats.

Simulate your seating area by applying the seating rules repeatedly until no seats change state. How many seats end up occupied?
"""
from __future__ import annotations
from pprint import PrettyPrinter
from helper import *

p = PrettyPrinter()


class Simulation:
    def __init__(self, data: list[list[str]]) -> None:
        self.current_data = data
        self.next_data = data
        self.num_rows = len(self.current_data)
        self.num_cols = len(self.current_data[0])

    def get_neighbours(self, pos: tuple[int, int]) -> int:
        neighbours = 0
        y, x = pos
        for i in range(-1, 2):
            for j in range(-1, 2):
                n_y = y + i
                n_x = x + j
                # don't count yourself
                if i == 0 and j == 0:
                    continue
                # don't cause an IndexOutOfBounds Error, trying to go off the left/top side
                if n_y < 0 or n_x < 0:
                    continue
                # don't run off the right/bottom side
                elif n_y >= self.num_rows or n_x >= self.num_cols:
                    continue
                else:
                    if self.current_data[n_y][n_x] == "#":
                        neighbours += 1
        return neighbours

    def single_pass(self) -> bool:
        changed_seat = False
        for row_index in range(self.num_rows):
            for column_index in range(self.num_cols):
                neighbours = self.get_neighbours((row_index, column_index))
                if (
                    self.current_data[row_index][column_index] == "L"
                    and neighbours == 0
                ):
                    self.next_data[row_index][column_index] = "#"
                    changed_seat = True
                if (
                    self.current_data[row_index][column_index] == "#"
                    and neighbours >= 4
                ):
                    self.next_data[row_index][column_index] == "L"
                    changed_seat = True
        self.current_data = self.next_data
        return changed_seat

    def simulate_until_static(self) -> int:
        occupied = 0
        change_occured = self.single_pass()
        while change_occured:
            change_occured = self.single_pass()
        for row in self.current_data:
            for value in row:
                if value == "#":
                    occupied += 1
        return occupied


def further_split_data(data: list[str]) -> list[list[str]]:
    new_data = [list(row) for row in data]
    return new_data


def part1(data: list[str]) -> int:
    split_data = further_split_data(data)
    sim = Simulation(split_data)
    occupied = sim.simulate_until_static()
    p.pprint(sim.current_data)
    return occupied


def part2(data):
    pass


if __name__ == "__main__":
    # data = read_as_string_list(
    #     "/home/dimitrios/dev/adventofcode2020/adventofcode2020/day11_input.txt"
    # )
    data = [
        "L.LL.LL.LL",
        "LLLLLLL.LL",
        "L.L.L..L..",
        "LLLL.LL.LL",
        "L.LL.LL.LL",
        "L.LLLLL.LL",
        "..L.L.....",
        "LLLLLLLLLL",
        "L.LLLLLL.L",
        "L.LLLLL.LL",
    ]
    result1 = part1(data)
    p.pprint(result1)

    result2 = part2(data)
    p.pprint(result2)
