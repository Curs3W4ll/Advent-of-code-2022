from typing import List
from itertools import groupby
from enum import Enum
from re import findall


def move(crates: List[List[str]], fromIndex: int, toIndex: int, moveNumber: int) -> List[List[str]]:
    popped: List[str] = []
    for i in range(0, moveNumber):
        popped.append(crates[fromIndex].pop())
    popped.reverse()
    crates[toIndex].extend(popped)
    return crates

def run(input: List[str]):
    blankLineIndex: int = input.index("")
    columnNumber: int = len(findall(r" \d ", input[blankLineIndex-1]))
    crates: List[List[str]] = []

    for line in input[:blankLineIndex-1]:
        line = line + " "
        occs = findall(r"(\[.\] |    )", line)
        i: int = 0
        for occ in occs:
            if occ.rstrip():
                print(occ)
                while len(crates) <= i:
                    crates.append([])
                crates[i].append(findall(r"\[(.*)\]", occ)[0])
            i += 1

    for crate in crates:
        crate = crate.reverse()

    print(len(crates))
    print(crates)

    for line in input[blankLineIndex+1:]:
        matches = findall(r"(\d+)", line)
        crates = move(crates, int(matches[1]) - 1, int(matches[2]) - 1, int(matches[0]))

    print(f"Crates top list: '{''.join(elem[-1] for elem in crates if elem[-1])}'")
