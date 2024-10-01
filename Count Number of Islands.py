# Medium
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        

        ROWS, COLS = len(grid), len(grid[0])
        numIslands = 0
        visit = set()

        def dfs(r, c):
            if (
                r not in range(ROWS) or
                c not in range(COLS) or
                grid[r][c] == "0" or
                (r, c) in visit):
                return
            
            visit.add((r, c))
            neighbors = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in neighbors:
                dfs(r + dr, c + dc)


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visit:
                    numIslands += 1
                    dfs(r, c)
                    
        return numIslands