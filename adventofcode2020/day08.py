"""
--- Day 8: Handheld Halting ---
Your flight to the major airline hub reaches cruising altitude without incident. While you consider checking the in-flight menu for one of those drinks that come with a little umbrella, you are interrupted by the kid sitting next to you.

Their handheld game console won't turn on! They ask if you can take a look.

You narrow the problem down to a strange infinite loop in the boot code (your puzzle input) of the device. You should be able to fix it, but first you need to be able to run the code in isolation.

The boot code is represented as a text file with one instruction per line of text. Each instruction consists of an operation (acc, jmp, or nop) and an argument (a signed number like +4 or -20).

acc increases or decreases a single global value called the accumulator by the value given in the argument. For example, acc +7 would increase the accumulator by 7. The accumulator starts at 0. After an acc instruction, the instruction immediately below it is executed next.
jmp jumps to a new instruction relative to itself. The next instruction to execute is found using the argument as an offset from the jmp instruction; for example, jmp +2 would skip the next instruction, jmp +1 would continue to the instruction immediately below it, and jmp -20 would cause the instruction 20 lines above to be executed next.
nop stands for No OPeration - it does nothing. The instruction immediately below it is executed next.
For example, consider the following program:

nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
These instructions are visited in this order:

nop +0  | 1
acc +1  | 2, 8(!)
jmp +4  | 3
acc +3  | 6
jmp -3  | 7
acc -99 |
acc +1  | 4
jmp -4  | 5
acc +6  |
First, the nop +0 does nothing. Then, the accumulator is increased from 0 to 1 (acc +1) and jmp +4 sets the next instruction to the other acc +1 near the bottom. After it increases the accumulator from 1 to 2, jmp -4 executes, setting the next instruction to the only acc +3. It sets the accumulator to 5, and jmp -3 causes the program to continue back at the first acc +1.

This is an infinite loop: with this sequence of jumps, the program will run forever. The moment the program tries to run any instruction a second time, you know it will never terminate.

Immediately before the program would run an instruction a second time, the value in the accumulator is 5.

Run your copy of the boot code. Immediately before any instruction is executed a second time, what value is in the accumulator?
"""
from __future__ import annotations
from enum import Enum, auto
from pprint import PrettyPrinter
from helper import *

p = PrettyPrinter()


class OPS(Enum):
    NOP = auto()
    ACC = auto()
    JMP = auto()


class VM:
    def __init__(self, instructions: list[str]) -> None:
        self.memory = self.generate_instruction_tape(instructions)
        self.pc = 0
        self.acc = 0

    def generate_instruction_tape(self, instructions: list[str]) -> list[dict]:
        encoded_tape = []
        for row in instructions:
            op, value = [i.strip() for i in row.split(" ")]
            op = self.parse_op(op)
            value = self.parse_value(value)
            encoded_tape.append({"op": op, "value": value, "visited": False})
        return encoded_tape

    def parse_op(self, op: str) -> OPS:
        if op == "nop":
            return OPS.NOP
        elif op == "acc":
            return OPS.ACC
        elif op == "jmp":
            return OPS.JMP
        else:
            raise ValueError(f"Invalid OP: {op=}")

    def parse_value(self, value: str) -> int:
        sign, val = value[0], value[1:]
        try:
            v = int(val)
            if sign == "+":
                return v
            else:
                return v * -1
        except:
            raise ValueError(f"Invalid {value=}")

    def simulate(self) -> int:
        while True:
            instruction = self.memory[self.pc]
            op, value, visited = (
                instruction["op"],
                instruction["value"],
                instruction["visited"],
            )
            p.pprint((op, value, visited))
            if visited:
                return self.acc
            else:
                if op == OPS.NOP:
                    self.pc += 1
                elif op == OPS.JMP:
                    self.pc += value
                elif op == OPS.ACC:
                    self.acc += value
                    self.pc += 1
                instruction["visited"] = True

    def simulate_part2(self) -> int | None:
        while True:
            if self.pc >= len(self.memory):
                return None
            instruction = self.memory[self.pc]
            op, value, visited = (
                instruction["op"],
                instruction["value"],
                instruction["visited"],
            )
            if self.pc == len(self.memory) - 1:
                return self.acc
            if visited:
                return None
            else:
                if op == OPS.NOP:
                    self.pc += 1
                elif op == OPS.JMP:
                    self.pc += value
                elif op == OPS.ACC:
                    self.acc += value
                    self.pc += 1
                instruction["visited"] = True


def part1(data: list[str]) -> int:
    vm = VM(data)
    final_value = vm.simulate()
    return final_value


def part2(data: list[str]):
    for i in range(len(data)):
        if data[i].startswith("jmp"):
            data[i] = data[i].replace("jmp", "nop")
        elif data[i].startswith("nop"):
            data[i] = data[i].replace("nop", "jmp")
        vm = VM(data)
        attempt = vm.simulate_part2()
        if attempt != None:
            return attempt


if __name__ == "__main__":
    data = read_as_string_list(
        "/home/dimitrios/dev/adventofcode2020/adventofcode2020/day08_input.txt"
    )
    result1 = part1(data)
    p.pprint(result1)

    result2 = part2(data)
    p.pprint(result2)
