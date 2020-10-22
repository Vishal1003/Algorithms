"""
Approach 1: Binary search
- O(log m*n), O(1)
"""
class Solution:
    # approach - 1
    def searchMatrix1(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])

        # binary search
        left, right = 0, m * n - 1
        while left <= right:
            pivot_idx = (left + right) // 2
            pivot_element = matrix[pivot_idx // n][pivot_idx % n]
            if target == pivot_element:
                return True
            else:
                if target < pivot_element:
                    right = pivot_idx - 1
                else:
                    left = pivot_idx + 1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix: return False

        R, C = len(matrix), len(matrix[0])
        cr, cc = 0, C - 1
        while cr < R and cc >= 0:
            if matrix[cr][cc] == target:
                return True
            elif matrix[cr][cc] > target:
                cc -= 1
            elif matrix[cr][cc] < target:
                cr += 1
            