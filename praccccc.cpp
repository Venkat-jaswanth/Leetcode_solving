#include <bits/stdc++.h>

using namespace std;

using vv = vector<int>;
vv primes;
vv ls;
void linearsieve(int n){
    ls.assign(n+1,0);
    for(int i = 2; i<n; i++){
        if(ls[i] == 0){
            primes.push_back(i);
            ls[i] = i;
        }
        for(auto p:primes){
            if((i*p)>n || p>ls[i]) break;
            ls[i*p] = p;
        }
    }
}

int main(){
    int n;
    cin >> n;
    cout << '\n';
    linearsieve(n);
    for(auto p : primes){
        cout << p << ",";
    }

}