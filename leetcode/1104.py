from typing import List, Optional
from math import log2, ceil, floor


class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        tot_len: int = floor(log2(label)) + 1  # length of returned array
        out = [None]*tot_len
        out[-1] = 1

        def get_val(row: int, col: int):
            return 2**row + col if row % 2 == 0 else 2 ** (row + 1) - 1 - col

        def get_coord(val: int):
            row = floor(log2(val))
            pow = 2**row
            col = val - pow if row % 2 == 0 else 2 ** (row + 1) - 1 - val
            return row, col

        def get_parent(row, col): return (row - 1), col // 2

        def get_parent_v(val: int): return get_parent(*get_coord(val))

        def rec(val: int, idx: int):
            if idx >= tot_len - 1: return out
            out[idx] = val
            return rec(get_val(*get_parent_v(val)), idx + 1)
        return rec(label, 0)[::-1]

def test_1():
    _s = Solution()


if __name__ == "__main__":
    s = Solution()
    res = s.pathInZigZagTree(16)
    print(res)
