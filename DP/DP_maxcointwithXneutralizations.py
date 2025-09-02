class Solution(object):
    def maximumAmount(self, coins):
        """
        :type coins: List[List[int]]
        :rtype: int
        """
        if not coins or not coins[0]:
            return 0
        m = len(coins)
        n = len(coins[0])
        dp = [[[-float('inf')] * 3 for _ in range(n)] for _ in range(m)]
        

        for k in range(3):
            dp[0][0][k] = coins[0][0] if coins[0][0] >= 0 else (0 if k > 0 else coins[0][0])
        
        for i in range(m):
            for j in range(n):
                for k in range(3):
                    if i > 0:
                        gain = coins[i][j] if coins[i][j] >= 0 else 0
                        loss = coins[i][j] if coins[i][j] < 0 else 0
                        dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k] + gain + loss)
                        if k > 0 and coins[i][j] < 0:
                            dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k-1] + gain)
                    if j > 0:
                        gain = coins[i][j] if coins[i][j] >= 0 else 0
                        loss = coins[i][j] if coins[i][j] < 0 else 0
                        dp[i][j][k] = max(dp[i][j][k], dp[i][j-1][k] + gain + loss)
                        if k > 0 and coins[i][j] < 0:
                            dp[i][j][k] = max(dp[i][j][k], dp[i][j-1][k-1] + gain)
        return max(dp[m-1][n-1])

