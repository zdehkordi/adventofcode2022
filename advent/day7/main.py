from __future__ import annotations

from pathlib import Path
import sys
from dataclasses import dataclass

sys.setrecursionlimit(30000)

class parse:
    @staticmethod
    def input(p: str):
        return Path(p).read_text()

    @staticmethod
    def directories(p: str):
        return [d[4:] for d in Path(p).read_text().splitlines() if d.startswith('dir')]

@dataclass(frozen=True)
class file:
    name: str
    size: int

    def get_size(self, input: str) -> int:
        return self.size

@dataclass(frozen=True)
class dir:
    name: str

    def get_size(self, input: str) -> int:
        return size(input, self.name)

class fs:
    @classmethod
    def parse(cls, console: str) -> file | dir:
        split = console.split(" ")
        if split[0] == "dir":
            return dir(split[1])
        else: 
            return file(split[1], int(split[0]))

def ls(input: str, dir: str) -> list[str]:
    return input.split(f"$ cd {dir}\n$ ls\n")[1].split("\n$")[0].split("\n")

def size(input: str, dir: str) -> int:
    objects = ls(input, dir)
    return sum(fs.parse(o).get_size(input) for o in objects)

def solve(p: str) -> int:
    input = parse.input(p)
    dirs = parse.directories(p)
    dir_sizes = [size(input, d) for d in dirs]
    big_dir_sizes = filter(lambda x: x <= 100000, dir_sizes)
    return sum(big_dir_sizes)