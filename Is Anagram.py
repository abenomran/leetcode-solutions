# Easy

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sHash, tHash = {}, {}
        for c in s:
            sHash[c] = 1 + sHash.get(c, 0)
        for c in t:
            tHash[c] = 1 + tHash.get(c, 0)

        return sHash == tHash