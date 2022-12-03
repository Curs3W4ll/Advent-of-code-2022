#!/usr/bin/env python3.10

from sys import stdin,argv
from datetime import datetime
from dataclasses import dataclass
from typing import List


asciiart: str = """
                  .-----.
                ,/ mmmmmm\\
               (  / o  o \\
   ,---.       /,L  ~,L~  J
   (.  n      /( #,.d##b.,#
   \\___/     (##)\"###uu###\"._
   P^~~?  _.--\"\"  \"######\"   ~-.
   /    \'          \"\"\"\"        `,
   |                 |||     _   .`-._                ,--._       ______.
    \\        ,       |||   ____..(,~  \\         _..--X:~.`\\`.    /:,----'
      ~----~/       ///  ./@==/\\  `~--~-.     ,'  ,'. \\| \\_.W\\  / /
            (..___,---,,'//  /_.-',`  \\  \\   /         '~-..' `/ /|
            |..___[=[-~X`----~   `    , __L__L________________/ /||
           /mmm,,_`,-'/ `  \\       \\   //~Y~7~~~~~~~~~~~~~~~~/ /~||
            `| ~\"\"\"`-'  \\       /  ' `//  \\: \\     (    )   / / /|/|
             |     /_________________//____L_______________/./___/:|
        ,-,  | `_,'//~~~~~~~~~~~~~~~77~~~~~Y~~~~~~~~~~~~~~7 /~7~7 /
       / /_____(__//   /    \\   \\  //     /  /      \\   \\/ / ( / /|
  =-=O(| Y~~~~~~~Y' -'            //     / _/._         / /   / /||
       \\  `--------.__.^-----------------+-----+-------/./---/./-'|
        `._____________________________________________~~Seal~~____~~~~~~/
     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
asciiartsnow: str = "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

@dataclass
class Arguments:
    dayToLaunch: int = datetime.today().day
    gettingContentFromStdin: bool = False
    fileToGetContentFrom: str = None

    def __init__(self, dayToLaunch: int = datetime.today().day, gettingContentFromStdin: bool = False, fileToGetContentFrom: str = None):
        self.dayToLaunch = dayToLaunch
        self.gettingContentFromStdin = gettingContentFromStdin
        self.fileToGetContentFrom = fileToGetContentFrom


def readInput() -> List[str]:
    print("Reading from stdin...")
    input = []
    for line in stdin:
        input.append(line.rstrip())
    return input

def readFile(filePath: str) -> List[str]:
    input: List[str] = []
    content: List[str] = []
    with open(filePath) as f:
        input: List[str] = f.readlines()

    [content.append(elem.rstrip()) for elem in input]
    print(f"Content got from {filePath}")
    return content

def readArgs():
    args: Arguments = Arguments()

    for arg in argv[1:]:
        if arg == "stdin":
            args.gettingContentFromStdin = True
        elif arg.isnumeric():
            args.dayToLaunch = int(arg)
        else:
            args.fileToGetContentFrom = arg

    return args


def entrypoint():
    args: Arguments = readArgs()
    content: List[str] = None

    if (args.dayToLaunch > 25 or args.dayToLaunch < 1):
        args.dayToLaunch = 1
    if not args.gettingContentFromStdin:
        try:
            if args.fileToGetContentFrom:
                content = readFile(args.fileToGetContentFrom)
            else:
                print(f"Trying reading file ./{args.dayToLaunch}/input.txt...")
                content = readFile(f"./{args.dayToLaunch}/input.txt")
        except:
            content = readInput()
    else:
        content = readInput()

    print(asciiart, end="")
    message: str = f"Starting day {args.dayToLaunch}"
    messagereplace: str = "".join('~' * len(message))
    print(f"{asciiartsnow}{message}{asciiartsnow}")
    print(f"{asciiartsnow}{messagereplace}{asciiartsnow}")
    dayModule = __import__(str(args.dayToLaunch))

    dayModule.run(content)


if __name__ == "__main__":
    entrypoint()
