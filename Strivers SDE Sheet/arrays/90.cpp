#include <bits/stdc++.h>

using namespace std;


class Solution {
public:
    void backtrack(vector<int>& curr, const vector<int>& nums, int pos, vector<vector<int>>& res) {
        res.push_back(curr);                      

        for (int i = pos; i < (int)nums.size(); ++i) {
            if (i > pos && nums[i] == nums[i - 1]) 
                continue;
            curr.push_back(nums[i]);              
            backtrack(curr, nums, i + 1, res);    
            curr.pop_back();                      
        }
    }

    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> res;
        vector<int> curr;
        backtrack(curr, nums, 0, res);
        return res;
    }
};

