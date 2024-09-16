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
    int findMinArrowShots(vector<vector<int>>& points) {
        if (points.size()==0)
        {
            return 0;
        }
        int ans = 1;
        sort(points.begin(), points.end(), [](vector<int> a, vector<int> b) {return a[1] < b[1]; });
        int anchor = points[0][1];
        for (int i = 1; i < points.size(); i++)
        {
            if (points[i][0]>anchor)
            {
                anchor = points[i][1];
                ans++;
            }
        }
        return ans;
    }
};