from typing import List, Dict, Tuple
from itertools import groupby
from enum import Enum
from re import findall
from sys import exit


class Dir:
    name: str
    files: Dict[str, int] = {}
    dirs: Dict[str, 'Dir'] = {}

    def __init__(self, name: str):
        self.name = name
        self.dirs = {}
        self.files = {}

    def getSize(self) -> int:
        return sum(self.files.values())

    def getAt(self, path: List[str]) -> 'Dir':
        if not path or not path[0]:
            return self
        if not path[0] in self.dirs:
            self.dirs[path[0]] = Dir(path[0])
        return self.dirs[path[0]].getAt(path[1:])

    def addFile(self, name: str, size: int) -> None:
        if name in self.files.keys():
            print(f"The file '{name}' already exists")
            exit(1)
        self.files[name] = size

    def getSums(self, fromDir: str = "") -> Dict[str, int]:
        sums: Dict[str, int] = {}
        currentPath: str = f"{fromDir}/{self.name}"
        if self.name == "/":
            currentPath = "/"

        sums[currentPath] = 0
        for fsize in self.files.values():
            sums[currentPath] += fsize

        if self.name == "/":
            currentPath = ""
        for dir in self.dirs.values():
            sums.update(dir.getSums(currentPath))

        return sums

    def getSumsRec(self, fromDir: str = "") -> Tuple[Dict[str, int], int]:
        sums: Dict[str, int] = {}
        currentPath: str = f"{fromDir}/{self.name}"
        if self.name == "/":
            currentPath = "/"

        sums[currentPath] = 0
        for fsize in self.files.values():
            sums[currentPath] += fsize

        for dir in self.dirs.values():
            if self.name == "/":
                s, size = dir.getSumsRec("")
            else:
                s, size = dir.getSumsRec(currentPath)
            sums.update(s)
            sums[currentPath] += size

        return sums, sums[currentPath]

    def displayDebug(self, prefix: str = ""):
        print(f"{prefix}- {self.name} (dir)")
        for dname, dir in self.dirs.items():
            dir.displayDebug(prefix + "  ")
        for fname, fsize in self.files.items():
            print(f"{prefix}  - {fname} (file, size={fsize})")

COMMAND_HEADER = "$ "
DIRECTORY_HEADER = "dir "

path: List[str] = []
data: Dir = Dir("/")
currentDir = data

def parseCommand(command: str) -> None:
    if command.startswith("cd"):
        goToPath: str = command[2:].lstrip(" ")
        global currentDir

        if goToPath == "..":
            path.pop()
        else:
            path.append(goToPath)
        currentDir = data.getAt(path)
    elif command.startswith("ls"):
        pass
    else:
        print(f"Unknown command: '{command}'")

def parseElemInfos(infos: str) -> None:
    if not infos.startswith(DIRECTORY_HEADER):
        storeFileSize(infos.split(" ")[0], " ".join(infos.split(" ")[1:]))

def storeFileSize(ssize: str, name: str) -> None:
    if not ssize.isdigit():
        exit(1)
    size: int = int(ssize)
    currentDir.addFile(name, size)

def run(input: List[str]):
    if input and input[0] == "$ cd /":
        input.pop(0)
    for line in input:
        if line.startswith(COMMAND_HEADER):
            parseCommand(line.lstrip(COMMAND_HEADER))
        else:
            parseElemInfos(line)

    sums = data.getSumsRec()[0]
    print(f"Sum of directories size < 100 000: {sum([v for v in sums.values() if v <= 100000])}")
    neededSize: int = 30000000 - (70000000 - sums["/"])
    couldDelete = [v for v in sums.values() if v > neededSize]
    if not couldDelete:
        print("None directory is large enough")
    else:
        couldDelete.sort()
        print(f"Size of the directory to delete: {couldDelete[0]}")
