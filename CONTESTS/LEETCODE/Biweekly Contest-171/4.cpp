#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

class Solution {
    vector<int> bit;
    int max_rank;
    void update(int idx, int delta) {
        for (; idx <= max_rank; idx += idx & -idx)
            bit[idx] += delta;
    }

    int query(int idx) {
        int sum = 0;
        for (; idx > 0; idx -= idx & -idx)
            sum += bit[idx];
        return sum;
    }

public:
    long long minInversionCount(vector<int>& nums, int k) {
        int n = nums.size();
        
        vector<int> sorted_nums = nums;
        sort(sorted_nums.begin(), sorted_nums.end());
        sorted_nums.erase(unique(sorted_nums.begin(), sorted_nums.end()), sorted_nums.end());
        
        auto getRank = [&](int val) {
            return lower_bound(sorted_nums.begin(), sorted_nums.end(), val) - sorted_nums.begin() + 1;
        };
        
        max_rank = sorted_nums.size();
        bit.assign(max_rank + 1, 0);

        long long currentInversions = 0;
        long long minInversions = -1;

        for (int i = 0; i < k; i++) {
            int rank = getRank(nums[i]);
            
            int countLarger = i - query(rank); 
            
            currentInversions += countLarger;
            update(rank, 1);
        }

        minInversions = currentInversions;

        for (int i = k; i < n; i++) {
            int leavingVal = nums[i - k];
            int leavingRank = getRank(leavingVal);
            
            update(leavingRank, -1);
            
            int countSmaller = query(leavingRank - 1);
            currentInversions -= countSmaller;

            int enteringVal = nums[i];
            int enteringRank = getRank(enteringVal);
            
            int countLarger = (k - 1) - query(enteringRank);
            currentInversions += countLarger;
            
            update(enteringRank, 1);

            if (currentInversions < minInversions) {
                minInversions = currentInversions;
            }
        }

        return minInversions;
    }
};