"""
--- Day 4: Passport Processing ---
You arrive at the airport only to realize that you grabbed your North Pole Credentials instead of your passport. While these documents are extremely similar, North Pole Credentials aren't issued by a country and therefore aren't actually valid documentation for travel in most of the world.

It seems like you're not the only one having problems, though; a very long line has formed for the automatic passport scanners, and the delay could upset your travel itinerary.

Due to some questionable network security, you realize you might be able to solve both of these problems at the same time.

The automatic passport scanners are slow because they're having trouble detecting which passports have all required fields. The expected fields are as follows:

byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)
Passport data is validated in batch files (your puzzle input). Each passport is represented as a sequence of key:value pairs separated by spaces or newlines. Passports are separated by blank lines.

Here is an example batch file containing four passports:

ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
The first passport is valid - all eight fields are present. The second passport is invalid - it is missing hgt (the Height field).

The third passport is interesting; the only missing field is cid, so it looks like data from North Pole Credentials, not a passport at all! Surely, nobody would mind if you made the system temporarily ignore missing cid fields. Treat this "passport" as valid.

The fourth passport is missing two fields, cid and byr. Missing cid is fine, but missing any other field is not, so this passport is invalid.

According to the above rules, your improved system would report 2 valid passports.

Count the number of valid passports - those that have all required fields. Treat cid as optional. In your batch file, how many passports are valid?
"""
from __future__ import annotations
from pprint import PrettyPrinter
from helper import *
import re

p = PrettyPrinter()


def validate_birth_year(year: str) -> bool:
    try:
        y = int(year)
        if 1920 <= y <= 2002:
            return True
        else:
            return False
    except:
        return False


def validate_issue_year(year: str) -> bool:
    try:
        y = int(year)
        if 2010 <= y <= 2020:
            return True
        else:
            return False
    except:
        return False


def validate_expiration_year(year: str) -> bool:
    try:
        y = int(year)
        if 2020 <= y <= 2030:
            return True
        else:
            return False
    except:
        return False


def validate_height(height: str) -> bool:
    matches = re.match(r"(\d+)(cm|in)", height)
    try:
        g = matches.groups()
        digits, unit = int(g[0]), g[1]
        if unit == "cm" and 150 <= digits <= 193:
            return True
        elif unit == "in" and 59 <= digits <= 76:
            return True
        else:
            return False
    except:
        return False


def validate_hair_color(color: str) -> bool:
    if re.match(r"^#[a-fA-F0-9]{6}$", color):
        return True
    else:
        return False


def validate_eye_color(color: str) -> bool:
    return color in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}


def validate_passport_id(number: str) -> bool:
    if re.match(r"^[0-9]{9}$", number):
        return True
    else:
        return False


def get_passport_dict(entry_list: list[str]) -> dict[str, str]:
    passport = {}
    for row in entry_list:
        seperated = row.split(" ")
        for entry in seperated:
            name, value = [item.strip() for item in entry.split(":")]
            passport[name] = value
    return passport


def contains_all_required_fields(passport: dict[str, str]) -> bool:
    without_cid = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    with_cid = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"}
    passport_set = set(passport.keys())
    if passport_set == without_cid or passport_set == with_cid:
        return True
    else:
        return False


def part1(data: list[list[str]]) -> int:
    valid_passports = 0
    for entry in data:
        passport = get_passport_dict(entry)
        if contains_all_required_fields(passport):
            valid_passports += 1
    return valid_passports


def run_all_validations(passport: dict[str, str]) -> bool:
    passed = 0
    for key, value in passport.items():
        if key == "byr" and validate_birth_year(value):
            passed += 1
        elif key == "ecl" and validate_eye_color(value):
            passed += 1
        elif key == "eyr" and validate_expiration_year(value):
            passed += 1
        elif key == "hcl" and validate_hair_color(value):
            passed += 1
        elif key == "hgt" and validate_height(value):
            passed += 1
        elif key == "iyr" and validate_issue_year(value):
            passed += 1
        elif key == "pid" and validate_passport_id(value):
            passed += 1

    if passed == 7:
        return True
    else:
        return False


def part2(data: list[list[str]]) -> int:
    valid_passports = 0
    for entry in data:
        passport = get_passport_dict(entry)
        if contains_all_required_fields(passport) and run_all_validations(passport):
            valid_passports += 1
    return valid_passports


if __name__ == "__main__":
    data = read_as_string_list_blanklines(
        "/home/dimitrios/dev/adventofcode2020/adventofcode2020/day04_input.txt"
    )
    result1 = part1(data)
    p.pprint(result1)

    result2 = part2(data)
    p.pprint(result2)
