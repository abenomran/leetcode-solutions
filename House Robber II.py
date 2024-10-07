# Medium
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for n in nums[:-1]:
            tmp = max(rob2, rob1 + n)
            rob1 = rob2
            rob2 = tmp

        rob3, rob4 = 0, 0
        for n in nums[:0:-1]:
            tmp = max(rob4, rob3 + n)
            rob3 = rob4
            rob4 = tmp

        return max(rob4, rob2, nums[0])
