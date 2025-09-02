'''
Problem: Goldmine Problem
Problem Statement:
You are given a n x m grid representing a gold mine. Each cell in the grid contains a non-negative integer that represents the amount of gold at that position. Your task is to find the maximum amount of gold you can collect starting from any cell in the first column and moving to the last column.

You can move in three possible directions from any cell:

Right: to the cell immediately to the right.
Right-Up: to the cell diagonally up towards the right.
Right-Down: to the cell diagonally down towards the right.
You cannot move outside the grid or go back to the left. You need to find the maximum amount of gold you can collect by starting at any cell in the first column and reaching the last column.

Input:
An integer n representing the number of rows (1 ≤ n ≤ 100).
An integer m representing the number of columns (1 ≤ m ≤ 100).
A n x m grid of non-negative integers where each value is between 0 and 100.
Output:
Return an integer representing the maximum amount of gold you can collect.


'''

class Solution:
    def getMaxGold(self, matrix, n, m):
        if not matrix or not matrix[0]:
            return 0
        
        dp = [[-1 for _ in range(m)] for _ in range(n)]
        
        def dfs(i, j):
            if j == m-1:
                return matrix[i][j]
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            directions = [(0, 1), (-1, 1), (1, 1)]  # right, right-up, right-down
            max_gold = 0
            
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m:
                    max_gold = max(max_gold, matrix[i][j] + dfs(ni, nj))
            
            dp[i][j] = max_gold
            return dp[i][j]
        
        max_gold_collected = 0
        for i in range(n):
            max_gold_collected = max(max_gold_collected, dfs(i, 0))
        
        return max_gold_collected

if __name__ == "__main__":
    n = int(input())
    m = int(input())
    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    
    solution = Solution()
    result = solution.getMaxGold(matrix, n, m)
    print("The maximum amount of gold that can be collected is:", result)



'''
Clearly given test cases are not correct. refer the query i sent to the organisers
i tried and corrected the test cases. which i have written below , 

WRONG TEST CASES:
Input:
# The code snippet you provided is an implementation of a solution to the Goldmine Problem. In this
# problem, you are given a grid representing a gold mine with each cell containing a non-negative
# integer representing the amount of gold at that position. The task is to find the maximum amount of
# gold you can collect starting from any cell in the first column and moving to the last column,
# following specific movement rules.
n = 2, m = 3
grid = [
    [10, 33, 13],
    [5, 15, 10]
]

Output: 48

Explanation:
The path with the maximum gold is: 10 -> 33 -> 15
BY THE GIVEN TEST CASES THE OUTPUT SHOULD BE 53
BECAUSE THE PATH WITH THE MAXIMUM GOLD IS: 10 -> 33 -> 13
AND 33->15 IS NOT POSSIBLE AS IT IS IN THE SAME COLUMN AND WE CAN MOVE ONLY RIGHT, RIGHT-UP, RIGHT-DOWN AS MENTIONED IN THE PROBLEM STATEMENT

'''
'''
Example 1:

Input:
n = 3, m = 4
grid = [
    [1, 3, 1, 5],
    [2, 2, 4, 1],
    [5, 0, 2, 3]
]

Output:
16

Explanation:
The path with the maximum gold is: 5 -> 4 -> 2 -> 5.

Example 2:

Input:
n = 4, m = 4
grid = [
    [1, 3, 1, 5],
    [2, 2, 4, 1],
    [5, 0, 2, 3],
    [0, 6, 1, 2]
]

Output:
16

Explanation:
The path with the maximum gold is: 5 -> 2 -> 4 -> 5.

Example 3:

Input:
n = 2, m = 3
grid = [
    [10, 33, 13],
    [5, 15, 10]
]

Output:
53

Explanation:
The path with the maximum gold is: 10 -> 33 -> 13

Example 4:

Input:
n = 1, m = 5
grid = [
    [1, 2, 3, 4, 5]
]

Output:
15

Explanation:
Since there is only one row, the path is simply all the elements in the row: 1 -> 2 -> 3 -> 4 -> 5.

'''