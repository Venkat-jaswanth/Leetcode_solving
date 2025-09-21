#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    void backtrack(vector<int>& candidates, int target, int pos, vector<int>& curr, vector<vector<int>>& res) {
        if (target == 0) {             
            res.push_back(curr);
            return;
        }
        if (target < 0) return;

        for (int i = pos; i < candidates.size(); ++i) {
            if (candidates[i] > target) break;
            if (i > pos && candidates[i] == candidates[i - 1]) continue;

            curr.push_back(candidates[i]);
            backtrack(candidates, target - candidates[i], i, curr, res);
            curr.pop_back();                             
        }
    }

    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        vector<vector<int>> res;
        vector<int> curr;
        backtrack(candidates, target, 0, curr, res);
        return res;
    }
};

