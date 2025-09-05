#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

# You are required to complete this function
# Function should return the an integer 
class Solution:
    def longestIncreasingPath(self, matrix,n,m):
        if not matrix or not matrix[0]:
            return 0
        dp = [[-1 for _ in range(m)] for _ in range(n)]
        
        def dfs(i, j):
            # If already computed, return stored value
            if dp[i][j] != -1:
                return dp[i][j]
            
            # Directions for moving in the matrix (up, down, left, right)
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            max_path = 1  # Minimum path length is 1 (starting cell)
            
            for di, dj in directions:
                ni, nj = i + di, j + dj
                # Check bounds and increasing condition
                if 0 <= ni < n and 0 <= nj < m and matrix[ni][nj] > matrix[i][j]:
                    max_path = max(max_path, 1 + dfs(ni, nj))
            
            # Store result in dp array
            dp[i][j] = max_path
            return dp[i][j]
        
        # Compute longest path starting from every cell
        max_len = 0
        for i in range(n):
            for j in range(m):
                max_len = max(max_len, dfs(i, j))
        
        return max_len

#{ 
 # Driver Code Starts.
# Your code goes here
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        matrix = [[0 for i in range(n[1])]for j in range(n[0])]
        c=0
        for i in range(n[0]):
            for j in range(n[1]):
                matrix[i][j] = arr[c]
                c+=1 
                
        ob = Solution()
        print(ob.longestIncreasingPath(matrix, n[0], n[1]))
        print("~")
# } Driver Code Ends