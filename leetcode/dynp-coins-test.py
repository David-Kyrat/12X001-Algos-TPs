from math import ceil
from typing import List

from prettytable import PrettyTable


def mprint(matrix: List[List], cns: str | List[int] = ""):
    p = PrettyTable()
    for i, row in enumerate(matrix):
        p.add_row([f"{i + 1}:", *(row or [""] * len(cns))])
    print("_________________")
    print("    ", cns)
    print(p.get_string(header=False, border=False))
    print("-----------------")


def solve(S: int, cs: List[int]) -> list[list[int]]:
    """S: goal,  cs: set of coins"""
    if S == 0 or not cs:
        return [[]]
    A = [[0] * len(cs) for _ in range(S)]

    def solve_before(s: int):
        for i, c in enumerate(cs):
            if c == s:
                A[s - 1][i] = 1
                return A[s - 1][:]
        # mprint(A, cs)
        tmp: List[List[int]] = []  # we have A[0] -> A[s-1] => find A[s]
        hi = s - 1  # i, hi => 2 pointers on 0 -> s//2 (i), s -> s//2 (hi)
        # e.g. 2: 1 + 1, 3: 1 + 2, 2 + 1
        for i in range(ceil(s / 2)):
            # print(f"{i+1} + {hi} = {i + 1 + hi}")
            tmp.append([amnt_i + amnt_hi for amnt_i, amnt_hi in zip(A[i], A[hi - 1])])
            hi -= 1
        sol = min(tmp, key=lambda lst: sum(lst))  # min amount of coin used, is min of the sum of each element
        A[s - 1] = sol
        return sol[:]

    for s in range(1, S + 1):
        solve_before(s)
    return A



def get_sol(filled_mat, goal: int, coin_set: List[int]) -> List[int]:
    """takes filled matrix of solution for the coins problem
    where `S` in [0, goal] and return the array of coined used"""
    amounts = filled_mat[goal - 1]
    out = []
    for idx, amount in enumerate(amounts):
        # appends `amount` times `coin_set[idx]` to `out`
        out.extend(coin_set[idx] for _ in range(amount))
    return out


if __name__ == "__main__":
    # S, cs = 5, [1, 3, 4]
    # S, cs = 62, [25, 21, 10, 5, 1]
    S, cs = 48,[30, 24, 12, 6, 3, 1]
    A = solve(S, cs)
    print("")
    mprint(A, cs)
    print(get_sol(A, S, cs))

