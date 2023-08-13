# from dynp_coins_test import mprint


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3: return n
        S = [0] * (n + 1)  # row 0 unused
        S[1], S[2] = 1, 2  # Basis Step

        def IH(k: int) -> int:
            """Induction Hypothesis (rec. relation)"""
            return S[k - 1] + S[k - 2]

        for i in range(3, n + 1):
            # don't recompute overlapping subproblems
            if S[i] == 0: S[i] = IH(i)
        return S[n]


if __name__ == "__main__":
    s = Solution()
    print(s.climbStairs(5))
