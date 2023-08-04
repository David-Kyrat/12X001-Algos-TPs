from typing import Tuple, List


class Solution:
    def to_dum_formatting(self, solutions: List[List[int]], n: int) -> List[List[str]]:
        res = []
        for sol in solutions:
            crt_res = [["." for _ in range(n)] for _ in range(n)]
            for i, xi in enumerate(sol):
                crt_res[i][xi] = "Q"
            for i in range(len(crt_res)):
                tmp = crt_res[i]
                crt_res[i] = "".join(tmp)
            res.append(crt_res)
        return res

    def solveNQueens(self, n: int) -> List[List[str]]:
        if n < 3: return [[]]
        out = []
        def is_same_diag(coord1: Tuple[int], coord2: Tuple[int]) -> bool:
            # c1 same diag c2 <==> (z:= c1-c2 => z_1 = z_2)
            z = (coord1[0] - coord2[0], coord1[1] - coord2[1])
            return z[0] == z[1]

        def is_same_anti_diag(coord1: Tuple[int], coord2: Tuple[int]) -> bool:
            # c1 same anti_diag c2 <==> (z:= c1-c2 => z_1 = -z_2)
            z = (coord1[0] - coord2[0], coord1[1] - coord2[1])
            return z[0] == -z[1]

        # position at x[i] indicate column of the queen on the i-th row
        # indicates available columns-indices at step k given moves at steps 0..k-1
        def T(x: List[int], k, N):
            base = set(range(N))
            # remove those that would induce colum collision
            for i in range(k): base.discard(x[i])  # if not present do nothing
            return base

        def B(x: List[int], k: int, N: int):
            tocheck = x[k]
            coord_1 = k, tocheck
            for i in range(k):
                crt = x[i]
                # coord_1, coord_2 = (k, tocheck), (i, crt)
                coord_2 = i, crt
                if is_same_diag(coord_1, coord_2) or is_same_anti_diag(coord_1, coord_2):
                    return False
            return True

        def P(x: List[int], k, N):
            if x[0] is None: return False
            # At each step check for diag collision between x[i] and each other x[i-j] for all j < i
            # print("in P:", x, f"k={k}")
            queen = 0
            for i, xi in enumerate(x):
                if i > k: break  # iterate through x[0] -> x[k] (included)
                if xi is None: return False
                if not B(x, i, N): return False
                queen += 1
            return queen >= N # return if enough queen were in x

        def bt_rec(x: List[List[int]], k: int, N: int):
            nonlocal out
            if k >= N: return
            for col in T(x, k, N):
                x[k] = col
                if B(x, k, N):
                    if P(x, k, N): out.append(x[: k + 1].copy())
                    bt_rec(x, k + 1, N)

        bt_rec([None]*n, 0, n)
        return self.to_dum_formatting(out, n)


if __name__ == "__main__":
    s = Solution()
    N = 4
    sols = s.solveNQueens(N)
    print("N =", N)
    for sol in sols:
        print("\nsolution:\n")
        print("----")
        for s in sol:
            print(s)
        print("----")
