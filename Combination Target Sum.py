# Medium
from typing import List

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, options, total):
            if total == target:
                res.append(options.copy())
                return
            if i >= len(nums) or total > target:
                return

            options.append(nums[i])
            dfs(i, options, total + nums[i])
            options.pop()
            dfs(i + 1, options, total)

        dfs(0, [], 0)
        return res
            