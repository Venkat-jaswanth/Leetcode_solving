#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    long long maxPoints(vector<int>& technique1, vector<int>& technique2, int k) {
        int n = technique1.size();
        vector<int> gain(n);
        long long base = 0;

        for (int i = 0; i < n; i++) {
            gain[i] = technique1[i] - technique2[i];
            base += technique2[i];
        }
        sort(gain.begin(), gain.end(), greater<int>());

        long long result = base;

        for (int i = 0; i < k; i++) {
            result += gain[i];
        }
        for (int i = k; i < n; i++) {
            if (gain[i] > 0) result += gain[i];
        }
        return result;
    }
};
