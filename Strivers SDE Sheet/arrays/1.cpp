#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int , int> mp;
        for (int i = 0 ; i < nums.size() ; i++ ){
            int num = nums[i];
            int need = target - num;
            if(mp.find(need)!= mp.end()) return {mp[need],i};
            mp[num] = i;
        }
        return {-1,-1};
    }
};