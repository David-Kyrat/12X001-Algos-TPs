from prettytable import PrettyTable


def mprint(matrix: list[list], cns: str | list[int] = ""):
    p = PrettyTable()
    for i, row in enumerate(matrix):
        p.add_row([f"{i + 1}:", *(row or [""] * len(cns))])
    print("_________________")
    print("    ", cns)
    print(p.get_string(header=False, border=False))
    print("-----------------")


# WARN: methodology to Find DP rec relation from
# BT impl then caching BT impl


# BUG: HAS EXPONENTIAL RUNTIME


def coins2_BT_version(S: int, coins: list[int]):
    """S: goal,  cs: set of coins, BT version => cached later"""
    if S == 0 or not cs:
        return [[]]

    def incr_ret(lst, idx):
        lst[idx] += 1
        return lst

    def solve_rec(N: int, used: list[int]) -> list[int]:
        nonlocal coins
        # print("\n", f"N = {N},  used: {used}")
        if N <= 0:
            return used
        # sol for N-c_1 + for (N-c_1)-c_1, for (N-c_1)-c_2 ...
        return min(
            (solve_rec(N - c_i, incr_ret(used.copy(), i)) for i, c_i in enumerate(coins) if N - c_i >= 0),
            key=lambda lst: sum(lst),
        )

    return solve_rec(S, [0] * len(coins))


# BUG: DOESNT WORK


def coins2_BT_version_2(S: int, coins: list[int]) -> list[list[int]]:
    """S: goal,  cs: set of coins, BT version => cached later"""
    if S == 0 or not cs:
        return [[]]
    cache: list[list[int]] = [[] for _ in range(S)]

    def incr_ret(lst, idx):
        lst[idx] += 1
        return lst

    """ def solve_rec(N: int, used: list[int]) -> list[int]:
        # and is_sol(N, cache[N - 1], coins):  # N-1, bcs goal is in [1, N]
        # print("\n", f"N = {N},  used: {used}")
        # sol for N-c_1 + for (N-c_1)-c_1, for (N-c_1)-c_2 ...
        nonlocal coins
        if N <= 0:
            return used
        return min2(
            [
                solve_rec(N - c_i, incr_ret(used.copy(), i)) if not cache[N - c_i - 1] else cache[N - c_i - 1]
                for i, c_i in enumerate(coins)
                if (N - c_i >= 0)
            ],
            key=lambda lst: sum(lst),
        )  # type: ignore

    K = len(coins)
    for i in range(1, S + 1):
        print(i)
        cache[i - 1] = solve_rec(i, [0] * K)  # restart whole expo loop
        # each iteration but, value filled from before are skipped
    mprint(cache, coins)
    return cache """
    return cache


# BUG: DOESNT WORK


def coins2_BT_version_cache(S: int, coins: list[int]):
    # sourcery skip: comprehension-to-generator
    """ "S: goal,  cs: set of coins, BT version => cached later"""
    if S == 0 or not cs:
        return [[]]
    cache: list[list[int]] = [[] for _ in range(S)]

    def incr_ret(lst, idx):
        lst[idx] += 1  # ; print(lst)
        # if sum(cache[val]) <= sum(lst): cache[val] = lst
        return lst

    def set_cache(idx: int, value: list[int], cache: list[list[int]]) -> list[int]:
        """set `cache[idx]` to `value` and return `value`"""
        cache[idx] = value
        return value

    def is_sol(goal: int, used: list[int], coins: list[int]):
        return sum(c_i * amnt_i for c_i, amnt_i in zip(coins, used)) == goal

    def solve_rec(N: int, used: list[int]) -> list[int]:
        nonlocal coins
        if N <= 0:
            return used

        print("\n", f"N = {N},  used: {used}")
        if cache[N - 1] and is_sol(N, cache[N - 1], coins):  # N-1, bcs goal is in [1, N]
            return cache[N - 1]  # if cache[N] sums up to N => return dont recompute

        # sol for N-c_1 + for (N-c_1)-c_1, for (N-c_1)-c_2 ...
        """ out1 = []
        for i, c_i in enumerate(coins):
            print("\n", f"c_{i} = {c_i},  N = {N},  N-c_{i} = {N-c_i}")
            if N-c_i < 0: break # sorted increasing
            tmp2 = solve_rec(N - c_i, incr_ret(used.copy(), i))
            out1.append(tmp2)
        return min(out1) """
        tmp2 = [solve_rec(N - c_i, incr_ret(used.copy(), i)) for i, c_i in enumerate(coins) if N - c_i >= 0]
        tmp = min(tmp2, key=lambda lst: sum(lst))
        cache[N - 1] = tmp
        mprint(cache, coins)
        return cache[N - 1]

    # set_cache(N, min_N, cache)
    # a = solve_rec(S, [0] * len(coins))
    # print(f"called {cnt} times")
    mprint(cache, coins)
    return solve_rec(S, [0] * len(coins))


if __name__ == "__main__":
    S, cs = 5, [1, 3, 4]
    K, N = len(cs), 40
    # S, cs = 62, [25, 21, 10, 5, 1]
    # S, cs = 48,[30, 24, 12, 6, 3, 1]

    res = coins2_BT_version_2(S, cs)
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
