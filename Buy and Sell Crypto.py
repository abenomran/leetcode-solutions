# Easy
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        res = 0
        for R in range(1, len(prices)):
            if prices[L] > prices[R]:
                L = R
                continue
            res = max(prices[R] - prices[L], res)

        return res