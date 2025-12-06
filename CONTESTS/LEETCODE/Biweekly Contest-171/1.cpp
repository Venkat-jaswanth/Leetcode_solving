#include <bits/stdc++.h>

using namespace std;
class Solution {
public:
    bool isPrime(long long n){
        if(n <= 1) return false;
        if(n <= 3) return true;
        if(n %2 == 0 || n%3 == 0 ) return false;
        for (long long i = 5; i*i <= n ; i+=6){
            if (n % i == 0 || n % (i + 2) == 0) return false;
        }
        return true;
    }
    bool completePrime(int num) {
        string s = to_string(num);
        int n = s.size();
        for(int k = 1; k<=n; k++){
            long long prefix = stoll(s.substr(0,k));
            long long suffix = stoll(s.substr(n-k,k));
            if(!isPrime(prefix) || !isPrime(suffix))
                return false;
        }
        return true;
    }
};