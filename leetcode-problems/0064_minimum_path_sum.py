"""

cost(i,j)=grid[i][j]+min(cost(i+1,j),cost(i,j+1))

Approach 1: Brute Force
- T: O(2^(m+n)) S: O(m+n)

Approach 2: Dynamic Programming 2D
- dp(i,j)=grid(i,j)+min(dp(i+1,j),dp(i,j+1))
- T: O(mn), S:O(mn)

Approach 3: Dynamic Programming 1D
- dp(j)=grid(i,j)+min(dp(j),dp(j+1))
- T: O(mn), S:O(n)

Approach 4: Dynamic Programming (Without Extra Space)
- grid(i,j)=grid(i,j)+min(grid(i+1,j),grid(i,j+1))
- T: O(mn), S:O(1)

"""
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        for i in range(1, r):
            grid[i][0] += grid[i-1][0]
            
        for i in range(1, c):
            grid[0][i] += grid[0][i-1]
            
        for i in range(1, r):
            for j in range(1, c):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
                
        return grid[-1][-1]