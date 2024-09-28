# Medium

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        cHash = {}
        maxC = 0

        for R in range(len(s)):
            cHash[s[R]] = 1 + cHash.get(s[R], 0)
            maxC = max(maxC, cHash[s[R]])
            
            if (R - L + 1) - maxC > k:
                cHash[s[L]] -= 1
                L += 1

        return (R - L + 1)
                