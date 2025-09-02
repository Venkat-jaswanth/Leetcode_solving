#include <bits/stdc++.h>
using namespace std;

#define fastio ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define ll long long
#define pb push_back

#define all(x) (x).begin(), (x).end()
#define loop(i,n) for(int i=0;i<(n);i++)
#define rep(i,a,b) for(int i=(a); i<(b); i++)
#define each(x,a) for (auto &x : a)

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
