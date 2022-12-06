from typing import List
from itertools import groupby
from enum import Enum
from re import findall


def run(input: List[str]):

    for line in input:
        tmp: List[str] = []
        i: int = 0

        for c in line:
            if c in tmp:
                while tmp and c in tmp:
                    tmp.pop(0)
            tmp.append(c)
            if len(tmp) > 3:
                print(i + 1)
                break
            i += 1

        for c in line:
            if c in tmp:
                while tmp and c in tmp:
                    tmp.pop(0)
            tmp.append(c)
            if len(tmp) > 13:
                print(i + 1)
                break
            i += 1
