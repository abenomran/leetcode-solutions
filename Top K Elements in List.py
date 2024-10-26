# Medium
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for n in nums:
            counts[n] = 1 + counts.get(n, 0)

        freq = [[] for i in range(len(nums) + 1)]
        for n, count in counts.items():
            freq[count].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
