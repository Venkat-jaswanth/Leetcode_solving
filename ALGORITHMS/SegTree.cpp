#include <bits/stdc++.h>

using namespace std;

// Standard Segment Tree for range sum and point update
struct SegTree {
    int n;
    vector<int> tree;

    SegTree(int n) : n(n), tree(2 * n, 0) {}

    void build(const vector<int>& a) {
        for (int i = 0; i < n; i++)
            tree[n + i] = a[i];
        for (int i = n - 1; i > 0; i--)
            tree[i] = tree[i << 1] + tree[i << 1 | 1];
    }

    // point update: a[idx] = val
    void update(int idx, int val) {
        idx += n;
        tree[idx] = val;
        while (idx > 1) {
            idx >>= 1;
            tree[idx] = tree[idx << 1] + tree[idx << 1 | 1];
        }
    }

    // range sum [l, r]
    int query(int l, int r) {
        int res = 0;
        for (l += n, r += n; l <= r; l >>= 1, r >>= 1) {
            if (l & 1) res += tree[l++];
            if (!(r & 1)) res += tree[r--];
        }
        return res;
    }
};

//Different way for max and count of max in range

struct Node {
    int mx;     // maximum value
    int cnt;    // count of maximum
};

class SegTree {
    int n;
    vector<Node> tree;

    // Merge two segments
    Node merge(Node a, Node b) {
        if (a.mx > b.mx) return a;
        if (b.mx > a.mx) return b;
        return {a.mx, a.cnt + b.cnt};
    }

public:
    SegTree(vector<int>& a) {
        n = a.size();
        tree.resize(4 * n);
        build(1, 0, n - 1, a);
    }

    void build(int node, int l, int r, vector<int>& a) {
        if (l == r) {
            tree[node] = {a[l], 1};
            return;
        }
        int mid = (l + r) / 2;
        build(node * 2, l, mid, a);
        build(node * 2 + 1, mid + 1, r, a);
        tree[node] = merge(tree[node * 2], tree[node * 2 + 1]);
    }

    void update(int node, int l, int r, int idx, int val) {
        if (l == r) {
            tree[node] = {val, 1};
            return;
        }
        int mid = (l + r) / 2;
        if (idx <= mid)
            update(node * 2, l, mid, idx, val);
        else
            update(node * 2 + 1, mid + 1, r, idx, val);

        tree[node] = merge(tree[node * 2], tree[node * 2 + 1]);
    }

    Node query(int node, int l, int r, int ql, int qr) {
        if (qr < l || r < ql) return {-INT_MAX, 0};
        if (ql <= l && r <= qr) return tree[node];
        int mid = (l + r) / 2;
        return merge(
            query(node * 2, l, mid, ql, qr),
            query(node * 2 + 1, mid + 1, r, ql, qr)
        );
    }

    // Public wrappers
    void update(int idx, int val) {
        update(1, 0, n - 1, idx, val);
    }

    Node query(int l, int r) {
        return query(1, 0, n - 1, l, r);
    }
};


// normal type segment tree for max and count of max in range

struct Node {
    int mx;
    int cnt;
};

Node merge(Node a, Node b) {
    if (a.mx > b.mx) return a;
    if (b.mx > a.mx) return b;
    return {a.mx, a.cnt + b.cnt};
}

class SegTree {
    int n;
    vector<Node> tree;

public:
    SegTree(vector<int>& a) {
        n = a.size();
        tree.assign(2 * n, {-INT_MAX, 0});
        // build leaves
        for (int i = 0; i < n; i++)
            tree[n + i] = {a[i], 1};
        // build parents
        for (int i = n - 1; i > 0; i--)
            tree[i] = merge(tree[i * 2], tree[i * 2 + 1]);
    }

    void update(int idx, int val) {
        idx += n;
        tree[idx] = {val, 1};
        while (idx > 1) {
            idx >>= 1;
            tree[idx] = merge(tree[idx * 2], tree[idx * 2 + 1]);
        }
    }

    Node query(int l, int r) {
        Node left = {-INT_MAX, 0}, right = {-INT_MAX, 0};
        for (l += n, r += n; l <= r; l >>= 1, r >>= 1) {
            if (l & 1) left = merge(left, tree[l++]);
            if (!(r & 1)) right = merge(tree[r--], right);
        }
        return merge(left, right);
    }
};

