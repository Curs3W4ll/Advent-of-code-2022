from typing import List
from itertools import groupby

def run(input: List[str]):
    l = [list(g) for k,g in groupby(input, key=bool) if k]
    l = [sum([int(e) for e in li]) for li in l]
    l.sort()

    if len(l) < 1:
        print("List is empty")
    else:
        print(f"Maximum number is {max(l)}")

    if len(l) < 3:
        print("List is too short to get three higher numbers sum, list len:", len(l))
    else:
        print(f"Sum of the three higher numbers is {l[-1] + l[-2] + l[-3]}")
