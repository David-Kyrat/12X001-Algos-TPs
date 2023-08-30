# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


class Solution:
    def partition(self, p: int, q: int) -> int:
        return (q + p) // 2

    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        if not nums or len(nums) == 0: return None
        N = len(nums)
        if N == 1: return TreeNode(nums[0])
        if N == 2: return TreeNode(nums[1], TreeNode(nums[0]))
        if N == 3: return TreeNode(nums[1], TreeNode(nums[0]), TreeNode(nums[2]))

        def sabst_rec(p: int, q: int) -> TreeNode | None:
            if q - p >= 1:
                middle = self.partition(p, q)
                return TreeNode(nums[middle], sabst_rec(p, middle), sabst_rec(middle + 1, q))
            else:
                return None

        return sabst_rec(0, N)


if __name__ == "__main__":
    in1 = [-10, -3, 0, 5, 9]
    s = Solution()
    out1 = s.sortedArrayToBST(in1)
    print("[", out1, out1.left, out1.right, out1.left.left, out1.left.right, out1.right.left, out1.right.right, "]")
