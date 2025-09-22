#include <bits/stdc++.h>

using namespace std;

// efficient
class Solution {
public:
    void helper(int idx, vector<int>& nums, vector<vector<int>>& ans) {
        if(idx == nums.size()) {
            ans.push_back(nums);
            return;
        }
        for(int i = idx; i < nums.size(); i++) {
            swap(nums[i], nums[idx]);
            helper(idx + 1, nums, ans);
            swap(nums[i], nums[idx]);
        }
    }

    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> ans;
        helper(0, nums, ans);
        return ans;
    }
};

// less efficient (using freq array)dd
class Solution {
public:
    void helper(vector<int> &perm , vector<int> &freq , vector<int> nums , vector<vector<int>> &ans){
        if(perm.size() == nums.size()){
            ans.push_back(perm);
            return;
        }
        for(int i = 0; i<nums.size();i++){
            if(freq[i]==0){
                freq[i]= 1;
                perm.push_back(nums[i]);
                helper(perm , freq , nums , ans);
                perm.pop_back();
                freq[i] = 0;
            }
        }
    }

    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> ans;
        vector<int> freq(nums.size(),0);
        vector<int> perm;
        helper(perm,freq,nums,ans);
        return ans;
    }
};