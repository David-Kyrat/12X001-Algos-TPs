from typing import List


class Solution:

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 2:
            return min(cost[0], cost[1])
        if len(cost) == 3:
            return min(cost[0] + min(cost[1], cost[2]), cost[1])

        def rec(step: int, crt_cost: int, costs: List[int]) -> int:
            if step <= 1:
                return crt_cost + costs[step]
            return min(
                rec(step - 1, crt_cost + costs[step - 1], costs),
                rec(step - 2, crt_cost + costs[step - 2], costs),
            )

        tmp = rec(len(cost), 0, cost)
        return tmp


if __name__ == "__main__":
    s = Solution()
    cost = []
    print(s.minCostClimbingStairs(cost))
