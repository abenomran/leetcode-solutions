# Easy
from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nHash = set()
        for n in nums:
            if n in nHash:
                return True
            nHash.add(n)

        return False