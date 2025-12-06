#include <bits/stdc++.h>

using namespace std;
class Solution {
public:
    bool isbinarypalindrome(long long x){
        string s;
        while (x>0){
            s.push_back('0'+(x&1));
            x>>=1;
        }
        int i=0, j = s.size() - 1;
        while (i<j){
            if(s[i]!=s[j]) return false;
            i++;
            j--;
        }
        return true;
    }
    vector<int> minOperations(vector<int>& nums) {
        static vector<int> palindromes;
        if(palindromes.empty()){
            for(int x = 1; x<5000; x++){
                if(isbinarypalindrome(x)){
                    palindromes.push_back(x);
                }
            }
        }
        vector<int> ans(nums.size());

        for(int i = 0; i<nums.size(); i++){
            int x = nums[i];
            auto it = lower_bound(palindromes.begin(),palindromes.end(),x);
            int best = INT_MAX;

            if(it!= palindromes.end())
                    best = min(best, abs(*it - x));
            if(it!= palindromes.begin()){
                it--;
                best = min(best, abs(*it - x));
            }
            ans[i] = best;
        }
        return ans;
    }
};