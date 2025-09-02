#include <bits/stdc++.h>
using namespace std;

#define fastio ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define ll long long
#define pb push_back
#define ff first
#define ss second
#define all(x) (x).begin(), (x).end()
#define rall(x) (x).rbegin(), (x).rend()
#define endl "\n"
#define sz(x) ((int)(x))
#define loop(i,n) for(int i=0;i<(n);i++)
#define rep(i,a,b) for(int i=(a); i<(b); i++)
#define each(x,a) for (auto &x : a)

const int MOD = 1e9 + 7;
const int INF = 1e9;

void solve() {
    int n; 
    cin >> n;
    vector<int> arr(n);
    loop(i,n) cin >> arr[i];

    sort(all(arr));

    each(x, arr) cout << x << " ";
    cout << endl;
}

int main() {
    fastio;
    int t = 1;
    cin >> t;
    while (t--) solve();
    return 0;
}
