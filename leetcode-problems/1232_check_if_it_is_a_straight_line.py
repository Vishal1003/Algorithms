class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        """
        Brute Force Solution
        1. find slope between each (xi, yi) and (x_i+1, y_i+1), i from [0, n-2]
        2. if slopes is different than previously stored slope then return False.
        """
        idx = 0
        while idx <= len(coordinates) - 2:
            x_i, y_i = coordinates[idx]
            x_i_next, y_i_next = coordinates[idx + 1]
            if x_i_next == x_i:
                slope = float('inf')
            else:
                slope = (y_i_next - y_i) / (x_i_next - x_i)

            if idx > 0 and slope != prev_slope:
                return False
            prev_slope = slope
            idx += 1
        return True
