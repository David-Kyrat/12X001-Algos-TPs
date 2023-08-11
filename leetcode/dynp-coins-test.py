from math import ceil
from pprint import PrettyPrinter
from typing import List, Set, Tuple

from prettytable import PrettyTable

pprint = PrettyPrinter(indent=4).pprint


def mprint(matrix: List[List], cns: str | List[int] = ""):
    p = PrettyTable()
    for i, row in enumerate(matrix):
        p.add_row([f"{i}:", *row])
    print("_________________")
    print("    ", cns)
    print(p.get_string(header=False, border=False))
    print("-----------------")


def solve(S: int, cs: List[int]):
    """S: goal,  cs: set of coins"""
    if S == 0 or not cs:
        return [[]]
    K = len(cs)
    A = [[0] * K for _ in range(S)]

    def solve_before(s: int):
        nonlocal A
        for i, c in enumerate(cs):
            if c == s:
                A[s - 1][i] = 1
                return A[s - 1][:]
        # if not
        print(" ")
        print("s =", s)
        mprint(A, cs)
        tmp: List[List[int]] = []  # we have A[0] -> A[s-1] => find A[s]
        hi = s - 1  # i, hi => 2 pointers on 0 -> s//2 (i), s -> s//2 (hi)
        # e.g. 2: 1 + 1, 3: 1 + 2, 2 + 1
        visited_pairs: Set[Tuple[int, int]] = set()
        for i in range(ceil(s / 2)):
            # p = i + 1, hi
            # m, M = min(p), max(p)
            # if (m, M) in visited_pairs: continue
            print(f"{i+1} + {hi} = {i + 1 + hi}")
            # visited_pairs.add((m, M))
            tmp.append([amnt_i + amnt_hi for amnt_i, amnt_hi in zip(A[i], A[hi - 1])])
            hi -= 1
        sol = min(tmp, key=lambda lst: sum(lst))  # min amount of coin used, is min of the sum of each element
        A[s - 1] = sol
        return sol[:]

    for s in range(1, S + 1):
        solve_before(s)

    return A


if __name__ == "__main__":
    S, cs = 20, [1, 3, 4]
    A = solve(S, cs)
    print("")
    print("Solution:")
    mprint(A, cs)
