from typing import List

class Solution:

    # HINT: Brute Force
    def mCCS_bf(self, cost: List[int]) -> int:
        N, j_m = len(cost), 2  # max stair index, max jump
        cost.append(0)
        calls: dict[int, int] = {}

        def F(k: int) -> int:
            if k <= 0: return cost[k]  # B. S.
            if k in calls: calls[k] += 1
            else: calls[k] = 1
            return cost[k] + min((F(k - j) for j in range(1, j_m + 1)))  # I. H.

        out = min(F(N - 1), F(N - 2))  # we can start at 0 or 1
        # expo. growth rate of calls (fibonacci to be precise, i.e.e 7:3, 6: 5, 4: 13...)
        for i in sorted(calls.keys()): print(f"{i}: Called {calls[i]} times")
        return out
        # return min(F(N - 1), F(N - 2))  # we can start at 0 or 1

    # HINT: Memoization (cache for recursive calls, Top-Down)
    def mCCS_memo(self, cost: List[int]) -> int:
        N, j_m = len(cost), 2  # max stair index, max jump
        cache = [-1] * N
        cost.append(0)

        def F(k: int) -> int:
            if k <= 0: return cost[k]  # B. S.
            if cache[k] != -1: return cache[k] # memoization

            min_cost: int = cost[k] + min((F(k - j) for j in range(1, j_m + 1)))  # I. H.
            cache[k] = min_cost
            return min_cost
        
        return min(F(N - 1), F(N - 2))  # we can start at 0 or 1
    
    # HINT: Dynamic Programming (Bottom-Up)

    def minCostClimbingStairs(self, cost: List[int]): # type: ignore
        cost.append(0)
        N = len(cost)
        j_m, dp = 2, [float('inf')] * N
        dp[0], dp[1] = cost[0], cost[1]
        for k in range(2, N):
            # choose the min cost from 0 to stair k
            # knowing the optimal costs from 0 to stairs 1 to k-1
            for j in range(1, j_m + 1):
                dp[k] = min(dp[k], cost[k] + dp[k - j])
 
            # NB. for loop is *absolutely* necessary:
            # dp[k] = cost[k] + min([dp[k - j] for j in range(1, j_m + 1)])

        return dp[-1]

    def minCostClimbingStairs(self, cost: List[int]) -> int: # noqa: F811
        # sourcery skip: comprehension-to-generator
        N, j_max = len(cost), 2
        # Initialize a DP array to store the minimum cost to reach each step.
        dp = [0] * N
        # Base cases: Cost to reach the first and second steps.
        dp[0], dp[1] = cost[0], cost[1]

        # Iterate through the rest of the steps and calculate the minimum cost.
        for i in range(2, N):
            # Minimum cost to reach the current step is the cost of the current step
            # plus the minimum of the cost to reach the previous step or the step before it.
            dp[i] = cost[i] + min([dp[i - j] for j in range(1, j_max + 1)])
            #dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])

        # The minimum cost to reach the top floor can be either from the last step or
        # the second to last step (since you can start from either step 0 or step 1).
        return min(dp[N - 1], dp[N - 2])


if __name__ == "__main__":
    s = Solution()
    # cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    cost = [10, 15, 20]
    print(s.minCostClimbingStairs(cost))
    # print(s.mCCS_bf(cost))
    # print(s.mCCS_memo(cost))
