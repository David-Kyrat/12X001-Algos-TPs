import timeit


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        S_i = set(range(len(nums)))
        pairs: dict[int, set[int]] = dict()
        for i in S_i:
            pairs[nums[i]] = set()

        def T(x, k, N):
            used = [] if x[0] is None else pairs[nums[x[0]]]
            out = S_i.difference(set(x[:k]).union(used))
            if x[0] is not None and x[k] is not None:
                pairs[nums[x[0]]].add(nums[x[k]])
            return out

        def sumk(x, k):
            summ, i = 0, 0
            for xi in x:
                summ += nums[xi]
                i += 1
                if i > k: return summ
            return 0

        def B(x, k, N):
            summ = sumk(x, k)
            return summ <= target if target >= 0 else summ >= target

        def P(x, k, N):
            if k != 1: return False
            summ = sumk(x, k)
            return summ == target
        out = None

        def rBT(x: list[int], k: int, N: int) -> list[int] | None:
            nonlocal out
            for y in T(x, k, N):
                # print(y)
                x[k] = y
                if B(x, k, N) and nums[x[k]] not in pairs[nums[x[0]]]:
                    # print("")
                    if P(x, k, N):
                        out = x[: k + 1]
                        return out
                    if k < N - 1:
                        rBT(x, k + 1, N)
                if out:
                    return out

        N = len(nums)
        return rBT([None] * N, 0, N)


if __name__ == "__main__":
    in2, t2 = [1,1,1,1,1,3, 2, 4], 7
    in3, t3 = [-1, -2, -3, -4, -5], -8
    in4, t4 = [1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1, 7, 1, 1, 1, 1, 1], 11
    s = Solution()
    res = s.twoSum(in2, t2)
    print("---")
    print(res)

    SETUP_CODE = "from __main__ import Solution;s = Solution()"

    def time(test_code, repeat):
        runtime = (
            timeit.timeit(setup=SETUP_CODE, stmt=test_code, number=repeat) / repeat
        )

        print("time: {} s,\t\t {}".format(runtime, test_code))

    TEST_CODE1 = "res=s.twoSum([-1, -2, -3, -4, -5], -8); assert(res==[2, 4])"
    TEST_CODE2 = "res=s.twoSum([1,1,1,1,1,3,2,4], 6); assert(res==[5, 6])"
    TEST_CODE3 = "res=s.twoSum([1,1,1,1,1,4,1,1,1,1,1,7,1,1,1,1,1], 11); assert(res==11)"
    TEST_CODES = [TEST_CODE1, TEST_CODE2, TEST_CODE3]

    repeat = 100
    """ for tc in TEST_CODES:
        time(tc, repeat) """
    # times = timeit.timeit(setup=SETUP_CODE, stmt=TEST_CODE1, number=repeat) / repeat
    # times = timeit.timeit(setup=SETUP_CODE, stmt=TEST_CODE2, number=repeat) / repeat
    # times = timeit.timeit(setup=SETUP_CODE, stmt=TEST_CODE3, number=repeat) / repeat
    # printing minimum exec. time
    # print("Binary search time: {}".format(times))
