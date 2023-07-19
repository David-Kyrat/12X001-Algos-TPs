from typing import List

class Solution:
    def bin_search(self, lst: List[int], wanted: int) -> int:
        def sg(lst, idx):
            return None if idx >= len(lst) else lst[idx]
        def bs_rec(p: int, q: int):
            if q - p > 0:
                middle = (q + p) // 2
                crt = lst[middle]
                if crt > wanted: return bs_rec(p, middle)
                if crt < wanted: return bs_rec(middle + 1, q)
                return middle
            else: # noqa: RET505
                if sg(lst, p) == wanted: return p
                if sg(lst, q) == wanted: return q
                return None

        return bs_rec(0, len(lst))

    # find indices i,j such that nums[i] + nums[j] = target
    def twoSum(self, nums: List[int], target: int) -> List[int]:  # noqa: E999
        pairs = set()
        # iterate on each element i and binary search on target - nums[i]
        for idx, xi in enumerate(nums):
            to_search = target - xi
            crt_pair = (xi, to_search)
            print(crt_pair, idx)
            if crt_pair not in pairs: found_idx = self.bin_search(nums, to_search)
            if found_idx is not None and found_idx != idx:
                return [idx, found_idx]
            else:
                pairs.add(crt_pair)
                pairs.add((to_search, xi))
        return [None, None]


if __name__ == "__main__":
    in1, t1 = sorted([3, 2, 4]), 6
    in2, t2 = sorted([1, 1, 1, 1, 1, 3, 2, 4]), 6
    in3, t3 = sorted([-1, -2, -3, -4, -5]), -8
    in4, t4 = sorted([1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1, 7, 1, 1, 1, 1, 1]), 11
    in5, t5 = sorted([3, 2, 3]), 6
    in6, t6 = [2, 7, 11, 15], 9

    s = Solution()
    res = s.twoSum(in4, t4)
    print("---")
    print(res)
