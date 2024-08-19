# Easy
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nHash = {}
        for i, n in enumerate(nums):
            dif = target - n
            if dif in nHash:
                return [nHash[dif], i]
            nHash[n] = i
        