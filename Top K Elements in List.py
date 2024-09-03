# Medium
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            counts[n] = 1 + counts.get(n, 0)

        for num, count in counts.items():
            freq[count].append(num)
        
        res = []
        for numList in freq[::-1]:
            for num in numList:
                res.append(num)
                if len(res) == k:
                    return res
