#include <string>

#include <vector>

#include <iostream>

#include <stdlib.h>

#include <time.h>

#include <sstream>

#include <algorithm>

#include <map>

#include <bitset>

using namespace std;


class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        int p1 = 0;
        int p2 = 0;
        int ans = 0;
        sort(g.begin(), g.end());
        sort(s.begin(), s.end());
        while (p2 < s.size())
        {
            if (p1 < g.size())
            {
                if (s[p2] >= g[p1])
                {
                    ans++;
                    p1++;
                    p2++;
                }
                else
                {
                    p2++;
                }
            }
            else
            {
                break;
            }
        }
        return ans;
    }
};