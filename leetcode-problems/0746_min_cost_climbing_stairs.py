class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [-1] * (n + 1)
        dp[0], dp[1] = cost[0], cost[1]

        for i in range(2, n + 1):
            if i == n:
                dp[i] = min(dp[i - 1], dp[i - 2])
            else:
                dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]

        return dp[n]
