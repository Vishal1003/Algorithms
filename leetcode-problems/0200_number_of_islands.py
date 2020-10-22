"""
Approach #1 DFS [Accepted]
- O(M*N), worst: O(M*N)

Approach #2: BFS [Accepted]
- O(M*N), O(min(M, N))

Approach #3: Union Find (aka Disjoint Set) [Accepted]
- O(M*N), O(M*N)
"""
class Solution:
    def dfs(self, mat):
        if not mat:
            return 0
        
        R, C = len(mat), len(mat[0])
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
        visited = [[False] * C for _ in range(R)]
        count = 0
        
        def traverse(i, j):
            if visited[i][j]:
                return
            visited[i][j] = True
            
            for d in dirs:
                next_i, next_j = i + d[0], j + d[1]
                if 0 <= next_i < R and 0 <= next_j < C:
                    if mat[next_i][next_j] == mat[i][j]:
                        traverse(next_i, next_j)
            
        for i in range(R):
            for j in range(C):
                if not visited[i][j] and mat[i][j] == '1':
                    count += 1
                    traverse(i, j)
        return count
                        
    def numIslands(self, grid: List[List[str]]) -> int:
        count = self.dfs(grid)
        return count