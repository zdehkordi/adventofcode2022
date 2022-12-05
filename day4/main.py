from pathlib import Path
from dataclasses import dataclass

def parse_input(path: str) -> list[tuple[range, range]]:
    raw_pairs = Path(path).read_text().splitlines()
    pairs = (x.split(',') for x in raw_pairs)
    final_pairs = ((p[0].split('-'), p[1].split('-')) for p in pairs)
    return [(range(int(p[0][0]), int(p[0][1])+1), range(int(p[1][0]), int(p[1][1])+1)) for p in final_pairs]

def fully_contains(r1: range, r2: range) -> bool:
    return set(r1).issuperset(set(r2)) or set(r2).issuperset(set(r1))

def num_supersets(p: str) -> int:
    pairs = parse_input(p)

    return sum(1 for p in pairs if fully_contains(*p))

