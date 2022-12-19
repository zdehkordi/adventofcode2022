from pathlib import Path
from functools import reduce

def parse_input(path: str) -> list[str]:
    return Path(path).read_text().splitlines()

def parse_input_group(path: str) -> list[list[str]]:
    compartments = parse_input(path)
    return [compartments[s:s+3] for s in range(0, len(compartments), 3)]

def is_capitalized(s: str) -> bool:
    return s.capitalize() == s

def get_priority(item: str) -> int:
    return ord(item) - 38 if is_capitalized(item) else ord(item) - 96

def split_rucksack(items: str) -> tuple[str, str]:
    return items[0:len(items)//2], items[len(items)//2:]

def common_type(items: str) -> str:
    compartments = split_rucksack(items)
    return next(set(compartments[0]).intersection(compartments[1]).__iter__())

def common_type_group(compartments: tuple[str, str, str]) -> str:
    common = reduce(lambda x, y: set(x).intersection(set(y)), compartments)
    return next(common.__iter__())

def find_comp_priority(items: str) -> int:
    return get_priority(common_type(items))

def sum_compartment_priority(p: str) -> int:
    compartments = parse_input(p)
    return sum([find_comp_priority(c) for c in compartments])

def sum_compartment_priority_group(p: str) -> int:
    groups = parse_input_group(p)
    return sum([get_priority(common_type_group(g)) for g in groups])