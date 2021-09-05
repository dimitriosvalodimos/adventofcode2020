from __future__ import annotations
from pathlib import Path
import re
from string import punctuation


def validate_path(path: str) -> Path:
    filepath = Path(path)
    if filepath.exists() and filepath.is_file():
        return filepath
    else:
        raise FileNotFoundError(f"Specified file: {path} doesn't exist!")


def read_as_int_list(path: str) -> list[int]:
    filepath = validate_path(path)
    with open(filepath, "r") as f:
        data = [int(row.strip()) for row in f.readlines()]
    return data


def read_as_string_list(path: str) -> list[str]:
    filepath = validate_path(path)
    with open(filepath, "r") as f:
        data = [row.strip() for row in f.readlines()]
    return data


def read_as_string_list_blanklines(path: str) -> list[list[str]]:
    filepath = validate_path(path)
    with open(filepath, "r") as f:
        data = []
        tmp = []
        for row in f.readlines():
            stripped = row.strip()
            if stripped != "":
                tmp.append(stripped)
            else:
                data.append(tmp)
                tmp = []
    return data


def remove_numbers(item: str) -> str:
    item = item.strip()
    regex = re.compile(r"\d+")
    return regex.sub("", item)


def sanitize_string(item: str) -> str:
    item = item.strip()
    regex = re.compile("[%s]" % re.escape(punctuation))
    return regex.sub("", item)


def sanitized_split(item: str, by: str) -> list[str]:
    split_items = [sanitize_string(remove_numbers(i)) for i in item.split(by)]
    return split_items


def split_no_whitespace(item: str, by: str) -> list[str]:
    split_items = [i.strip() for i in item.split(by)]
    return split_items
