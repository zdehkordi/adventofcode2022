from pathlib import Path

def sum_calories(cals: list[list[int]]) -> list[int]:
    return list(map(sum, cals))

def find_max_calories(p: str) -> int:
    inventory = parse_input(p)
    sums = sum_calories(inventory)
    return max(sums)

def find_calories_in_top_three_elves(p: str) -> int:
    inventory = parse_input(p)
    sums = sorted(sum_calories(inventory), reverse=True)
    return sum(sums[:3])

def parse_input(path: str) -> list[list[int]]:
    with Path(path).open("r") as f:
        elves = []
        elf = []
        for line in f.readlines():
            l = line.replace("\n", "")
            if l:
                elf.append(int(l))
            else:
                elves.append(elf[:])
                elf = []
        elves.append(elf[:])
        return elves


