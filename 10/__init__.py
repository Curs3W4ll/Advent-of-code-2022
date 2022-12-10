from typing import List, Dict, Tuple
from itertools import groupby
from enum import Enum
from re import findall
from sys import exit


x: int = 1
cycle: int = 0
nextCycleStep: int = 20
cycleSteps: Dict[int, Tuple[int, int]] = {}


def drawCycle() -> None:
    global cycle

    #  print("For cycle", cycle)
    index: int = (cycle-1)%40
    #  print("Index:", index)
    print("#" if index in [x-1, x, x+1] else ".", end="")
    if index == 39:
        print()

def addCycle(n: int = 1) -> None:
    global cycle
    global nextCycleStep
    global cycleSteps

    for i in range(0, n):
        cycle+=1
        drawCycle()
        if cycle >= nextCycleStep:
            cycleSteps[cycle] = x, cycle*x
            nextCycleStep += 40

def doNoop() -> None:
    addCycle()

def doAddx(n: int) -> None:
    global x

    addCycle(2)
    x+=n

def parseInstruction(line: str) -> None:
    instr: str = line.split(" ")[0]
    match instr:
        case "noop":
            doNoop()
        case "addx":
            doAddx(int(line.split(" ")[1]))

def run(input: List[str]) -> None:
    global cycleSteps

    for line in input:
        parseInstruction(line)

    print("Cycle steps are:")
    print(cycleSteps)
    print("=" * 100)

    for cycle, t in cycleSteps.items():
        x, strength = t
        print(f"During the {cycle}th cycle, register X has the value {x}, so the signal strength is {strength} = {cycle*x}.")
    print("=" * 100)

    print(f"Sum of the first six cycles (20th, 60th, 100th, 140th, 180th and 220th): {sum([cycleSteps[cycle][1] for cycle in range(20, 221, 40)])}")
