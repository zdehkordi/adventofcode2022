from pathlib import Path
from typing import NamedTuple
import numpy as np

class Neighbors(NamedTuple):
    t: int
    b: int
    l: int
    r: int

class Coordinate(NamedTuple):
    x: int
    y: int

def num_visible(m: np.ndarray[np.ndarray[int]]) -> int:
    s = 0
    for x in range(m.shape[0]):
        for y in range(m.shape[1]):
            if is_edge(m, Coordinate(x, y)):
                s += 1
            elif is_visible(m[y][x], get_neighbors(m, Coordinate(x, y))):
                s += 1

    return s

def get_neighbors(m: np.ndarray[np.ndarray[int]], c: Coordinate) -> Neighbors:
    return Neighbors(m[:,c.x][0:c.y].max(),
                     m[:,c.x][c.y+1:].max(),
                     m[c.y,:][:c.x].max(),
                     m[c.y,:][c.x+1:].max())


def is_edge(m: np.ndarray[np.ndarray[int]], c: Coordinate) -> bool:
    return c.x in [0, m.shape[0] - 1] or c.y in [0, m.shape[1] - 1]

def is_visible(t: int, ns: Neighbors) -> bool:
    return any(t > n for n in ns)

def solve(p: str) -> int:
    m = [list(map(int, [*x])) for x in Path(p).read_text("UTF-8").splitlines()]
    return num_visible(np.array(m))
