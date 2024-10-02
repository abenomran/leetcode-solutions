# Easy
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevNums = {}
        for i, n in enumerate(nums):
            dif = target - n 
            if dif in prevNums:
                return [prevNums[dif], i]
            prevNums[n] = i
        