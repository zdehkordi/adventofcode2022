from pathlib import Path
import sys

sys.setrecursionlimit(5000)

class parse:
    @staticmethod
    def input(p: str):
        return Path(p).read_text()

def find_marker(s: str, i: int = 4) -> int:
    if len(set(s[:4])) == 4:
        return i
    else:
        return find_marker(s[1:], i + 1)

def find_message_marker(s: str, i: int = 14) -> int:
    if len(set(s[:14])) == 14:
        return i
    else:
        return find_message_marker(s[1:], i + 1)
    
def solve(p: str) -> int:
    return find_marker(parse.input(p))

def solve2(p: str) -> int:
    return find_message_marker(parse.input(p))