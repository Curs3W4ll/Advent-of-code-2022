from typing import List
from itertools import groupby
from enum import Enum


def getRange(s: str):
    ranges = [int(e) for e in s.split('-')]
    if len(ranges) < 2:
        return range(0, 1)
    return range(ranges[0], ranges[1])

def getRanges(line: str):
    return [getRange(elem) for elem in line.split(',')]

def rangeContains(range1, range2) -> bool:
    container = range(range1.start, range1.stop + 1)
    return range2.start in container and range2.stop in container

def rangeOverlap(range1, range2) -> bool:
    container = range(range1.start, range1.stop + 1)
    return range2.start in container or range2.stop in container

def run(input: List[str]):
    completeOverlapSum: int = 0
    partialOverlapSum: int = 0
    for line in input:
        ranges = getRanges(line)
        if rangeContains(ranges[0], ranges[1]) or rangeContains(ranges[1], ranges[0]):
            completeOverlapSum = completeOverlapSum + 1
        if rangeOverlap(ranges[0], ranges[1]) or rangeOverlap(ranges[1], ranges[0]):
            partialOverlapSum = partialOverlapSum + 1
    print(f"Number of pairs that contains the other: {completeOverlapSum}")
    print(f"Number of pairs that overlaps with another: {partialOverlapSum}")
