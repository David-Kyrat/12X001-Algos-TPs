from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        def G(nums): return nums[0]
        if len(nums) == 1: return G(nums)
        N = len(nums)
        def is_majority(m):
            nonlocal N
            count = 0
            for k in nums:
                if  k == m:
                    count += 1
                    if count > N / 2: return True
            return False
        
        def REDUCE(crt_list: List[int]):
            out = []
            for i in range(0, len(crt_list) - 1, 2):
                crt = crt_list[i]
                if crt == crt_list[i+1]: out.append(crt)
            return out


        def me_rec(crt: List[int]):
            n = len(crt)
            if n == 1: return G(nums)
            # if length of crt is odd => check if crt[-1] is majority element
            # if its not => rec call for reduce(crt)
            if n % 2 == 1:
                last = crt[-1]
                if is_majority(last): return last
                else: crt.pop()
            return me_rec(REDUCE(crt))
        # REDUCE can create a majority element but can never remove one.
        # hence => check if one returned by me_rec was created or is genuine
        candidate = me_rec(nums)
        return candidate if is_majority(candidate) else None


def test():
    inp1, e1 = [3,2,3], 3
    inp2, e2 = [2,2,1,1,1,2,2], 2
    s = Solution()
    assert s.majorityElement(inp1) == e1
    assert s.majorityElement(inp2) == e2


if __name__ == "__main__":
    inp1, e1 = [3,2,3], 3
    inp2, e2 = [2,2,1,1,1,2,2], 2
    s = Solution()
    assert s.majorityElement(inp1) == e1
    assert s.majorityElement(inp2) == e2

