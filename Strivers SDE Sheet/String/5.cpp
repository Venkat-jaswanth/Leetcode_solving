#include <bits/stdc++.h>

using namespace std;

class Solution
{
public:
    string longestPalindrome(string s)
    {
        if (s.length() <= 1)
            return s;
        int n = s.length();
        string maxstr = s.substr(0, 1);
        auto expand = [&](int left, int right)
        {
            while (left >= 0 && right < n && s[left] == s[right])
            {
                left--;
                right++;
            }
            return s.substr(left + 1, right - left - 1);
        };
        for (int i = 0; i < n - 1; i++)
        {
            string odd = expand(i, i);
            string even = expand(i, i + 1);
            if (odd.length() > maxstr.length())
                maxstr = odd;
            if (even.length() > maxstr.length())
                maxstr = even;
        }
        return maxstr;
    }
};
