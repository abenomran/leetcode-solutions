# Easy
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opDict = {"]":"[", "}":"{", ")":"("}

        for c in s:
            if c in opDict:
                if not stack or stack[-1] != opDict[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)

        return not stack