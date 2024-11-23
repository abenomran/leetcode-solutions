# Medium
from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visit = set()
        neighbors = [[0,1],[0,-1],[1,0],[-1,0]]
        i = 0

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (
                min(r, c) < 0 or
                r >= ROWS or c >= COLS or
                (r, c) in visit or
                board[r][c] != word[i]
            ):
                return

            visit.add((r,c))        

            res = (
                dfs(r + 1, c, i + 1) or
                dfs(r - 1, c, i + 1) or
                dfs(r, c + 1, i + 1) or
                dfs(r, c - 1, i + 1)
            )

            visit.remove((r,c))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0): return True

        return False
            