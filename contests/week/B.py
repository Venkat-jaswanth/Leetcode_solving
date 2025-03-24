from typing import List

class Solution:
    def longestPalindromicSubsequence(self, s: str, k: int) -> int:
        def cost(a: str, b: str) -> int:
            diff = abs(ord(a) - ord(b))
            return min(diff, 26 - diff)
        
        memo = {}
        
        def dp(i: int, j: int, rem: int) -> int:

            if i > j:
                return 0
            if i == j:
                return 1 
            

            if (i, j, rem) in memo:
                return memo[(i, j, rem)]
            
            res = dp(i + 1, j, rem)
            res = max(res, dp(i, j - 1, rem))
            
            c = cost(s[i], s[j])
            if c <= rem:
                res = max(res, 2 + dp(i + 1, j - 1, rem - c))
            
            memo[(i, j, rem)] = res
            return res
        
        return dp(0, len(s) - 1, k)

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    s = "abced"
    k = 2
    # Expected output: 3, since we can form "ccc" with two operations.
    print(solution.longestPalindromicSubsequence(s, k))

