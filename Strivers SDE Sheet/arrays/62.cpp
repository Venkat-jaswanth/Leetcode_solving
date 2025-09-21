#include <bits/stdc++.h>

using namespace std;

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



