from typing import List


class Solution:
    def maximumProfit(self, prices) -> int:
        # code here
        max_profit = 0
        min_price = float('inf')
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit
    
# if __name__ == "__main__":
#     prices = list(map(int, input().split()))
#     obj = Solution()
#     print(obj.maximumProfit(prices))
# # list(map(int, input().split()))

# # multiple transactions allowed
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         max_profit = 0
#         for i in range(1, len(prices)):
#             if prices[i] > prices[i-1]:
#                 max_profit += prices[i] - prices[i-1]
#         return max_profit
# if __name__ == "__main__":
#     prices = list(map(int, input().split()))
#     obj = Solution()
#     print(obj.maxProfit(prices))


# # 2 transactions allowed
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         n = len(prices)
#         if n == 0:
#             return 0
#         dp = [[0 for i in range(n)] for j in range(3)]
#         for i in range(1, 3):
#             max_diff = -prices[0]
#             for j in range(1, n):
#                 dp[i][j] = max(dp[i][j-1], prices[j] + max_diff)
#                 max_diff = max(max_diff, dp[i-1][j] - prices[j])
#         return dp[2][n-1]
    
    
    


# class Solution:
#     def maximumProfit(self, prices) -> int:
#         if not prices:
#             return 0

#         n = len(prices)
#         max_profit_left = [0] * n
#         max_profit_right = [0] * n

#         # Step 1: Calculate max_profit_left
#         min_price = float('inf')
#         for i in range(n):
#             if i > 0:
#                 max_profit_left[i] = max(max_profit_left[i - 1], prices[i] - min_price)
#             else:
#                 max_profit_left[i] = prices[i] - min_price
#             min_price = min(min_price, prices[i])

#         # Step 2: Calculate max_profit_right
#         max_price = float('-inf')
#         for i in range(n - 1, -1, -1):
#             if i < n - 1:
#                 max_profit_right[i] = max(max_profit_right[i + 1], max_price - prices[i])
#             else:
#                 max_profit_right[i] = max_price - prices[i]
#             max_price = max(max_price, prices[i])

#         # Step 3: Combine results
#         max_profit = 0
#         for i in range(n):
#             if i + 1 < n:
#                 max_profit = max(max_profit, max_profit_left[i] + max_profit_right[i + 1])
#             else:
#                 max_profit = max(max_profit, max_profit_left[i])

#         return max_profit

# if __name__ == "__main__":
#     prices = list(map(int, input().split()))
#     obj = Solution()
#     print(obj.maximumProfit(prices))


class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        if k >= n // 2:
            # Simplified case: Unlimited transactions
            return self.maxProfitUnlimited(prices)

        # DP table for at most k transactions
        dp = [[0] * n for _ in range(k + 1)]

        for i in range(1, k + 1):
            max_diff = -float('inf')
            for j in range(1, n):
                max_diff = max(max_diff, dp[i-1][j-1] - prices[j-1])
                dp[i][j] = max(dp[i][j-1], prices[j] + max_diff)

        return dp[k][n-1]

    def maxProfitUnlimited(self, prices: list[int]) -> int:
        # Simplified case where you can make as many transactions as you want
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                max_profit += prices[i] - prices[i-1]
        return max_profit
