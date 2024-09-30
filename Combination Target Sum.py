# Medium
from typing import List

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        if not nums:
            return res

        def dfs(options, currAdditions, currSum, n, target):
            if (currSum + n > target):
                return

            if (currSum + n == target):
                res.append(currAdditions + [n])
                return
            
            for i, option in enumerate(options):
                dfs(options[i:], currAdditions + [n], currSum + n, option, target)

        for i, n in enumerate(nums):
            dfs(nums[i:], [], 0, n, target)
            print(res)
        return res