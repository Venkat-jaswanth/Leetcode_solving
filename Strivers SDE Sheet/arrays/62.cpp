#include <bits/stdc++.h>

using namespace std;


// TOP DOWN APPROACH WITH MEMOIZATION
class Solution {
public:
    int countPaths(int i, int j, int n, int m , vector<vector<int>> &dp){
        if(i==(n-1) && j==(m-1)) return 1;
        if(i>=n || j>=m) return 0;
        if (dp[i][j]!= -1) return dp[i][j];
        else return dp[i][j] = countPaths(i+1,j,n,m ,dp) + countPaths(i,j+1,n,m ,dp);
    }
    
    int uniquePaths(int m, int n) {
        vector<vector<int>> dp(m, vector<int>(n, -1));
        return dp[0][0] = countPaths(0,0,m,n,dp);
    }

};

// BOTTOM UP APPROACH WITH TABULATION
class Solution {
public:
    int uniquePaths(int m, int n) {
    vector<vector<int>> dp(m, vector<int>(n, 1));
    for (int i = 1; i < m; i++) {
        for (int j = 1; j < n; j++) {
            dp[i][j] = dp[i-1][j] + dp[i][j-1];
        }
    }
    return dp[m-1][n-1];
}
};


// OPTIMIZED SPACE COMPLEXITY
class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<int> dp(n, 1);
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                dp[j] = dp[j] + dp[j-1];
            }
        }
        return dp[n-1];
    }
};