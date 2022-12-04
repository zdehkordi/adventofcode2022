from pathlib import Path
from operator import add
from typing import Callable

def parse_input(path: str) -> list[list[int]]:
    return [x.split(" ") for x in Path(path).read_text().splitlines()]

def score_action(them: str, you: str) -> int:
    score: dict[str, dict[str, int]] = {
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

    bonus: dict[str, int] = {
        "X": 1, "Y": 2, "Z": 3
    }

    return add(score[them][you], bonus[you])

def score_outcome(them: str, outcome: str) -> int:
    score: dict[str, dict[str, int]] = {
        "A": {
            "X": 3,
            "Y": 1,
            "Z": 2
        },
        "B": {
            "X": 1,
            "Y": 2,
            "Z": 3
        },
        "C": {
            "X": 2,
            "Y": 3,
            "Z": 1
        },
    }

    bonus: dict[str, int] = {
        "X": 0, "Y": 3, "Z": 6
    }

    return add(score[them][outcome], bonus[outcome]) 

def score_game(p: str, strategy: Callable[[str, str], int]) -> int:
    rounds = parse_input(p)
    return sum([strategy(*r) for r in rounds])

def score_game_with_action(p: str) -> int:
    return score_game(p, score_action)

def score_game_with_outcome(p: str) -> int:
    return score_game(p, score_outcome)