# Medium
from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + ((r-l) // 2)
            if nums[m] < nums[r]:
                r = m
                continue
            elif nums[m] > nums[r]:
                l = m + 1
                continue
            if nums[m] >= nums[l] and nums[m] <= nums[r]:
                return nums[m]
            