#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> generate(int n) {
        vector<vector<int>> result;
        vector<int> prevrow;
        for(int i=0 ; i<n ; i++){
            vector<int> curr_row(i+1 , 1);
            for(int j = 1; j<i ; j++){
                curr_row[j] = prevrow[j-1]+prevrow[j];
            }
            result.push_back(curr_row);
            prevrow = curr_row;
        }
         
        return result;
    }
};
