#include <bits/stdc++.h>

using namespace std;

vector<int> primes;
vector<int> lp; // lowest prime factor

void linearSieve(int n) {
    lp.assign(n + 1, 0);

    for (int i = 2; i <= n; i++) {
        if (lp[i] == 0) {
            lp[i] = i;
            primes.push_back(i);
        }
        for (int p : primes) {
            if (p > lp[i] || i * p > n) break;
            lp[i * p] = p;
        }
    }
}
