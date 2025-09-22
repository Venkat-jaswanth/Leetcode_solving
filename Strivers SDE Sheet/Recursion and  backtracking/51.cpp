#include <bits/stdc++.h>

using namespace std;

// N-Queens Problem

// efficient
class Solution {
public:
    void solve(int col, vector<string> &board, vector<vector<string>> &ans,
               vector<int> &rowUsed,
               vector<int> &diagTRBL,
               vector<int> &diagTLBR, 
               int n) {

        if (col == n) {
            ans.push_back(board);
            return;
        }

        for (int row = 0; row < n; row++) {

            if (rowUsed[row] == 0 &&
                diagTRBL[row + col] == 0 &&
                diagTLBR[n - 1 + row - col] == 0) {

                board[row][col] = 'Q';
                rowUsed[row] = 1;
                diagTRBL[row + col] = 1;
                diagTLBR[n - 1 + row - col] = 1;

                solve(col + 1, board, ans, rowUsed, diagTRBL, diagTLBR, n);

                board[row][col] = '.';
                rowUsed[row] = 0;
                diagTRBL[row + col] = 0;
                diagTLBR[n - 1 + row - col] = 0;
            }
        }
    }

    vector<vector<string>> solveNQueens(int n) {
        vector<vector<string>> ans;
        vector<string> board(n, string(n, '.'));

        vector<int> rowUsed(n, 0);
        vector<int> diagTRBL(2 * n - 1, 0);
        vector<int> diagTLBR(2 * n - 1, 0);

        solve(0, board, ans, rowUsed, diagTRBL, diagTLBR, n);
        return ans;
    }
};



// less efficient
class Solution {
  public:
    bool isSafe1(int row, int col, vector < string > board, int n) {
      int duprow = row;
      int dupcol = col;

      while (row >= 0 && col >= 0) {
        if (board[row][col] == 'Q')
          return false;
        row--;
        col--;
      }

      col = dupcol;
      row = duprow;
      while (col >= 0) {
        if (board[row][col] == 'Q')
          return false;
        col--;
      }

      row = duprow;
      col = dupcol;
      while (row < n && col >= 0) {
        if (board[row][col] == 'Q')
          return false;
        row++;
        col--;
      }
      return true;
    }

  public:
    void solve(int col, vector < string > & board, vector < vector < string >> & ans, int n) {
      if (col == n) {
        ans.push_back(board);
        return;
      }
      for (int row = 0; row < n; row++) {
        if (isSafe1(row, col, board, n)) {
          board[row][col] = 'Q';
          solve(col + 1, board, ans, n);
          board[row][col] = '.';
        }
      }
    }

  public:
    vector < vector < string >> solveNQueens(int n) {
      vector < vector < string >> ans;
      vector < string > board(n);
      string s(n, '.');
      for (int i = 0; i < n; i++) {
        board[i] = s;
      }
      solve(0, board, ans, n);
      return ans;
    }
};
