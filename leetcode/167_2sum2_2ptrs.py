from typing import List


class Solution:
    @staticmethod
    def two_sum(nums: list[int], target: int) -> list[int]:
        """
        :rtype: list[int]
        :param nums: input list
        :param target:  goal to reach
        :return: stuff
        """
        left, right = 0, len(nums) - 1
        while nums[left] + nums[right] != target:
            if nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1
        return [left + 1, right + 1]
