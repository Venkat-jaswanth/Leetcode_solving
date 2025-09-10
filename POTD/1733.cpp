#include <bits/stdc++.h>
using namespace std;

#define sz(x) (x).size()
#define all(v) (v).begin(), (v).end()

bitset<500> bs[500];

class Solution {
public:
    int minimumTeachings(int m, vector<vector<int>>& lang, vector<vector<int>>& frnd) {
        int n = sz(lang);
        for (int i = 0; i < n; i++) {
            bs[i].reset();
            for (auto &l : lang[i])
                bs[i].set(--l);
        }
        vector<bool> no_talk(n, false);
        vector<int> freq(m, 0);
        for (auto &vec : frnd) {
            int u = vec[0], v = vec[1];
            u--, v--;
            int i = 0, j = 0;
            if ((bs[u] & bs[v]).any())
                continue;
            if (!no_talk[u]) {
                no_talk[u] = true;
                for (auto &l : lang[u])
                    freq[l]++;
            }
            if (!no_talk[v]) {
                no_talk[v] = true;
                for (auto &l : lang[v])
                    freq[l]++;
            }
        }
        int total = accumulate(all(no_talk), 0);
        return total - *max_element(all(freq));
    }
};