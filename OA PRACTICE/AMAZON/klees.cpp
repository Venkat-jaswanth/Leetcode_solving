
#include <bits/stdc++.h>

using namespace std;


int solve(vector<pair<int,int>>& guys) {
    sort(guys.begin(), guys.end(),
         [](auto &a, auto &b) {
             if(a.first == b.first)
                 return a.second > b.second; 
             return a.first < b.first;
         });
    int active = 0, max_people = 0;
    for(auto &g : guys) {
        active += g.second;
        max_people = max(max_people, active);
    }
    return max_people;
}

int main() {
    int n;
    cin >> n;
    int start , end;
    vector<pair<int,int>> guys;
    guys.reserve(2*n);

    for(int i = 0; i < n; i++) {
        cin >> start >> end;
        guys.push_back({start,+1});
        guys.push_back({end,-1});
    }

    int result = solve(guys);
    cout << result;
    return 0;
}
// 5
// 0900 1000
// 1000 1100
// 1200 1300
// 1400 1500
// 1500 1600



// int solve(vector<pair<int,int>>& intervals) {
//     priority_queue<int, vector<int>, greater<int>> pq;
//     int max_overlap = 0;

//     for(auto &inv : intervals) {
//         int start = inv.first;
//         int end   = inv.second;

//         while(!pq.empty() && pq.top() <= start) {
//             pq.pop();
//         }
//         pq.push(end);
//         max_overlap = max(max_overlap, (int)pq.size());
//     }
//     return max_overlap;
// }
