from copy import deepcopy
from math import inf, isfinite
from pprint import PrettyPrinter

from prettytable import PrettyTable

pprint = PrettyPrinter(indent=4).pprint


def mprint(matrix: list[list]):
    p = PrettyTable()
    for row in matrix: p.add_row(row)
    # for i, row in enumerate(matrix):
        # p.add_row([f"{i + 1}:", *row])
    print("_________________")
    print(p.get_string(header=False, border=False))
    print("-----------------")


def dp_all_pair_sp(V: list[int], L: list[list[int | float]]):
    # sourcery skip: use-itertools-product
    """Dyn-Prog sol to all pair shortest path problem,
    V: list of vertices, L: adjencency matrix (with weights)
    (non-existant edges must be present with weight inf)"""
    N, D = len(V), deepcopy(L)
    P = [[[i + 1] for _ in range(N)] for i in range(N)]
    # basis step for P
    for i, row in enumerate(D):
        for j, val in enumerate(row):
            if isfinite(val) and j != i:  # edge (i, j) exists
                P[i][j].append(j + 1)  # type: ignore
    mprint(P)
    for k in range(N):
        for i in range(N):
            for j in range(N):
                crt, candidate = D[i][j], min(D[i][j], D[i][k] + D[k][j])
                if candidate < crt:
                    P[i][j] = P[i][k] + P[k][j][1:] # dont add k twice
                    D[i][j] = candidate

        mprint(P)
                # D[i][j] = min(D[i][j], D[i][k] + D[k][j])
        print(" ")
    return D


if __name__ == "__main__":
    N = 6
    M = [
        [0, 1, inf, inf, 2, inf],
        [inf, 0, 6, 3, inf, inf],
        [inf, 5, 0, inf, inf, inf],
        [7, inf, inf, 0, inf, 2],
        [inf, inf, inf, inf, 0, 1],
        [inf, inf, inf, inf, inf, 0],
    ]
    V = list(range(1, N + 1))

    dp_all_pair_sp(V, M)
