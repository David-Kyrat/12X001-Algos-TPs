from typing import Tuple, List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = "%s" % self.val
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = "%s" % self.val
            u = len(s)
            first_line = (x + 1) * " " + (n - x - 1) * "_" + s
            second_line = x * " " + "/" + (n - x - 1 + u) * " "
            shifted_lines = [line + u * " " for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = "%s" % self.val
            u = len(s)
            first_line = s + x * "_" + (n - x) * " "
            second_line = (u + x) * " " + "\\" + (n - x - 1) * " "
            shifted_lines = [u * " " + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = "%s" % self.val
        u = len(s)
        first_line = (x + 1) * " " + (n - x - 1) * "_" + s + y * "_" + (m - y) * " "
        second_line = (x * " " + "/" + (n - x - 1 + u + y) * " " + "\\" + (m - y - 1) * " ")
        if p < q: left += [n * " "] * (q - p)
        elif q < p: right += [m * " "] * (p - q)
        lines = [first_line, second_line] + [a + u * " " + b for a, b in zip(left, right, strict=False)]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


class Solution:
    def _max(self, nums: List[int]) -> Tuple[int]:
        crt_idx, crt = 0, nums[0]
        for i, x in enumerate(nums):
            if x > crt:
                crt_idx, crt = i, x
        return crt_idx, crt

    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def rec(acc: List[int]):
            if acc is None or len(acc) == 0:
                return None
            idx_max, vmax = self._max(acc)
            return TreeNode(vmax, rec(acc[:idx_max]), rec(acc[idx_max + 1 :]))
        return rec(nums)

    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        if not root or val > root.val: return TreeNode(val, root, None)
        root.right = self.insertIntoMaxTree(root.right, val)
        return root

    def BFS(self, root: TreeNode):
        def neighbours(node: TreeNode):
            out = []
            if node.left is not None: out.append(node.left)
            if node.right is not None: out.append(node.right)
            return out

        print(root.val)
        next_list: List[TreeNode] = [neighbours(root)]
        while next_list != []:
            next = next_list.pop()
            line = ""
            for node in next:
                # print(node.val)
                line += f"{node.val} "
                next_list.append(neighbours(node))
            print(line)


def test_specific():
    nums = [1, 7, 6, 5]
    s = Solution()
    res = s.constructMaximumBinaryTree(nums)
    # s.BFS(res)
    res.display() 
    res2 = s.insertIntoMaxTree(res, 4)
    res2.display()

if __name__ == "__main__":
    test_specific()
