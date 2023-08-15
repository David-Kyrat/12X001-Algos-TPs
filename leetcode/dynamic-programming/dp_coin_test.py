from dp_coins import mprint #type: ignore

def get_sol(filled_mat, goal: int, coin_set: list[int]) -> list[int]:
    amounts = filled_mat[goal]
    out = []
    for idx, amount in enumerate(amounts):
        # appends `amount` times `coin_set[idx]` to `out`
        out.extend(coin_set[idx] for _ in range(amount))
    return out


def coin_change(goal: int, coins: list[int]) -> list[list[int]]:
    if not coins: return [[]] # type: ignore
    #if goal == 0: return [[0]*len(coins)]


    K, N = len(coins), goal
    DP = [[0 for _ in range(K)] for _ in range(N + 1)]  # 0 unused

    def incr_ret(lst: list[int], idx: int):
        tmp = lst.copy()
        tmp[idx] += 1
        return tmp

    # DP[k] represents the optimal amount of change that sums up to k
    for k in range(1, N + 1):
        DP[k] = min((
            incr_ret(DP[k - c_i], i)
            for i, c_i in enumerate(coins)
            if k - c_i >= 0

        ), key=lambda lst: sum(lst))

    return DP


if __name__ == "__main__":
    # S, cs = 5, [4, 3, 1]
    S, cs = 48, [30, 24, 12, 6, 3, 1]
    # S, cs = 62, [25, 21, 10, 5, 1]
    A = coin_change(S, cs)
    print("")
    mprint(A, cs)
    print(get_sol(A, S, cs))
