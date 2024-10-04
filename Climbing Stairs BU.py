# Easy
# BOTTOM-UP IMPLEMENTATION

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return n

        dpArray = [0, 1]
        for i in range(n):
            tmp = dpArray[1]
            dpArray[1] = dpArray[0] + dpArray[1]
            dpArray[0] = tmp

        return dpArray[1]
            
