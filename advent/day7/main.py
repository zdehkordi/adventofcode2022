from __future__ import annotations
from functools import reduce

import os
from pathlib import Path
import re
from itertools import accumulate

def exec_command(path: list[str], directories: dict, cmd: str) -> list[str, dict]:
    if cmd == "$ cd /":
        return [["/"], directories]
    if cmd == "$ cd ..":
        return [path[:-1], directories]
    if cmd == "$ ls":
        return [path, directories]
    if re.match(r"\$ cd (.+)$", cmd):
        return [[*path, re.match(r"\$ cd (.+)$", cmd)[1]], directories]
    if re.match(r"dir (.+)$", cmd):
        new_dir = re.match(r"dir (.+)$", cmd)[1]
        return [path, {**directories, os.path.join(os.path.join(*path), new_dir): {}}]
    if re.match(r"(\d+) (.+)$", cmd):
        m = re.match(r"(\d+) (.+)$", cmd)
        p = os.path.join(*path)
        return [path, {**directories, p: {**directories[p], m[2]: int(m[1])}}]
    else:
        raise Exception("cmd not found")

def exec_command_file(p: str) -> dict:
    cmds = Path(p).read_text().splitlines()

    def help(path, directories, cmds):
        if not cmds:
            return [path, directories]
        else:
            return help(*exec_command(path, directories, cmds[0]), cmds[1:])

    return help([], {"/": {}}, cmds)[1]

def size(p: str, dir: str) -> int:
    directories = exec_command_file(p)

    dir_sums = [sum(v.values()) for k, v in directories.items() if str(k).startswith(dir)]

    return sum(dir_sums)

def solve(p: str) -> int:
    directories = exec_command_file(p).keys()

    return sum(filter(lambda x: x <= 100000, [size(p, d) for d in directories]))

