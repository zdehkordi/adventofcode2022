from pathlib import Path
from operator import add

def parse_input(path: str) -> list[list[int]]:
    return [x.split(" ") for x in Path(path).read_text().splitlines()]

rules: dict[str, dict[str, int]] = {
    "A": {
        "X": 3,
        "Y": 6,
        "Z": 0
    },
    "B": {
        "X": 0,
        "Y": 3,
        "Z": 6
    },
    "C": {
        "X": 6,
        "Y": 0,
        "Z": 3
    },
}

rules2: dict[str, int] = {
    "X": 1, "Y": 2, "Z": 3
}

def score_round(them: str, you: str) -> int:
    return add(rules[them][you], rules2[you])

def score_game(p: str) -> int:
    rounds = parse_input(p)
    return sum([score_round(*r) for r in rounds])