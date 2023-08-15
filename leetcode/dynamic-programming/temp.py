from typing import List
from dp_coins import mprint # type: ignore
from dp_coin_test import get_sol # type: ignore

class Solution:

    def coinChange(self, coins: List[int], goal: int) -> int:
        if not coins or 1 not in coins:
            return -1  # type: ignore
        if goal == 0:
            return 0

        def is_coin_i(x: int) -> int:
            """Check if there is an `i` coin in coins
            returns its index. If there isn't return -1"""
            for i, c_i in enumerate(coins):
                if c_i == x:
                    return i
            return None  # type: ignore

        K, N = len(coins), goal
        DP = [[0 for _ in range(K)] for _ in range(N + 1)]  # 0 unused

        def incr_ret(lst: list[int], idx: int):
            tmp = lst.copy()
            tmp[idx] += 1
            return tmp

        def combine(lst1: list[int], lst2: list[int]):
            return [x1 + x2 for x1, x2 in zip(lst1, lst2)]

        DP[1][is_coin_i(1)] += 1  # coins[-1] has to be -1 or problem cant be solved for all `goal`
        # DP[k] represents the optimal amount of change that sums up to k
        for k in range(2, N + 1):
            DP[k] = min(
                (incr_ret(DP[k - c_i], i) for i, c_i in enumerate(coins) if k - c_i >= 0),
                key=lambda lst: sum(lst),
            )
            print(f"DP[{k}] = {DP[k]}")

        # return sum(DP[-1])
        return DP # type: ignore


if __name__ == "__main__":
    # S, cs = 5, [4, 3, 1]
    # S, cs = 48, [30, 24, 12, 6, 3, 1]
    S, cs = 62, [25, 21, 10, 5, 1]
    s = Solution()
    A = s.coinChange(cs, S)
    print("")
    mprint(A, cs)
    print(get_sol(A, S, cs))
