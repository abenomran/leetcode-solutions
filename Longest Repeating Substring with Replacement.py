# Medium

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        maxF = 0
        L = 0

        for R in range(len(s)):
            counts[s[R]] = 1 + counts.get(s[R], 0)
            maxF = max(maxF, counts[s[R]])

            if (R - L + 1) - maxF > k:
                counts[s[L]] -= 1
                L += 1

            
        return (R - L + 1)
                