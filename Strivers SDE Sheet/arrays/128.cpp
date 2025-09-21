#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> num_set(nums.begin(), nums.end());
        int longest_streak = 0;

        for (int num : num_set) {
            if (num_set.find(num - 1) == num_set.end()) {
                int current_num = num;
                int current_streak = 1;

                while (num_set.find(current_num + 1) != num_set.end()) {
                    current_num++;
                    current_streak++;
                }
                

                longest_streak = max(longest_streak, current_streak);
            }
        }
        return longest_streak;
    }
};