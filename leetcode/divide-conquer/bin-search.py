from typing import List, Optional
import numpy as np

class Solution:
    def binary_search(self, nums: List[int], goal: int) -> Optional[int]:
        if not nums: return None

        def bs_rec(p: int, q: int):
            if p >= q: return p if nums[p] == goal else None
            m = (p + q) // 2
            val = nums[m]
            if val < goal: return bs_rec(m + 1, q)
            elif val > goal: return bs_rec(p, m)
            else: return m
        return bs_rec(0, len(nums) - 1)

if __name__ == "__main__":
   inp = list(np.random.randint(0, 200, size=1))
   inp.sort()
   goal = inp[-1]
   print(inp)
   print("goal =", goal)
   print(" ")
   s = Solution()
   res = s.binary_search(inp, goal)
   print(f"inp[{res}] = {goal} ?  {inp[res]}")

