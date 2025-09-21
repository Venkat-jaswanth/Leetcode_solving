#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int majorityElement(vector<int>& v) {
        int n = v.size();
        int cnt = 0; 
        int el;    

        for (int i = 0; i < n; i++) {
            if (cnt == 0) {  
                el = v[i];
                cnt = 1;
            }
            else if (el == v[i]) {
                cnt++;
            }
            else {
                cnt--;
            }
        }

        if (cnt > 0 ) return el;
        return -1;
        }

};