# Easy
# BOTTOM-UP IMPLEMENTATION

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return n
        
        steps = [1, 2]
        for i in range(2, n):
            tmp = steps[1]
            steps[1] = steps[0] + steps[1]
            steps[0] = tmp

        return steps[1]
            
