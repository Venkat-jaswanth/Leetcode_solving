#include <bits/stdc++.h>

using namespace std;


class Solution {
public:
    void helper(string s ,int pos, vector<string> &sub , vector<vector<string>> &result){
        if (pos == s.size()){
            result.push_back(sub);
            return;
        }
        for(int i = pos ; i < s.size() ; i++){
            if (isPalindrome(s, pos, i)){
                sub.push_back(s.substr(pos , i-pos+1));
                helper(s ,i+1, sub,result);
                sub.pop_back();
            }
        }
    }
    bool isPalindrome(string s, int start, int end) {
    while (start <= end) {
      if (s[start++] != s[end--])
        return false;
    }
    return true;
  }
    vector<vector<string>> partition(string s) {
        vector<vector<string>> result;
        vector<string> sub;
        helper(s,0,sub,result);
        return result;
    }
};
