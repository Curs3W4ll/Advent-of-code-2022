from typing import List
from itertools import groupby
from enum import Enum


def getCharPriority(char: str) -> int:
    adjust: int = 0

    if not char:
        return 0

    if char[0].isupper():
        adjust = 38
    elif char[0].islower():
        adjust = 96
    else:
        return 0
    return ord(char[0]) - adjust


i = 0
def run(input: List[str]):
    halfing_sum: int = 0
    for line in input:
        half1, half2 = line[:int(len(line)/2)], line[int(len(line)/2):]
        commons = list(set(half1)&set(half2))
        if commons:
            halfing_sum = halfing_sum + getCharPriority(commons[0])
    print(f"Sum of halfing priorities is: {halfing_sum}")

    lines_sum: int = 0
    i: int = 0
    while i < len(input):
        line1, line2, line3 = input[i], input[i+1], input[i+2]
        commons = list(set(line1)&set(line2)&set(line3))
        if commons:
            lines_sum = lines_sum + getCharPriority(commons[0])
        i = i + 3
    print(f"Sum of lines priorities is: {lines_sum}")
