from __future__ import annotations
from pathlib import Path


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
