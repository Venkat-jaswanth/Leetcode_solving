#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    struct Fenwick {
    int n;
    vector<int> tree;

    Fenwick(int n) {
        this->n = n;
        tree.assign(n + 1, 0);
    }

    void add(int idx, int val) {
        int pos = idx + 1;
        while (pos <= n) {
            tree[pos] += val;
            pos += pos & -pos;
        }
    }

    int prefixSum(int idx) {
        int pos = idx + 1;
        int result = 0;
        while (pos > 0) {
            result += tree[pos];
            pos -= pos & -pos;
        }
        return result;
    }
    int rangeSum(int l, int r) {
        if (l > r) return 0;
        if (l == 0) return prefixSum(r);
        return prefixSum(r) - prefixSum(l - 1);
    }
};
}