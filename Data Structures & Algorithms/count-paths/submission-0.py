class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[float("-inf")] * (n + 1) for _ in range(m + 1)]
        
        for i in range(m - 1, -1, -1):
            for j in range(n -1, -1, -1):
                dp[i][j] = max(1, dp[i + 1][j] + dp[i][j + 1])
        return dp[0][0]        


        