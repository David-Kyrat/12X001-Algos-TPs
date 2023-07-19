import timeit
from typing import List


# Divide and conquer approach
class Solution:
    # return index of wanted or -1 if not found
    def bin_search(self, lst: List[int], wanted: int) -> int:
        def sg(lst, idx):
            return None if idx >= len(lst) else lst[idx]
        def bs_rec(p: int, q: int):
            if q - p > 0:
                middle = (q + p) // 2
                crt = lst[middle][1]
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
        numss = sorted([(idx, x) for idx, x in enumerate(nums)], key=lambda x: x[1])
        pairs = set()
        # iterate on each element i and binary search on target - nums[i]
        for idx, xi in numss:
            to_search = target - xi
            crt_pair = (xi, to_search)
            print(crt_pair, idx)
            if crt_pair not in pairs: found_idx = self.bin_search(numss, to_search)
            if found_idx is not None and numss[found_idx][0] != idx:
                return [idx, numss[found_idx][0]]
            else:
                pairs.add(crt_pair)
                pairs.add((to_search, xi))
        return [None, None]


if __name__ == "__main__":
    in1, t1 = [3, 2, 4], 6
    in2, t2 = [1, 1, 1, 1, 1, 3, 2, 4], 6
    in3, t3 = [-1, -2, -3, -4, -5], -8
    in4, t4 = [1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1, 7, 1, 1, 1, 1, 1], 11
    in5, t5 = [3, 2, 3], 6
    s = Solution()
    res = s.twoSum(in4, t4)
    print("---")
    print(res)

    """ SETUP_CODE = "from __main__ import Solution;s = Solution()"

    def time(test_code, repeat):
        runtime = (
            timeit.timeit(setup=SETUP_CODE, stmt=test_code, number=repeat) / repeat
        )
        print("time: {} s,\t\t {}".format(runtime, test_code))

    TEST_CODE1 = "res=s.twoSum([-1, -2, -3, -4, -5], -8)"
    TEST_CODE2 = "res=s.twoSum([1,1,1,1,1,3,2,4], 6)"
    TEST_CODE3 = "res=s.twoSum([1,1,1,1,1,4,1,1,1,1,1,7,1,1,1,1,1], 11)"
    TEST_CODES = [TEST_CODE1, TEST_CODE2, TEST_CODE3]

    repeat = 100_000
    for tc in TEST_CODES:
        time(tc, repeat) """
