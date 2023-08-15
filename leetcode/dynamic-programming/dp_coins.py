from math import ceil
from typing import List
from util import mprint, get_sol

# HINT: ============ Lecture Note version ============

def coinChange_lecture(cs: List[int], S: int) -> list[list[int]]:
    """S: goal,  cs: set of coins"""
    if S == 0 or not cs: return [[]]
    A = [[0] * len(cs) for _ in range(S)]

    def solve_before(s: int):
        for i, c in enumerate(cs):
            if c == s:
                A[s - 1][i] = 1
                return A[s - 1][:]
        tmp: List[List[int]] = []  # we have A[0] -> A[s-1] => find A[s]
        hi = s - 1  # i, hi => 2 pointers on 0 -> s/2 (i), s -> s/2 (hi)
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


# HINT: ============ Classic dp ======================


def coinChange_classic_dp(coins: list[int], goal: int) -> list[list[int]]:
    if not coins: return [[]]
    K, N = len(coins), goal
    # (N + 1): 0 is necessary for B.S. & I.S. [0..0]
    DP = [[0 for _ in range(K)] for _ in range(N + 1)]

    def incr_ret(lst: list[int], idx: int):
        tmp = lst.copy()
        tmp[idx] += 1
        return tmp

    # DP[k] represents the optimal amount of change that sums up to k
    for k in range(1, N + 1):
        DP[k] = (
            min(
                (incr_ret(DP[k - c_i], i) for i, c_i in enumerate(coins) if k - c_i >= 0),
                key=lambda lst: sum(lst),
            )
        )
    return DP

# NOTE: ==========================================

def coinChange_classic_dp_2(coins: list[int], goal: int) -> list[list[int]]:
    if not coins: return [[]]
    K, N = len(coins), goal
    # (N + 1): 0 is necessary for B.S. & I.S. [0..0]
    DP = [[0 if i == 0 else goal + 1 for _ in range(K)] for i in range(N + 1)]

    coins.sort() # sort coins if not already done

    def incr_ret(lst: list[int], idx: int):
        tmp = lst.copy()
        tmp[idx] += 1
        return tmp

    # DP[k] represents the optimal amount of change that sums up to k
    for k in range(1, N + 1):
        for i, c_i in enumerate(coins):
            if k - c_i >= 0:
                DP[k] = min(DP[k], incr_ret(DP[k - c_i], i), key=lambda lst: sum(lst))
            else:
                break

    return DP


if __name__ == "__main__":
    # S, cs = 5, [1, 3, 4]
    # S, cs = 62, [25, 21, 10, 5, 1]
    S, cs = 48, [30, 24, 12, 6, 3, 1]
    # A = coinChange_lecture(cs, S)
    A = coinChange_classic_dp_2(cs, S)
    print("")
    mprint(A, cs)
    print(get_sol(A, S+1, cs))

