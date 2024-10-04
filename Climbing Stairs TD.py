# Easy
# TOP-DOWN IMPLEMENTATION

class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        return self.memo(n, cache)
        
    def memo(self, n, cache):
        if n <= 1:
            return 1
        if n in cache:
            return cache[n]

        cache[n] = self.memo(n - 1, cache) + self.memo(n - 2, cache)
        return cache[n]