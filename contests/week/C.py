class Solution:
    def maxSum(self, nums: List[int], k: int, m: int) -> int:
        n = len(nums)
        if k * m > n:
            return float('-inf')
        
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]
        
        dp = [[float('-inf')] * (n + 1) for _ in range(k + 1)]
        for i in range(n + 1):
            dp[0][i] = 0
        
        for j in range(1, k + 1):
            max1 = float('-inf')
            for i in range(1, n + 1):
                if i >= m:
                    max1 = max(max1, dp[j-1][i - m] - prefix[i - m])
                    max2 = prefix[i] + max1
                    dp[j][i] = max(dp[j][i-1], max2)
                else:
                    dp[j][i] = dp[j][i-1]
                    
        return dp[k][n]©leetcode