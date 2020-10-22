import collections
"""
key thing to notice:
- need to traverse whole matrix and paint connected cells
- can use DFS/BFS (recursion, iteration) [in 4 ways]

T: O(# pixels) | S: O(# pixels)

Note:
visited = [[False] * C for _ in range(R)]
* We generally use "visited" variable to keep track of the nodes which have been visited.
* But, not required in this problem as we already know that we want to traverse the nodes which have old color.
"""


class Solution:
    # BFS --> using dirs()
    def floodFill(self, image, sr, sc, newColor):
        R, C = len(image), len(image[0])
        color = image[sr][sc]
        # vertical and horizontal directions. Can't traverse diagonally, hence can't have (1, 1) or (-1, -1)
        dirs = ((0, 1), (1, 0), (-1, 0), (0, -1))

        if color != newColor:
            q = collections.deque([(sr, sc)])
            while q:
                r, c = q.popleft()
                image[r][c] = newColor

                for dr, dc in dirs:
                    cr, cc = r + dr, c + dc
                    # General Case: 0 <= cr < R and 0 <= cc < C and not visited[cr][cc]
                    if 0 <= cr < R and 0 <= cc < C and image[cr][cc] == color:
                        # stack --> q.appendleft() || queue --> q.append()
                        q.appendleft((cr, cc))
        return image

    def floodFill2(self, image, sr, sc, newColor):
        R, C = len(image), len(image[0])
        color = image[sr][sc]
        if color != newColor:
            q = collections.deque([(sr, sc)])
            while q:
                r, c = q.popleft()
                # if inside boundary and color is old
                if 0 <= r < R and 0 <= c < C and image[r][c] == color:
                    image[r][c] = newColor
                    q.append((r+1, c))
                    q.append((r-1, c))
                    q.append((r, c+1))
                    q.append((r, c-1))

        return image
    """
    Recursion: two variants:
    1) Check for all corner/base cases and return if conditions are not met.  
    2) Check before each recursion call.
    """
    def floodFill3(self, image, sr, sc, newColor):
        R, C = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor:
            return image

        def dfs(r, c):
            # check for corner points
            if not (0 <= r < R and 0 <= c < C):
                return
            if image[r][c] == newColor or image[r][c] != color:
                return

            image[r][c] = newColor
            # these four recursion call can be in any order. Doesn't matter.
            dfs(r, c-1)
            dfs(r, c+1)
            dfs(r+1, c)
            dfs(r-1, c)

        # start dfs with starting point
        dfs(sr, sc)
        return image

    def floodFill4(self, image, sr, sc, newColor):
        R, C = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor:
            return image

        def dfs(r, c):
            if image[r][c] == color:
                image[r][c] = newColor

                if c+1 <= C-1: dfs(r, c+1)
                if r+1 <= R-1: dfs(r+1, c)
                if c-1 >= 0: dfs(r, c-1)
                if r-1 >= 0: dfs(r-1, c)

        dfs(sr, sc)
        return image

soln = Solution()
image = [[1,1,1],[1,1,0],[1,0,1]]
sr, sc = 1, 1
newColor = 2
ans = soln.floodFill(image, sr, sc, newColor)
# [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
print(ans)
