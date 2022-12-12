from typing import List, Dict, Tuple
from itertools import groupby
from enum import Enum
from re import findall
from sys import exit
from copy import deepcopy

class Monkey:
    id: int
    items: List[int]
    operation: str
    testOperation: str
    testOperationTrueThrowTo: int
    testOperationFalseThrowTo: int
    inspected: int = 0

    def __init__(self, items: List[int], operation: str, testOperation: str, testOperationTrueThrowTo: int, testOperationFalseThrowTo: int, id: int = None):
        self.id = id
        self.items = items
        self.operation = operation
        self.testOperation = testOperation
        self.testOperationTrueThrowTo = testOperationTrueThrowTo
        self.testOperationFalseThrowTo = testOperationFalseThrowTo

    def playWithFirstItem(self, divide: bool = True) -> Tuple[int, int]:
        old: int = self.items.pop(0)
        throwTo: int = self.testOperationFalseThrowTo
        new: int = eval(self.operation)
        if divide:
            new = int(new // 3)

        if eval(self.testOperation) == 0:
            throwTo = self.testOperationTrueThrowTo

        self.inspected+=1

        return new, throwTo

    def run(self, divide: bool = True) -> Dict[int, List[str]]:
        toMove: Dict[int, List[str]] = {}

        while self.items:
            item, throwTo = self.playWithFirstItem(divide)
            if not throwTo in toMove.keys():
                toMove[throwTo] = []
            toMove[throwTo].append(item)
        return toMove

    def display(self) -> None:
        print(f"Monkey {self.id}")
        print(f"  Starting items: {self.items}")
        print(f"  Operation: {self.operation}")
        print(f"  Test: {self.testOperation}")
        print(f"    If true: throw to monkey {self.testOperationTrueThrowTo}")
        print(f"    If false: throw to monkey {self.testOperationFalseThrowTo}")

    def getId(self) -> int:
        return self.id

    def addItems(self, items: List[int]) -> None:
        self.items.extend(items)

    def getInspected(self) -> int:
        return self.inspected


def parseMonkey(data: List[str]) -> Monkey:
    id: int = int(findall(r"(\d+)", data[0])[0])
    items: List[int] = [int(x) for x in findall(r"[^\d](\d+)", data[1])]
    operation: str = findall(r"= (.*)", data[2])[0]
    testOperation: str = "new % " + findall(r"(\d+)", data[3])[0]
    testOperationTrueThrowTo: int = int(findall(r"(\d+)", data[4])[0])
    testOperationFalseThrowTo: int = int(findall(r"(\d+)", data[5])[0])

    return Monkey(items, operation, testOperation, testOperationTrueThrowTo, testOperationFalseThrowTo, id)

def parseMonkeys(input: List[str]) -> List[Monkey]:
    data: List[List[str]] = []
    tmp: List[str] = []

    for e in input:
        if not e:
            data.append(deepcopy(tmp))
            tmp.clear()
        else:
            tmp.append(e)
    if tmp:
        data.append(deepcopy(tmp))

    return [parseMonkey(x) for x in data]

def doRound(monkeys: List[Monkey], divide: bool = True) -> List[Monkey]:
    for monkey in monkeys:
        toThrow: Dict[int, List[str]] = monkey.run()
        for m in monkeys:
            id: int = m.getId()
            if id in toThrow.keys():
                m.addItems(toThrow.pop(id))

    return monkeys

def run(input: List[str]) -> None:
    monkeys: List[Monkey] = parseMonkeys(input)

    #  for i in range(0, 20):
    #      monkeys = doRound(monkeys)
    for i in range(0, 10000):
        monkeys = doRound(monkeys, False)

    inspected: List[int] = [monkey.getInspected() for monkey in monkeys]
    inspected.sort()
    print(inspected[-1] * inspected[-2])
