from typing import List, Dict, Tuple
from itertools import groupby
from enum import Enum
from re import findall
from sys import exit


def isVisible(x: int, y: int, trees: List[List[int]], debug: bool = False) -> bool:
    checkingHigh: int = trees[y][x]
    hidden: bool = False

    if debug:
        print()
        print(f"For: [{x}, {y}]: {trees[y][x]}")

    for i in reversed(range(0, x)):
        if trees[y][i] >= checkingHigh:
            hidden = True
            break
    if not hidden:
        if debug:
            print("Visible from left")
        return True
    if debug:
        print("Not visible from left")

    hidden = False
    for i in range(x+1, len(trees[0])):
        if trees[y][i] >= checkingHigh:
            hidden = True
            break
    if not hidden:
        if debug:
            print("Visible from right")
        return True
    if debug:
        print("Not visible from right")

    hidden = False
    for i in reversed(range(0, y)):
        if trees[i][x] >= checkingHigh:
            hidden = True
            break
    if not hidden:
        if debug:
            print("Visible from top")
        return True
    if debug:
        print("Not visible from top")

    hidden = False
    for i in range(y+1, len(trees)):
        if trees[i][x] >= checkingHigh:
            hidden = True
            break
    if not hidden:
        if debug:
            print("Visible from bottom")
        return True
    if debug:
        print("Not visible from bottom")

    return False

def getViewScore(x: int, y: int, trees: List[List[int]], debug: bool = False) -> int:
    checkingHigh: int = trees[y][x]
    score: int = 0
    s: int = 1

    if debug:
        print()
        print(f"For: [{x}, {y}]: {trees[y][x]}")

    score = 0
    for i in reversed(range(0, x)):
        score += 1
        if trees[y][i] >= checkingHigh:
            break
    s *= score
    if debug:
        print("Score at left:", score, "So total score is:", s)

    score = 0
    for i in range(x+1, len(trees[0])):
        score += 1
        if trees[y][i] >= checkingHigh:
            break
    s *= score
    if debug:
        print("Score at right:", score, "So total score is:", s)

    score = 0
    for i in reversed(range(0, y)):
        score += 1
        if trees[i][x] >= checkingHigh:
            break
    s *= score
    if debug:
        print("Score at top:", score, "So total score is:", s)

    score = 0
    for i in range(y+1, len(trees)):
        score += 1
        if trees[i][x] >= checkingHigh:
            break
    s *= score
    if debug:
        print("Score at bottom:", score, "So total score is:", s)

    return s

def run(input: List[str]):
    if not input:
        print("Empty input")
        exit(1)

    trees: List[List[int]] = []
    width: int = len(input[0])
    for line in input:
        if not line.isdigit():
            print(f"Line '{line}' contains other than digits")
            exit(1)
        if len(line) != width:
            print(f"Line '{line}' as different width({len(line)}) than the reference line '{input[0]}'({width})")
            exit(1)

        trees.append([int(x) for x in line])

    scores: List[int] = []
    sum: int = 0
    for i in range(0, len(trees)):
        for y in range(0, width):
            sum += (1 if isVisible(y, i, trees) else 0)
            scores.append(getViewScore(y, i, trees, True))

    print(f"{sum} trees visible from outside")
    print(f"Maximum scenic score is {max(scores)}")
