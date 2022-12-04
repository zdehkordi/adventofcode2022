from pathlib import Path

def parse_input(path: str) -> list[list[int]]:
    return Path(path).read_text().splitlines()

def is_capitalized(s: str) -> bool:
    return s.capitalize() == s

def get_priority(item: str) -> int:
    return ord(item) - 38 if is_capitalized(item) else ord(item) - 96

