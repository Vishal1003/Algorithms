class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        dp, m, n = collections.defaultdict(int), len(A), len(B)
        for i in range(m):
            for j in range(n):
                dp[i, j] = max(dp[i-1, j-1] + (A[i] == B[j]), dp[i-1, j], dp[i, j-1])
                print(dp)
        return dp[m-1, n-1]

    def maxUncrossedLines2(self, A: List[int], B: List[int]) -> int:
        len_a, len_b = len(A), len(B)
        dp = [[0] * (len_b + 1) for _ in range(len_a + 1)]

        for i in range(len_a):
            for j in range(len_b):
                if A[i] == B[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

        return dp[len_a][len_b]