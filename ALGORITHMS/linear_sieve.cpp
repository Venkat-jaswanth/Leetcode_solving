#include <bits/stdc++.h>
#include <time.h>
using namespace std;

using vv = vector<long long>;
vv primes;
vv ls;


void linearsieve(long long n)
{
    ls.assign(n + 1, 0);
    for (long long i = 2; i < n; i++)
    {
        if (ls[i] == 0)
        {
            primes.push_back(i);
            ls[i] = i;
        }
        for (auto p : primes)
        {
            if ((i * p) > n || p > ls[i])
                break;
            ls[i * p] = p;
        }
    }
}

vector<long long> sieve(long long n)
{
    primes.clear();
    primes.assign(n + 1, true);
    // creation of boolean array
    for (long long p = 2; p * p <= n; p++)
    {
        if (primes[p] == true)
        {

            // marking as false
            for (long long i = p * p; i <= n; i += p)
                primes[i] = false;
        }
    }

    vector<long long> res;
    for (int p = 2; p <= n; p++)
    {
        if (primes[p])
        {
            res.push_back(p);
        }
    }
    return res;
}

int main()
{
    long long n;
    cin >> n;
    double start = clock();
    cout << "Linear Sieve: \n";
    cout << '\n';
    linearsieve(n);
    double end = clock();
    cout << "Time: " << (end - start) / CLOCKS_PER_SEC << " sec\n";
    cout << "Number of primes found: " << primes.size() << '\n';
    // for(auto p : primes){
    //     cout << p << ",";
    // }
    cout << '\n';
    cout << "------------------\n";
    cout << "Sieve of Eratosthenes: Normal \n";
    start = clock();
    vector<long long> res = sieve(n);
    end = clock();
    cout << "Time: " << (end - start) / CLOCKS_PER_SEC << " sec\n";
    cout << "Number of primes found: " << res.size() << '\n';
    // for(auto p : res){
    //     cout << p << ",";
    // }
    cout << '\n';
}