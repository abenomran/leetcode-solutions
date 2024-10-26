# Medium
from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            letters = [0] * 26
            for c in s:
                letters[ord(c.lower()) - ord('a')] += 1
            
            anagrams[tuple(letters)].append(s)

        return anagrams.values()