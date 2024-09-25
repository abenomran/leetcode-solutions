# Easy
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L, maxProfit = 0, 0

        for R in range(1, len(prices)):
            maxProfit = max(maxProfit, prices[R] - prices[L])
            if prices[L] > prices[R]:
                L = R

        return maxProfit