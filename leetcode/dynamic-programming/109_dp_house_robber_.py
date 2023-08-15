class Solution:
    def rob(self, nums: list[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        N, dp = len(nums), [0]*len(nums)
        dp[0], dp[1] = nums[0], nums[1]
        
        for k in range(2, N):
            dp[k] = nums[k] + max((dp[k - j] for j in range(2, k + 1)))
        return max(dp[-1], dp[-2])

if __name__ == "__main__":
    s = Solution()
    in1, in2, in3 = [1,2,3,1], [2,7,9,3,1], [2, 1, 1, 2]
    res1, res2, res3 = s.rob(in1), s.rob(in2), s.rob(in3)
    print(f"in1 = {in1}\n res1 = {res1}\n")
    print(f"in2 = {in2}\n res2 = {res2}\n")
    print(f"in3 = {in3}\n res3 = {res3}\n")

    assert res1 == 4
    assert res2 == 12
    assert res3 == 4
