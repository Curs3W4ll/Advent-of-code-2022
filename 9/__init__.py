from typing import List, Dict, Tuple
from itertools import groupby
from enum import Enum
from re import findall
from sys import exit

class Elem:
    visitedByTail: bool = False
    isStart: bool = False
    isTail: bool = False
    isHead: bool = False

    def __init__(self, start: bool = False, tail: bool = False, head: bool = False):
        self.isStart = start
        self.isTail = tail
        self.isHead = head
        self.visitedByTail = tail

    def hasBeenVisitedByTail(self) -> bool:
        return self.visitedByTail

    def notAnymoreHead(self) -> None:
        self.isHead = False
    def notAnymoreTail(self) -> None:
        self.isTail = False
    def nowHead(self) -> None:
        self.isHead = True
    def nowTail(self) -> None:
        self.isTail = True
        self.visitedByTail = True

    def display(self, printVisited: bool = False) -> None:
        print("H" if self.isHead else "T" if self.isTail else "s" if self.isStart else "#" if self.hasBeenVisitedByTail() and printVisited else ".", end="")

class Map:
    headX: int = 0
    headY: int = 0
    tailX: int = 0
    tailY: int = 0
    m: List[List[Elem]] = [[Elem(True)]]

    def display(self, printVisited: bool = False) -> None:
        for line in self.m:
            for elem in line:
                elem.display(printVisited)
            print()

    def getTailVisitedCases(self) -> int:
        sum: int = 0
        for line in self.m:
            for elem in line:
                sum += 1 if elem.hasBeenVisitedByTail() else 0
        return sum

    def addLine(self, top: bool = False) -> None:
        if top:
            self.m.insert(0, [Elem() for i in range(0, len(self.m[0]))])
            self.headY += 1
            self.tailY += 1
        else:
            self.m.append([Elem() for i in range(0, len(self.m[0]))])

    def addColumn(self, left: bool = False) -> None:
        if left:
            self.headX += 1
            self.tailX += 1
        for line in self.m:
            if left:
                line.insert(0, Elem())
            else:
                line.append(Elem())

    def doHeadMove(self, move: str) -> None:
        self.m[self.headY][self.headX].notAnymoreHead()

        match move:
            case "R":
                if len(self.m[0])-1 <= self.headX:
                    self.addColumn()
                self.headX+=1
            case "L":
                if self.headX <= 0:
                    self.addColumn(True)
                self.headX-=1
            case "U":
                if self.headY <= 0:
                    self.addLine(True)
                self.headY-=1
            case "D":
                if len(self.m)-1 <= self.headY:
                    self.addLine()
                self.headY+=1

        self.m[self.headY][self.headX].nowHead()

    def isTailAroundHead(self) -> bool:
        if abs(self.headX - self.tailX) > 1 or abs(self.headY - self.tailY) > 1:
            return False
        return True

    def doTailMove(self):
        self.m[self.tailY][self.tailX].notAnymoreTail()

        if not self.isTailAroundHead():
            if self.headX > self.tailX:
                self.tailX+=1
            elif self.headX < self.tailX:
                self.tailX-=1
            if self.headY > self.tailY:
                self.tailY+=1
            elif self.headY < self.tailY:
                self.tailY-=1

        self.m[self.tailY][self.tailX].nowTail()

    def makeMove(self, move: str, times: int, debug: bool = False) -> None:
        if debug:
            print(f"Doing move '{move}' {times} times")
        for i in range(0, times):
            if debug:
                print("==================")
            self.doHeadMove(move)
            if debug:
                self.display()
                print()
            self.doTailMove()
            if debug:
                self.display()
                print("==================")


def run(input: List[str]):
    m: Map = Map()

    for line in input:
        move: str = line.split(" ")[0]
        times: int = int(line.split(" ")[1])
        m.makeMove(move, times)

    m.display(True)
    print(f"Tail has visited {[m.getTailVisitedCases()]} cases")
