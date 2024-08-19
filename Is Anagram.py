# Easy

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        charStack = {}
        charStack2 = {}
        for c in s:
            charStack[c] = 1 + charStack.get(c, 0)
        for c in t:
            charStack2[c] = 1 + charStack2.get(c, 0)

        return charStack == charStack2
        