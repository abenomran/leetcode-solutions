# Medium
from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxA = 0

        while l < r:
            area = (r - l) * min(heights[r], heights[l])
            print (heights[r], heights[l])
            print(area)
            if area > maxA:
                maxA = area
            if heights[l] <= heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1

        return maxA 
