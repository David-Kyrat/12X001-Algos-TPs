from typing import List, Optional, Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _max(self, nums: List[int]) -> Tuple[int, int]:
        crt_idx, crt = 0, nums[0]
        for i, x in enumerate(nums):
            if x > crt: crt_idx, crt = i, x
        return crt_idx, crt

    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def rec(acc: List[int]):
            if acc is None or len(acc) == 0: return None
            idx_max, vmax = self._max(acc)
            return TreeNode(vmax, rec(acc[:idx_max]), rec(acc[idx_max + 1 :]))
        return rec(nums)

    # IN PLACE:
    def constructMaximumBinaryTree2(self, nums: List[int]) -> Optional[TreeNode]:
        def _max(p: int, q: int):
            crt_idx, crt = p, nums[p]
            for i in range(p + 1, q + 1):
                x = nums[i]
                if x > crt: crt_idx, crt = i, x
            return crt_idx, crt

        def rec(p: int, q: int):
            if p >= q:
                if p == q: return TreeNode(nums[p])
                return None
            idx_max, vmax = _max(p, q)
            return TreeNode(vmax, rec(p, idx_max - 1), rec(idx_max + 1, q))

        return rec(0, len(nums) - 1)
