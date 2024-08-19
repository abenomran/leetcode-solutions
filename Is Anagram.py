# Easy

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sStack = {}
        tStack = {}
        for c in s:
            sStack[c] = 1 + sStack.get(c, 0)
        for c in t:
            tStack[c] = 1 + tStack.get(c, 0)

        return sStack == tStack
        