class Solution:
    def climbStairs(self, n: int) -> int:
        # dp[i]: number of distinct ways to climb to (i+1)th step
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]