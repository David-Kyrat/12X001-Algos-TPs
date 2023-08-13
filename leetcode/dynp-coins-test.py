import enum
from math import ceil
from pprint import PrettyPrinter
from typing import List, Set, Tuple

from prettytable import PrettyTable

pprint = PrettyPrinter(indent=4).pprint


def mprint(matrix: List[List], cns: str | List[int] = ""):
    p = PrettyTable()
    for i, row in enumerate(matrix): p.add_row([f"{i + 1}:", *row])
    print("_________________")
    print("    ", cns)
    print(p.get_string(header=False, border=False))
    print("-----------------")

def solve(S: int, cs: List[int]) -> list[list[int]]:
    """S: goal,  cs: set of coins"""
    if S == 0 or not cs: return [[]]
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

    for s in range(1, S + 1): solve_before(s)
    return A

# WARN: methodology to Find DP rec relation from
# BT impl then caching BT impl

def coins2_BT_version(S: int, coins: list[int]):
    # sourcery skip: comprehension-to-generator
    """S: goal,  cs: set of coins, BT version => cached later"""
    if S == 0 or not cs: return [[]]
    def incr_ret(lst, idx):
        lst[idx] += 1#; print(lst)
        return lst
    cnt = 0
    def solve_rec(N: int, used: list[int]) -> list[int]:
        nonlocal coins, cnt
        #print("\n", f"N = {N},  used: {used}")
        if N <= 0: return used
        cnt += 1
        out1 = []
        # sol for N-c_1 + for (N-c_1)-c_1, for (N-c_1)-c_2 ...
        """ for i, c_i in enumerate(coins):
            print("\n", f"c_{i} = {c_i},  N = {N},  N-c_{i} = {N-c_i}")
            if N-c_i < 0: break # sorted increasing
            tmp2 = solve_rec(N - c_i, incr_ret(used.copy(), i))
            out1.append(tmp2)
        return min(out1) """
        return min(
            [
                solve_rec(N - c_i, incr_ret(used.copy(), i))
                for i, c_i in enumerate(coins)
                if N - c_i >= 0
            ]
        )
    a = solve_rec(S, [0] * len(coins))
    print(f"called {cnt} times")
    return a, cnt


def get_sol(filled_mat, goal: int, coin_set: List[int]) -> List[int]:
    """takes filled matrix of solution for the coins problem
    where `S` in [0, goal] and return the array of coined used"""
    amounts = filled_mat[goal - 1]
    out = []
    for idx, amount in enumerate(amounts):
        # appends `amount` times `coin_set[idx]` to `out`
        out.extend(coin_set[idx] for _ in range(amount))
    return out

import matplotlib.pyplot as plt
import numpy as np
def plot_solo(plot_x, plot_f, title: str = None, xlabel: str = None, ylabel: str = None, fLabel: str = None):
    """Plots a single function
    - plot_x: the x-axis values
    - plot_f: the y-values of the function
    - title: the title of the plot
    - xlabel: the label of the x-axis
    - ylabel: the label of the y-axis
    - fLabel: the label of the function
    """
    #plt.tight_layout(pad=5)
    fig = plt.figure()
    if title: plt.title(title)
    plt.grid()
    if xlabel: plt.xlabel(xlabel)
    if ylabel: plt.ylabel(ylabel)
    M, gap = max(plot_f), 0.25
    
    plt.xticks(plot_x)
    #plt.ylim(0, M + gap*M)
    plt.yticks(np.linspace(0, M, 27))
    if fLabel:
        plt.plot(plot_x, plot_f, '-b', label=fLabel, linewidth=1)
    else:
        plt.plot(plot_x, plot_f, '-b')
    #  plt.legend(prop={'size': 5})
    #  plt.legend(fontsize=7)
    fig.set_figheight(7)
    plt.legend()
    print("\nshowing plot\n")
    plt.show()
    #fig.show()
    #fig.tight_layout()

if __name__ == "__main__":
    S, cs = 20, [1, 3, 4]
    for 
    # S, cs = 62, [25, 21, 10, 5, 1]
    # S, cs = 48,[30, 24, 12, 6, 3, 1]
    
    res = coins2_BT_version(S, cs)
    # A = solve(S, cs)
    print("")
    print("Goal:", S, "coins:", cs)
    print("Solution:")
    print(res)
    # mprint(A, cs)
    # print(get_sol(A, S, cs))

""" def combine(l1: list[int], l2: list[int]):
    ""if l1 is sol for n1 and l2 for n2, then returned is the sol for n1+n2""
    if not l2: return l1
    if not l1: return l2
    print("combine", l1, l2)
    return [amnt_i_1 + amnt_i_2 for amnt_i_1, amnt_i_2 in zip(l1, l2)] """
