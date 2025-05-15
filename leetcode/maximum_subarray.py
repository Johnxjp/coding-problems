from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest_sum = nums[0]
        running_sum = nums[0]
        for i in nums[1:]:
            if running_sum <= 0:
                running_sum = i
            else:
                running_sum += i

            if running_sum > largest_sum:
                largest_sum = running_sum

        return largest_sum
