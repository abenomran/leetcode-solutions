# Medium
from typing import List
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)
        for course, prereq in prerequisites:
            preMap[course].append(prereq)

        visit = set()

        def dfs(course):
            if course in visit:
                return False
            if not preMap[course]:
                return True

            visit.add(course)

            for pre in preMap[course]:
                if not dfs(pre): return False

            visit.remove(course)
            preMap[course] = [] # WE KNOW THIS COURSE WORKS -> optimization
            return True

        for course in range(numCourses):
            if not dfs(course): return False

        return True