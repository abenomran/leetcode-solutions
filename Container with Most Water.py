# Medium
from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxArea = 0

        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            maxArea = max(maxArea, area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return maxArea