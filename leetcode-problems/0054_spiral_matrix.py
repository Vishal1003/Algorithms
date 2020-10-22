class Solution:
    def spiralOrder(self, matrix):
        if not matrix: return []
        R, C = len(matrix), len(matrix[0])
        visited = [[False] * C for _ in range(R)]
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        ans = []
        x = y = di = 0
        for _ in range(R * C):
            ans.append(matrix[x][y])
            visited[x][y] = True

            cx, cy = x + dr[di], y + dc[di]
            if 0 <= cx < R and 0 <= cy < C and not visited[cx][cy]:
                x, y = cx, cy
            else:
                di = (di + 1) % 4
                x, y = x + dr[di], y + dc[di]

        return ans


if __name__ == "__main__":
    sol = Solution()
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = sol.spiralOrder(mat)
    print(result)
