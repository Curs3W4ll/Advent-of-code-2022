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
    gettingContentFromStdin: bool = True
    fileToGetContentFrom: str = None

    def __init__(self, dayToLaunch: int = datetime.today().day, gettingContentFromStdin: bool = True, fileToGetContentFrom: str = None):
        self.dayToLaunch = dayToLaunch
        self.gettingContentFromStdin = gettingContentFromStdin
        self.fileToGetContentFrom = fileToGetContentFrom


def readInput() -> List[str]:
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
    return content

def readArgs():
    args: Arguments = Arguments()

    for arg in argv[1:]:
        if arg.isnumeric():
            args.dayToLaunch = int(arg)
        else:
            args.gettingContentFromStdin = False
            args.fileToGetContentFrom = arg

    return args


def entrypoint():
    args: Arguments = readArgs()
    content: List[str] = None

    if not args.gettingContentFromStdin:
        try:
            content = readFile(args.fileToGetContentFrom)
        except:
            content = readInput()
    else:
        content = readInput()

    if (args.dayToLaunch > 25 or args.dayToLaunch < 1):
        args.dayToLaunch = 5
    print(asciiart, end="")
    message: str = f"Starting day {args.dayToLaunch}"
    messagereplace: str = "".join('~' * len(message))
    print(f"{asciiartsnow}{message}{asciiartsnow}")
    print(f"{asciiartsnow}{messagereplace}{asciiartsnow}")
    dayModule = __import__(str(args.dayToLaunch))

    dayModule.run(content)


if __name__ == "__main__":
    entrypoint()
