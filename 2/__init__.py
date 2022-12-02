from typing import List
from itertools import groupby
from enum import Enum

class MATCH_RESULT(Enum):
    LOSE = 0
    DRAW = 3
    WIN = 6

class PLAY(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

P1_PLAY_IDENTIFIERS: dict[str, PLAY] = {
    "A": PLAY.ROCK,
    "B": PLAY.PAPER,
    "C": PLAY.SCISSORS,
}

P2_PLAY_IDENTIFIERS: dict[str, PLAY] = {
    "X": PLAY.ROCK,
    "Y": PLAY.PAPER,
    "Z": PLAY.SCISSORS,
}

MATCH_RESULT_IDENTIFIERS: dict[str, PLAY] = {
    "X": MATCH_RESULT.LOSE,
    "Y": MATCH_RESULT.DRAW,
    "Z": MATCH_RESULT.WIN,
}


def getPlayForResult(play: PLAY, result: MATCH_RESULT) -> PLAY:
    match result:
        case MATCH_RESULT.WIN:
            match play:
                case PLAY.ROCK:
                    return PLAY.PAPER
                case PLAY.PAPER:
                    return PLAY.SCISSORS
                case PLAY.SCISSORS:
                    return PLAY.ROCK
        case MATCH_RESULT.DRAW:
            return play
        case MATCH_RESULT.LOSE:
            match play:
                case PLAY.ROCK:
                    return PLAY.SCISSORS
                case PLAY.PAPER:
                    return PLAY.ROCK
                case PLAY.SCISSORS:
                    return PLAY.PAPER

def getMatchResult(p2: PLAY, p1: PLAY) -> MATCH_RESULT:
    matchResult: MATCH_RESULT

    match p1:
        case PLAY.ROCK:
            match p2:
                case PLAY.ROCK:
                    matchResult = MATCH_RESULT.DRAW
                case PLAY.PAPER:
                    matchResult = MATCH_RESULT.LOSE
                case PLAY.SCISSORS:
                    matchResult = MATCH_RESULT.WIN
        case PLAY.PAPER:
            match p2:
                case PLAY.ROCK:
                    matchResult = MATCH_RESULT.WIN
                case PLAY.PAPER:
                    matchResult = MATCH_RESULT.DRAW
                case PLAY.SCISSORS:
                    matchResult = MATCH_RESULT.LOSE
        case PLAY.SCISSORS:
            match p2:
                case PLAY.ROCK:
                    matchResult = MATCH_RESULT.LOSE
                case PLAY.PAPER:
                    matchResult = MATCH_RESULT.WIN
                case PLAY.SCISSORS:
                    matchResult = MATCH_RESULT.DRAW
    return p1.value + matchResult.value

def getP1Play(match: str) -> PLAY:
    if len(match) < 3 or not match[0] in P1_PLAY_IDENTIFIERS:
        raise Exception(f"Cannot find any player 1 play in match: '{match}'")

    return P1_PLAY_IDENTIFIERS[match[0]]

def getP2Play(match: str) -> PLAY:
    if len(match) < 3 or not match[2] in P2_PLAY_IDENTIFIERS:
        raise Exception(f"Cannot find any player 2 play in match: '{match}'")

    return P2_PLAY_IDENTIFIERS[match[2]]

def getMatchShouldResult(match: str) -> PLAY:
    if len(match) < 3 or not match[2] in MATCH_RESULT_IDENTIFIERS:
        raise Exception(f"Cannot find any provided match result in match: '{match}'")

    return MATCH_RESULT_IDENTIFIERS[match[2]]

def run(input: List[str]):
    print(f"(1) Total score: {sum([getMatchResult(getP1Play(match), getP2Play(match)) for match in input])}")
    print(f"(2) Total score: {sum([getMatchResult(getP1Play(match), getPlayForResult(getP1Play(match), getMatchShouldResult(match))) for match in input])}")
