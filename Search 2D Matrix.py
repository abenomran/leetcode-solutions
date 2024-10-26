# Medium
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1

        while l <= r:
            m = l + ((r - l) // 2)
            
            if matrix[m][0] > target:
                r = m - 1
            elif matrix[m][-1] < target:
                l = m + 1
            else:
                break

        l, r = 0, len(matrix[m]) - 1
        while l <= r:
            m_in = l + ((r - l) // 2)
            
            if matrix[m][m_in] > target:
                r = m_in - 1
            elif matrix[m][m_in] < target:
                l = m_in + 1
            else:
                return True

        return False