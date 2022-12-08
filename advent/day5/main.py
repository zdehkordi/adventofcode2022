from pathlib import Path
import sys

sys.setrecursionlimit(5000)

Stack = list[str]
Stacks = list[Stack]

class parse:
    @staticmethod
    def num_stacks(input: str) -> int:
        return int(input[-2])

    @staticmethod
    def stacks(path: str) -> Stacks:
        raw = Path(path).read_text().split('\n\n')[0].splitlines()
        stacks = raw[:-1]
        num = parse.num_stacks(raw[-1])

        return [[s[4*i + 1] for s in stacks if s[4*i + 1] != ' '] for i in range(num)]
        
    @staticmethod
    def instructions(path: str) -> list[str]:
        return Path(path).read_text().split('\n\n')[1].splitlines()

def top(s: Stack) -> str:
    return s[0]

def remove(s: Stack, i: int) -> Stack:
    return s[i:]

def add(s: Stack, crates: list[str]) -> Stack:
    return [*crates, *s]


def decide(s: Stack, i: int, num: int, fro: int, to: int, add_crates: list[str]) -> Stack:
    if i == fro - 1:
        return remove(s, num)
    elif i == to - 1:
        return add(s, add_crates)
    else:
        return s

def move(ss: Stacks, fro: int, to: int) -> Stacks:
    return [decide(s, i, 1, fro, to, [ss[fro-1][0]]) for i, s in enumerate(ss)]

def move_many(ss: Stacks, num: int, fro: int, to: int) -> Stacks:
    return [decide(s, i, num, fro, to, ss[fro-1][:num]) for i, s in enumerate(ss)]

def move_all(ii: list[str], ss: Stacks) -> Stacks:
    if not ii:
        return ss
    else:
        inst = ii[0].split(" ")
        num, fro, to = int(inst[1]), int(inst[3]), int(inst[5])
        if num > 1:
            return move_all([f"move {num-1} from {fro} to {to}"] + ii[1:], move(ss, fro, to))
        else:
            return move_all(ii[1:], move(ss, fro, to))

def move_all_simultaneous(ii: list[str], ss: Stacks) -> Stacks:
    if not ii:
        return ss
    else:
        inst = ii[0].split(" ")
        num, fro, to = int(inst[1]), int(inst[3]), int(inst[5])
        return move_all_simultaneous(ii[1:], move_many(ss, num, fro, to))

def solve(p: str) -> str:
    instructions = parse.instructions(p)
    stacks = parse.stacks(p)

    moved_stacks = move_all(instructions, stacks)
    return str().join([top(s) for s in moved_stacks])

def solve2(p: str) -> str:
    instructions = parse.instructions(p)
    stacks = parse.stacks(p)

    moved_stacks = move_all_simultaneous(instructions, stacks)
    return str().join([top(s) for s in moved_stacks])