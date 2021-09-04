from __future__ import annotations

import argparse
from os import scandir
from pathlib import Path
from tkinter import Button, Label, Text, Tk, mainloop
from tkinter.constants import END

CHALLENGE_TEXT = ""
INPUT_DATA = ""


def get_text_input(root: Tk, challenge: Text, input_data: Text) -> None:
    challenge_text = challenge.get("1.0", END)
    global CHALLENGE_TEXT
    CHALLENGE_TEXT = challenge_text.strip()
    input_text = input_data.get("1.0", END)
    global INPUT_DATA
    INPUT_DATA = input_text.strip()
    root.destroy()


def create_textfield_gui() -> Tk:
    root = Tk()
    root.title("Add challenge text to the file template")
    challenge_text = Text(root, height=10, width=100)
    challenge_label = Label(root, text="Enter the challenge text below:")
    input_data_text = Text(root, height=10, width=100)
    input_data_label = Label(root, text="Enter iput data:")
    create_button = Button(
        root,
        text="Create",
        command=lambda: get_text_input(root, challenge_text, input_data_text),
    )
    exit_button = Button(root, text="Exit", command=root.destroy)
    challenge_label.pack()
    challenge_text.pack()
    input_data_label.pack()
    input_data_text.pack()
    create_button.pack()
    exit_button.pack()
    return root


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Simple script to create the boilerplate for each challenge day."
    )
    parser.add_argument(
        "-d",
        "--day",
        required=False,
        default=None,
        type=int,
        choices=range(1, 26),
        dest="day",
        help="Specify the day. This will override any existing files with the same day number.",
    )
    return parser


def import_block() -> str:
    imports = [
        "from __future__ import annotations",
        "from pprint import PrettyPrinter",
        "from helper import *",
    ]
    return "\n".join(imports)


def init_code_string() -> str:
    code = [
        "p = PrettyPrinter()",
    ]
    return "\n".join(code)


def function_headers() -> str:
    code = ["def part1(data):", "    pass", "\n", "\n", "def part2(data):", "    pass"]
    return "\n".join(code)


def main_code(formatted_day: str) -> str:
    code = [
        "if __name__ == '__main__':",
        f"    data = read_as_int_list('/home/dimitrios/dev/adventofcode2020/adventofcode2020/{formatted_day}_input.txt')",
        "    result1 = part1(data)",
        "    p.pprint(result1)",
        "\n",
        "    result2 = part2(data)",
        "    p.pprint(result2)",
    ]
    return "\n".join(code)


def get_challenge_text() -> None:
    create_textfield_gui()
    mainloop()


def format_day(day: int) -> str:
    d = str(day).zfill(2)
    return f"day{d}"


def create_input_file(formatted_day: str) -> None:
    input_filename = f"{formatted_day}_input.txt"
    input_filepath = Path(
        f"/home/dimitrios/dev/adventofcode2020/adventofcode2020/{input_filename}"
    )

    try:
        with open(input_filepath, "w") as f:
            global INPUT_DATA
            f.writelines([INPUT_DATA])
    except Exception as e:
        raise e


def create_code_file(formatted_day: str) -> None:
    code_filename = f"{formatted_day}.py"

    code_filepath = Path(
        f"/home/dimitrios/dev/adventofcode2020/adventofcode2020/{code_filename}"
    )

    with open(code_filepath, "w") as f:
        f.writelines(
            [
                '"""',
                "\n",
                CHALLENGE_TEXT,
                "\n",
                '"""',
                "\n",
                import_block(),
                "\n",
                "\n",
                init_code_string(),
                "\n",
                "\n",
                function_headers(),
                "\n",
                "\n",
                main_code(formatted_day),
            ]
        )


def get_py_files() -> list[str]:
    py_files = []
    for entry in scandir("/home/dimitrios/dev/adventofcode2020/adventofcode2020/"):
        if (
            entry.name.startswith("__")
            or entry.name.startswith("template")
            or entry.name.startswith("helper")
        ):
            continue
        if entry.name.endswith(".py"):
            py_files.append(entry.name)
    return py_files


def get_day_number_from_filename(file: str) -> int:
    removed_py = file.split(".")[0]
    return int(removed_py[-2:])


def get_next_day() -> int:
    existing_files = get_py_files()
    if len(existing_files) == 0:
        return 1
    else:
        current_biggest = max(
            [get_day_number_from_filename(filename) for filename in existing_files]
        )
        return current_biggest + 1


def main() -> None:
    parser = create_parser()
    args = parser.parse_args()
    get_challenge_text()
    formatted_day = ""
    if args.day != None:
        formatted_day = format_day(args.day)
    else:
        next_day = get_next_day()
        formatted_day = format_day(next_day)

    create_input_file(formatted_day)
    create_code_file(formatted_day)


if __name__ == "__main__":
    main()
